class cal():

    def __init__(self):
        self.answer = 0

    def ac(self, calcula):
        return self.answer

    def delete(self, calcula):
        input = str(calcula)
        ans = input[0:len(input) - 1]
        return ans

    def evaluate(self, calcula):
        ans = str(calcula)
        ans = eval(ans)
        return ans
