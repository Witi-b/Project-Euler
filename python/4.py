n = 999
m = 999
y = str(n*m)
j = [] #Empty set of string numbers that will be converted to int
x = None   #Final set with integers
while x == None:        #While we do not have the set of palindrome numbers
    if y == y[::-1]: #if y is a palindrome, add it to the set j and move to the next number
        j.append(y)
        n = n - 1
        y = str(n*m)
        continue
    elif n < 1:
        n = m - 1
        m = m - 1
    else:
        n = n - 1
        y = str(n*m)
    if m == 900:
        x = [eval(i) for i in j]
        break
print(max(x))