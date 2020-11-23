initial=input()
untouched=input()
a=initial.split('|')
summ=len(a[0])+len(a[1])+len(untouched)
needed=abs(len(a[0])-len(a[1]))
if summ%2!=0:
    print("Impossible")
elif needed>len(untouched):
    print("Impossible")
else:
    if len(a[0])>len(a[1]):
        for i in range(needed):
            a[1]+=untouched[i]
    else:
        for i in range(needed):
            a[0]+=untouched[i]
    for i in range(len(untouched)-needed):
        if i%2==0:
            a[0]+=untouched[needed+i]
        else:
            a[1] +=untouched[needed+i]
    print(a[0],'|',a[1],sep="")