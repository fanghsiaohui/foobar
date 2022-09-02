#!/bin/bash
while true;do
    a=$(date +%R)
    if [ $a == '06:20' ]; then
        echo -e "\nALERT:\n\ttime now\n\tgo out"
        break
    fi
    sleep 60
done
