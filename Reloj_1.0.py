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

def getColumnSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)

def getRowsSize():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows)

def centerVertically():
    j = getRowsSize()/2-2
    i = 0
    while i < j:
        print("")
        i += 1

def recuadro():
    baseTecho = "------------------------".center(getColumnSize())
    return baseTecho
    
def showHour():
    centerVertically()
    horaActual = formatHour().center(getColumnSize())
    print(recuadro())
    print(horaActual)
    print(recuadro())

def limpiar():
    os.system('clear')
    
while True:
    limpiar()
    showHour()
    time.sleep(1)
    pass
