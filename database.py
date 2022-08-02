import pymysql as pm
con=pm.connect(host="localhost",user="root",password="",database="bank")


def openAc(CustomerName,AccountNumber,DateOfBirth,Contact,Address,Balance):
    cursor=con.cursor()
    SQLQuery="insert into account(CustomerName,AccountNumber,DateOfBirth,Contact,Address,Balance) values (%s,%s,%s,%s,%s,%s)"
    i=cursor.execute(SQLQuery,(CustomerName,AccountNumber,DateOfBirth,Contact,Address,Balance))
    con.commit()
    return i

def bal(AccountNumber):
    cursor=con.cursor()
    SQLQuery="select Balance from account where AccountNumber=%s"
    cursor.execute(SQLQuery,(AccountNumber))
    row=cursor.fetchone()
    return row

def displayAccount(CustomerName):
    cursor=con.cursor()
    SQLQuery="select * from account where CustomerName=%s"
    cursor.execute(SQLQuery,(CustomerName))
    row=cursor.fetchone()
    return row



def depam(am,AccountNumber):
    cursor=con.cursor()
    row=bal(AccountNumber)
    tam=int(row[0])+am
    SQLQuery="update account set Balance=%s where AccountNumber=%s"
    cursor.execute(SQLQuery,(tam,AccountNumber))
    con.commit()
    

def widram(am,AccountNumber):
    cursor=con.cursor()
    row=bal(AccountNumber)
    tam=int(row[0])-am
    if tam<0:
        return 0
    SQLQuery="update account set Balance=%s where AccountNumber=%s"
    cursor.execute(SQLQuery,(tam,AccountNumber))
    con.commit()


def display(AccountNumber):
    cursor=con.cursor()
    SQLQuery="select * from account where AccountNumber=%s"
    cursor.execute(SQLQuery,(AccountNumber))
    row=cursor.fetchone()
    return row
    

def clsac(AccountNumber):
    cursor=con.cursor()
    SQLQuery="delete from account where AccountNumber=%s"
    i=cursor.execute(SQLQuery,(AccountNumber))
    con.commit()
    return i

def all():
    cursor=con.cursor()
    SQLQuery="select * from account"
    cursor.execute(SQLQuery)
    rows=cursor.fetchall()
    return rows

def update(CustomerName,DateOfBirth,Contact,Address,Balance,AccountNumber):
    cursor=con.cursor()
    SQLQuery="update account set CustomerName=%s,DateOfBirth=%s,Contact=%s,Address=%s,Balance=%s where AccountNumber=%s"
    row=cursor.execute(SQLQuery,(CustomerName,DateOfBirth,Contact,Address,Balance,AccountNumber))
    con.commit()
    return row
