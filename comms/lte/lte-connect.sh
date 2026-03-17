#!/bin/bash

echo "[LTE] Starting connection..."

nmcli radio wwan on
nmcli connection add type gsm ifname "*" con-name lte apn internet

nmcli connection up lte

echo "[LTE] Connected"