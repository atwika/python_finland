import pymysql

con = pymysql.connect(host='localhost', user='root', port=3306, password='', database='db')

cursorObject = con.cursor()

sqlQuery = "CREATE TABLE Twitter (id int AUTO_INCREMENT PRIMARY KEY, tweet_id varchar(250) DEFAULT NULL, screen_name varchar(128) DEFAULT NULL, created_at timestamp NULL DEFAULT NULL, contenu text)"

cursorObject.execute(sqlQuery)
