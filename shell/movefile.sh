#!/bin/bash
for filename in *; do
    a=$(file $filename | awk '{print $2}')
    if [ $a = "PDF" ]; then
        mv $filename docs/
        echo "move $filename to docs"
    elif [ $a = "ISO" ]; then
        mv $filename video/
        echo "move $filename to video"
    fi
done
