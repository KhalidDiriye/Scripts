#!/bin/bash
# Simple decrypt using gpg
read -p "Enter path: " $file
# Check if directory exists
if [ -e "$file" ] 
then
		echo "Please enter a path!"
else 
		# decrypt and write it to stdout
		gpg -d $file
		echo "File has been successfully decrypted"
fi 
exit