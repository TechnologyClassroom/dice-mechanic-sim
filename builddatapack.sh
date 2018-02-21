#!/bin/bash

# builddatapack.sh v1.0

# Michael McMahon

# This script only works with GNU/Linux.  To run this on Mac and GNU/Linux distros
# without gpicview, remove all lines that reference gpicview.

# builddatapack works with dicemechanicsim to run tests, display the output, and
# package the contents.

# To run, open a terminal and enter:
#   bash builddatapack.sh


# Generate timestamp variable
pack=$(date +%Y%m%d-%H%M)

# Run 40 simulations and display contents
for i in {1..40}
do
  # Run dms
  python3 dicemechanicsim.py 2>/dev/null
  # Display the latest png file
  ls -tr | tail -n 1 | xargs gpicview 2>/dev/null &
  # From bmb at https://stackoverflow.com/questions/1587059/bash-find-highest-numbered-filename-in-a-directory-where-names-start-with-digit
  # Wait 3 second
  sleep 3
  # Stop gpicview
  pkill gpicview
done

# Create a temp directory and copy work files
mkdir $pack
cd $pack
mv ../*.csv .
mv ../*.png .
cp ../dicemechanicsim.py .
cp ../plotdicemechanic.py .
cp ../builddatapack.sh .

# Archive in zip format
zip -r data$pack.zip ./*

# Remove temp directory and work files
mv data$pack.zip ../data/
cd ..
rm -fr $pack
