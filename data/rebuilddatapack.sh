#!/bin/bash

# rebuilddatapack.sh
# Rebuild Data Pack v1.0.0
# Copyright (C) 2017-2020 Michael McMahon

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This script only works with GNU/Linux.  To run this on Mac and GNU/Linux distros
# without gpicview, remove all lines that reference gpicview.

# rebuilddatapack works with DMS datapacks that do not contain graphs, plot,
# display, and package the contents again.

# To run, open a terminal and enter:
#   bash rebuilddatapack.sh datapack.zip


# Generate timestamp variable based on first argument
pack=$1

# Unzip the datapack from first argument
unzip $1 -d $1.d

cd $1.d

# Remove all files except for the top 40.
ls | grep csv | tail -n +40 | xargs rm

# Graph all csv files and display contents
for file in *.csv
do
  # Add index to csv
  awk -F',' -v OFS=',' 'NR == 1 {print "'\''Event'\''", $0; next} \
{print (NR-2), $0}' $file > i$file
  cp i$file $file
  rm i$file
  # From larsks and Tom Fenech at https://stackoverflow.com/questions/30530407/add-index-column-to-csv-file
  # From Steve and fedorqui at https://stackoverflow.com/questions/9899001/how-to-escape-a-single-quote-inside-awk
  # Run plotcsv
  python3 ../plotcsv.py $file 2>/dev/null
  # Display the latest png file
  ls -tr | tail -n 1 | xargs gpicview &
  # From bmb at https://stackoverflow.com/questions/1587059/bash-find-highest-numbered-filename-in-a-directory-where-names-start-with-digit
  # Wait 2 second
  sleep 2
  # Stop gpicview
  pkill gpicview
done

first=$(ls | grep csv | head -n 1)

# Create a temp directory and copy work files
mkdir $first
cd $first
mv ../*.csv .
mv ../*.png .
cp ../dicemechanicsim.py .
cp ../../plotcsv.py .
cp ../../rebuilddatapack.sh .

# Archive in zip format
zip -9 -r data$first.zip ./*

# Remove temp directory and work files
mv data$first.zip ..
cd ..
rm -fr $first
rm -fr $1.d
