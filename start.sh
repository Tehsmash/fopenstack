#!/bin/bash

# FIdentity
pushd ./fidentity 

screen -S fidentity -dm pecan serve config.py
screen -S fidentityadmin -dm pecan serve configadmin.py

popd

# FCompute
pushd ./fcompute

screen -S fcompute -dm pecan serve config.py

popd

# FNetworking
pushd ./fnetworking

screen -S fnetworking -dm pecan serve config.py

popd

# FImage
pushd ./fimage

screen -S fimage -dm pecan serve config.py

popd
