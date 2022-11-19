#!/usr/bin/bash

choose() {
    local default="$1"
    local prompt="$2"
    local choice_yes="$3"
    local choice_no="$4"
    local answer

    read -p "$prompt" answer
    [ -z "$answer" ] && answer="$default"
    case "$answer" in
        [yY1] ) eval "$choice_yes"
            echo yes
            #error check
            ;;
        [nNO] ) eval "$choice_no"
            echo no
            # error check
            ;;
        * ) printf "%b" "Unexpected answer '$answer'!" >&2 ;;
    esac
} # 函数choose结束

choice() {
    CHOICE=''
    local prompt="$*"
    local answer

    read -p "$prompt" answer
    case "$answer" in
        [yY1] ) CHOICE='y';;
        [nN0] ) CHOICE='n';;
        *     ) CHOICE="$answer";;
    esac
} #函数 choice 结束


CHOICE=''
echo $THISPACKAGE
until [ "$CHOICE" = "y" ]; do
    printf "This package's date is $THISPACKAGE\n"
    choice "Is that correct? [Y/,<New date>]: "
    if [ -z "$CHOICE" ]; then
        CHOICE='y'
    elif [ "$CHOICE" != "y" ]; then
        printf "%b" "Overriding $THISPACKAGE with $CHOICE\n"
        THISPACKAGE=$CHOICE
    fi
done

choice "Do you want to look at the error logfile? [Y/n]: "
if [ "$CHOICE" != "n" ]; then
    echo error.log
fi
choice "Do you want to look at the message logfile? [y/N]: "
if [ "$CHOICE" = "y" ]; then
    echo message.log
fi


# 实例文件：func_choice.3
choice "Enter your favorite color, if you have one: "
if [ -n "$CHOICE" ]; then
    printf "%b" "You choise: $CHOICE\n"
else
    printf "%b" "You do not have a favorite color. \n"
fi


# 实例文件：select_dir
directorylist="Finished $(for i in *; do [ -d "$i" ] && echo $i; done)"
PS3='Directory to process?' # 设置有帮助的选择提示
until [ "$directory" = "Finished" ]; do
    printf "%b" "\a\n\nSelect a directory to process: \n" >&2
    select directory in $directorylist; do
        # 用户输入的数字被保存在 SREPLY 中，
        # 但是 select 返回的是用户选中的选项值
        if [ "$directory" = "Finished" ]; then
            echo "Finished processing directories."
            break
        elif [ -n "$directory" ]; then
            echo "You chose number $REPLY, processing $directory..."
            # 在此进行相关处理
            break
        else
            echo "Invalid selection!"
        fi # 结束选项处理
    done # 结束目录选择处理
done # 如果用户选中 Finished 选项，则结束循环
