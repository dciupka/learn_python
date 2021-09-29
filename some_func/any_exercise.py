# List
l = [4, 5, 1]
print(any(l)) # output TRUE

z =[0,0,False]
print(any(z)) # output  FALSE


x = [1, 2, False]
print(any(x)) # output True

# Tuple
empty = ()
print(any(empty)) # output FALSE


# Set
print('*******sets*******')
s = {1,2,3,4,True}
print(any(s)) # output TRUE

x= {False,0, False,0}
print(any(x)) # output FALSE


empty_set = {} 
print(any(empty_set)) #output FALSE


print('******dic********')

d ={ 1: 'Hello', 2: 'HI'}
print(any(d)) # output True

d = { 0: 'hello', False:'nic'}
print(any(d)) # output False

d = { 0:'hi', 1:'hello'}
print(any(d)) #output True


print('*******STRINGS******')

s = 'Hello World'
print(any(s)) #output True

s = '000'
print(any(s)) #output TRUE

s= ''
print(any(s)) #output FALSE
