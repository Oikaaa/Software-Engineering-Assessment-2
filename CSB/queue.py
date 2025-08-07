import random

class Queue:
    def __init__(self):
        self.array = []
    
    def printQueue(self):
        return self.array

    def appendQueue(self, newValue):
        self.array.append(newValue)
        return self.array
    
    def removeQueue(self):
        removedValue = self.array.pop(0)
        return removedValue
    
    def lengthQueue(self):
        length = len(self.array)
        return length
    
    def emptyQueue(self):
        if len(self.array) == 0:
            return "Queue is empty"
        else:
            return "Queue is not empty"