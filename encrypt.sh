#!/bin/bash
# Simple encrypt using gpg
read -p "Enter path: " $file
# Check if directory exists
if [ -e "$file" ] 
then
		echo "Please enter a path!"
else 
		# encrypt with symmetric cipher
		gpg -c $file
		echo "File has been successfully encrypted"
fi 
exit