single_instance_str='p,k,f,n,f,n,f,c,n,w,e,?,k,y,w,n,p,w,o,e,w,v,d'
# print(single_instance_str)
single_instance_list=single_instance_str.split(',')
# print(single_instance_list)

# Accessing sequence elements & subsequences¶

# note the difference between the below two lines
print(single_instance_str[2])       #it will return the second indexed character(it can be anything), and in this case it would be the comma
print(single_instance_list[2])      #it will return the second element in the list. Elements contained in the list are seperated by comma, so the second element after the first comma would be printed

print(single_instance_str[-1])      #it will print the last character from the last
print(single_instance_list[-1])     #it will print the last element of the list. Basically the negative index implies the offset value from the end

print(single_instance_str[-2])      #conclusive from line number 12
print(single_instance_list[-2])     #conclusive from line number 13

print(single_instance_str[2:4])     #returns sliced set of characters from the pattern containing all the values between [start:end] exclusive of the 'end'
print(single_instance_list[2:4])

print(single_instance_str[-4:-2])
print(single_instance_list[-4:-2])

print(single_instance_str[:-1])
print(single_instance_str[:-2])
print(single_instance_str[1:])
print(single_instance_str[2:])

print(single_instance_list[:-1])
print(single_instance_list[1:])

print(single_instance_str[::2])
print(single_instance_str[1::2])
print(single_instance_str[::-1])

print('*', '\tp,k,f,n,f,n,f,c,n,w,e,       ?,k,y\t,w,n,p,w\n,o,e,w,v,d\n'.strip(), '*')

# Python strings are immutable, i.e., they cannot be modified. Most string methods (like str.strip()) return modified copies of the strings on which they are used.

# Python lists are mutable, i.e., they can be modified

list1=[1,2,3,4,5]

list2=list1 #list2 references to the same object as list1..hence any changes made to lsit1 will be reflected in list2

list2=list1[:]  #return a copy of list1 and now the two lists refer to two different objects

list1.remove(1) #removes the first occurence of 1 from the list





