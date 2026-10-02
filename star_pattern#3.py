j=3
k=1
ch='A'
for i in range(0,5):
    for m in range(1,5):
        print(j*"  "+(m)*(ch+(" ")))
        ch=chr(ord(ch)+1)
        m+=2 
    j-=1
