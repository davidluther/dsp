# scratch code for faculty.csv question

import csv
import re

# Q1

def count_degrees(csv_file_name):

    with open(csv_file_name, 'r') as f:
        fac_read = csv.reader(f)
        next(fac_read)
        facultylist = []
        for line in fac_read:
            facultylist.append(line)

    # make set from punctuation-stripped, upper-case degrees:
    degrees_set = set()
    for member in facultylist:
        m_degs = member[1].strip().split(' ')
        for deg in m_degs:
            deg = ''.join(a for a in deg if a != '.').upper()
            degrees_set.add(deg)

    degrees = list(degrees_set)
    degree_counts = {}

    # search member[1] for RE matches for each degree
    # loop over set, create RE from each member (join on '\.?')
    # add '\.?' to end as well
    # count matches in member[1].upper()
    # add degree: count to dictionary
    for degree in degrees:
        deg_rx = '\.?'.join(a for a in degree) + '\.?'
        deg_finder = re.compile(deg_rx, re.I)
        deg_count = 0
        for member in facultylist:
            match = deg_finder.search(member[1])
            if match:
                deg_count += 1
            else:
                pass
        degree_counts[degree] = deg_count

    return degree_counts

# Q2

def count_titles(csv_file_name):

    with open(csv_file_name, 'r') as f:
        fac_read = csv.reader(f)
        next(fac_read)
        facultylist = []
        for line in fac_read:
            facultylist.append(line)

	# make set of all (corrected) titles
    titles_set = set()
    for member in facultylist:
        titles_set.add(member[2].strip().replace('is ','of '))

    titles = sorted(list(titles_set))
    tcount_list = [0,0,0] 
    
    # counter loop
    # this could be much more general/robust...
    for member in facultylist:
        if titles[0][:9] in member[2]:
            tcount_list[0] += 1
        elif titles[1][:9] in member[2]:
            tcount_list[1] += 1
        else:
            tcount_list[2] += 1
        
    title_counts = {}
    for i in range(len(titles)):
        title_counts[titles[i]] = tcount_list[i]

    return title_counts

# Q3

def emails(csv_file_name):

    with open(csv_file_name, 'r') as f:
        fac_read = csv.reader(f)
        next(fac_read)
        facultylist = []
        for line in fac_read:
            facultylist.append(line)

    # original solution
    # emails = [x[3] for x in facultylist]

    # RE solution
    p = re.compile(r'.+@.+\.\w{2,3}')
    emails = [n for m in facultylist for n in m if p.match(n) != None]

    return emails

# Q4

def unique_domains(emails):

    domains_set = set()
    for email in emails:
        domains_set.add(email.split('@')[1])

    domains = sorted(list(domains_set))

    return domains

# Q5

def write_to_csv(list_of_emails):
    
    with open('emails.csv', 'w') as f:
        e_out = csv.writer(f, lineterminator='\n')
        e_out.writerow(['Emails'])
        for email in list_of_emails:
            e_out.writerow([email])

# Q6

def get_dict():

    with open('faculty.csv', 'r') as f:
        fac_read = csv.reader(f)
        next(fac_read)
        facultylist = []
        for line in fac_read:
            facultylist.append(line)

    for member in facultylist:
        name = member[0].strip().split()
        member[0] = name[-1]
        # ok through here

    faculty_dict = {}
    lastnames = set([m[0] for m in facultylist])
    for lastname in lastnames:
        value = [[m[1],m[2],m[3]] for m in facultylist if m[0] == lastname]
        faculty_dict[lastname] = value

    return faculty_dict

# Q7

def get_dict2():

    with open('faculty.csv', 'r') as f:
        fac_read = csv.reader(f)
        next(fac_read)
        facultylist = []
        for line in fac_read:
            facultylist.append(line)

    faculty_dict = {}
    for member in facultylist:
        name = tuple(member[0].strip().split())
        faculty_dict[name] = [member[1], member[2], member[3]]

    return faculty_dict


# print(count_degrees('faculty.csv'))
# print(count_titles('faculty.csv'))
print(emails('faculty.csv'))
# print(unique_domains(emails('faculty.csv')))
# write_to_csv(emails('faculty.csv'))
# get_dict()
# get_dict2()
