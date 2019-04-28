# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:36:04 2019

@author: melkhafef
"""
import tkinter
root = tkinter.Tk()
X=True
def tictactoe(button) :
    global X,buttons,label
    if(X==True):
        button["text"]="X"
        button["command"]=""
        X=False
        if (buttons[0]["text"]=="X" and buttons[1]["text"]=="X" and buttons[2]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[1].config(fg="red", bg="blue")
            buttons[2].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="X" and buttons[3]["text"]=="X" and buttons[6]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[3].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[5]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[6]["text"]=="X" and buttons[7]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[6].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="X" and buttons[4]["text"]=="X" and buttons[8]["text"]=="X"):
            buttons[0].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[4]["text"]=="X" and buttons[6]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[3]["text"]=="X" and buttons[4]["text"]=="X" and buttons[5]["text"]=="X"):
            buttons[3].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="X" and buttons[4]["text"]=="X" and buttons[7]["text"]=="X"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            label["text"]="X Win"
            for b in range(0,9):
                buttons[b]["command"]=""
    else :
        button["text"]="O"
        button["command"]=""
        X=True
        if (buttons[0]["text"]=="O" and buttons[1]["text"]=="O" and buttons[2]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[1].config(fg="red", bg="blue")
            buttons[2].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[3]["text"]=="O" and buttons[6]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[3].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[5]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[6]["text"]=="O" and buttons[7]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[6].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[0]["text"]=="O" and buttons[4]["text"]=="O" and buttons[8]["text"]=="O"):
            buttons[0].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[8].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[4]["text"]=="O" and buttons[6]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[6].config(fg="red", bg="blue")
            label = tkinter.Label( root, text="O Win")
            label.grid(row=4,column=1)
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[3]["text"]=="O" and buttons[4]["text"]=="O" and buttons[5]["text"]=="O"):
            buttons[3].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[5].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
        elif (buttons[2]["text"]=="O" and buttons[4]["text"]=="O" and buttons[7]["text"]=="O"):
            buttons[2].config(fg="red", bg="blue")
            buttons[4].config(fg="red", bg="blue")
            buttons[7].config(fg="red", bg="blue")
            label["text"]="O Win"
            for b in range(0,9):
                buttons[b]["command"]=""
def replay():
     global X,buttons,label
     X=True
     label.destroy()
     for i in range(0,10):
       buttons[i].destroy()
     buttons=[]
     b=0
     for i in range(0,10):
       buttons.append(tkinter.Button(root,width=20))
     for r in range(3):
             for c in range(3):
               buttons[b]["command"]=lambda button=buttons[b]: tictactoe(button)
               buttons[b].grid(row=r,column=c)
               b+=1
     label = tkinter.Label( root, text="                   ")
     label.grid(row=4,column=1)
     buttons[9]["command"]=replay
     buttons[9]["text"]="replay"
     buttons[9].grid(row=6,column=1)
  
buttons=[]
b=0
for i in range(0,10):
    buttons.append(tkinter.Button(root,width=20))
for r in range(3):
   for c in range(3):
       buttons[b]["command"]=lambda button=buttons[b]: tictactoe(button)
       buttons[b].grid(row=r,column=c)
       b+=1
label = tkinter.Label( root, text="")
label.grid(row=4,column=1)
buttons[9]["command"]=replay
buttons[9]["text"]="replay"
buttons[9].grid(row=6,column=1)
root.mainloop()

