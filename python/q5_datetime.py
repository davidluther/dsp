# Hint:  use Google to find python function

from time import mktime

def convert_a(date):
    m, d, y = map(int, date.split('-'))
    ttup = (y,m,d,0,0,0,0,0,0)
    return mktime(ttup)

def convert_b(date):
    m = int(date[0:2])
    d = int(date[2:4])
    y = int(date[4:])
    ttup = (y,m,d,0,0,0,0,0,0)
    return mktime(ttup)

def convert_c(date):
    months = {'Jan': 1,
              'Feb': 2,
              'Mar': 3,
              'Apr': 4,
              'May': 5,
              'Jun': 6,
              'Jul': 7,
              'Aug': 8,
              'Sep': 9,
              'Oct': 10,
              'Nov': 11,
              'Dec': 12}
    date_list = date.split('-')
    y = int(date_list[2])
    m = months[date_list[1]]
    d = int(date_list[0])
    ttup = (y,m,d,0,0,0,0,0,0)
    return mktime(ttup)

def days_transpired(mode, d1, d2):
    spd = 86400
    if mode == 'a':
        return int((convert_a(d2) - convert_a(d1)) / spd)
    elif mode == 'b':
        return int((convert_b(d2) - convert_b(d1)) / spd)
    elif mode == 'c':
        return int((convert_c(d2) - convert_c(d1)) / spd)
    else:
        return None


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

print("Days transpired:", days_transpired('a', date_start, date_stop))

####b)  
date_start = '12312013'  
date_stop = '05282015'  

print("Days transpired:", days_transpired('b', date_start, date_stop))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

print("Days transpired:", days_transpired('c', date_start, date_stop))
