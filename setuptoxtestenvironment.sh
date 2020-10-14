#!/bin/bash

# setuptoxtestenvironment.sh
# Setup tox test environment for dicemechanicsim (DMS) v1.0.1

# Copyright (C) 2017-2020 Michael McMahon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Compile various versions of Python for local tox testing using pyenv.

# To run, open a terminal and enter:
#   bash setuptoxtestenvironment.sh


# Initialization checks

# Check for /bin/bash.
if [ "$BASH_VERSION" = '' ]; then
  echo "You are not using bash."
  echo "Use this syntax instead:"
  echo "sudo bash bluearchive.sh"
  exit 1
fi

# Check networking
# https://unix.stackexchange.com/questions/190513/shell-scripting-proper-way-to-
#   check-for-internet-connectivity
echo Checking network...
if ping -q -c 1 -W 1 google.com >/dev/null; then
  echo "The network is up."
else
  echo "The network is down."
  echo "Check connection and restart script!"
  exit 1
fi

# Check for root.
if [[ $EUID -e 0 ]]; then
  echo "This script must not be run as root!"
  exit 1
fi

# Disable screensaver
echo "Disabling screensaver..."
xset s off 2>/dev/null
xset -dpms 2>/dev/null
xset s noblank 2>/dev/null
gsettings set org.gnome.desktop.screensaver idle-activation-enabled false 2>/dev/null
setterm -blank 0 -powerdown 0  -powersave off 2>/dev/null

echo "Installing Debian dependencies..."
apt update
echo "If you see an error that reads:"
echo "  E: You must put some 'source' URIs in your sources.list"
echo "or" 
echo "  E: Invalid operation build-deps"
echo "after the next command, edit your /etc/apt/sources.list"
echo "file and remove the comments before all deb-src lines that"
echo "follow lines that start with 'deb' that are uncommented."
echo \ 
apt-get build-deps -y python
apt install -y libssl1.0-dev
apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev
# https://github.com/pyenv/pyenv/wiki/common-build-problems

echo "Installing pyenv..."
wget https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer
bash pyenv-installer

# TODO Check if pyenv was already configured in /etc/bash.bashrc
echo "Adding pyenv to the /etc/bash.bashrc..."
echo '# pyenv' >> /etc/bash.bashrc
echo 'export PATH="/home/user/.pyenv/bin:$PATH"' >> /etc/bash.bashrc
echo 'eval "$(pyenv init -)"' >> /etc/bash.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> /etc/bash.bashrc

echo "Reloading bash..."
source ~/.bashrc

echo "Updating pyenv..."
~/.pyenv/bin/pyenv update

echo "Installing multiple Python versions..."

# Function to find the latest python version of available within pyenv
latestpyenv () {
   ~/.pyenv/bin/pyenv install -l | sed 's/  //g' | egrep "^$1" | sort -V | tail -n 1
   # Breakdown of this one-liner
   # ~/.pyenv/bin/pyenv install -l  # List available versions of Python.
   # | sed 's/  //g'                # Remove the empty space before the strings.
   # | egrep "^$1"                  # Limit the output to standard versions of python.
   # | sort -V                      # Sort by version number format.
   # | tail -n 1                    # Output the last entry.
}

# Create variables for the current versions of python
py36=$(latestpyenv 3.6)
py37=$(latestpyenv 3.7)
py38=$(latestpyenv 3.8)
py39=$(latestpyenv 3.9)

~/.pyenv/bin/pyenv install $py36
~/.pyenv/bin/pyenv install $py37
~/.pyenv/bin/pyenv install $py38
~/.pyenv/bin/pyenv install $py39

echo "pyenv shell $py36 $py37 $py38 $py39" >> /etc/bash.bashrc
echo \ 

echo "Installing tox..."
pip3 install tox

echo "Installing tox-pyenv..."
pip3 install tox-pyenv

echo "Building tox python instances and testing..."
tox
