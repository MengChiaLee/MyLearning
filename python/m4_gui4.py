# how to change the text of a label

from tkinter import *    # get the GUI package

################################################################################
# callback function to change a label                                          #
# input:                                                                       #
#    label: the label whose text to change                                     #
# output:                                                                      #
#    change the label                                                          #
################################################################################

def chg_lab(label):
    label.configure(text = "new label")

root = Tk()                                  # start the gui
label = Label(root, text = "original label") # create a label and place it
label.grid(row=0)
Button(root,text='change the label',         # Button to execute the change
       command = lambda: chg_lab(label)).grid(row=1)

Button(root,text="Exit",width=12,command=root.destroy).grid(row=2)

mainloop()    # start the GUI

