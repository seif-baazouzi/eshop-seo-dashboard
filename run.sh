#!/bin/bash

export ESHOP_DATABASE="eshop"
export ESHOP_USERNAME="postgres"
export ESHOP_PASSWORD="password"
export ESHOP_HOSTNAME="172.17.0.1"

python -B get-logs.py
