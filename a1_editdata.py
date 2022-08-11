# a1 status
# Editing existing data program
import dbf
# importing database package

def a1_editdatafunc(admissionno, newdata):
    try:

        # accessing table in file DATABASE.dbf
        table = dbf.Table('DATABASE.dbf')

        table.open(mode=dbf.READ_WRITE)  # opening file in read write mode

        # creating list of field names of table
        tablefields = list(table.field_names)

        for record in table:  # searching each row in table

            with record as kernel:  # aliasing record as kernel

                if(kernel.adminno == admissionno):  # to edit data primary checker is adminno

                    for fieldname in tablefields:  # taking fieldnames to align proper data to proper positiokernel

                        kernel[tablefields.index(
                            fieldname)] = newdata[fieldname]
                        # assigning data at the index where fieldname is present in field list

        # dormant code to print all data
        # ######################################
        # print ('updated records')
        # for record in table:
        #     print (record)
        #     print ('-----')
        # #####################################

        table.close()  # closing table

        return "SUCCESS"  # returning execution complete status

    except:

        return "ERROR"  # returning error value in case of error



# n=a1_editdatafunc(1234,{'ADMINNO':1234, 'NAME':'Rajesh','CLASS':'LKG','BIRTH':dbf.Date(1979, 9,13),'AGE':34, 'PHONE':79392828})
# n=a1_editdatafunc(0,(0,'abc','UKG','12.07.2022',34,79392828))
# print(n)