from tkinter import *
import math
def leftClickButton(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if bmi>=30.0:
        status = "Extreme Obesity"
    elif bmi>=25.0:
        status = "Medically Weight"
    elif bmi>=23.0:
        status = "Overweight"
    elif bmi>=18.6:
        status = "Normal"
    else:
        status = "Underweight"

    labelResult.configure(text = bmi)
    labelStatus.configure(text = status)


mainWindow = Tk()
labelHeight = Label(mainWindow, text="Height (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(mainWindow, text="Weight (kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(mainWindow, text="Calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)

labelResult = Label(mainWindow, text="Result")
labelResult.grid(row=2, column=1)

labelStatus = Label(mainWindow, text="Weight Status")
labelStatus.grid(row=3, column=1)
mainWindow.mainloop()