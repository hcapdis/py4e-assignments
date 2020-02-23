fname = input("Enter file name: ")
fh = open(fname)
count = 0
confidence = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    for i in line.split():
        try:
            confidence_line = float(i)
            break
        except:
            continue
    confidence = confidence + confidence_line
print("Average Confidence:", confidence/count)    
print("Done")
