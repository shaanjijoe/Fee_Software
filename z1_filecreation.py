# z1 status
# Data storing file creation program
import dbf
# importing dbf package

def z1_filecreationfunc(fields='adminno N(6,0); name C(50); class C(3); birth D'):
    
    try:
        # fields='name C(30); age N(3,0); birth D'    #info regarding fields accepted
        
        table = dbf.Table('DATABASE.dbf', fields)   #creating table in file DATABASE.dbf

        fieldnames=list(table.field_names)          #saving fieldnames in list

        table.close()                               #closing table link

        return fieldnames                           #returning list of names
    
    except:

        return "ERROR"                              #returning error value in case of error

# print(z1_filecreationfunc())      #Testing
