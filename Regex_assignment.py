import re
fname = input("Enter file:")
fhand = open(fname)
Sum = 0
numbers = []
for line in fhand:
    line.rstrip()
    number = re.findall('[0-9]+' , line)
    for n in number:
        int_n = int(n)
        #print(int_n)
        Sum = int_n + Sum
    #int_number = int(number)
    #Sum = int_number + Sum
print(Sum)
#for n in numbers:
    #Sum = n + Sum
#print(Sum)
