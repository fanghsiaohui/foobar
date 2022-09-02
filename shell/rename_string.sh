#/usr/bin/sh
d=${HOME}/bar
for i in zp/* ;do
    #f=$(basename $i)
    f="${i#*/}"
    echo $f
    touch "$d/$f"
done
