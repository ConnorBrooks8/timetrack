from collections import defaultdict
from tkinter import *

class Task(object):

    def __init__(self, value,children=None,parents=None):
        self.value = value
        self.children = []
        self.parents = []
        self.depth=0

    def __repr__(self):
        return str(self.value)

    def add_child(self,obj):
        self.children.append(obj)
        obj.parents.append(self)
        obj.setDepth(self.depth+1)

    def add_parent(self,obj):
        self.parents.append(obj)
        obj.child.append(self)

    def setDepth(self,depth):
        self.depth=depth

    def PrintTree(self):
        print(self.value)
        self.PrintChildren()

    def PrintChildren(self):
        for child in self.children:
            print('-'*child.depth + child.value)
            child.PrintChildren()





master = Task('This is a Task')
task2 = Task('One thing required')
task3 = Task('Another thing')
subtask = Task('Task 2 req')

master.add_child(task2)
master.add_child(task3)
task2.add_child(subtask)


#walk tree and print values



def commandloop():
    quit = False
    while quit == False:
        command  = input( '\n add task: 1 \n see tree: 2 \n quit: 3 \n')
        print('\n')
        if command[0] == '1':
            print('lol nah')
        if command[0] == '2':
            master.PrintTree()
        if command[0] == '3':
            quit = True

Tasks = []
Tasks.append(Task('hello'))
print(Tasks[0].parents)


class Gui:
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()

        self.quitbutton = Button(frame,text="QUIT",fg="red",command=frame.quit)
        self.quitbutton.pack(side=LEFT)
        Button(frame,text="Tree",command=self.showtree()).pack(side=LEFT)

    def showtree(self):
        master.PrintTree()

root = Tk()
gui = Gui(root)
root.mainloop()
root.destroy()

commandloop()
