#!/usr/bin/env python
import os
import tarfile
import shutil

#1 Delete the directory PA4 if it already exists in your home directory PA4 if it already exists in home directory

if os.path.exists('/home/student/Khalid/PA4'):
    shutil.rmtree('/home/student/Khalid/PA4')

#2 Delete the tar.gz file created in step 11 if it already exists.

if os.path.exists('/home/student/Khalid/PA4.tar.gz'):
    os.remove('/home/student/Khalid/PA4.tar.gz')

#3 Create the directory PA4 in your home directory

os.makedirs('/home/student/Khalid/PA4')

#4 Create the directory PA4/part1

os.makedirs('/home/student/Khalid/PA4/part1')

#5 Create the directory PA4/part2

os.makedirs('/home/student/Khalid/PA4/part2')

#6 Create a file containing the first 50 lines of /usr/share/dict/words and name it first50.txt and place it in the directory part1

N = 50
file1 = open('/usr/share/dict/words', 'r')
file2 = open('/home/student/Khalid/PA4/part1/first50.txt', 'w')
for i in range(N):
    line = file1.readline()
    file2.writelines(line)
file1.close()
file2.close()

#7 Create a file containing all lines of /usr/share/dict/words that contain the (sub)string 'ea' followed by any one of b,c,d, or t and place these lines in a file named eax.txt in directory part2 and the count of the number of eax.txt words in eaxCount.txt in the same directory.

file3 = open('/usr/share/dict/words', 'r')
file4 = open('/home/student/Khalid/PA4/part2/eax.txt', 'w')
for line in file3:
    if "eab" in line or "eac" in line or "ead" in line or "eat" in line:
        file4.writelines(line)
file3.close()
file4.close()

file4 = open('/home/student/Khalid/PA4/part2/eax.txt', 'r')
file5 = open('/home/student/Khalid/PA4/part2/eaxCount.txt', 'w')
counter = 0
for line in file4:
    counter = counter + 1
file5.write(str('%d\n' % counter) + '\n')
file4.close()
file5.close()

#8 Prompt the user for the user's name and create the file name.txt containing your name and place it in PA4 (not in part1 or part2)

user_input = raw_input("What is your name? \n")
file6 = open('/home/student/Khalid/PA4/name.txt', 'w')
file6.write(user_input + '\n')
file6.close()

#9 Create a file containing all the lines of /etc/passwd that do not contain the letter 'a' and call it no_a.txt in directory part2

file7 = open('/etc/passwd', 'r')
file8 = open('/home/student/Khalid/PA4/part2/no_a.txt', 'w')
for line in file7:
    if 'a' not in line:
        file8.writelines(line)
file7.close()
file8.close()

#10 Place a copy of the script that is running (as specified by these instructions) in directory part1

file9 = open('PA4Script.py', 'r')
file10 = open('/home/student/Khalid/PA4/part1/PA4Script.py', 'w')

for line in file9:
    file10.writelines(line)
file9.close()
file10.close()

#11 Use tar to create PA4.tar.gz file containing the entire PA4 directory

create_tar = tarfile.open('/home/student/Khalid/PA4.tar.gz', 'w:gz')
create_tar.add('/home/student/Khalid/PA4')
create_tar.close()





