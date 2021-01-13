from flask import Flask
from flask_restful import Resource, Api
import pymysql


# variables
host = "localhost"
registration_login, registration_password = "", ""
entry_login, entry_password = "", ""
exist = False
users_list, status_list = [], []
user_status, status = "", ""
message_records = []
message_records_from = []
count_message = 0
count_list = []


class ClientsRegistration(Resource):
    def get(self, login, password):
        global registration_login, registration_password, exist
        registration_login, registration_password = login, password

        if user_exist_check(registration_login, registration_password):
            exist = True
            return exist
        else:
            exist = False
            add_users_to_db(registration_login, registration_password)
            return exist


class ClientsEntry(Resource):

    def get(self, login, password):
        global entry_login, entry_password, exist
        entry_login, entry_password = login, password
        if user_exist_check(entry_login, entry_password):
            exist = True
        else:
            exist = False

        return exist


# DATABASE
def create_table():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    myCursor.execute("DROP TABLE user;")
    myCursor.execute("""CREATE TABLE user
        (
        id int primary key,
        login varchar(20),
        password varchar(20),
        status varchar(20)
        )
        """)
    conn.commit()
    conn.close()


def add_users_to_db(login, password):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    sql = "INSERT INTO user(login, password) VALUES(%s, %s);"
    val = (login, password)
    myCursor.execute(sql, val)
    conn.commit()
    conn.close()


def user_exist_check(login, password):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    myCursor.execute(
        "SELECT login, COUNT(*) FROM user WHERE (login, password) = (%s, %s)   GROUP BY login, password",
        (login, password,)
    )

    row_count = myCursor.rowcount

    conn.close()
    if row_count == 0:
        return False
    else:
        return True


def get_users():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    sql = "SELECT * FROM user;"
    myCursor.execute(sql)
    records = myCursor.fetchall()
    global users_list
    users_list.clear()
    for user in records:
        users_list.append((user[1],  user[3]))
    conn.close()


def update_status(user_login, status_avl):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    sql = "UPDATE user SET status = %s WHERE login = %s;"
    val = (status_avl, user_login)
    myCursor.execute(sql, val)
    conn.commit()
    conn.close()


class CheckDB(Resource):
    def post(self):
        get_users()
        list_from_db = sorted(users_list, key=lambda x: x[1])
        return list_from_db


class ChangeStatus(Resource):
    def get(self, user_logged, login_status):
        update_status(user_logged, login_status)
        return {'user': user_logged, 'status': login_status}


def add_messages_to_db(user, to_user, message, data_time):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    sql = "INSERT INTO message(user, to_user, message, date_time) VALUES(%s, %s, %s, %s);"
    val = (user, to_user, message, data_time)
    myCursor.execute(sql, val)
    conn.commit()
    conn.close()


class Message(Resource):
    def get(self, user, to_user,  message, data_time):
        add_messages_to_db(user, to_user, message, data_time)
        return {'user': user, 'to_user': to_user, 'message': message, 'time': data_time}


def get_message(user, to_user):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()

    sql = "SELECT message, date_time FROM message WHERE (user, to_user) = (%s, %s);"
    val = (to_user, user)

    myCursor.execute(sql, val)

    records = myCursor.fetchall()
    print(records)
    global message_records
    message_records.clear()
    for message in records:
        message_records.append([to_user, message])
    conn.close()


def get_message_from(user, to_user):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()

    sql = "SELECT message, date_time FROM message WHERE (user, to_user) = (%s, %s);"
    val = (user, to_user)

    myCursor.execute(sql, val)
    records = myCursor.fetchall()
    global message_records
    message_records_from.clear()
    for message in records:
        message_records_from.append([user, message])
    conn.close()


class CheckMessage(Resource):
    def get(self, user, to_user):
        get_message_from(user, to_user)
        get_message(user, to_user)
        global message_records, message_records_from
        return [message_records, message_records_from]


def message_exist_check(user, to_user):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    sql = "SELECT count_message, COUNT(*) FROM count_msg WHERE (user, to_user) = (%s, %s) GROUP BY user, to_user;"
    val = (user, to_user)
    myCursor.execute(sql, val)
    print(user, to_user)
    row_count = myCursor.rowcount
    print(row_count)
    conn.close()

    if row_count == 0:
        return False
    else:
        return True


def update_count_message(user, to_user, count):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    print(f"Exist {message_exist_check(user, to_user)}")

    if message_exist_check(user, to_user) is True:
        sql = "UPDATE count_msg SET count_message = %s WHERE (user, to_user) = (%s, %s);"
        val = (count, user, to_user)
    else:
        sql = "INSERT INTO count_msg(user, to_user, count_message) VALUES(%s, %s, %s);"
        val = (user, to_user, count)

    myCursor.execute(sql, val)
    conn.commit()
    conn.close()


class UpdateCountMessage(Resource):
    def get(self, user, to_user, count):
        global count_message

        if count == 0:
            count_message = 0
        else:
            count_message += count

        update_count_message(user, to_user, count_message)
        return "Update was OK"


def get_count_msg():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='my_python')
    myCursor = conn.cursor()
    sql = "SELECT * FROM count_msg;"
    myCursor.execute(sql)
    records = myCursor.fetchall()
    global count_list
    count_list.clear()
    for user in records:
        count_list.append((user[0], user[1], user[2]))
    conn.close()


class CheckCountDB(Resource):
    def post(self):
        get_count_msg()
        return count_list


def create_api():
    api = Api(app)
    api.add_resource(ClientsRegistration, "/server_reg/<string:login>/<string:password>")
    api.add_resource(ClientsEntry, "/server_login/<string:login>/<string:password>")
    api.add_resource(ChangeStatus, "/login_status/<string:user_logged>/<string:login_status>")
    api.add_resource(CheckDB, "/check_db/")
    api.add_resource(Message, "/message/<string:user>/<string:to_user>/<string:message>/<string:data_time>")
    api.add_resource(CheckMessage, "/message_recv/<string:user>/<string:to_user>")
    api.add_resource(UpdateCountMessage, "/message_count/<string:user>/<string:to_user>/<int:count>")
    api.add_resource(CheckCountDB, "/check_count_db/")


# Create App
app = Flask(__name__)
create_api()

if __name__ == '__main__':
    app.run(debug=True)

