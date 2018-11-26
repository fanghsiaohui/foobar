#!/usr/bin/sh
# 批量更新git repo
for dir in $(ls -d */)
do
    if [ -d "$dir"/.git ]; then
        #echo "$dir" && cd "$dir" && git pull && cd ..
        echo $dir
        cd $dir
        git pull
        cd ..
    fi
done
