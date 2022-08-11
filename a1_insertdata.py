# a1 status
# Inserting new data program
import dbf
from a1_getdata import a1_getdatafunc
# importing database package
# importing a1_getdatafunc function to check for duplicate

def a1_insertdatafunc(newdata):
    try:

        # accessing table in file DATABASE.dbf
        table = dbf.Table('DATABASE.dbf')

        table.open(mode=dbf.READ_WRITE)  # opening file in read write mode

        # Checking for existing data
        if(a1_getdatafunc(newdata['ADMINNO'])!="NO_DATA"):

            table.close()  # closing table
            return "DATA_EXISTS"
        

        table.append(newdata)           # inserting new data at end

        table.close()  # closing table

        return "SUCCESS"  # returning execution complete status

    except:

        return "ERROR"  # returning error value in case of error


# n=a1_insertdatafunc({'ADMINNO':934, 'CLASS':'I','NAME':'Raju','BIRTH':dbf.Date(2000, 9,13),'AGE':4, 'PHONE':1234567890})
# print(n)