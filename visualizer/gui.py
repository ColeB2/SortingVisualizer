'''
gui.py
'''
import algorithms
from pyVariables import *
import random
import sys
import tkinter as tk
from tkinter import ttk


class SortVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm Visualizer")
        self.master.geometry(WINDOW_SIZE)
        self.master.wm_resizable(width=False, height=False)

        self.line_array = []
        self.draw_frame()
        self.current_algorithm = None
        self.run = False

    '''Main Frame Draw Elements'''
    def draw_frame(self):
        self.draw_buttons()
        self.draw_drop_down()
        self.draw_scales()
        self.draw_canvas()

    '''Widget Elements'''
    def draw_buttons(self):
        self.generate_list_button = ttk.Button(
            self.master, text="Generate List", command=self.generate_list)
        self.generate_list_button.grid(row=0, column=0, sticky='w')

        self.start_sort_button = ttk.Button(
            self.master, text="Start Sort", command=self.start_sort)
        self.start_sort_button.grid(row=0, column=2, sticky='w')

    def draw_drop_down(self):
        self.sort_algos = SORTING_ALGORITHMS_LIST
        self.option_variable = tk.StringVar()
        self.option_drop_down = ttk.OptionMenu(
            self.master, self.option_variable, *self.sort_algos,
            command=self.set_sort_algo)
        self.option_drop_down.config(width=15)
        self.option_drop_down.grid(row=0, column=1, sticky='w')

    '''Tkinter SCALES'''
    def draw_scales(self):
        self.draw_size_scale()
        self.draw_speed_scale()

    def draw_size_scale(self):
        '''Tkinter Scale used to control size of array'''
        self.size_scale = ttk.Scale(self.master, from_=ARRAY_LOW, to=ARRAY_HIGH,
            value=8, orient='horizontal', command=self.size_scale_value,
            length=SCALE_LENGTH)

        self.size_scale.grid(row=2, column=1, sticky='sw')
        self.size_label = ttk.Label(self.master, text='Size', font=('Verdana', 15))
        self.size_label.grid(row=2, column=0, sticky='e')

    def draw_speed_scale(self):
        '''
        Tkinter Scale used to control speed of animation
        Done so by setting a value in millisecond to subtract from 1000
        for self.master.after() to call.
        '''
        self.speed_scale = ttk.Scale(self.master, from_=SPEED_LOW,
            to=SPEED_HIGH, value=900, orient='horizontal',
            command=self.speed_scale_value, length=SCALE_LENGTH)

        self.speed_scale.grid(row=2, column=3, sticky='sw')
        self.speed_label = ttk.Label(self.master, text='Speed', font=('Verdana', 15))
        self.speed_label.grid(row=2, column=2, sticky='e')

    def draw_canvas(self):
        self.canvas = tk.Canvas(self.master, width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT)
        self.canvas.grid(row=1, column=0,columnspan=50)

    '''COMMANDS'''
    def get_array_size(self):
        n=self.size_scale.get()
        if int(n) != n:
            self.size_scale.set(round(value))
        return n

    def generate_list(self):
        if len(self.line_array) != 0:
            self.line_array = []
            self.canvas.delete('all')

        n = self.get_array_size()
        for i in range(int(n)):
            line = random.randint(LINE_LENGTH_LOW, LINE_LENGTH_HIGH)
            self.line_array.append(line)

        self.draw_all_lines()


    def start_sort(self):
        speed = int(self.get_speed())
        algo = self.get_sort_algo()
        if algo != None and len(self.line_array) != 0:
            self.run = True
            self.sort_handler(algo,speed)

    def scale_value(self, e=None, scale=None):
        value = scale.get()
        if int(value) != value:
            scale.set(round(value))

    def size_scale_value(self, e=None):
        self.scale_value(scale=self.size_scale)

    def speed_scale_value(self, e=None):
        self.scale_value(scale=self.speed_scale)

    def get_speed(self):
        speed = 1000 - self.speed_scale.get()
        return int(speed)

    def set_sort_algo(self, algo):
        self.current_algorithm = algo

    def get_sort_algo(self):
        if self.current_algorithm == 'Bubble Sort':
            return algorithms.bubble_sort
        elif self.current_algorithm == 'Fast Bubble Sort':
            return algorithms.fast_bubble_sort
        elif self.current_algorithm == 'Selection Sort':
            return algorithms.selection_sort
        elif self.current_algorithm == 'Insertion Sort':
            return algorithms.insertion_sort
        elif self.current_algorithm == 'Shell Sort':
            return algorithms.shell_sort
        elif self.current_algorithm == 'Merge Sort':
            return algorithms.merge_sort
        elif self.current_algorithm == 'Heap Sort':
            return algorithms.heap_sort
        elif self.current_algorithm == 'Quick Sort':
            return algorithms.quick_sort


    '''SORTING HANDLER'''
    def sort_handler(self, algo=None, speed=500):
        '''
        Handles sorting by using information from Algorithm generator
        to call the correct drawing functions to color lines correct colors
        generators yield values:
        '''
        generator = algo(self.line_array)
        while self.run:
            for info in generator:
                if info[0] == 'compare': # selecting lines --comparison
                    self.selected_line_colors(line1=info[2], line2=info[3],
                        line3=info[4], line_color='green')
                elif info[0] == 'swapping': #sqapping lines --swap lines
                    self.selected_line_colors(line1=info[2], line2=info[3],
                        line3=info[4], line_color='red')
                elif info[0] == 'draw all': #post swap, all blue
                    self.update_canvas(line1=info[2], line2=info[3])


                self.master.after(speed)
            self.run = False
            e = sys.exc_info()

        self.canvas.delete('all')
        self.draw_all_lines(color1='purple')

    '''Canvas Draw Methods'''
    def draw_all_lines(self, line1=None, line2=None, line3=None, line4=None,
        color1='blue',color2='red'):
        padding = 5
        line_width = int((CANVAS_WIDTH / self.get_array_size()) - padding)
        spacing = line_width/2
        scale = line_width + padding
        for line in enumerate(self.line_array):
            color = color1
            if line[0] == line1 or line[0] == line2:
                color = color2
                xcoord = line[0] * scale + spacing
            elif line[0] == line3:
                color = 'yellow'

            xcoord = line[0] * scale + spacing
            ycoord = 0
            length = line[1]
            self.canvas.create_line(xcoord, ycoord, xcoord, length,
            width=line_width, tag=str(line[0]), fill=color)

    def selected_line_colors(self, line1, line2, line_color, line3=None):
        self.canvas.delete('all')
        self.draw_all_lines(line1, line2, color2 = line_color, line3=line3)
        self.master.update_idletasks()

    def update_canvas(self, line1, line2, color='blue'):
        self.canvas.delete('all')
        self.draw_all_lines(line1, line2, color1=color)
        self.master.update_idletasks()
