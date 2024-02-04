def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
operations={
    1:add,
    2:subtract,
    3:multiply,
    4:divide
}
def calculate():
    print("Menu")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice=input_number("Enter your choice(1-4): ")
    num_1=input_number("Enter the value of p: ")
    num_2=input_number("Enter the value of q: ")
    func=operations.get(choice)
    if func:
        result=func(num_1,num_2)
        if result is not None:
            print(result)
        else:
            print("Invalid operatiob")
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input")
            continue
calculate()
