# SortingVisualizer

SortingVisualizer is a Tkinter app made for visualizing various sorting algorithms.


# Author Notes
- I will keep up for learning purposes, mostly on what not to do. I may refactor in the future.

- Main issues:
-Main loop is poorly made, 
-- calls draw too often --> leads to flicker effect as it redraws all the lines, while still trying to draw them from before.
- Also imo tkinter not a great option for long main loops without user intertation. Causes hanging when speed is too slow or when loop runs too long.


# Technologies

Written in Python 3.6  
Using Tkinter 8.6

# Acknoledgements

[Orangefish](https://github.com/Orangefish/algo/blob/master/sorting_and_search/sort_merge.py) for their implementation of merge sort

[geeksforgeeks](https://www.geeksforgeeks.org/) for their information on algorithms

# License
[MIT](https://choosealicense.com/licenses/mit/)

# Application

![Image of App](https://github.com/ColeB2/SortingVisualizer/blob/master/images/sortingapp.jpg)
