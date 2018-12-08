#!/bin/sh

echo 'Enter Block Size [8-64]:'
read bsize
touch block.txt

# Generate private key
python ishkabibble.py -manual $bsize $bsize >> block.txt
block=$(sha256sum block.txt); rm block.txt
echo $block >> block.txt
key=$(sha256sum block.txt | cut -b 1-64)
rm block.txt

# Let the User see the Private Key
echo 'PRIVATE KEY: ['$key']'

#EOF
