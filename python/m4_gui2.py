# example of a button and a counting label

import tkinter as tk                    # import the GUI package

def counter_label(label):               # a function to count up
    def count(counter):                 # only creates a new function if called!
        counter += 1                               # increment the counter
        label.config(text=str(counter))            # update the label
        label.after(1000, lambda: count(counter))  # after 1000ms, call again!
    count(0)                                       # make the first call

root = tk.Tk()                                     # create widget
root.title("Counting Seconds")                     # give it a title
label = tk.Label(root,fg="dark green")             # make a green label
label.pack()                                       # put it into the widget
counter_label(label)                               # now call function

# now create a button to kill the GUI
button = tk.Button(root,text='Stop', width=12, command=root.destroy)
button.pack()

# finally, start things going
root.mainloop()

input()          # pause here

# let's just create a nice message
root = tk.Tk()                         # create the top-level widget

# Create the string with our message. Note the continuation character.
churchill = "Success is not final. Failure is not fatal. \
It is the courage to continue that counts. Winston Churchill"

msg = tk.Message(root, text = churchill)               # use a message widget
msg.config(bg='lightgreen',font=('times',24,'italic')) # configure it a bit
msg.pack()                                             # put it in
root.mainloop()                                        # go!

input()          # pause here

# now let's do check boxes!
from tkinter import *                                  # again, tired of tk.

root = Tk()                          # create the top-level widget

################################################################################
# Function to show values of check buttons                                     #
# input:                                                                       #
#    var1, var2: containers for the check button values                        #
# output:                                                                      #
#    prints button values to the screen                                        #
################################################################################

def var_states(var1,var2):             
    print("undergrad: %d,\ngrad: %d"%(var1.get(),var2.get()))

# label to ask the question
Label(root,text="Your status:").grid(row=0,sticky=W)

# create a check buttons
# We need a container to hold the "value" of the button
var1 = IntVar()    # create the container (Stringvar, DoubleVar...)
Checkbutton(root,text="undergrad",variable=var1).grid(row=1,sticky=W)

var2 = IntVar()
Checkbutton(root,text="grad",variable=var2).grid(row=2,sticky=W)

# now, add control buttons...
Button(root,text='Quit',command=root.destroy).grid(row=3,sticky=W,pady=4)
Button(root,text='Show',command=lambda: var_states(var1,var2)).grid(row=4,
                                                            sticky=W,pady=4)

mainloop()     # and kick it off

