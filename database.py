import mysql.connector

def ConnectorMysql():

    mydb = mysql.connector.connect(
            host="localhost",
            user="user",
            passwd="password",
            database="db",
    )
    return mydb

def get_data():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM user'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    result_list = []
    if len(myresult) > 0: 
        for x in myresult:
            data_dict = {
                "id": x[0],
                "email":  x[1],
                "fname":  x[3],
                "lname":  x[4]
            }
            result_list.append(data_dict)
    return result_list

def insert_data(body):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (email, password, fname, lname) VALUES (%s ,%s, %s, %s)"
    val = (body['email'], body['password'], body['fname'], body['lname'])
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()  

def delete_data(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "DELETE  FROM user WHERE id={}".format(_id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()