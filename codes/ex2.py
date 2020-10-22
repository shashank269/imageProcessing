fname = input("Enter file name: ")
fh = open(fname)
count=dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    word=words[1]
    ipos=word.find("@")
    ser=word[ipos+1:]
    
    count[ser] = count.get(ser, 0) + 1
print(count)      
