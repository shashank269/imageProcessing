text=open("mbox-short.txt")
smm=0
count=0
for line in text:
    if line.startswith("X-DSPAM-Confidence:"):
        ipos=line.find(":")
        val1 = line[ipos+1:]
        
        val2 = float(val1)
        
        smm += val2
        count = count+1
avg=smm/count        
print("Average spam confidence:", avg)


