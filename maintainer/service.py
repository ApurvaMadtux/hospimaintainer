#contains business  
from maintainer import dao


def sort_records():
    headers = []
    data = []
    rows = dao.read_file()
    if len(rows) > 1 :
        for row in rows:
            r = row.split('|')
            if r[1]=='H':
                headers = r[2:]
            elif r[1]=='D':
                data.append(r[2:]) 

def store_records():
    dao.insert(sort_records())

    
def create_table():
    dao.create_table()