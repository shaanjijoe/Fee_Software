## code to work with dbf module  aenum-2.1.2 dbf-0.97.11

import dbf

table = dbf.Table('DATA4.dbf', 'name C(30); age N(3,0); birth D')

print('db definition created with field names:', table.field_names)

table.open(mode=dbf.READ_WRITE)
for datum in (('John Doe', 31, dbf.Date(1979, 9,13)),('Ethan Furman', 102, dbf.Date(1909, 4, 1)),('Jane Smith', 57, dbf.Date(1954, 7, 2)),('John Adams', 44, dbf.Date(1967, 1, 9)),):
    table.append(datum)

print ('records added:')
for record in table:
    print (record)
    print ('-----')

table.close()

table.open(mode=dbf.READ_WRITE)

table.add_fields('telephone C(10)')

telephones = {'John Doe': '1234', 'Ethan Furman': '2345', 'Jane Smith': '3456', 'John Adams': '4567'}
for record in table:
    with record as r:
        r.telephone = telephones[r.name.strip()]

print ('updated records')
for record in table:
    print (record)
    print ('-----')