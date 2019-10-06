# Python Arrays (List, Tuple, Set and Dictionary)
# https://www.w3schools.com/python/python_lists.asp
import csv

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
with open('simple_past.csv', 'r') as f:

    # csv.reader (csvfile, demiliter, dialect, **fmtparams)
    reader = csv.reader(f, delimiter=';')
    
    sp_list = list(reader)
    sp_dict = dict(sp_list)

print ('Full list...')
print (sp_list)

print ('\nFull dictionary...')
print (sp_dict)

print ('\nPrint (item) of list...')
print (sp_list[2])

print ('\nPrint (verb) of dictionary...')
print (sp_dict['be'])


