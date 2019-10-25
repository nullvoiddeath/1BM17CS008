import sqlite3

conn = sqlite3.connect("./void.db")
c = conn.cursor()
create_table = """ 
CREATE TABLE Employee(
id integer PRIMARY KEY,
name text,
dept text,
sal integer);"""
c.execute(create_table)
print('Table Created! \nInserting values...');
insert_script = """
insert into Employee values(1,'Addie', 'Security', 5000);
insert into Employee values(2,'Void', 'Hacking', 10000);
insert into Employee values(3,'ZeroCode', 'VAPT', 8000);
insert into Employee values(4,'DarkByte', 'Malware Analysis', 15000);"""
c.executescript(insert_script)
conn.commit()
print('Table after inserting: \n')
c.execute("Select * from Employee");
row = c.fetchall()
for i in row:
	print(i)
id = int(input('Enter id of the employee: '))
ret_query = "select * from Employee where id = " + str(id) + ";"
c.execute(ret_query)
row = c.fetchall()
for i in row:
	print(i)
id = int(input('Enter id of the employee to update: '))
sal = int(input('Enter new salary: '))
upd_query = "update Employee set sal = " + str(sal) + " where id = " + str(id) + ";"
c.execute(upd_query)
conn.commit()
print('Table after updation: ')
c.execute("Select * from Employee");
row = c.fetchall()
for i in row:
        print(i)
id = int(input('Enter id of the employee to delete: '))
del_query = "delete from Employee where id = " + str(id) + ";"
c.execute(del_query)
print('Table after deletion: ')
c.execute("Select * from Employee");
row = c.fetchall()
for i in row:
        print(i)
