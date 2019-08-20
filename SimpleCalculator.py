class Calculator:
    lastAnswer = 0
    # def __init__(self):
    #     last = 0

    def multiply(self,*args):
        overall_num = 1
        for num in args:
            overall_num *= num
        self.lastAnswer = overall_num
        return overall_num

    def addition(self,*args):
        overall_num = 0
        for num in args:
            overall_num += num
        self.lastAnswer = overall_num
        return overall_num
    def last(self):
        return self.lastAnswer

calculator_instance = Calculator()
print(calculator_instance.addition(2,2,2))
print(calculator_instance.last())
print(calculator_instance.multiply(2,2,2))
print(calculator_instance.last())


