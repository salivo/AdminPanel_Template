import sqlite3

connection = sqlite3.connect("server.db")
cursor = connection.cursor()
res = cursor.execute("SELECT name FROM sqlite_master")
tableslist = res.fetchone()
if tableslist == None:
    tableslist = ()
if not "users" in tableslist:
    print(".... Creating Table 'users' ....")
    # TODO: email verification
    cursor.execute("CREATE TABLE users(username, email, fullname, password, salt, verified, level)")
# res = cursor.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())  # shows list of tables 
res = cursor.execute("SELECT username FROM users")
print(res.fetchall())