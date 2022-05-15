from audioop import add
from doctest import OutputChecker
from unittest import result


class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s


    def show(self):
        print(self.hour, ":", self.minute, ":", self.second )

    def add(self, B):
        result = Time(0, 0, 0)
        result.hour = self.hour + B.hour
        result.minute = self.minute + B.minute
        result.second = self.second + B.second
        return result
    
    def sub(self, B):
        result = Time(0, 0, 0)
        result.hour = self.hour - B.hour
        result.minute = self.minute - B.minute
        result.second = self.second - B.second
        return result
        
    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        
        if self.second < 0:
            self.second +=60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

        
t1 = Time(2, 45, 10)
t2 = Time(5, 25, 45)

t1.show()
t2.show()

output1 = t1.add(t2)
output2 = t1.sub(t2)

output1.fix()
output2.fix()

output1.show()
output2.show()
        