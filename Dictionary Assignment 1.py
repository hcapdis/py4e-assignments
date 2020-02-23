fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
count = 0
sender_names = {}
for line in fhand:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        #print(words[1])
        sender_names[words[1]] = sender_names.get(words[1],0) + 1
        count += 1
#print(sender_names)
max_count = 0
max_count_sender = []
for senders in sender_names:
    if sender_names[senders] > max_count:
       max_count = sender_names[senders]
       max_count_sender = senders
print(max_count_sender, max_count)
