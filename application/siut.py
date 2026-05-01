import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("SIUT")

studentNameInpFrame = tk.Frame(window)
studentNameL = tk.Label(studentNameInpFrame, text="Enter student's name: ", font={"Arial", 12})
studentname = tk.Entry(studentNameInpFrame, font={14})
studentNameInpFrame.pack(pady=10)
studentNameL.pack(side="left")
studentname.pack()

window.mainloop()