import datetime as d

gb = []
gno = 1

def findall()->list:
    return gb

def findone(gno:int):
    for lb in gb:
        if lb['gno']==gno:
            lb['ingi']=lb['ingi']+1
            return lb
    
def save(title:str, writer:str,content:str)->bool:
    global gno
    writeday = d.datetime.now().date()
    lb = dict(gno=gno, title=title, writer=writer, writeday=writeday, content=content)
    gb.append(lb)
    gno+=1
    return True

def delete(gno:int)->bool:
    for lb in gb:
        if lb['gno']==gno:
            gb.remove(lb)
            return True
    return False