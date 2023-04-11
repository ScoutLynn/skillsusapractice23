import tkinter as tk

root = tk.Tk()
root.title("Payroll-Contestant #1-Program #2")

# exit command
def exit():
    root.destroy()

def clear():
    # 
    employee_nameEntry.delete(0,'end')
    employee_ssnEntry.delete(0,'end')
    tkpayCodes.set("Select an option")
    employee_hoursworkedEntry.delete(0,'end')
    employee_shiftEntry.delete(0,'end')

def calculate():
    # frame that holds the calculation result
    resultFrame = tk.Frame(root,highlightbackground="cyan",highlightthickness=5)
    resultFrame.grid(row=2,column=0)





# string variables
nameVar = tk.StringVar()
ssnVar = tk.StringVar()
hoursVar= tk.StringVar()
shiftVar = tk.StringVar()
payCodes = {
    1 : 10.00,
    2 : 12.50,
    3 : 15.00,
    4 : 17.50,
    5 : 20.00
}

# frame for all inputs
inputFrame = tk.Frame(root, highlightbackground="red",highlightthickness=5)
inputFrame.grid(row = 0, column = 0)

tkpayCodes = tk.StringVar(inputFrame)
tkpayCodes.set("Select an option")

# employee name entry code
employee_nameLabel = tk.Label(inputFrame, text="Enter your name:")
employee_nameLabel.grid(row=0,column=0)

employee_nameEntry = tk.Entry(inputFrame, textvariable= nameVar)
employee_nameEntry.grid(row = 0, column= 1)

# employee social security number entry code
employee_ssnLabel = tk.Label(inputFrame, text = "Enter your social security number:")
employee_ssnLabel.grid(row = 1, column = 0)

employee_ssnEntry = tk.Entry(inputFrame, textvariable= ssnVar)
employee_ssnEntry.grid(row=1, column=1)

# hourly rate of pay code option code
employee_paycodeLabel = tk.Label(inputFrame, text= "Select your hourly pay code:")
employee_paycodeLabel.grid(row=2,column=0)

employee_paycodeOptionMenu = tk.OptionMenu(inputFrame, tkpayCodes, *payCodes)
employee_paycodeOptionMenu.grid(row=2, column=1)

# hours worked entry code
employee_hoursworkedLabel = tk.Label(inputFrame, text= "Enter your hours worked this week")
employee_hoursworkedLabel.grid(row=3,column=0)

employee_hoursworkedEntry = tk.Entry(inputFrame, textvariable=hoursVar)
employee_hoursworkedEntry.grid(row=3,column=1)

# shift entry code
employee_shiftLabel = tk.Label(inputFrame, text="Enter the shift you work")
employee_shiftLabel.grid(row=4,column=0)

employee_shiftEntry = tk.Entry(inputFrame, textvariable=shiftVar)
employee_shiftEntry.grid(row=4,column=1)

# button frame
btnFrame = tk.Frame(root,highlightbackground="lime", highlightthickness=5)
btnFrame.grid(row=1,column=0)

# calculate button
btn_calculate = tk.Button(btnFrame, text="Calculate")
btn_calculate.grid(row=0,column=0)

# clear button
btn_clear = tk.Button(btnFrame,text="Clear", command=clear)
btn_clear.grid(row=0,column=1)

# exit button
btn_exit = tk.Button(btnFrame,text="Exit", command=exit)
btn_exit.grid(row=0,column=2)

root.mainloop()