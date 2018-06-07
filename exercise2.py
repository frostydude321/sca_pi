x = raw_input('enter the first Interger')
y = raw_input('enter the second Interger')

print 'x =', x,'type is',type(x)
print 'y =', y,'type is',type(y)

if x > y:
    maximum = int(x)
    minimum = int(y)
else: 
    maximum = int(y)
    minimum = int(x)

print 'the maximum is',maximum
print 'the minimum is', minimum
print 'the maximum - mimimum',maximum - minimum


