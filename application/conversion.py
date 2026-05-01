import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="vapor")
window.geometry("400x300")
window.title("conversion")

answerLabel = ttk.Label(window, text="Your answer is {}.", font={16})

infoLabel = ttk.Label(window, text="Miles to km.", font={16})
infoLabel.pack(pady=20)

inputFrame = ttk.Frame(window)
inputFrame.pack()

inputMiles = ttk.Entry(inputFrame, font={14})
inputMiles.pack(side="left", padx=10)

def convert():
    km = float(inputMiles.get()) * 1.609344
    return round(km, 1)

def submitAnswer():
    answerLabel.pack(pady=20)
    answerLabel.config(text=f"{inputMiles.get()} miles is {convert()} km.")

submitButton = ttk.Button(inputFrame, text="Convert", command=submitAnswer)
submitButton.pack()

window.mainloop()
