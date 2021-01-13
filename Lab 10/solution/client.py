from tkinter import *
import requests
import asyncio
import websockets
from datetime import datetime
from win10toast import ToastNotifier


# Server
BASE = "http://localhost:5000/"
toaster = ToastNotifier()

# variables
registration_login, registration_password = "", ""
entry_login, entry_password = "", ""
exist, registered_user = False, False
users_list, count_list = [], []
message_records = []
recv_msg_spl, to_user_count_msg, count_msg, user_sent = "", "", "", ""
login_status, user_logged = "", ""


def send_registration():
    response = requests.get(BASE + f"server_reg/{registration_login.get()}/{registration_password.get()}")
    print(response.json())
    global registered_user
    registered_user = response.json()
    return response


def inform_new_user_registered(user):
    async def message():
        async with websockets.connect("ws://localhost:1234/") as socket:
            msg = f'New user: {user} was registered'
            await socket.send(msg)
            recv_msg = await socket.recv()
            print(recv_msg)

    asyncio.get_event_loop().run_until_complete(message())


def send_login():
    response = requests.get(BASE + f"server_login/{entry_login.get()}/{entry_password.get()}")
    print(response.json())
    global exist
    exist = response.json()
    return response


def main(root):
    for widget in root.winfo_children():
        widget.destroy()

    welcome_lable = Label(root, text="Welcome to PyMessenger", pady=15, font=("Segoe UI", 20))
    welcome_lable.pack()

    signUp = Button(root, text="SignUp", command=lambda: signup(root), width=10)
    signUp.pack()

    logIn = Button(root, text="LogIn", command=lambda: login(root), width=10)
    logIn.pack()


def signup(root):
    for widget in root.winfo_children():
        widget.destroy()

    sign_widget = Label(root, text="Registration", font=("Segoe UI", 20))
    sign_widget.pack()

    id_widget = Label(root, text="Enter your Login: ", pady=10)
    id_widget.pack()

    global registration_login
    registration_login = StringVar()
    registration_login_text = Entry(root, textvariable=registration_login)
    registration_login_text.pack()

    password_widget = Label(root, text="Enter your Password: ", pady=10)
    password_widget.pack()

    global registration_password
    registration_password = StringVar()
    registration_password_text = Entry(root, textvariable=registration_password)
    registration_password_text.pack()

    widg = Button(root, text="Enter", command=lambda: [send_registration(), registration_completed(root)
    if registered_user is False else registration_not_completed(root), inform_new_user_registered(registration_login.get())], width=10)
    widg.pack()

    widg_back = Button(root, text="Return", command=lambda: main(root), width=10)
    widg_back.pack()


def registration_completed(root):
    for widget in root.winfo_children():
        widget.destroy()

    registration_completed_widget = Label(root, text="Registration completed successfully", font=("Segoe UI", 20))
    registration_completed_widget.pack()

    widg_back = Button(root, text="Return", command=lambda: main(root), width=10)
    widg_back.pack()


def registration_not_completed(root):
    for widget in root.winfo_children():
        widget.destroy()

    registration_not_completed_widget = Label(root, text="Registration not completed! \n This user is registered",
                                              font=("Segoe UI", 20))
    registration_not_completed_widget.pack()

    widg_back = Button(root, text="Return", command=lambda: main(root), width=10)
    widg_back.pack()


def login(root):
    for widget in root.winfo_children():
        widget.destroy()

    login_widget = Label(root, text="LogIn", font=("Segoe UI", 20))
    login_widget.pack()

    id_widget = Label(root, text="Enter your Login: ", pady=10)
    id_widget.pack()

    global entry_login
    entry_login = StringVar()
    entry_login_text = Entry(root, textvariable=entry_login)
    entry_login_text.pack()

    password_widget = Label(root, text="Enter your Password: ", pady=10)
    password_widget.pack()

    global entry_password
    entry_password = StringVar()
    entry_password_text = Entry(root, textvariable=entry_password, show="*")
    entry_password_text.pack()

    widg = Button(root, text="Enter", command=lambda: [send_login(),
                                                       check_logged_users(entry_login.get(), True),
                                                       login_not_exist(root) if exist is False else [login_status_ch(),
                                                                                                     main_page(root)]],
                  width=10)
    widg.pack()

    widg_back = Button(root, text="Return", command=lambda: main(root), width=10)
    widg_back.pack()


def login_not_exist(root):
    for widget in root.winfo_children():
        widget.destroy()

    login_error_widget = Label(root, text="This user does not exist \n"
                                          " Please check your login or password and try again", font=("Segoe UI", 20))
    login_error_widget.pack()

    widg_back = Button(root, text="Return", command=lambda: login(root), width=10)
    widg_back.pack()


def refresh_main_page(self):
    for widget in self.winfo_children():
        widget.destroy()

    main_page(root)


def main_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    greeting_widget = Label(root, text=f"Hello {entry_login.get()}!!!", font=("Segoe UI", 20), pady=10)
    greeting_widget.pack()

    users_listbox = Listbox(root, bd=2, width=50, font=("Segoe UI", 12))
    users_listbox.pack(pady=15)

    check_db()
    get_count_msg()

    def select_item_listbox():
        if users_listbox.get(ANCHOR):
            split_user = users_listbox.get(ANCHOR).split(" ")
            messages_page(root, split_user[0])
            selection_update_count(split_user[0], entry_login.get(), 0)

    print(f'Count list :{count_list}')

    for user in users_list:
        if user[0] != entry_login.get():
            for msg in count_list:
                if msg[1] == entry_login.get():
                    if user[0] == msg[0]:
                        users_listbox.insert(END, user[0] + " " + user[1] + " " + str(msg[2]))

    # for user in users_list:
    #     if user[0] != entry_login.get():
    #             users_listbox.insert(END, user[0] + " " + user[1] + " 0")

    select_btn = Button(root, text="Select", command=lambda: select_item_listbox(), width=10)
    select_btn.pack()

    refresh_btn = Button(root, text="Refresh", command=lambda: refresh_main_page(root), width=10)
    refresh_btn.pack()

    logout = Button(root, text="LogOut", command=lambda: [main(root), check_logged_users(entry_login.get(), False),
                                                          login_status_ch()],
                    width=10)
    logout.pack()


def get_count_msg():
    response = requests.post(BASE + f"check_count_db/")
    print(response.json())
    global count_list
    count_list = response.json()
    return response


def selection_update_count(user, to_user, count):
    response = requests.get(BASE + f"message_count/{user}/{to_user}/{count}")
    print(response.json())

    async def message():
        async with websockets.connect("ws://localhost:1222/") as socket:
            msg = f'User: {to_user} read a message'
            await socket.send(msg)
            recv_msg = await socket.recv()
            print(recv_msg)

    asyncio.get_event_loop().run_until_complete(message())

    return response


def check_db():
    response = requests.post(BASE + f"check_db/")
    print(response.json())
    global users_list
    users_list = response.json()
    return response


def check_logged_users(user, status):
    async def message():
        async with websockets.connect("ws://localhost:12345/") as socket:
            msg = f'{user},{status}'
            await socket.send(msg)
            recv_msg = await socket.recv()
            recv_msg_spl = recv_msg.split()
            global login_status, user_logged
            login_status = recv_msg_spl[-1]
            user_logged = recv_msg_spl[1]

    asyncio.get_event_loop().run_until_complete(message())


def login_status_ch():
    status = 'Not Available'

    if login_status == "True":
        status = 'Available'

    response = requests.get(BASE + f"login_status/{user_logged}/{status}")
    print(response.json())
    return response


def messages_page(root, user):
    for widget in root.winfo_children():
        widget.destroy()

    # variables
    a = 0
    b = 1
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y %H:%M:%S")

    # page
    greeting_widget = Label(root, text=f"Conversation with {user}", font=("Segoe UI", 20), pady=5)
    greeting_widget.grid(row=0, column=0)

    main_frame = LabelFrame(root, width=500)

    my_canvas = Canvas(main_frame, width=500)
    my_canvas.grid(row=1, column=0, pady=10)

    my_scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scroll.grid(row=1, column=1, sticky=NSEW, pady=10)

    my_canvas.configure(yscrollcommand=my_scroll.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    second_frame = Frame(my_canvas, width=500)

    my_canvas.create_window((0, 0), window=second_frame, width=500)

    main_frame.grid()

    recv_message(entry_login.get(), user)

    get_count_msg()

    print(count_list)
    user_read = ''

    for x in count_list:
        if x[1] == user and x[0] == entry_login.get():
            if x[2] == 0:
                user_read = '✓'
            else:
                user_read = ''

    for record in message_records:
        for x in record:
            a += 1
            b += 1
            if x[0] == entry_login.get():
                Label(second_frame, text=f'{x[0]} ({x[1][1]}): {x[1][0]} {user_read}', font=('Helvetica', 10, 'bold'))\
                    .grid(row=a, column=1, pady=10)
            else:
                Label(second_frame, text=f'{x[0]} ({x[1][1]}): {x[1][0]} {user_read}').grid(row=b, column=0, pady=10)

    message_txt = StringVar()
    txt_your_message = Entry(root, textvariable=message_txt, width=50)
    txt_your_message.grid(row=2, column=0, pady=10)

    btn_send_message = Button(root, text="Send", width=10,
                              command=lambda: [Label(second_frame, text=f'You: {message_txt.get()}').grid(column=1),
                                               send_message(entry_login.get(), user,
                                                            message_txt.get(), dt_string),
                                               send_count_message(entry_login.get(), user, 1)])
    btn_send_message.grid(row=3, column=0)

    widg_back = Button(root, text="Return", command=lambda: main_page(root), width=10)
    widg_back.grid(row=4, column=0)


def send_message(user, to_user, message, data_time):
    response = requests.get(BASE + f"message/{user}/{to_user}/{message}/{data_time}")
    print(response.json())
    return response


def send_count_message(user, to_user, count):
    async def message():
        async with websockets.connect("ws://localhost:55555/") as socket:
            msg = f'{user},{to_user},{count}'
            await socket.send(msg)
            recv_msg = await socket.recv()
            global recv_msg_spl
            recv_msg_spl = recv_msg.split(',')
            global user_sent, to_user_count_msg, count_msg
            user_sent = recv_msg_spl[0]
            to_user_count_msg = recv_msg_spl[1]
            count_msg = recv_msg_spl[2]

            print(f"User_sent: {user_sent}", f"to_user_count_msg: {to_user_count_msg}", f"count_msg: {count_msg}")

    asyncio.get_event_loop().run_until_complete(message())

    response = requests.get(BASE + f"message_count/{user}/{to_user}/{count}")
    print(response.json())
    return response


def recv_message(user, to_user):
    response = requests.get(BASE + f"message_recv/{user}/{to_user}")
    global message_records
    print(response.json())
    message_records = response.json()
    return response


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x430")
    root.title("PyMessenger")
    main(root)
    root.mainloop()
