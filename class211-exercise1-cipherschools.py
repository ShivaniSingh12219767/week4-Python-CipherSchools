def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # You can't divide a number by zero(0)
        print(err)
    except TypeError as err:
        print("Numbers must be integer or floats")
    except:
        print("Unexpected error")
a=int(input("Enter a number:")) 
b=int(input("Enter second number:"))       
print(divide(a,b))