# y1 status
# Fields editing program
import dbf
# importing dbf package

def y1_editfileattributesfunc(newfields=''):
    
    try:
        table = dbf.Table('DATABASE.dbf')           #accessing table in file DATABASE.dbf

        table.open(mode=dbf.READ_WRITE)             #Opeing table in edit mode

        table.add_fields(newfields)                 #adding new fields

        fieldnames=list(table.field_names)          #saving all fieldnames in list
        
        table.close()                               #closing table link

        return fieldnames                           #returning list of new names
    
    except:

        return "ERROR"                              #returning error value in case of error


def y1_removefileattributesfunc(removefields=''):
    
    try:
        table = dbf.Table('DATABASE.dbf')           #accessing table in file DATABASE.dbf

        table.open(mode=dbf.READ_WRITE)             #Opeing table in edit mode

        table.delete_fields(removefields)              #adding new fields

        fieldnames=list(table.field_names)          #saving all fieldnames in list
        
        table.close()                               #closing table link

        return fieldnames                           #returning list of new names
    
    except:

        return "ERROR"                              #returning error value in case of error

# print(y1_editfileattributesfunc('Phone N(10,0); Age N(3,0)'))      #Testing
