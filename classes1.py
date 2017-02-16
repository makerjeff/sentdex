class calculator:
    # class methods need to have 'self' as the first argument in Python.
    def addition(self, x,y):
        added = x + y
        print added

    def subtraction(self, x,y):
        sub = x - y
        print sub

    def multiplication(self, x,y):
        mult = x * y
        print mult

    def division(self,x,y):
        div = x / y
        print div


calc = calculator()

calc.addition(5,6)