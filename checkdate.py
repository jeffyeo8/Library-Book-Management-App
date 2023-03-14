import datetime

def checkDate(d):
    try:
        day, month, year = d.split("/")
    except ValueError:
        return False
    
    if any(len(x) == 0 for x in [day, month, year]):
        return False

    if len(year) == 1 or len(day) > 2 or len(month) > 2:
        return False

    val = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        val = False
    
    return val