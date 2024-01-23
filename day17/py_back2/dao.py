import datetime as d

gb = []
gno = 1

def findall()->list:
    return gb

def save(title:str, writer:str, ingi:str, content:str)->bool:
    global gno
    writeday = d.datetime.now().date()
    lb = dict(gno=gno, title=title, writer=writer, writeday=writeday, 
              ingi=ingi, content=content)
    list.append(lb)
    gno+=1
    return True

def delete(gno:int)->bool:
    for lb in gb:
        if lb['gno']==gno:
            gb.remove(lb)
            return True
    return False