fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
   words_in_line = (line.rstrip()).split()
   for words in words_in_line:
      if words not in lst:
         lst.append(words)
print(lst)
lst_sor = sorted(lst)
print(lst_sor)
