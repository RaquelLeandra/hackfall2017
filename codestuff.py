import sys
import os
import sys
import os

def reformatDate(dates):
    result = ''
    months = {'Jan': '01',
              'Feb': '02',
              'Mar': '03',
              'Apr': '04',
              'May': '05',
              'Jun': '06',
              'Jul': '07',
              'Aug': '08',
              'Sep': '09',
              'Oct': '10',
              'Nov': '11',
              'Dec': '12'
              }
    for date in dates[1:len(dates)]:
        lis = date.split()
        day = lis[0]
        month = lis[1]
        year = lis[2]

        result = year + '-' + months[month] + '-' + day[0:-2]
    return result

dates = [10,'20th Oct 2052','2th May 1993']

print(reformatDate(dates))