a = [2,0,5,7,1,3,0,4,9]

d = []
r = a[0]
for i in range(len(a)*2) :
    try :
        e = a[r]
        d.append(e)
        r = d[i]
    except :
        m='yahya_rhiba_code'

if len(d)<=len(a) :
    print("\ncircuit fermér n'existe pas et voila le circuit :")
    print(f"{d}\n")
else :
    print("\ncircuit fermér existe voila le : ")
    print(f"{d}\n")
