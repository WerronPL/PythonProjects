import tkinter as tk
import datetime

def check_for_imposter(event):
    print("LOL your friend is SUS")
window=tk.Tk()
window.title(" Real Amongus Pro v1.9.10.3f ")
window.geometry("1200x800")
newlabel = tk.Label(text = " This is Real Amongus, don't mind it looking bit sus ")
newlabel.grid(column=0,row=0)
check_for_imposter_button = tk.Button(window, text = "Check for Imposters")
check_for_imposter_button.grid(column=1,row=0)
check_for_imposter_button.bind("<Button-1>",check_for_imposter)
text1 = tk.Text(height=20,width=10)
text1 = tk.Label(text = "Are you SUS? yes/no")
text1.grid(column=2,row=1)

class PossibleAnswers:

    yes = tk.Label(text="yes")
    no = tk.Label(text="no")

someanswer = tk.Entry()
someanswer.grid(column=2,row=0)

def __init__(self,yes, no):
    self.yes = yes
    self.no = no
def sus_or_not(self):
        if PossibleAnswers.someanswer == yes:
            sus_or_not = "sus"
            return sus_or_not
        elif PossibleAnswers.someanswer == no:
            sus_or_not = "not sus"
            return sus_or_not

def are_you_sus():
    yes=someanswer.get()
    no=someanswer.get()
    monkey = PossibleAnswers(yes, no)
    textarea = tk.Text(height=2,width=40)
    textarea.grid(column=2,row=1)
    answered = " Wait {monkey}!!!, You are {sus_or_not} LOL!!! ".format(monkey=yes, sus_or_not=monkey.sus_or_not())
    textarea.insert(tk.END, answered)

sus_or_not_button = tk.Button(window,text="Check for sus", command=are_you_sus,bg="white")
sus_or_not_button.grid(column=3,row=0)

window.mainloop()

