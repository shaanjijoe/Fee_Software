# Reading data from .dbf files

from dbfread import DBF
# importing dbfread necessary to connect to dbf files
for record in DBF('DATA4.dbf'):   
    # Probably DBF('DATA.dbf') here must be whole page  
    # record here is an ordered dictionary for each row
    print(record['ADMINNO'])
    # Above prints value of cell where column header is ADMINNO


recore=DBF('DATA4.dbf',load=True)
# here recore becomes a table
print(recore.records)
# recore.records is a list of all the rows, with each row as a dictionary 
