#!/bin/bash

# killing all other bars before 
# launching another one
killall -q polybar
# main bar
polybar main 2>&1 | tee -a /tmp/polybar.log && disown

echo "Bars launched..."