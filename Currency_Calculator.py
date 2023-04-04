import tkinter as tk


root = tk.Tk()
root.title("Currency Conversion")
root.geometry("400x400")

amountVar=tk.StringVar()


# deleting everything
def exit():
    root.destroy()

# Calculating and checking for errors
def calc():
    if len(cFrame.winfo_children()) == 3:
        cFrame.winfo_children()[2].destroy()
    if len(root.winfo_children()) == 3:
        root.winfo_children()[2].destroy()
    
    try:
        dollars = float(amountVar.get())
        conversionFrame = tk.Frame(root,highlightbackground="green",highlightthickness=5)
        conversionFrame.grid(row = 2, column = 0)

        poundLabel = tk.Label(conversionFrame, text = "British Pounds: " + str(round(dollars*values[0],2)))
        poundLabel.pack()

        francLabel = tk.Label(conversionFrame, text = "French Francs: " + str(round(dollars*values[1],2)))
        francLabel.pack()

        lireLabel = tk.Label(conversionFrame, text = "Italian Lire: " + str(round(dollars*values[2],2)))
        lireLabel.pack()

        markLabel = tk.Label(conversionFrame, text = "German Deutsche Mark: " + str(round(dollars*values[3],2)))
        markLabel.pack()

        pesetasLabel = tk.Label(conversionFrame, text = "Spanish Pesetas: " + str(round(dollars*values[4],2)))
        pesetasLabel.pack()
    except ValueError:
        amount.delete(0,'end')
        error_label = tk.Label(cFrame,text="Entry must be a number",background="red")
        error_label.grid(row =0, column=2)
        
# clearing function for the entry box
def clear():
    amount.delete(0, "end")
    if len(cFrame.winfo_children()) == 3:
        cFrame.winfo_children()[2].destroy()
    if len(root.winfo_children()) == 3:
        root.winfo_children()[2].destroy()

#conversion values
values = [0.64, 6.07426, 1793.62, 1.811, 154.076]

# calculator frame. recieves inputd
cFrame = tk.Frame(root,bg="#8D876E", height = 200, width = 400,highlightbackground="blue",highlightthickness=5)
cFrame.grid(sticky='N',row=0,column=0)

# button frame. holds all the buttons
bFrame = tk.Frame(root,bg="#BE6B89",height = 200, width = 400, highlightbackground="red",highlightthickness=5)
bFrame.grid(sticky='S',row=1,column=0)

conversionFrame = tk.Frame(root,highlightbackground="green",highlightthickness=5,height = 200, width = 400)
conversionFrame.grid(row = 2, column = 0)

#Enter an amount label
label = tk.Label(cFrame, text = "Enter an amount in $")
label.grid(sticky="W",row=0,column=0)

#
amount = tk.Entry(cFrame, textvariable= amountVar)
amount.grid(sticky="E",row=0,column=1)

calculate =  tk.Button(bFrame,text="Calculate",command = calc)
calculate.grid(row=0,column=0)

clear_btn =  tk.Button(bFrame,text="Clear",command=clear)
clear_btn.grid(row=0,column=1)

exit_btn =  tk.Button(bFrame,text="Exit", command = exit)
exit_btn.grid(row=0,column=3)

root.mainloop()