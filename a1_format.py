# formats string to appropriate format
# from tokenize import Double
import re

def a1_formatname(strin):
    strin=strin.strip()
    strin=strin.upper()
    strin=strin.replace("_"," ")
    strin=re.sub(' +', ' ',strin)
    return strin

def a1_formatnumber(num):
    num=str(num)
    num=num.strip()
    num=num.replace(" ","")
    return num


def a1_checkstring(strin):
    strin=str(strin)
    if(strin.isalpha()==False):
        return False
    return True

def a1_checknumber(num):
    try:
        num=int(num)
        return True
    except:
        return False


# print(a1_checknumber("-90"))
# print(a1_formatnumber("7887967898676456 989"))
# print(check_string('fFf'))
# print(format_name("Hi   ghg"))
# print(check_number('69-34589'))