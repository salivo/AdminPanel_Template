import sqlite3

connection = sqlite3.connect("server.db", check_same_thread=False)
cursor = connection.cursor()
res = cursor.execute("SELECT username FROM users")
users = res.fetchall()
toadd = input("type new admin username\n")
isintable = False
for user in users:
    if toadd in user:
        isintable = True
if isintable:
    new_level = int(input("set permission level\n"))
    cursor.execute("UPDATE users SET level = ? WHERE username = ?", (new_level, toadd))
    connection.commit()
    connection.close()
else:
    print("can't find username")