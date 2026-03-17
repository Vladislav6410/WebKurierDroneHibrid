#!/bin/bash

ping -c 2 8.8.8.8 > /dev/null

if [ $? -eq 0 ]; then
    echo "LTE_OK"
else
    echo "LTE_FAIL"
fi