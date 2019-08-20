class Calculator:
    lastAnswer = 0
    dictionary = {}

    def multiply(self,*args):
        overall_num = 1
        for num in args:
            if num == 'LAST':
                num = self.lastAnswer
            elif num == 'SLOT_1':
                num = self.dictionary[1]
            elif num == 'SLOT_2':
                num = self.dictionary[2]
            overall_num *= num
        self.lastAnswer = overall_num
        return overall_num

    def addition(self,*args):
        overall_num = 0
        for num in args:
            if num == 'LAST':
                num = self.lastAnswer
            elif num == 'SLOT_1':
                num = self.dictionary[1]
            elif num == 'SLOT_2':
                num = self.dictionary[2]
            overall_num += num
        self.lastAnswer = overall_num
        return overall_num
    
    def last(self):
        return self.lastAnswer

    def set_slot(self,single_num):
        self.dictionary[single_num] = self.lastAnswer

    def get_slot(self,single_number):
        return self.dictionary[single_number]

calculator_instance = Calculator()
# print(calculator_instance.addition(2,2,2))
# print(calculator_instance.last())
# print(calculator_instance.multiply(2,2,2))
# print(calculator_instance.last())
# print(calculator_instance.addition(1,2))
# print(calculator_instance.multiply("LAST",5))

print(calculator_instance.addition(1,2))
calculator_instance.set_slot(1)
print(calculator_instance.get_slot(1))
calculator_instance.addition(10,20)
calculator_instance.set_slot(2)
print(calculator_instance.get_slot(2)) # should return 30
print(calculator_instance.addition(100,200)) # returns 300. The "last" value is updated
print(calculator_instance.get_slot(1)) # should return 3
print(calculator_instance.get_slot(2)) # should return 30
print(calculator_instance.last())

print(calculator_instance.addition(100,200)) # returns 300. The "last" value is updated
print(calculator_instance.get_slot(1) )# should return 3
print(calculator_instance.get_slot(2)) # should return 30
print(calculator_instance.last()) # should return 300 (just like before)

# THE FOLLOWING FUNCTIONALITY SHOULD WORK

print(calculator_instance.addition("LAST",10)) # should return 310 (= 300 + 10)
print(calculator_instance.addition("SLOT_1",5)) # should return 8 (= 3 + 5)
print(calculator_instance.multiply("SLOT_2",2)) # should return 60 (= 30 * 2)


