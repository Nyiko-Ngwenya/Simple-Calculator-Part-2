class Calculator:
    # def __init__(self,name):
    #     self.name = name
        
    def multiply(self,*args):
        overall_num = 1
        for num in args:
            overall_num *= num
        return overall_num

    def addition(self,*args):
        overall_num = 0
        for num in args:
            overall_num += num
        return overall_num

calculator_instance = Calculator()
print(calculator_instance.addition(2,2,2))
print(calculator_instance.multiply(2,2,2))
