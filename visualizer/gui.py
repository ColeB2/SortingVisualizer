'''
gui.py
'''
import tkinter as tk
from tkinter import ttk
import random
import sys

import algorithms

class SortVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Sort Algorithm Visualization")
        self.master.geometry('607x500')
        self.master.wm_resizable(width=False, height=False)

        self.line_array = []
        self.draw_frame()
        self.current_algorithm = None
        self.run = False

    '''Frame Widgets'''
    def draw_frame(self):
        self.draw_buttons()
        self.draw_drop_down()
        self.draw_size_scale()
        self.draw_speed_scale()
        self.draw_canvas()

    def draw_buttons(self):
        self.generate_list_button = ttk.Button(
            self.master, text="Generate List", command=self.generate_list)
        self.generate_list_button.grid(row=0, column=0, sticky='w')

        self.start_sort_button = ttk.Button(
            self.master, text="Start Sort", command=self.start_sort)
        self.start_sort_button.grid(row=0, column=2, sticky='w')

    def draw_drop_down(self):
        self.sort_algos = ['Select Algorithm',
        'Bubble Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']
        self.option_variable = tk.StringVar()
        self.option_drop_down = ttk.OptionMenu(
            self.master, self.option_variable, *self.sort_algos,
            command=self.set_sort_algo)
        self.option_drop_down.config(width=15)
        self.option_drop_down.grid(row=0, column=1, sticky='w')

    def draw_size_scale(self):
        self.size_scale = ttk.Scale(self.master, from_=5, to=24, value=24,
        orient='horizontal', command=self.size_scale_value, length=100)

        self.size_scale.grid(row=2, column=1, sticky='sw')
        self.size_label = ttk.Label(self.master, text='Size', font=('Verdana', 15))
        self.size_label.grid(row=2, column=0, sticky='e')

    def draw_speed_scale(self):
        self.speed_scale = ttk.Scale(self.master, from_=1, to=41, value=21,
        orient='horizontal', command=self.speed_scale_value, length=100)

        self.speed_scale.grid(row=2, column=3, sticky='sw')
        self.speed_label = ttk.Label(self.master, text='Speed', font=('Verdana', 15))
        self.speed_label.grid(row=2, column=2, sticky='e')

    def draw_canvas(self):
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.grid(row=1, column=0,columnspan=50)

    '''COMMANDS'''
    def get_array_size(self):
        n=self.size_scale.get()
        if int(n) != n:
            self.size_scale.set(round(value))
        return n

    def generate_list(self):
        print('Generate New List')
        if len(self.line_array) == 0:
            n = self.get_array_size()
            for i in range(int(n)):
                line = random.randint(10, 350)
                self.line_array.append(line)
        else:
            self.line_array = []
            self.canvas.delete("all")
            n = self.get_array_size()
            for i in range(int(n)):
                line = random.randint(10,350)
                self.line_array.append(line)
        self.draw_all_lines()


    def start_sort(self):
        speed = int(self.get_speed())
        algo = self.get_sort_algo()
        if algo != None and len(self.line_array) != 0:
            print("Starting Sort")
            self.run = True
            self.sort_handler(algo,speed)


    def sort_handler(self, algo=None, speed=500):
        generator = algo(self.line_array)
        while self.run:
            try:
                info = next(generator)
                if info[0] == 0:
                    self.selected_line_colors(line1=info[1], line2=info[2],
                        line_color='green')
                elif info[0] == 1:
                    self.selected_line_colors(line1=info[1], line2=info[2],
                        line_color='red')
                elif info[0] == 2:
                    self.update_canvas(line1=info[1], line2=info[2])
                self.master.after(speed)
            except:
                self.run = False
                e = sys.exc_info()
                print(e)
                print('Breaking')

                break
        self.canvas.delete('all')
        self.draw_all_lines(color1='purple')


    def size_scale_value(self, e=None):
        value = self.size_scale.get()
        if int(value) != value:
            self.size_scale.set(round(value))
        pass

    def speed_scale_value(self, e=None):
        value = self.speed_scale.get()
        if int(value) != value:
            self.speed_scale.set(round(value))

    def get_speed(self):
        n = self.get_array_size()
        s = self.speed_scale.get()
        speed = (1000 - (n * s))
        return int(speed)

    def set_sort_algo(self, value):
        self.current_algorithm = value
        print(self.current_algorithm)

    def get_sort_algo(self):
        if self.current_algorithm == 'Bubble Sort':
            return algorithms.bubble_sort
        else:
            pass
    '''Canvas Draw Methods'''
    def draw_all_lines(self, line1=None, line2=None, color1='blue',
        color2='red'):
        for line in enumerate(self.line_array):
            color = color1
            if line[0] == line1 or line[0] == line2:
                color = color2
            xcoord = line[0] * 25 + 10
            ycoord = 0
            length = line[1]
            self.canvas.create_line(xcoord, ycoord, xcoord, length, width=20,
            tag=str(line[0]), fill=color)

    def selected_line_colors(self, line1, line2, line_color):
        self.canvas.delete('all')
        self.draw_all_lines(line1, line2, color2 = line_color)
        self.master.update_idletasks()

    def update_canvas(self, line1, line2):
        self.canvas.delete('all')
        self.draw_all_lines(line1, line2)
        self.master.update_idletasks()
