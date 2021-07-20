from tkinter import *
from tkinter import messagebox

root=Tk()
root.config(bg='red')
# root.iconbitmap("ticactoe.jpg")
winner = False
def iswon():
    global winner

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner =True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "You Win!!!")
    elif  b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner =True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")

    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner =True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "You Win!!!")
    elif  b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif  b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe","You Win!!!")
    elif count%9==0 and winner==False:
        messagebox.showinfo("tic tac toe","Tie")


click = 0
count = 0
def b_click(b):
    global click, count
    if b["text"]==" " and click==0:
        b.config(text="X")
        click=1
        count+=1
        iswon()
    elif b["text"]==" " and click==1:
        b.config(text="O")
        click = 0
        count += 1
        iswon()

def restart():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b1))
    b2=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b2))
    b3=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b3))
    b4=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b4))
    b5=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b5))
    b6=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b6))
    b7=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b7))
    b8=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b8))
    b9=Button(root, text=" ",width=8,height=4,font="Calibri 30",bg="SystemButtonFace",command=lambda:b_click(b9))
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
restart()
restartb=Button(root,text="restart", font="Calibri 30",bg="SystemButtonFace",command=restart)
restartb.grid(row=3,column=2,sticky=E,pady=10)

mainloop()