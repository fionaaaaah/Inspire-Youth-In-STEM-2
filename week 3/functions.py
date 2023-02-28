#block of code that are executed together

#function use def keyword
def print_name():
    print("My name is Fiona")
    print("I am 18 years old")
    print("I live in Nairobi")

def add_numbers(num1 , num2):
    sum_num = num1 + num2
    print(sum_num)

def sub_numbers(num1 , num2):
    sub_num = num1 - num2
    print(sub_num)

def quo_numbers(num1 , num2):
    quo_num = num1 / num2
    print(quo_num)

def pro_numbers(num1 , num2):
    pro_num = num1 * num2
    print(pro_num)

#calling/invoking is the function
print_name()
add_numbers(20,30) #pass the parameters
add_numbers(4,5)
sub_numbers(20,30)
quo_numbers(20,30)
pro_numbers(20,30)