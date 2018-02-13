#!/usr/bin/env bash

#1 Delete the directory PA4 if it already exists in your home directory PA4 if it already exists in home directory

if [ -d "/home/student/he1296qc/PA4" ]; then
  rm -rf /home/student/he1296qc/PA4
fi

#2 Delete the tar.gz file created in step 11 if it already exists.

if [ -f "/home/student/he1296qc/PA4/PA4.tar.gz" ]; then
	rm -rf /home/student/he1296qc/PA4/PA4.tar.gz
fi

#3 Create the directory PA4 in your home directory

mkdir /home/student/he1296qc/PA4

#4 Create the directory PA4/part1

mkdir /home/student/he1296qc/PA4/part1

#5 Create the directory PA4/part2

mkdir /home/student/he1296qc/PA4/part2

#6 Create a file containing the first 50 lines of /usr/share/dict/words and name it first50.txt and place it in the directory part1

head -50 /usr/share/dict/words > /home/student/he1296qc/PA4/part1/first50.txt

#7 Create a file containing all lines of /usr/share/dict/words that contain the (sub)string 'ea' followed by any one of b,c,d, or t and place these lines in a file named eax.txt in directory part2 and the count of the number of eax.txt words in eaxCount.txt in the same directory.

grep "eab" /usr/share/dict/words >> /home/student/he1296qc/PA4/part2/eax.txt
grep "eac" /usr/share/dict/words >> /home/student/he1296qc/PA4/part2/eax.txt
grep "ead" /usr/share/dict/words >> /home/student/he1296qc/PA4/part2/eax.txt
grep "eat" /usr/share/dict/words >> /home/student/he1296qc/PA4/part2/eax.txt

cat /home/student/he1296qc/PA4/part2/eax.txt| wc -l > /home/student/he1296qc/PA4/part2/eaxCount.txt

#8 Prompt the user for the user's name and create the file name.txt containing your name and place it in PA4 (not in part1 or part2)

echo "What is your name? "
read user_input
echo $user_input > /home/student/he1296qc/PA4/name.txt
 
#9 Create a file containing all the lines of /etc/passwd that do not contain the letter 'a' and call it no_a.txt in directory part2

grep -v 'a' /etc/passwd > /home/student/he1296qc/PA4/part2/no_a.txt

#10 Place a copy of the script that is running (as specified by these instructions) in directory part1

cat PA4Script > /home/student/he1296qc/PA4/part1/PA4Script

#11 Use tar to create PA4.tar.gz file containing the entire PA4 directory

tar -czvf PA4.tar.gz /home/student/he1296qc/PA4

