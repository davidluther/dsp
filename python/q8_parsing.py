# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

footlist = []

with open('football.csv', 'r') as foot_in:
    foot_obj = csv.reader(foot_in)
    for line in foot_obj:
        footlist.append(line)

del footlist[0]

foot_difs = []

for line in footlist:
    item = []
    item.append(line[0])
    item.append(abs(int(line[5])-int(line[6])))
    foot_difs.append(item)

min_dif = 1000
for item in foot_difs:
    min_dif = min(min_dif, item[1])

print("Minimum difference between 'for' and 'agains' goals:", min_dif)
print("Team with the minimum difference:")
for item in foot_difs:
    if item[1] == min_dif:
        print(item[0])
