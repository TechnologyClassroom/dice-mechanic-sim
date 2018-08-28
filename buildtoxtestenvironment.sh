#!/bin/bash

# buildtoxtestenvironment.sh v1.0

# Michael McMahon
# Compile various versions of Python for local tox testing using pyenv.

# To run, open a terminal and enter:
#   bash buildtoxtestenvironment.sh

echo "Installing Debian dependencies..."
sudo apt update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev
# https://github.com/pyenv/pyenv/wiki/common-build-problems

echo "Installing pyenv..."
wget https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer
bash pyenv-installer

echo "Adding pyenv to the .bash_profile..."
echo '# pyenv' >> ~/.bashrc
echo 'export PATH="/home/user/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

echo "Updating pyenv..."
~/.pyenv/bin/pyenv update

echo "Listing available versions of Python..."
~/.pyenv/bin/pyenv install -l

echo "Installing multiple Python version..."
# TODO automatically find the latest dot release for every main version >2.6
#~/.pyenv/bin/pyenv install 2.6.9
#~/.pyenv/bin/pyenv install 2.7.15
#~/.pyenv/bin/pyenv install 3.0.1
#~/.pyenv/bin/pyenv install 3.1.5
#~/.pyenv/bin/pyenv install 3.2.6
#~/.pyenv/bin/pyenv install 3.3.7
~/.pyenv/bin/pyenv install 3.4.9
~/.pyenv/bin/pyenv install 3.5.6
~/.pyenv/bin/pyenv install 3.6.6
#~/.pyenv/bin/pyenv install 3.7.0

echo "Installing tox..."
sudo pip3 install tox

echo "Installing tox-pyenv..."
sudo pip3 install tox-pyenv

echo "Building tox python instances and testing..."
tox
