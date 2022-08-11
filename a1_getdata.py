# a1 status
# Reading existing data program
import dbf
# importing database package

def a1_getdatafunc(admissionno):
    try:

        # accessing table in file DATABASE.dbf
        table = dbf.Table('DATABASE.dbf')

        # opening file in read mode
        table.open(mode=dbf.READ_ONLY)  

        # creating list of field names of table
        tablefields = list(table.field_names)

        required="NO_DATA"    #assigning default data not found

        for record in table:  # searching each row in table

            if(record.adminno == admissionno):  # to read data primary checker is adminno

                required=dict()                 #setting required as new dictionary
                
                for fieldname in tablefields:   #going through fieldnames
                    
                    # adding value to new dictionary
                    required[fieldname]=record[fieldname]
                
                break           #stopping iterations
                    
        table.close()           #closing table

        return required  # returning execution complete status

    except:

        return "ERROR"  # returning error value in case of error



# print(a1_getdatafunc(934))