#!/usr/bin/bash

WORKDIR=$1

consul exec ipmitool sdr list | grep degrees | awk '{gsub(":","|"); print}' | sort -u > "$WORKDIRipmitool_sdr_temp.out"
#consul exec ipmitool sdr list | grep -v ns | awk '{gsub(":","|"); print}' | sort -u > "$WORKDIRipmitool_sdr_temp.out"