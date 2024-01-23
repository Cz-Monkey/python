# 게시판 dao 작성
board_list = []
bno = 1

# 게시판은 글번호, 제목, 내용, 글쓴이, 조회수로 구성

# save

def save(title:str, content:str, nickname:str)->bool:
    global bno
    bl = dict(bno=bno, title=title, content=content, nickname=nickname, readcnt=0)
    board_list.append(bl)
    bno+=1
    return True

def findall()->list:
    return board_list

def delete(bno:int)->bool:
    for bl in board_list:
        if bl['bno']==bno:
            board_list.remove(bl)
            return True
    return False