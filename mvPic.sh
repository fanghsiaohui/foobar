#!/usr/bin/bash

OLDIFS=$IFS
IFS=$'\n'
src=c1
des=tp
re_jpg="[jJ][pP][eE]?[gG]"
re_png="[pP][nN][gG]"
n=3207
for f in $(find "$src" -type f); do
    printf -v newname '%04d' $((++n))
    ext="${f##*.}"
    if [[ ${ext} =~ ${re_jpg} ]]; then
        newext=".jpg"
        mv "${f}" "${des}"/"${newname}""${newext}"
    elif [[ ${ext} =~ ${re_png} ]]; then
        newext=".png"
        mv "${f}" "${des}"/"${newname}""${newext}"
    elif [[ ${ext} =~ [mM][pP]4 ]]; then
        newext=".mp4"
        ((n--))
        mv "${f}" tv/
    else
        ((n--))
        mv -i ${f} .
    fi
    if ! ((${n}%500)); then
        echo "${n}"
    fi
done

IFS=$OLDIFS
