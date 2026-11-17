import random
import sys
import matplotlib.pyplot as plt
sys.set_int_max_str_digits(0) #remove limit for output
a = [0]*100 #a is array for occurences of number from 1 to 100. tweak if needed
attempts = int(input()) #how many times should we test for the collatz conjecture
for i in range(attempts):
    n = random.randint((2**31)-1,(2**61)-1) #decrease numbers since we are repeating, again i chose Mersenne primes
    t = n
    while (n != 1):
        if (n%2):
            n *= 3
            n += 1
        else:
            n //= 2
        for _ in range(2):
            if (t%2):
                t *= 3
                t += 1
            else:
                t //= 2
        if (n <= 100):
            a[n-1] += 1
        if t==n:
            if (n != 1 and n != 2 and n != 4):
                print("loop")
                print(n) #outputs number if loop found. by conjecture this part of the code should never be run
            break
    print("Simulation:",i+1)
a[0] = attempts
a[1] = attempts
a[3] = attempts
#technically speaking 4 2 1 will always be reached by any number but my loop checker sorts of messes this up sometimes hence its hardcoded
#if necessary, do "print(a)" to output the array raw
print(a)
#just naming the bar chart
b = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
plt.yscale("log") #self-explanatory
plt.bar(b, a, color='darkslateblue', edgecolor='lavender', width = 0.8) #colour and edgecolour is just the colour and edge colour of the matplotlib graph
#0.8 is width default value (default heioght i using barh for horizontal bars)
plt.xticks(b[1::2], rotation = 30, fontsize = 10) #b[1:2] cause only even numbers to display on x-coordinates
plt.show()
