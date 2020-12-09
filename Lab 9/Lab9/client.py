from tkinter import *
import requests

BASE = "http://127.0.0.1:5000/"

user_ID = ""
text = ""
user_password = ""
destination = ""
new_id = ""
new_password_u = ""


def main(root):
    for widget in root.winfo_children():
        widget.destroy()

    signUp = Button(root, text="SignUp", command=lambda: sign(root))
    signUp.pack()

    logIn = Button(root, text="LogIn", command=lambda: put_id(root))
    logIn.pack()


def send():
    response = requests.get(BASE + f"server/{user_ID}/{user_password}/{retrieve_input()}/{send_to_input()}")
    global response_post
    response_post = requests.post(BASE + f"server/")
    print(response.json(), response_post)
    return response, response_post


def send_new():
    global new_id
    new_id = new_id_to_text.get()
    print(new_id)

    global new_password_u
    new_password_u = new_password_to_text.get()
    print(new_password_u)

    response_new = requests.get(BASE + f"server_new/{new_id}/{new_password_u}")
    print(response_new.json())

    return response_new


def sign(root):
    for widget in root.winfo_children():
        widget.destroy()

    sign_widget = Label(root, text="SignUn: ")
    sign_widget.pack()

    id_widget = Label(root, text="Enter your Login: ")
    id_widget.pack()

    global new_id_to_text
    new_id_to_text = StringVar()
    new_id_text = Entry(root, textvariable=new_id_to_text)
    new_id_text.pack()

    password_widget = Label(root, text="Enter your Password: ")
    password_widget.pack()

    global new_password_to_text
    new_password_to_text = StringVar()
    new_password_text = Entry(root, textvariable=new_password_to_text)
    new_password_text.pack()

    widg = Button(root, text="Enter", command=lambda: [send_new(), put_id(root)])
    widg.pack()

    widg_back = Button(root, text="Return", command=lambda: main(root))
    widg_back.pack()


def put_id(root):
    for widget in root.winfo_children():
        widget.destroy()

    log_in_widget = Label(root, text="LogIn: ")
    log_in_widget.pack()

    id_widget = Label(root, text="Enter your Login: ")
    id_widget.pack()

    global id_text
    id_text = Entry(root)
    id_text.pack()

    password_widget = Label(root, text="Enter your Password: ")
    password_widget.pack()

    global password_text
    password_text = Entry(root, show="*")
    password_text.pack()

    widg = Button(root, text="Enter", command=lambda: messenger(root))
    widg.pack()

    widg_back = Button(root, text="Return", command=lambda: main(root))
    widg_back.pack()


def retrieve_input():
    inputValue = new_message.get("1.0", "end-1c")
    return inputValue


def send_to_input():
    global destination
    destination = send_to_text.get()
    print(destination)
    return destination


def messenger(root):
    global user_ID
    user_ID = id_text.get()
    print(user_ID)

    global user_password
    user_password = password_text.get()
    print(user_password)

    for widget in root.winfo_children():
        widget.destroy()

    hello_widget = Label(root, text=f"Hello {user_ID}!!!")
    hello_widget.pack()

    if (user_ID != new_id and user_password != new_password_u) or (new_id == "" and new_password_u == ""):
        hello_widget = Label(root, text=f"LogIn not successful")
        hello_widget.pack()
    else:
        hello_widget = Label(root, text=f"LogIn successful")
        hello_widget.pack()


    global new_message
    new_message = Text(root, width=33, height=5)
    new_message.pack()

    btn = Button(root, text="Send", command=lambda: [send(), retrieve_input(), send_to_input()])
    btn.pack()

    lbl = Label(root, text="to user")
    lbl.pack()

    global send_to
    global send_to_text

    send_to_text = StringVar()
    send_to = Entry(root, textvariable=send_to_text)
    send_to.pack()

    widg_back = Button(root, text="LogOut", command=lambda: put_id(root))
    widg_back.pack()


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x350")
    main(root)
    # put_id(root)
    root.mainloop()
