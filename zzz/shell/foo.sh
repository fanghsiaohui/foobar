#!/bin/bash
i=5
echo i=$i
while [ $i -gt 0 ]; do
    echo $i
    sleep 1
    i=$((i-1))
done
echo $i
echo i=$i
