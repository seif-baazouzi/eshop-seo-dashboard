#!/bin/bash

export ESHOP_DATABASE="eshop"
export ESHOP_USERNAME="postgres"
export ESHOP_PASSWORD="password"
export ESHOP_HOSTNAME="172.17.0.1"

export DB_HOSTNAME="172.17.0.4"

(
  while true; do
    python -B get-logs.py
    sleep $(( 60*60*2 )) # 2h 

  done
) &

wait
