daysA = {'월', '화', '수', '목'}
daysB = set(['수', '목', '금', '토', '일'])
weekends = set(('토', '일'))

allDays = daysA | daysB
print(allDays)

workdays = allDays - weekends
print(workdays)

print(daysA & daysB)
print(daysA.symmetric_difference(daysB))





