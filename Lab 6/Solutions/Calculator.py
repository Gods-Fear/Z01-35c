from tkinter import *
import math
import tkinter.messagebox

res_tree_str = ""
root = Tk()
root.geometry("650x400+300+300")
root.title("Calculator")

disp = Entry(root, font="Verdana 20", fg="black", bg="#6E6E6E", bd=0, justify=RIGHT, insertbackground="#6E6E6E",
             cursor="arrow")
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=True, fill=BOTH)


# Click for ROW 1
def btn_div_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '/')


def btn_brackets_r_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, ')')


def btn_brackets_l_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '(')


def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


# Click for ROW 2
def btn_mul_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '*')


def btn_9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn_8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn_7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn_fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


# Click for ROW 3
def btn_sub_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '-')


def btn_6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn_5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn_4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn_abs_clicked():
    try:
        ans = float(disp.get())
        ans = abs(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")


def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


# Click for ROW 4
def btn_plus_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '+')


def btn_3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn_2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn_1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn_log_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, 'Log(')


def btn_inverse_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    res = str(1 / float(disp.get()))
    disp.delete(0, END)
    disp.insert(pos, res)


# Click for ROW 5
def btn_dot_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '.')


def btn_0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def btn_ln_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, 'Ln(')


def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btn_c_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


# Calculate

def calculate():
    try:
        if disp.get() == '0':
            disp.delete(0, END)
            disp.insert(0, 'NaN')
        res = disp.get()

        if "Ln(" in str(res):
            sep_ln = res.split("Ln(")
            sep_end = str(sep_ln[1]).split(')')
            res_ln = math.log(float(eval(sep_end[0])))
            resultat = res.replace(f'Ln({sep_end[0]})', str(res_ln))
            res = resultat

        if "Log(" in str(res):
            sep_ln = res.split("Log(")
            sep_end = str(sep_ln[1]).split(')')
            res_ln = math.log(10, float(eval(sep_end[0])))
            resultat = res.replace(f'Log({sep_end[0]})', str(res_ln))
            res = resultat

        disp.delete(0, END)
        res_tree_str = eval(str(res))
        disp.insert(0, eval(str(res)))

    except Exception:
        disp.delete(0, END)
        res_tree_str = "NaN"
        disp.insert(0, "NaN")


# buttons ROW 1
row1 = Frame(root, bg="#000000")
row1.pack(expand=True, fill=BOTH)

btn_div = Button(row1, text="%", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=btn_div_clicked)
btn_div.pack(side=RIGHT, expand=True, fill=BOTH)

btn_bracts_r = Button(row1, text=")", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                      command=btn_brackets_r_clicked)
btn_bracts_r.pack(side=RIGHT, expand=True, fill=BOTH)

btn_bracts_l = Button(row1, text="(", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                      command=btn_brackets_l_clicked)
btn_bracts_l.pack(side=RIGHT, expand=True, fill=BOTH)

btn_power = Button(row1, text="x^y", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                   command=pow_clicked)
btn_power.pack(side=RIGHT, expand=True, fill=BOTH)

btn_e_pow = Button(row1, text="e^x", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5)
btn_e_pow.pack(side=RIGHT, expand=True, fill=BOTH)

btn_factorial = Button(row1, text="x!", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                       command=btn_fact_clicked)
btn_factorial.pack(side=RIGHT, expand=True, fill=BOTH)

# buttons ROW 2
row2 = Frame(root, bg="#000000")
row2.pack(expand=True, fill=BOTH)

btn_mul = Button(row2, text="x", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=btn_mul_clicked)
btn_mul.pack(side=RIGHT, expand=True, fill=BOTH)

btn_9 = Button(row2, text="9", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_9_clicked)
btn_9.pack(side=RIGHT, expand=True, fill=BOTH)

btn_8 = Button(row2, text="8", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_8_clicked)
btn_8.pack(side=RIGHT, expand=True, fill=BOTH)

btn_7 = Button(row2, text="7", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_7_clicked)
btn_7.pack(side=RIGHT, expand=True, fill=BOTH)

btn_sqrt = Button(row2, text="sqrt(x)", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                  command=sqr_clicked)
btn_sqrt.pack(side=RIGHT, expand=True, fill=BOTH)

btn_pi = Button(row2, text="π", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                command=pi_clicked)
btn_pi.pack(side=RIGHT, expand=True, fill=BOTH)

# buttons ROW 3
row3 = Frame(root, bg="#000000")
row3.pack(expand=True, fill=BOTH)

btn_sub = Button(row3, text="-", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=btn_sub_clicked)
btn_sub.pack(side=RIGHT, expand=True, fill=BOTH)

btn_6 = Button(row3, text="6", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_6_clicked)
btn_6.pack(side=RIGHT, expand=True, fill=BOTH)

btn_5 = Button(row3, text="5", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_5_clicked)
btn_5.pack(side=RIGHT, expand=True, fill=BOTH)

btn_4 = Button(row3, text="4", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_4_clicked)
btn_4.pack(side=RIGHT, expand=True, fill=BOTH)

btn_absolute = Button(row3, text="|x|", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                      command=btn_abs_clicked)
btn_absolute.pack(side=RIGHT, expand=True, fill=BOTH)

btn_e = Button(row3, text="e", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=e_clicked)
btn_e.pack(side=RIGHT, expand=True, fill=BOTH)

# buttons ROW 4
row4 = Frame(root, bg="#000000")
row4.pack(expand=True, fill=BOTH)

btn_plus = Button(row4, text="+", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                  command=btn_plus_clicked)
btn_plus.pack(side=RIGHT, expand=True, fill=BOTH)

btn_3 = Button(row4, text="3", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_3_clicked)
btn_3.pack(side=RIGHT, expand=True, fill=BOTH)

btn_2 = Button(row4, text="2", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_2_clicked)
btn_2.pack(side=RIGHT, expand=True, fill=BOTH)

btn_1 = Button(row4, text="1", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_1_clicked)
btn_1.pack(side=RIGHT, expand=True, fill=BOTH)

btn_log = Button(row4, text="Log(x)", font="Segoe 17", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=btn_log_clicked)
btn_log.pack(side=RIGHT, expand=True, fill=BOTH)

btn_inverse = Button(row4, text="x^-1", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                     command=btn_inverse_clicked)
btn_inverse.pack(side=RIGHT, expand=True, fill=BOTH)

# buttons ROW 5
row5 = Frame(root, bg="#000000")
row5.pack(expand=True, fill=BOTH)

btn_eql = Button(row5, text="=", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=calculate)
btn_eql.pack(side=RIGHT, expand=True, fill=BOTH)

btn_dot = Button(row5, text=".", font="Segoe 20", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=btn_dot_clicked)
btn_dot.pack(side=RIGHT, expand=True, fill=BOTH)

btn_0 = Button(row5, text="0", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
               command=btn_0_clicked)
btn_0.pack(side=RIGHT, expand=True, fill=BOTH)

btn_clear = Button(row5, text="C", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                   command=btn_c_clicked)
btn_clear.pack(side=RIGHT, expand=True, fill=BOTH)

btn_Ln = Button(row5, text="ln", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                command=btn_ln_clicked)
btn_Ln.pack(side=RIGHT, expand=True, fill=BOTH)

btn_mod = Button(row5, text="mod", font="Segoe 18", relief=GROOVE, bd=0, fg="white", bg="#333333", width=5,
                 command=mod_clicked)
btn_mod.pack(side=RIGHT, expand=True, fill=BOTH)

root.mainloop()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def treeToString():
    root: Node
    res = res_tree_str.split()

    for x in res:
        root.data = x
        if x == '-' or x == '+' or x == '(' or x == ')' or x == 'Log(' or x == '!' or x == '/'or x == '*' or x == '**':
            root.right = x
        else:
            root.left = x

    def PrintTree():
        if root.left:
            root.left.PrintTree()
        print(root.data),
        if root.right:
            root.right.PrintTree()