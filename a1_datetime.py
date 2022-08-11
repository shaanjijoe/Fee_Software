from datetime import datetime

def a1_date():
    now=datetime.now()

    s=now.strftime("%d %m %Y")
    s=str(s)
    return s

def a1_time():
    now=datetime.now()

    s=now.strftime("%H:%M")
    s=str(s)
    return s


print(a1_date())