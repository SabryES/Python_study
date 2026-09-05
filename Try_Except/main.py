###to raise execption use keyword raise
#exmaple:
def div (num:int,num2:int):
    if num2==0:
        raise ArithmeticError("Division by zero ")
    return num/num2

# div(1,0)

## to handle execption use try except method 
try :
    div(1,2)
except Exception :
    print("an error occured during division")

#if i need to print the message at the the exception print e
try :
    div(1,2)
except ArithmeticError as e:
    print(f"an error occured during division:{e}")

else:
    print("passed") #not will executed if there is error 
finally:
    print("execution completed whatere succeedd or not") #keda keda hytnafez ayan kan fyh excpetion wla la2a