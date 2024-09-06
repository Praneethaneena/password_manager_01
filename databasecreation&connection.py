
# ---------------Database Creation------------
import mysql.connect
db = mysql.connector.connect(host='localhost',user='root',passwd='root')
cur=db.cursor()
cur.execute("CREATE DATABASE password_manager")


#----------Table Creation----------
import mysql.connect
db = mysql.connector.connect(host='localhost',user='root', passwd='root',database="password_manager")
cur = db.cursor()
cur.execte(“CREATE TABLE useraccounts (userID int PRIMARY KEYAUTO_INCREMENT, Username VARCHAR(30), Password VARCHAR(30)”)
cur.execte(“CREATE TABLE userdata (Website VARCHAR(50), UsernameVARCHAR(30), Password VARCHAR(30), Email_id VARCHAR(30)” )

db.commit()
