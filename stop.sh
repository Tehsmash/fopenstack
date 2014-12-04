#!/bin/bash

echo "Kill Fidentityadmin"
screen -X -S fidentityadmin quit

echo "Kill Fcompute"
screen -X -S fcompute quit

echo "Kill Fidentity"
screen -X -S fidentity quit

echo "Kill Fnetworking"
screen -X -S fnetworking quit

echo "Kill Fimage"
screen -X -S fimage quit
