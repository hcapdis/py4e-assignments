#fname = input("Enter file name: ")
#fh = open(fname)
#output = []
#count = 0
#for line in fh:
    #words = line.split()
    #if 'From' in words:
      #print(words)
      #output_1 = words[words.index('From') + 1 : words.index('From') + 2]
      #print(str(output_1))
      #output.append(output_1)
      #count = count + 1 
#print(*output, sep = "\n")
#print('\n'.join(map(str, output)))
#print("There were", count, "lines in the file with From as the first word")

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fhand = open(fname)
count = 0

for line in fhand:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1
	
    

print("There were", count, "lines in the file with From as the first word")
