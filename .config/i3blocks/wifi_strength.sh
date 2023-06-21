#!/bin/bash
OUTPUT=$(nmcli dev wifi list | awk '/\*/{if (NR!=1) {print $8}}')
echo $OUTPUT