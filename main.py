import tkinter as tk
window=tk.Tk()
window.geometry("210x200")
def onclick():
    print(1)
btn1=tk.Button(text="нажми меня",command=onclick)
btn1.grid(row=0,column=0)
Chkvar=tk.IntVar()
Chkbtn=tk.Checkbutton(text="выбор лампочки",variable=Chkvar,onvalue=1,offvalue=0)
Chkbtn.grid(row=1,column=0)
Scl=tk.Scale(label="яркость",from_=1,to=100,orient=tk.HORIZONTAL,length=200,width=10)
Scl.grid(row=2,column=0)
window.mainloop()
