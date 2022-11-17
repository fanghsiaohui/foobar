#!/usr/bin/bash

cd tptest
n=1
for oldf in $(ls | sort -n); do
    newf=$(printf '%04d' $n)
    ext=${oldf#*.}
    mv "${oldf}" "${newf}.${ext}"
    if ! ((n%5)); then
        printf '%4d, %s\n' $n "$(date)"
    fi
    ((n++))
done
echo complete
