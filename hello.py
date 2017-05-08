from collections import defaultdict
from Tkinter import *

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

master = Task('This is a Task')
task2 = Task('One thing required')
task3 = Task('Another thing')
subtask = Task('Task 2 req')

master.add_child(task2)
master.add_child(task3)
task2.add_child(subtask)


#walk tree and print values


def PrintTree(obj):
    print(obj.value)
    PrintChildren(obj)

def PrintChildren(obj):
    for child in obj.children:
        print('-'*child.depth + child.value)
        PrintChildren(child)


def commandloop():
    quit = False
    while quit == False:
        command  = input( '\n add task: 1 \n see tree: 2 \n quit: 3 \n')
        print('\n')
        if command[0] == '1':
            print('lol nah')
        if command[0] == '2':
            PrintTree(master)
        if command[0] == '3':
            quit = True

Tasks = []
Tasks.append(Task('hello'))
print(Tasks[0].parents)

commandloop()
