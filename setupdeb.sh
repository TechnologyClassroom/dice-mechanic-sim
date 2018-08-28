#!/bin/bash

# setupdeb.sh v1.0

# Michael McMahon

# setup.sh installs the necessary pacakges to run builddatapack.sh
# on Debian based GNU/Linux distributions.

# To run, open a terminal and enter:
#   sudo sh builddatapack.sh

# Check for root.
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root"
  exit 1
fi

apt update
apt install -y python3-pip
apt install -y python3-tk
pip3 install numpy==1.15.0
pip3 install pandas==0.20.3
pip3 install matplotlib
apt install -y gpicview
apt install -y zip

echo "To configure tox, run"
echo "  bash buildtoxtestenvironment.sh"
