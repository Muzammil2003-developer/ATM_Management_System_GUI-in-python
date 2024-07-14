import tkinter.messagebox
from tkinter import *
screen =Tk()
screen.geometry("620x560")
space=" "
done=space*77
screen.title(done+"MBL-ATM MACHINE")
screen.config(bg="Gray")
screen.minsize(width=620, height=560)
screen.maxsize(width=620, height=560)

#================================================Function Arrow Buttons   (WITHDRAW)==============

def arrow_5000():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n\n\n")
    screen.txtReceipt.insert(END, "Process Successfully Done\n\n")
    screen.txtReceipt.insert(END, "5000 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)
def arrow_10000():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n\n\n")
    screen.txtReceipt.insert(END, "Process Successfully Done\n\n")
    screen.txtReceipt.insert(END, "10000 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="gredimGrayy", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)

def arrow_15000():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n\n\n")
    screen.txtReceipt.insert(END, "Process Successfully Done\n\n")
    screen.txtReceipt.insert(END, "15000 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)

def arrow_20000():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n\n\n")
    screen.txtReceipt.insert(END, "Process Successfully Done\n\n")
    screen.txtReceipt.insert(END, "20000 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")
    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)

def arrow_500():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n\n\n")
    screen.txtReceipt.insert(END, "Process Successfully Done\n\n")
    screen.txtReceipt.insert(END, "500 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)

def arrow_1500():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n\n\n")
    screen.txtReceipt.insert(END, "Process Successfully Done\n\n")
    screen.txtReceipt.insert(END, "1500 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)

def arrow_2000():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited\n")
    screen.txtReceipt.insert(END, "\n\nProcess Successfully Done\n\n")
    screen.txtReceipt.insert(END, "2000 amount Withdraw")
    screen.txtReceipt.insert(END, "\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)
def back():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.delete("1.0", END)

    screen.txtReceipt.insert(END, "\t\tWELCOME\n\n\n")
    screen.txtReceipt.insert(END, "Withdraw\t\t\t\tNew PIN\n\n\n")
    screen.txtReceipt.insert(END, "Deposit\t\t\t\tHistory\n\n\n\n")
    screen.txtReceipt.insert(END, "Balance Inquairy\n\n\n\n")
    screen.txtReceipt.insert(END, "Log Out")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_1)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_2)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_3)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_4)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=NORMAL, command=new_p)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=NORMAL, command=hist)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_4R.grid(row=3, column=0)


#================================================Function Arrow Buttons==============

def arrow_1():
    but_enter()
#    global amount
#    amount =150000
    screen.txtReceipt.delete("1.0", END)
    #screen.txtReceipt.insert(END,"Enter Amount You Want to withdraw\n\n")
    value = screen.txtReceipt.get("1.0", "end-1c")
    if value==str(value):
        screen.txtReceipt.insert(END,"\t\tWithdraw\n\n\n")
        screen.txtReceipt.insert(END,"5000 \t\t\t\t  500\n\n\n")
        screen.txtReceipt.insert(END,"10000\t\t\t\t  1500\n\n\n\n")
        screen.txtReceipt.insert(END,"15000\t\t\t\t  2000\n\n\n\n")
        screen.txtReceipt.insert(END,"20000\t\t\t\t  Back")

        but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_5000)
        but_side_1L.grid(row=0, column=0)
        but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_10000)
        but_side_2L.grid(row=1, column=0)
        but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_15000)
        but_side_3L.grid(row=2, column=0)
        but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_20000)
        but_side_4L.grid(row=3, column=0)

        but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_500)
        but_side_1R.grid(row=0, column=0)
        but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_1500)
        but_side_2R.grid(row=1, column=0)
        but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_2000)
        but_side_3R.grid(row=2, column=0)
        but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
        but_side_4R.grid(row=3, column=0)

def arrow_2():
    but_enter()
#    global amount
#    amount =150000
    screen.txtReceipt.delete("1.0", END)
    am_wd=screen.txtReceipt.focus_set()
    screen.txtReceipt.get("1.0", "end-1c")

    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited")
    screen.txtReceipt.insert(END, "\n\nAmount Deposit:\n\n")
    screen.txtReceipt.insert(END, "Sorry!\n   Option of Amount deposit is not\nworking here due to technical Problem")
    screen.txtReceipt.insert(END, "\n\nThanks for Choosing us")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)


def arrow_3():
    but_enter()
#    global amount
#    amount =150000
    screen.txtReceipt.delete("1.0", END)
    am_wd=screen.txtReceipt.focus_set()
    screen.txtReceipt.get("1.0", "end-1c")
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited")
    screen.txtReceipt.insert(END,"\n\nProcess Completed\n")
    screen.txtReceipt.insert(END,"\nYour Present balanced is 150000")
    screen.txtReceipt.insert(END, "\n\nThanks for Choosing us")


    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_5000)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_10000)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_15000)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_20000)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_500)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_1500)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED, command=arrow_2000)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)
def arrow_4():

    cancel=tkinter.messagebox.askyesno("ATM","Confirm If you want to Log Out")
    if cancel>0:
        screen.txtReceipt.delete("1.0", END)
        screen.txtReceipt.delete("1.0", END)
        but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_1L.grid(row=0, column=0)
        but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_2L.grid(row=1, column=0)
        but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_3L.grid(row=2, column=0)
        but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_4L.grid(row=3, column=0)

        but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_1R.grid(row=0, column=0)
        but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_2R.grid(row=1, column=0)
        but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_3R.grid(row=2, column=0)
        but_side_4R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
        but_side_4R.grid(row=3, column=0)

   #     but_enter()
        return

def new_p():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited")
    screen.txtReceipt.insert(END,"\n\nProcess Completed\n")
    screen.txtReceipt.insert(END,"Your new PIN is generated.\nWe will send you through E-mail")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=DISABLED)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=DISABLED)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=DISABLED)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)


def hist():
    screen.txtReceipt.delete("1.0", END)
    screen.txtReceipt.insert(END,"\t MBL  Mughlia Bank Limited")
    screen.txtReceipt.insert(END,"\n\nProcess Completed\n")
    screen.txtReceipt.insert(END,"\t\tWe will send you Your\t\nTransaction History through Email.\n    Thanks")

    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="Back", width=15, height=3, bg="dimGray", state=NORMAL, command=back)
    but_side_4R.grid(row=3, column=0)
#==========================================FUNCTIONS=================

def but1():
    value1=1
    screen.txtReceipt.insert(END,value1)

def but2():
    value2=2
    screen.txtReceipt.insert(END,value2)

def but3():
    value3=3
    screen.txtReceipt.insert(END,value3)
def but4():
    value4=4
    screen.txtReceipt.insert(END,value4)
def but5():
    value5=5
    screen.txtReceipt.insert(END,value5)
def but6():
    value6=6
    screen.txtReceipt.insert(END,value6)

def but7():
    value7=7
    screen.txtReceipt.insert(END,value7)

def but8():
    value8=8
    screen.txtReceipt.insert(END,value8)
def but9():
    value9=9
    screen.txtReceipt.insert(END,value9)
def but0():
    value0=0
    screen.txtReceipt.insert(END, value0)

#=================================================function Buttons=============================

def but_exit():
    cancel=tkinter.messagebox.askyesno("ATM","Confirm If you want to cancel")
    if cancel>0:
        screen.destroy()
        return
def but_enter():
    #screen.txtReceipt.insert(END,"Enter Your PIN")
    pin_No =screen.txtReceipt.get("1.0","end-1c")
    if (pin_No==str("4567")):
        screen.txtReceipt.delete("1.0",END)

        screen.txtReceipt.insert(END, "\t\tWELCOME\n\n\n")
        screen.txtReceipt.insert(END, "Withdraw\t\t\t\tNew PIN\n\n\n")
        screen.txtReceipt.insert(END, "Deposit\t\t\t\tHistory\n\n\n\n")
        screen.txtReceipt.insert(END, "Balance Inquairy\n\n\n\n")
        screen.txtReceipt.insert(END, "Log Out")

        but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=NORMAL, command=arrow_1 )
        but_side_1L.grid(row=0, column=0)
        but_side_2L= Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=NORMAL, command=arrow_2)
        but_side_2L.grid(row=1, column=0)
        but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=NORMAL, command=arrow_3)
        but_side_3L.grid(row=2, column=0)
        but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=NORMAL, command=arrow_4)
        but_side_4L.grid(row=3, column=0)

        but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray",state=NORMAL, command=new_p)
        but_side_1R.grid(row=0, column=0)
        but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray",state=NORMAL, command=hist)
        but_side_2R.grid(row=1, column=0)
        but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray",state=DISABLED)
        but_side_3R.grid(row=2, column=0)
        but_side_4R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray",state=DISABLED)
        but_side_4R.grid(row=3, column=0)
        # ==================================
    else:
        screen.txtReceipt.delete("1.0", END)
        screen.txtReceipt.insert(END, "You entered Wrong PIN\n")


def but_cancel():
    screen.txtReceipt.delete("1.0", END)
    but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_1L.grid(row=0, column=0)
    but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=DISABLED)
    but_side_2L.grid(row=1, column=0)
    but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=DISABLED)
    but_side_3L.grid(row=2, column=0)
    but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="dimGray",state=DISABLED)
    but_side_4L.grid(row=3, column=0)

    but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_1R.grid(row=0, column=0)
    but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_2R.grid(row=1, column=0)
    but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_3R.grid(row=2, column=0)
    but_side_4R = Button(frame1right, text="<<<<", width=15, height=3, bg="dimGray", state=DISABLED)
    but_side_4R.grid(row=3, column=0)

#=================================================Frames=============================

frame1=Frame(screen,width=900, height=300, relief=RIDGE, bg="Gray", bd=5 )
frame1.grid(row=0,column=0)
frame2=Frame(screen, width=900, height=300, relief=RIDGE, bg="Gray",  bd=5 )
frame2.grid(row=1,column=0)

frame1left=Frame(frame1, width=125, height=300, relief=RIDGE, bg="Gray" )
frame1left.grid(row=0,column=0)
frame1center=Frame(frame1, width=350, height=300, relief=RIDGE, bg="Gray",  bd=2 )
frame1center.grid(row=0,column=1)
frame1right=Frame(frame1, width=125, height=300, relief=RIDGE, bg="Gray",  bd=2 )
frame1right.grid(row=0,column=2)

frame2left=Frame(frame2, width=125, height=300, relief=RIDGE, bg="Gray", bd=2 )
frame2left.grid(row=0,column=0)
frame2center=Frame(frame2, width=350, height=300, relief=RIDGE, bg="Gray",  bd=2 )
frame2center.grid(row=0,column=1)
frame2right=Frame(frame2, width=125, height=300, relief=RIDGE, bg="Gray",  bd=2 )
frame2right.grid(row=0,column=2)


#==============================================Label==========================================

screen.txtReceipt=Text(frame1center, height=17, width=42, relief=SUNKEN, bd=10, bg="Lightgray")
screen.txtReceipt.grid(row=0,column=0)

#=============================================BUTTONS============================================

but9=Button(frame2center,text="9",width=10, height=3, bg="dimgray", command=but9)
but8=Button(frame2center,text="8",width=10, height=3, bg="dimGray", command=but8)
but7=Button(frame2center,text="7",width=10, height=3, bg="dimGray", command=but7)
but6=Button(frame2center,text="6",width=10, height=3, bg="dimGray", command=but6)
but5=Button(frame2center,text="5",width=10, height=3, bg="dimGray", command=but5)
but4=Button(frame2center,text="4",width=10, height=3, bg="dimGray", command=but4)
but3=Button(frame2center,text="3",width=10, height=3, bg="dimGray", command=but3)
but2=Button(frame2center,text="2",width=10, height=3, bg="dimGray", command=but2)
but1=Button(frame2center,text="1",width=10, height=3, bg="dimGray", command=but1)
butn=Button(frame2center,text="",width=10, height=3 , bg="dimGray", state=DISABLED)
but0=Button(frame2center,text="0",width=10, height=3, bg="dimGray", command=but0)
butnn=Button(frame2center,text="",width=10, height=3 , bg="dimGray",state=DISABLED )
butnnn=Button(frame2center,text="",width=10, height=3 , bg="dimGray",state=DISABLED )
butenter=Button(frame2center,text="Enter",width=10, height=3 , bg="darkgreen", command=but_enter)
butcancel=Button(frame2center,text="Cancel",width=10, height=3, bg="Maroon", command=but_cancel)
butexit=Button(frame2center,text="Exit",width=10, height=3 , bg="Blue", command=but_exit)

but9.grid(row=0, column=2)
but8.grid(row=0, column=1)
but7.grid(row=0, column=0)
but6.grid(row=1, column=2)
but5.grid(row=1, column=1)
but4.grid(row=1, column=0)
but3.grid(row=2, column=2)
but2.grid(row=2, column=1)
but1.grid(row=2, column=0)
butn.grid(row=3, column=0)
but0.grid(row=3, column=1)
butnn.grid(row=3, column=2)
butcancel.grid(row=0, column=3)
butenter.grid(row=1, column=3)
butexit.grid(row=2, column=3)
butnnn.grid(row=3,column=3)
#==========================================Side Buttons(Arrows)LEFT===================================

but_side_1L = Button(frame1left, text=">>>>", width=15, height=3, bg="grey", state=DISABLED)
but_side_1L.grid(row=0, column=0)
but_side_2L = Button(frame1left, text=">>>>", width=15, height=3, bg="grey", state=DISABLED)
but_side_2L.grid(row=1, column=0)
but_side_3L = Button(frame1left, text=">>>>", width=15, height=3, bg="grey", state=DISABLED)
but_side_3L.grid(row=2, column=0)
but_side_4L = Button(frame1left, text=">>>>", width=15, height=3, bg="grey", state=DISABLED)
but_side_4L.grid(row=3, column=0)


#==========================================Side Buttons(Arrows)RIGHT===================================

but_side_1R = Button(frame1right, text="<<<<", width=15, height=3, bg="grey", state=DISABLED)
but_side_1R.grid(row=0, column=0)
but_side_2R = Button(frame1right, text="<<<<", width=15, height=3, bg="grey", state=DISABLED)
but_side_2R.grid(row=1, column=0)
but_side_3R = Button(frame1right, text="<<<<", width=15, height=3, bg="grey", state=DISABLED)
but_side_3R.grid(row=2, column=0)
but_side_4R = Button(frame1right, text="<<<<", width=15, height=3, bg="grey", state=DISABLED)
but_side_4R.grid(row=3, column=0)



screen.mainloop()