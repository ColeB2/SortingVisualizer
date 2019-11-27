'''
main.py
'''
from tkinter import Tk
from gui import SortVisualizer

if __name__ == '__main__':
    root = Tk()
    my_gui = SortVisualizer(root)
    root.mainloop()
