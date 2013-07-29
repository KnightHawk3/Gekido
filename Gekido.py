#!/usr/bin/python2
# Import the maths
import math
import decimal
# Some pretty stuff I will use.
import locale
import time
import csv

# Choose if we want to measure how long its taking.
useTime = False

# Time when we start working on the program
if time: then = time.time()

# Make it known we want US style locale
locale.setlocale(locale.LC_ALL, 'en_US')

context = decimal.Context(rounding=decimal.ROUND_05UP,)

# Set it to be really accurate. If you want to run this in a shortis ammount of
# Time, set this to be smaller.
# Basically this means 1k decimal places.
decimal.getcontext().prec = 10000

# Set my deltas to be really accurate

# Hey, want to know what 999 zeros looks like.
k = decimal.Decimal("0.0000000000000000000000000000000000000000000000000000001")

delta = decimal.Decimal("0.000000000000000000000000000000000000000000000000001")


# What are we making a start as
a = decimal.Decimal("5.0")
# Calculating the gradient with thisvv
m = ((a**k)-1)/(k)

# b is the value I am subtracting or adding for my binary search algorithm
b = decimal.Decimal("2.5")

if time: print "Time:   %s" % (time.time() - then)

# While the gradient isn't equal to 1 + my delta (delta is how accurate it is)
with open('results.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Equation", "Result", "Gradient"])

i = 0

while m != 1 + delta:
    if time == True: then = time.time()
    
    # Use i to keep track of whether to print the full number of the scientific 
    # notation.
    if i != 5:
        i += 1
    else:
        i = 0
        
    a2 = a
    b2 = b
    # if the a value is too big, make it a bit smaller
    if m > 1:
        a = a - b

    # if the a value is too small, make it a bit larger
    elif m < 1:
        a = a + b

    # Make b smaller
    b = b / 2

    # Recalculate the gradient
    m = ((a**k)-1)/(k)
    # Print the working total
    print "Number: %s" % context.to_eng_string(a)
    if time == True: print "Time:   %s" % (time.time() - then)
    
    with open('results.csv', 'ab') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # If its the fith time, write it in full.
        if i == 5:
            writer.writerow(["$%s - %s$" % (a2, b2), "$%s$" % (a), "$%s$" % (m)])
        # Otherwise, write it in scientific notation.
        else:
            writer.writerow(["$%e - %e$" % (a2, b2), "$%e$" % (a), "$%e$" % (m)])

# Print it one last time when we are done!
print 10*"-"
print a