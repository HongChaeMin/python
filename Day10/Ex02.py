pl = ['python', 'java', 'c++', 'Go', 'swift']
print(sorted(pl, key = len))
print(sorted(pl, key = lambda x : x[1]))

pl = [('python', 1990), ('java', 2000), ('C++', 1983), ('Go', 2009), ('swift', 2014)]
print(sorted(pl, key = lambda item : item[0]))
print(sorted(pl, key = lambda item : item[1]))

