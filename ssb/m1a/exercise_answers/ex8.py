#!/usr/bin/python3


# a) Write a script that opens a text file and prints the contents to
# screen
with open('entamoeba.txt') as in_file:
    for line in in_file:
        print(line)

#b) Modify the script to write the contents of a file to a second
#file. Do this twice, the first time as an exact copy and the second
#removing all of the newlines.
out_file1 = open("temp1.txt", "w")
out_file2 = open("temp2.txt", "w")
with open('entamoeba.txt') as in_file:
    for line in in_file:
        out_file1.write(line)
        out_file2.write(line.strip('\n'))

out_file1.close()
out_file2.close()
