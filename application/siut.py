import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("SIUT")

student = {
    "name":"",
    "number":0,
    "dms":0,
    "app":0,
    "oop":0,
    "m2":0
}

entries = []
total = 0
avg = 0

def calcMarks():
    values = []
    for e in entries:
        values.append(e.get())

    student["name"] = values[0]
    student["number"] = values[1]
    student["dms"] = int(values[2])
    student["app"] = int(values[3])
    student["oop"] = int(values[4])
    student["m2"] = int(values[5])

    global total
    total = student["app"]+student["dms"]+student["m2"]+student["oop"]
    global avg
    avg = total/4

def findTotal():
    calcMarks()

    labelT = tk.Label(window, text=f"Total: {total}", font={"Arial", 12})

    labelT.pack()

def findAvg():
    calcMarks()

    labelAvg = tk.Label(window, text=f"Avg: {avg}", font={"Arial", 12})
    labelAvg.pack()

def createInput(inpText):
    Frame = tk.Frame(window)
    label = tk.Label(Frame, text=inpText, font={"Arial", 12})
    inp = tk.Entry(Frame, font={14})
    Frame.pack(pady=10)
    label.pack(side="left")
    inp.pack()
    entries.append(inp)

createInput("Enter student's name")
createInput("Enter student's number")
createInput("Enter student's App marks")
createInput("Enter student's M2 marks")
createInput("Enter student's DMS marks")
createInput("Enter student's OPP marks")

totalBtn = tk.Button(text="Total", command=findTotal)
totalBtn.pack()

avgBtn = tk.Button(text="Avg", command=findAvg)
avgBtn.pack()

window.mainloop()