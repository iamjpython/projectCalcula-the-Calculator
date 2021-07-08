import math

class Calcula():

    def __init__(self):
        self.answer = 0
        self.input = ""

    def all_clear(self):
        return self.answer

    def delete(self, cal):
        input = str(cal)
        ans = input[0:len(input)-1]
        return ans

    # 4 basic operators ( + , - , × , ÷ )
    def evaluate(self):
        try:
            input = str(self.input)
            ans = eval(input)
            return ans
        except ZeroDivisionError:
            return "Can't divide zero"
        except SyntaxError:
            return "Syntax Error"

    def sin(self, num):
        try:
            input = num
            ans = math.sin(input)
            return ans
        except ValueError:
            return "Syntax Error"

    def cos(self, num):
        try:
            input = num
            ans = math.cos(input)
            return ans
        except ValueError:
            return "Syntax Error"

    def tan(self, num):
        try:
            input = num
            ans = math.tan(input)
            return ans
        except ValueError:
            return "Syntax Error"

    # arcsin
    def asin(self, num):
        try:
            input = num
            ans = math.asin(input)
            return ans
        except ValueError:
            return "Math Error"

    # arccos
    def acos(self, num):
        try:
            input = num
            ans = math.acos(input)
            return ans
        except ValueError:
            return "Math Error"

    # arctan
    def atan(self, num):
        try:
            input = num
            ans = math.atan(input)
            return ans
        except ValueError:
            return "Math Error"

    def ln(self, num):
        try:
            input = num
            ans = math.log(float(input))
            return ans
        except ValueError:
            return "Math Error"

    def log(self, num):
        try:
            input = num
            ans = math.log10(input)
            return ans
        except ValueError:
            return "Math Error"

    def factorial(self, num):
        try:
            input = num
            ans = math.factorial(input)
            return ans
        except ValueError:
            return "Math Error"

    def square(self, num):
        try:
            input = num
            ans = math.pow(input, 2)
            return ans
        except ValueError:
            return "Syntax Error"

    def cube(self, num):
        try:
            input = num
            ans = math.pow(input, 3)
            return ans
        except ValueError:
            return "Syntax Error"

    def square_root(self, num):
        try:
            input = num
            ans = math.sqrt(input)
            return ans
        except ValueError:
            return "Math Error"

    def pi(self, num):
        input = num
        ans = math.pi*input
        return ans

c = Calcula()
print(c.evaluate())
