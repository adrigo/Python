import datetime, time, os

def getHour():
    now = datetime.datetime.now()
    return now

def formatHour():
    now = getHour()
    hora = '0'+str(now.hour) if len(str(now.hour))==1 else str(now.hour)
    min = '0'+str(now.minute) if (len(str(now.minute))==1) else str(now.minute)
    sec = '0'+str(now.second) if (len(str(now.second))==1) else str(now.second)
    horaActual = hora + ":" + min + ":" + sec
    return horaActual

def getSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)
    
def showHour():
    horaActual = formatHour().center(getSize())
    print(horaActual)
        
while True:
    showHour()
    time.sleep(1)
    pass
