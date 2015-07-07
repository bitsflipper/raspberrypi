#!/bin/bash
createTunnel() {
  ssh -N -R 1234:localhost:22 -p 12822 pi@tatskie-rpi.homeip.net &
  if [[ $? -eq 0 ]]; then
    echo Tunnel to the server created successfully
  else
    echo An error occurred creating a tunnel to the server. RC was $?
  fi
}
/bin/pidof ssh
if [[ $? -ne 0 ]]; then
  echo Creating new tunnel connection
  createTunnel
fi
