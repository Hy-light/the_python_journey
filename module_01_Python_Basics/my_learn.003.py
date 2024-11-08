# Strings
# Strides in strings
letters = "ABCDEFGHIJK"
strided_letters = letters[0:4] #returns the first four lettters
print(strided_letters)

good = "GsoAo+d"
strided_good = good[::2] # returns the alternating characters starting at index 0 
print(strided_good)

word = "uppercase"
print(word.upper())

a = "hello"
# print(dir(a))

b = [1, 2, 0]
# print(dir(b))

b = {
    'key' : 'value',
    'num' : 1
}
print(dir(b))