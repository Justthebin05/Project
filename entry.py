from tkinter import *

# root widget
root = Tk()
root.title("Simple Calculator")

'''
"Easy"
implement backspace =====                                       Completed!!!
    - the opposite of putting the numbers in?
implement point or decimal button                               Completed
    - just use the regular number buttons to make this happen.  Completed
    - switch from int() to decimal or float.                    Completed
implement exponent x²
    - make the x² and put it on the button
    - just use f_num times itself 
implement an exponent that we put in x^y
    - use that for the button
    - look up how to do exponents on python
    - reuse math global to implement
implement +/- button
    - use f_num and multiply it  by -1
Organizing the buttons on the GUI
    -layout based on the windows calculator
    

"Medium"
implement changing the  math global operator so that it doesn't cause an error.
    - example hitting + and then -
    - putting a value in to be set for the f_num might be an answer
    - Switching should not change the value for math operators
Always show current value instead of disappearing
    - use global current value?
    - show 0 at the start
    - show int when whole number, float when decimal number
Implement showing previous calculation history
    - show at least 3 previous
    - Example: 4 x 3 = 12

"Hard"
Implement showing current scientific formula
    - Example: 4 x 6 - 3 + 4
    - = will stop the formula
Implement parentheses
    - Include ( and ) buttons
    - Changes order of operations when evaluating scientific formula
'''

# Creating an entry area
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0,"Enter Your Name: " )
## Understanding button by button
# 1     display 1
# 0     display 0 to the right of 1
# -     store 10 -> f_num; stores "subtraction" -> math; clear
# 1     display 1
# -     store 1 -> into s_num and perform caculation of 10 - 1 display 9
# "9"   store 9 -> into f_num
# 1     display 1
# -     store 1 -> s-num and calculate f_num - s_num display result
# "8"   store 8 -> f_num

## Understanding  calculation for the equals being pressed repeatedly
# 10
# -  f_num math "subtraction"
# 1
# =     10 - 1
# "9" f_num
# =     9 - 1
# "8"
# =     8 - 1
# "7"
#
f_num= 'a'
math= 0
sign = 0
s_num = 0




def button_equal():
    global f_num, math, s_num, sign
    if math == 0:
        print(f_num, sign, s_num)
        f_num= float(e.get())
        e.delete(0, END)
        e.insert(0, s_num)
        math = sign
        button_calculate()
    else:
        second_number = e.get()
        s_num= second_number
        sign = math
        button_calculate()
    e.insert(0, str(f_num))
    math = 0

def button_calculate():
    global f_num
    global math
    if not f_num == 'a':
        second_number = e.get()

        if math == "addition":
            f_num = f_num + float(second_number)

        if math == "subtraction":
            f_num = f_num - float(second_number)

        if math == "multiplication":
            f_num = f_num * float(second_number)

        if math == "division":
            f_num = f_num // float(second_number)
    else:
        f_num = float(e.get())
    e.delete(0, END)

# puts the buttons numbers on the display on the farthest right
def button_click(number): # value from button
   current = e.get() # make a copy of displayed value
   e.delete(0, END) # clear display
   e.insert(0, current + str(number)) # add (copy and button's value) on left of display

def button_backspace():
    # remove grabs all the information except the last entry
    remove = e.get()[:-1]
    # delete gets rid of all the entries that are showing
    e.delete(0, END)
    # insert shows the entries that remove grabbed
    e.insert(0, remove)

def button_delete():
    e.delete(0, END)
    global f_num, math, sign, s_num
    f_num = 'a'
    math = 0
    sign = 0
    s_num = 0

def button_dec():
    # tests to make sure only one decimal is used in e.get
    if '.' not in e.get():
        button_click('.')

def button_add():
    button_calculate()
    global math
    math = "addition"

def button_subtract():
    button_calculate()
    global math
    math = "subtraction"

def button_multiply():
    button_calculate()
    global math
    math = "multiplication"

def button_divide():
    button_calculate()
    global math
    math = "division"

# f_num should update every time the button_equal is clicked
# first number should have the second number be subtracted from the first
# number and use the result to take the second number from the new
# result
# 10 - 5 = 5 ; 5 - 5 = 0
# 1  this number is displayed
# 0  this is added to the right of 1
# -  store 10 -> f_num; "subtraction" store -> math; display emptied
# 1  is displayed
# =  store 1 -> second_number; do calculation of f_num - second_number;
# "9"  result inserted
# -    store 9 -> f_num; "subtraction" stored -> math; displayed emptied
# 1    1 displayed
# =    store 1 -> second_number; calculate f_num - second_number; display result
# "8"  result displayed
# 1 0 - 1 = "9" = "8" = "7" # What I want
# 1 0 - 1 = "9" = "1" = "9" # Current situation


# Defining some buttons with a loop (1-9)

for buttonNumber in range(1,10):
    variable= buttonNumber
    row= 3 - (buttonNumber -1) // 3 # rowNumber - (buttonNumber - 1) // rowNumber
    column= (buttonNumber -1) % 3 # (buttonNumber - 1) % columnNumber
    button_1 = Button(root, text=buttonNumber, padx=40, pady=20, command=lambda v=variable: button_click(v)).grid(row=row, column=column)

# All other buttons

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_decimal = Button(root, text=".", padx=40, pady=20, command= button_dec)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_delete)
button_back = Button(root, text="<x|", padx=79, pady=20, command=button_backspace)

button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
#
# # Put the buttons on the screen
'''
button_1.grid(row=3, column=0) # row= 1/3 = .33 = 0 , remainder 1
button_2.grid(row=3, column=1) # row= 2/3 = .67 = 0 , remainder 2
button_3.grid(row=3, column=2) # row= 3/3 = 1 = 1 , remainder 0

button_4.grid(row=2, column=0) # row= 4/3 = 1.33 = 1 , remainder 1
button_5.grid(row=2, column=1) # row= 5/3 = 1.67 = 1 , remainder 2
button_6.grid(row=2, column=2) # row= 6/3 = 2 = 2 , remainder 0

button_7.grid(row=1, column=0) # row= 7/3 = 2.33 = 2 , remainder 1
button_8.grid(row=1, column=1) # row= 8/3 = 2.67 = 2 , remainder 2
button_9.grid(row=1, column=2) # row= 9/3 = 3 = 3 , remainder 0
# 3 - (buttonNumber - 1) // rowNumber = decimal (/), integer (//), remainder (%)
'''
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)
button_back.grid(row=7, column=2)
button_decimal.grid(row=7, column=1)

# Creating Buttons

# Button with grid and padding button on x axis




# Creating an invent loop.
root.mainloop()
