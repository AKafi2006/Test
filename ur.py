class Docstate:

    def __init__(self , content):
        self.content = content
        self.next = None
        self.previos = None


class TextEditor:
    def __init__(self):
        self.current = None

    def addstate(self , content):

        newstate = Docstate(content)
        newstate.previos = self.current
        if self.current:
            self.current.next = newstate
        self.current = newstate

    def undo(self):
        if self.current and self.current.previos:
            self.current = self.current.previos

    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next

    def print(self):
        currentstate = self.current
        while currentstate.previos:
            currentstate = self.currentstate.previos
            

        while currentstate:
            print(currentstate.content)
            currentstate = currentstate.next



editor1 = TextEditor()

editor1.addstate('First state')

editor1.addstate('Second state')



editor1.undo()
editor1.undo()

editor1.redo()
editor1.redo()


editor1.print()

print(editor1.current.content)

