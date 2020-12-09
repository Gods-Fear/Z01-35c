from tkinter import *
import requests


BASE = "http://127.0.0.1:5000/"

user_ID = 0
text = ""


def put_id(root):
    id_widget = Label(root, text="Enter your ID: ")
    id_widget.pack()
    global id_text
    id_text = Entry(root)
    id_text.pack()
    widg = Button(root, text="Enter", command=lambda: messenger(root))
    widg.pack()


def send():
    response = requests.get(BASE + f"server/{user_ID}/{retrieve_input()}, {send_to_input()}")
    print(response.json())
    return response


def retrieve_input():
    inputValue = new_message.get("1.0","end-1c")
    return inputValue


def send_to_input():
    inputValue = send_to.get()
    print(inputValue)
    return inputValue


def messenger(root):
    global user_ID
    user_ID = int(id_text.get())
    print(user_ID)
    for widget in root.winfo_children():
        widget.destroy()

    global new_message
    new_message = Text(root, width=33, height=5)
    new_message.grid(row=0, column=1)

    btn = Button(root, text="Send", command=lambda : [send(), retrieve_input(), send_to_input()])
    btn.grid(row=1, column=1)
    lbl = Label(root, text="to user ")
    lbl.grid(row=2, column=1)
    global send_to
    global send_to_text
    send_to_text = StringVar()
    send_to = Entry(root, textvariable=send_to_text)
    send_to.grid(row=3, column=1)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x350")
    put_id(root)
    root.mainloop()
    pass



