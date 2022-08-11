# a1 status
# Removing existing data program
import dbf
# importing database package

def a1_removedatafunc(admissionno):
    try:

        # accessing table in file DATABASE.dbf
        table = dbf.Table('DATABASE.dbf')

        table.open(mode=dbf.READ_WRITE)  # opening file in read write mode

        result="NO_DATA"

        for record in table:  # searching each row in table

            with record as kernel:  # aliasing record as kernel

                if(record.adminno == admissionno):  # to delete data primary checker is adminno
                    
                    result="SUCCESS"
                    dbf.delete(kernel)
                    break

        table.pack()
        table.close()  # closing table

        return result  # returning execution complete status

    except:

        return "ERROR"  # returning error value in case of error



# n=a1_removedatafunc(934)
# n=a1_editdatafunc(0,(0,'abc','UKG','12.07.2022',34,79392828))
# print(n)