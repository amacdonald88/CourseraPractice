def dtrial (n):
    x = 1
    sum = 0
    while x < n != 0:
        if n % x == 0:
            sum = sum + x
        x+=1
    return sum
print ("I think it is " + str(dtrial (256)))