#!/bin/bash

screen -S fidentity -dm pecan serve config-identity.py
screen -S fidentityadmin -dm pecan serve config-identityadmin.py
screen -S fcompute -dm pecan serve config-compute.py
screen -S fnetworking -dm pecan serve config-networking.py
screen -S fimage -dm pecan serve config-image.py
