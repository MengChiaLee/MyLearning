# now show some radio buttons

import tkinter as tk                               # get the package

LANGS = ["None","Python","Perl","Java","C++","C"]  # language choices

################################################################################
# callback function to display which button was pushed                         #
# inputs:                                                                      #
#    v: container holding radio button value                                   #
# output to screen:                                                            #
#    print the number of the button                                            #
################################################################################

def show_choice(v):       # a function to show the current choice
    print(v.get())

root = tk.Tk()                          # start the top-level widget
v = tk.IntVar()                         # create a container
v.set(0) #initializing the choice       # initialize it to "None"

# create the label for the box and left justify it
tk.Label(root, text="What is your favorite programming language:",
         justify = tk.LEFT, padx = 20).pack()

# now a button for each language...
for val, language in enumerate(LANGS):
    # they each put their value into v and call the printer when pressed
    tk.Radiobutton(root, text=language, padx = 20, variable=v,
                   command=lambda: show_choice(v),
                   value=val).pack(anchor=tk.W)      # their value is val

# and, of course, create a kill button and put it at the bottom
b1 = tk.Button(root,text="Stop",width=12,command=root.destroy)
b1.pack(side='bottom')

root.mainloop()  # and start it up
