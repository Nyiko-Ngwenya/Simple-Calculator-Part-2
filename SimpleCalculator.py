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
        return 'Set'

    def get_slot(self,single_number):
        return self.dictionary[single_number]





