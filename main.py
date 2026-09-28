import sys
import tkinter as tk
from gui import EasyAssistantApp

def launch_gui():
    root = tk.Tk()
    app = EasyAssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
