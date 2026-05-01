import connection as c, tkinter as tk


window = tk.Tk()
window.geometry("1000x800")
window.title("My first application.")

studentNameInpFrame = tk.Frame(window)
studentNameL = tk.Label(studentNameInpFrame, text="Enter students name: ", font={"Arial", 12})
studentname = tk.Entry(studentNameInpFrame, font={14})
studentNameInpFrame.pack(pady=10)
studentNameL.pack(side="left")
studentname.pack()

studentIdInpFrame = tk.Frame(window)
studentIdL = tk.Label(studentIdInpFrame, text="Enter enter students id: ", font={"Arial", 12})
studentId = tk.Entry(studentIdInpFrame, font={14})
studentIdInpFrame.pack(pady=10)
studentIdL.pack(side="left")
studentId.pack()

submitBtn = tk.Button(window, width=12, height=3, text="Submit")
submitBtn.pack()

# for row in c.studentsTable:
#     student = tk.Frame(window, bg="blue", width=400, height=500)
#     name = tk.Label(student, font={24}, text=f"Name: {row[1]}")
#     name.pack()
#     dms = tk.Label(student, text=f"Dms: {row[2]}")
#     dms.pack()
#     msc2 = tk.Label(student, text=f"Msc2: {row[3]}")
#     msc2.pack()
#     app = tk.Label(student, text=f"App: {row[4]}")
#     app.pack()
#     oop = tk.Label(student, text=f"Oop: {row[5]}")
#     oop.pack()
#     student.pack(pady=20)

window.mainloop()