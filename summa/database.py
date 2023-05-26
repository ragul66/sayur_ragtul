import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='Ragul.123',
    database='cafe'
)
mycursor=mydb.cursor()
# mycursor.execute("insert into cafeproduct values('tea',10)"))
# mycursor.execute("insert into cafeproduct values('coffee',15)")
# mycursor.execute("create table cafe(itemid varchar(30),itemname varchar(30),price int"

mycursor.execute("select * from cafeitems")

myresult=mycursor.fetchall()
for x in myresult:
    print(x)

print("Welcome to MOMOS cafe")
print("Items in Cafe")
for x in myresult:
    print(x[0])
# mycursor=mydb.cursor()
# mycursor.execute("select * from cafe_inventory")

# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor.execute


