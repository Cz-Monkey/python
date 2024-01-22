import datetime as date

guestbook = list()

gno = 1

def findall():
    return guestbook

def save(content:str, name:str):
    global gno
    writeday = date.datetime.now().date()
    gb = dict(gno=gno, name=name, content=content, writeday=writeday)
    guestbook.append(gb)
    gno+=1

def delete(gno:int):
    for gb in guestbook:
        if gb['gno'] == gno:
            guestbook.remove(gb)

def update(gno:int, content:str):
    for gb in guestbook:
        if gb['gno'] == gno:
            gb['content']==content
            break
            


            
            