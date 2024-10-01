'''num = int(input("Enter a number"))

match num:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case _:
        print("None")
'''

num = int(input("Enter a num : "))
match num:
    case 1:
        for i in range(1,11):
            print(1*i)
        
    case 2:
        for i in range(1,11):
            print(2*i)
    case 3:
        for i in range(1,11):
            print(3*i)
    case 4:
        for i in range(1,11):
            print(4*i)
    case 5:
        for i in range(1,11):
            print(5*i)
    case 6:
        for i in range(1,11):
            print(6*i)
    case 7:
        for i in range(1,11):
            print(7*i)
    case 8:
        for i in range(1,11):
            print(8*i)
    case 9:
        for i in range(1,11):
            print(9*i)
    case 10:
        for i in range(1,11):
            print(10*i)
    case _:
        print("Thik number type kar")