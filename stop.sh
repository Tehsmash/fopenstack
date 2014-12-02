#!/bin/bash

echo "Kill Fidentityadmin"
screen -X -S fidentityadmin quit

echo "Kill Fcompute"
screen -X -S fcompute quit

echo "Kill Fidentity"
screen -X -S fidentity quit
