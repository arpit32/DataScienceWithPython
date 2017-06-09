#a sample use case without list comprehension

DELIMITER = ' | '
delimiter_string = ''

token_list = ['a', 'b', 'c']

for token in token_list[:-1]:
    delimiter_string += token+DELIMITER

delimiter_string += token_list[-1]

print(delimiter_string)

#now with the help of the delimiter string

delimiter_string=DELIMITER.join(token for token in token_list) #simple!!!
print(delimiter_string)

