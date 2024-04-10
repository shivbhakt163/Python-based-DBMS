dbs = {'test1': {'students': [['name', 'class', 'roll'], ['aryan', 'xii', '10']], 'xyz': [['g_name', 'p_name', 'win_score'], ['ludo', 'aryan', '2'], ['ludo', 'vansh', '3']]}}
def create_db(dbs):
    dbnm = str(input("  -> Enter the database name : "))
    dbs[dbnm] = {}
    return dbs
def drop_table(dbs,dbnm):
    tb_nm = str(input("  -> Enter the table name : "))
    if tb_nm in dbs[dbnm].keys():
        dbs[dbnm].pop(tb_nm)
        return dbs
    else:
        print("PQl> TABLE DOES NOT EXIST !!")
        return dbs
def drop_db(dbs):
    dbnm = str(input("  -> Enter the database name : "))
    if dbnm in dbs.keys():
        dbs.pop(dbnm)
        print("PQL> DATABASE SUCCESSFULLY REMOVED !!")
    else:
        print("PQl> DATABASE DOES NOT EXIST !!")
    return dbs
def create_tbl(dbs,dbnm):
    tblnm = str(input("  -> Enter the table name : "))
    lt = []
    N = int(input("  -> Enter the number of records : N(integer value needed only) = "))
    a = 0
    i=0
    while i<=N:
        if i==0:
            attr = str(input("  -> Enter the attributes as in the given way : "))
            t = [x.strip() for x in attr.split(",")]
            a = a+len(t)
            lt.append(t)
        else:
            st = str(input("  -> Enter the rec : "))
            l = [x.strip() for x in st.split(",")]
            if len(l)==a:
                lt.append(l)
            else:
                print("PQl> RECORD EXCEEDS THE ATTRIBUTE SIZE !, RECORD NOT ACCEPTED.")
                pass
        i+=1
    dbs[dbnm][tblnm] = lt
    return dbs
def add_rec(dbs,dbnm,table):
    n = int(len((dbs[dbnm][table])[0]))
    c = ""
    for i in (dbs[dbnm][table])[0]:
        c = c+" "+i
    print("PQl> ATTr(s) : ",c)
    print(f"PQl> MAXIMUM ATTr = {n}")
    M = int(input("  -> No. of records to append : NR(integer value needed only) = "))
    lr = []
    for i in range(M):
        if i == 0:
            rec = str(input("PQl> Enter the record : => "))
            t = [x.strip() for x in rec.split(",")]
            if len(t) == n:
                lr.append(t)
            else:
                print("PQl> RECORD EXCEEDS THE ATTRIBUTE SIZE !, RECORD NOT ACCEPTED.")
                pass
        else:
            rec = str(input("  -> Enter the record : => "))
            t1 = [x.strip() for x in rec.split(",")]
            if len(t1)==n:
                lr.append(t1)
            else:
                print("PQl> RECORD EXCEEDS THE ATTRIBUTE SIZE !, RECORD NOT ACCEPTED.")
                pass
    lc = (dbs[dbnm][table])
    lt = lc+lr
    dbs[dbnm][table] = lt
    return dbs
def del_rec(dbs,dbnm,table):
    n = int(len((dbs[dbnm][table])[0]))
    c = ""
    for i in (dbs[dbnm][table])[0]:
        c = c+","+i
    print("PQl> ATTr(s) : ",c)
    print(f"PQl> MAXIMUM ATTr(COLUMNS) = {n}")
    print("PQl> SHOWING ALL COLUMNS FOR SELECTION ⬇")
    for i in range(len(dbs[dbnm][table])):
        if i==0:
            continue
        else:
            print("  -> ",(dbs[dbnm][table])[i])
    K = int(input("PQl> Enter the no. of records to remove : NR(integer value needed only) = "))
    dr = []
    for j in range(K):
        if j == 0:
            rec = str(input("PQl> Enter the record to be deleted : => "))
            dr.append([x.strip() for x in rec.split(",")])
        else:
            rec = str(input("  ->                                : => "))
            dr.append([x.strip() for x in rec.split(",")])
    rl = (dbs[dbnm][table])
    for k in dr:
        if k in rl:
            rl.remove(k)
        else:
            pass
    dbs[dbnm][table] = rl
    return dbs
def view_table(dbs,dbnm,tbnm):
    l = dbs[dbnm][tbnm]
    l1 = []
    for i in range(len(l[0])):
        l2 = []
        for j in l:
            l2.append(j[i])
        l1.append(l2)
    l3 = []
    for i in l1:
        l3.append(len(max(i,key = len)))
    d = ""
    for j in l3:
        d = d+"+"+"-"*(j+1)
    d = d+"+"
    c = d+"\n"
    for i in range(len(l)):
        for j in range(len(l[0])):
            c=c+"|"+l[i][j]+" "*(l3[j]-len(l[i][j])+1)
        if i==0:
            c=c+'|\n'+d+"\n"
        else:
            c=c+'|\n'
    c=c+d
    return c
import time as tm
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PQl-Monitor-Server")
print("PQl Monitor version - 1.0.0(Type - - FREE OPEN SOURCE SOFTWARE - - publicaly available on github)\nCommunity Software Developed By - Aryan Saraswat\nRelease date - 09-04-2024, 23:49, TUESDAY. Developers' Github Profile - https://github.com/shivbhakt163 \n")
print("Software downloaded through - https://github.com/shivbhakt163/Python-based-DBMS")
print("TO INPUT A RECORD FOLLOW THIS FORMAT - (PQl> Enter the rec : a1, a2, a3, a4, ... ,aN)\nCOMMANDS HERE END WITH ';'. REACH THE DEVELOPER THROUGH ⬇\naryansaraswatepi163@gmail.com")
print()
print("FOR EXTERNAL HELP TYPE : help; or Hlp;")
print()
while True:
    q = input("PQl> ")
    if q.lower()=="create db;":
        dbs1 = create_db(dbs)
        with open("PQl_User_Server.py",'r') as f:
            l = f.readlines()
        l[0] = f"dbs = {dbs1}\n"
        with open("PQl_User_Server.py",'w') as f1:
            f1.writelines(l)
        print("PQl> DATABASE CREATED!")
    elif q.lower() == "create table;":
        dbnm = str(input("PQl> Enter db_name = "))
        if dbnm in dbs.keys():
            dbs2 = create_tbl(dbs,dbnm)
            with open("PQl_User_Server.py",'r') as f2:
                l1 = f2.readlines()
            l1[0] = f"dbs = {dbs2}\n"
            with open("PQl_User_Server.py",'w') as f3:
                f3.writelines(l1)
            print("PQl> TABLE CREATED!")
        else:
            print("PQl> DATABASE DOES NOT EXIST!")
    elif q.lower() == "show dbs;":
        print("PQl> SHOWING ALL DATABASES ⬇")
        for k in dbs.keys():
            print("  -> ",k)
    elif q.lower() == "show tables;":
        print("PQl> PLEASE SELECT A DATABASE :")
        db_nm = str(input("PQl> Enter the db_name = "))
        if db_nm in dbs.keys():
            print(f"PQl> SHOWING ALL TABLES IN {db_nm} ⬇")
            for k in dbs[db_nm].keys():
                print("  -> ",k)
        else:
            print("PQl> DATABASE DOES NOT EXIST !!")
    elif q.lower() == "add record;":
        print("PQl> PLEASE SPECIFY THE DATABASE ⬇")
        db_nm1 = str(input("  -> db_name = "))
        if db_nm1 in dbs.keys():
            print("PQl> PLEASE SPECIFY THE TABLE ⬇")
            tb_nm = str(input("  -> tbl_name = "))
            if tb_nm in dbs[db_nm1].keys():
                dbs3 = add_rec(dbs,db_nm1,tb_nm)
                with open("PQl_User_Server.py","r") as f4:
                    l4 = f4.readlines()
                l4[0] = f"dbs = {dbs3}\n"
                with open("PQl_User_Server.py","w") as f5:
                    f5.writelines(l4)
                print("PQl> RECORD SUCCESSFULLY ADDED!")
            else:
                print("PQl> TABLE DOES NOT EXIST !!")
        else:
            print("PQl> DATABASE DOES NOT EXIST !!")
    elif q.lower() == "del record;":
        print("PQl> PLEASE SPECIFY THE DATABASE ⬇")
        db_nm2 = str(input("  -> db_name = "))
        if db_nm2 in dbs.keys():
            print("PQl> PLEASE SPECIFY THE TABLE ⬇")
            tb_nm1 = str(input("  -> tbl_name = "))
            if tb_nm1 in dbs[db_nm2].keys():
                dbs4 = del_rec(dbs,db_nm2,tb_nm1)
                with open("PQl_User_Server.py","r") as f6:
                    l5 = f6.readlines()
                l5[0] = f"dbs = {dbs4}\n"
                with open("PQl_User_Server.py","w") as f7:
                    f7.writelines(l5)
                print("PQl> RECORDS DELETED SUCCESSFULLY !!")
            else:
                print("PQl> TABLE DOES NOT EXIST!")
        else:
            print("PQl> DATABASE DOES NOT EXIST!")
    elif q.lower() == "drop db;":
        print("PQl> PLEASE SPECIFY THE DATABASE NAME ⬇")
        dbsd = drop_db(dbs)
        with open("PQl_User_Server.py","r") as f8:
            l6 = f8.readlines()
        l6[0] = f"dbs = {dbsd}\n"
        with open("PQl_User_Server.py","w") as f9:
            f9.writelines(l6)
        print("PQl> TASK COMPLETE !")
    elif q.lower() == "drop table;":
        print("PQl> PLEASE SPECIFY THE DATABASE NAME ⬇")
        db_nm4 = str(input("  -> db_name = "))
        if db_nm4 in dbs.keys():
            dbst = drop_table(dbs,db_nm4)
            with open("PQl_User_Server.py","r") as f10:
                l7 = f10.readlines()
            l7[0] = f"dbs = {dbst}\n"
            with open("PQl_User_Server.py","w") as f11:
                f11.writelines(l7)
            print("PQl> TASK COMPLETE !")
        else:
            print("PQl> DATABASE DOES NOT EXIST !!")
    elif q.lower() == "view table;":
        print("PQl> PLEASE SPECIFY THE DATABASE ⬇")
        db_nm3 = str(input("  -> db_name = "))
        if db_nm3 in dbs.keys():
            print("PQl> PLEASE SPECIFY THE TABLE ⬇")
            tb_nm2 = str(input("  -> tbl_name = "))
            if tb_nm2 in dbs[db_nm3].keys():
                table = view_table(dbs,db_nm3,tb_nm2)
                print("PQl> TABLE LOADED ⬇")
                print(table)
            else:
                print("PQL> TABLE DOES NOT EXIST !!")
        else:
            print("PQL> DATABASE DOES NOT EXIST !!") 
    elif q.lower() == "help;" or q.lower() == "Hlp;":
        print("PQl> ALL KNOWN PQl COMMANDS ARE ⬇")
        print("PQl> CREATE DB;")
        print("  -> CREATE TABLE;")
        print("  -> DROP DB;")
        print("  -> VIEW TABLE;")
        print("  -> e;")
        print("  -> ADD RECORD;")
        print("  -> DEL RECORD;")
        print("  -> SHOW DBS;")
        print("  -> SHOW TABLES;")
    elif q.lower() == "e;":
        break
    else:
        print("PQl> COMMAND NOT RECOGNISED!!")
        continue
print("PQl> DBMS closed!!")
tm.sleep(8)
