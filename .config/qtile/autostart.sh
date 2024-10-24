#!/bin/sh

# systray battery icon
cbatticon -u 13 &
# systray for networks
nm-applet &
# systray volume
volumeicon &
