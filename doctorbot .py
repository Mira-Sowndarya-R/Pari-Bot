import sqlite3

conn = sqlite3.connect('hos.db')
#M represents today and T represents tomorrow
conn.execute('''CREATE TABLE IF NOT EXISTS M
         (NAME TEXT,SLOT1 INT,SLOT2 INT,SLOT3 INT);''')
print ("Table created successfully");
conn.execute("INSERT INTO M (NAME,SLOT1,SLOT2,SLOT3) \
      VALUES ('Dr.Allen',0,0,0 )");
conn.execute("INSERT INTO M (NAME,SLOT1,SLOT2,SLOT3) \
      VALUES ('Dr.Mishra',0,0,0 )");
conn.execute("INSERT INTO M (NAME,SLOT1,SLOT2,SLOT3) \
      VALUES ('Dr.John',0,0,0 )");
conn.commit()


conn.execute('''CREATE TABLE IF NOT EXISTS T
         (NAME TEXT,SLOT1 INT,SLOT2 INT,SLOT3 INT);''')
print ("Table created successfully");
conn.execute("INSERT INTO T (NAME,SLOT1,SLOT2,SLOT3) \
      VALUES ('Dr.Allen',0,0,0 )");
conn.execute("INSERT INTO T (NAME,SLOT1,SLOT2,SLOT3) \
      VALUES ('Dr.Mishra',0,0,0 )");
conn.execute("INSERT INTO T (NAME,SLOT1,SLOT2,SLOT3) \
      VALUES ('Dr.John',0,0,0 )");
conn.commit()


cursor = conn.execute("SELECT * FROM M")
for row in cursor:
   print ("DOCTOR = ", row[0])
   print ("SLOT1 = ", row[1])
   print ("SLOT2 = ", row[2])
   print ("SLOT3 = ", row[3], "\n")


cursor = conn.execute("SELECT * FROM T")
for row in cursor:
   print ("DOCTOR = ", row[0])
   print ("SLOT1 = ", row[1])
   print ("SLOT2 = ", row[2])
   print ("SLOT3 = ", row[3], "\n")
conn.close()
