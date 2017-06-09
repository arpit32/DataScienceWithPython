# An important feature of Python functions is that arguments are passed using call by sharing.
#
# If a mutable object is passed as an argument to a function parameter, assignment statements using that parameter
# do not affect the passed argument, however other modifications to the parameter (e.g., modifications to a list using methods such as append(), remove(), reverse() or sort()) do affect the passed argument.

def modify_parameters(parameter1, parameter2):
    parameter1.insert(0,'x')
    print('paramter 1 after insert :', parameter1 )
    parameter2=[7,8,9]
    print('paramter 2 after assignment:' , parameter2)
    return

argument1=[1,2,3]
argument2=[4,5,6]
modify_parameters(argument1,argument2)
print(argument2,argument1)


# One way of preventing functions from modifying mutable objects passed as parameters is to make a copy of those objects inside the function.
#  Here is another version of the function above that makes a shallow copy of the list_parameter using the slice operator.

# Another way to avoid modifying parameters is to use assignment statements which do not modify the parameter objects but return a new object that is bound to the name (locally).


