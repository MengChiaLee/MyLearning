# examples for building GUIs

#import tkinter as tk                     # the GUI package we'll be using
from tkinter import *                     # be careful of collisions!

# make a label
root = Tk()                               # root widget
w = Label(root, text = "Hello World")     # root is the parent window
w2 = Label(root, text = "Hello Again")    # root is the parent window
w.pack()                                  # put it in the widget
w2.pack()                                 # this one too!

root.mainloop()                           # this runs until we close window

# make labels with some padding
# root widget (previous one was destroyed!
root = Tk()                           
w = Label(root, text = "Hello World")
w.grid(padx=10,pady=5)                    # now add padding
w2 = Label(root, text = "Hello Again")
w2.grid(padx=50,pady=50)                  # more padding
w3 = Label(root, text = "Hello Again")
w3.grid(padx=200,pady=100)                # even more padding

root.mainloop()                           # runs until we close window

input()    # pause here

################################################################################
# callback function to retrieve data from the fields                           #
# calculate the wealth and generate a plot of yearly wealth                    #
# inputs:                                                                      #
#    e1: first entry field                                                     #
#    e2: second entry field                                                    #
# output to screen:                                                            #
#    print the contents of the fields                                          #
# side effects:                                                                #
#    clears the field
# NOTE: the values in the entries are strings that need to be                  #
#       converted to int or float.                                             #
################################################################################

def show_entry_fields(e1,e2):
    print("First Name: %s\nLast Name: %s"%(e1.get(),e2.get()))
    e1.delete(0,END)                     # must supply start/end positions!
    e2.delete(0,END)                     # must supply start/end positions!
    
root = Tk()                                   # top-level widget
Label(root,text="First Name").grid(row=0)     # Labels - specify which row
Label(root,text="Last Name").grid(row=1)

e1 = Entry(root)                              # these allow data entry
e2 = Entry(root)                              # so two pieces to enter

e1.grid(row=0,column=1)                       # line them up with the labels
e2.grid(row=1,column=1)

# now add a button that will kill the GUI with the built-in function "destroy"
# the button executes the command "root.destroy" when it is pressed,
# and has text "Quit"
# we'll put this on row 3
# we'll add some vertical padding
# we want it in the first (left) column
# sticky is West, that is to the left, as opposed to N, S, or E
# Note it is sometimes ok to put line break within parentheses...

Button(root,text='Quit',command=root.destroy).grid(row=3,column=0,
                                                       sticky=W,pady=4)

# now create a button to print out the entry and then clear it.
# These fields are similar, but...
# we'll put it in row 3 and the second column
# and we'll use lambda to allow us to pass arguments to the function
# so we don't need global variables!
# Why lambda? Because the value given to command is executed immediately.
# As a result, if we said command=show_entry_fields(e1,e2), the e1 and e2
# would be evaluated immedately and then not again. Alternatively, we could
# do this: command=show_entry_fields and that's it. However, then e1 and e2
# have to be referenced in the function as global variables and that's
# bad practice. So, instead, we use lambda!
# Another way to look at this is command wants the "name" of the function
# to call. By using lambda, we fool it into allowing us to pass arguments.

Button(root,text='Show',command=lambda: show_entry_fields(e1,e2)).grid(row=3,
                                                      column=1,sticky=W,pady=4)

mainloop()     # now kick it off!

