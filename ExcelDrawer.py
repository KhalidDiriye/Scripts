#!/usr/bin/env python3
## Khalid Diriye
## Compares Drawer Fields in Excel Forms
#
#
#

from sys import argv
import csv

def rowOperation(csvReader, encode):
     errorNum = 0
     rowNum = 1

     for row in csvReader:
         e1, e2 = (row[0].lower().split(sep=' ')[0],
                   row[1].lower().split(sep=' ')[0])
         if (e1 != '' and e2 != '') and (e1 != e2) \
             and (row[1].find('Excel Forms') == -1 \
             and row[0].find('**Select Drawer**') == -1) \
             and (e1 != 'msctc' and e2 != 'mstate') \
             and (e1[:2] != 'cc' and e2[:2] != 'cc'):
             if e1.find(e2) == -1 and e2.find(e1) == -1:
                 if rowNum == 1:
                     outTup = ('Row', row[0], row[1], '-' * 80)
                     outStr = "%-4s\t%-31s\t%-30s\n%s"
                 else:
                     outTup = (rowNum + 1, row[0], row[1])
                     outStr = "%-4s\t%-30s:\t%-30s"
                 print(outStr % outTup)
                 #outCSV.write("%s,%s,%s" % outTup[:3]+ '\n')
                 errorNum += 1
         rowNum += 1
     print("Number of Mis-Matches: %d" % errorNum)

try:
     fileName = argv[1]
except:
     fileName = 'ExcelForm.csv'

try:
     encode = 'UTF16'
     csvFile = open(fileName, 'r', encoding=encode)
     csvReader = csv.reader(csvFile, dialect = 'excel-tab')

     print('-' * 80)

     try:
         rowOperation(csvReader, encode)
     except UnicodeDecodeError:
         csvFile.close()
         csvFile =  open(fileName, 'r')
         csvReader = csv.reader(csvFile, dialect = 'excel-tab')
         rowOperation(csvReader, 'utf-8')
     finally:
         csvFile.close()
except IOError as e:
     print(e)

csvFile.close()
