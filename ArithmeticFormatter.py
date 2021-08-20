def arithmetic_arranger(arr,value=False):
    n1 = []
    n2 = []
    l1 = []
    l2 = []
    l3 = []
    h = []
    op = []
    out = []
    for items in arr:
        if '+' in items:
            number = items.split(' + ')
            n1.append(int(number[0]))
            n2.append(int(number[1]))
            l1.append(len(number[0]))
            l2.append(len(number[1]))
            op.append("+")
        elif '-' in items:
            number = items.split(' - ')
            n1.append(int(number[0]))
            n2.append(int(number[1]))
            l1.append(len(number[0]))
            l2.append(len(number[1]))
            op.append("-")
    for i in range(len(n1)):
        if n1[i] >= n2[i]:
            h.append(l1[i] + 2)
        else:
            h.append(l2[i] + 2)
    for i in range(len(n1)):
        j = h[i]
        for k in range(j-l1[i]):
            print(" ",end="")
        print(n1[i],end="")
        print("\t",end="")
    print("")
    for i in range(len(n1)):
        print(op[i],end="")
        j = h[i]
        for k in range(j-l2[i]-1):
            print(" ",end="")
        print(n2[i],end="")
        print("\t",end="")
    print("")
    for i in range(len(n1)):
        for k in range(h[i]):
            print("_",end="")
        print("\t",end="")
    print("")
    if value:
        for i in range(len(n1)):
            out.append(eval(arr[i]))
            val = len(str(eval(arr[i])))
            l3.append(val)
        for j in range(len(n1)):
            for k in range(h[i]-l3[i]):
                print(" ",end="")
            print(out[j],end="")
            print("\t",end="")
                
if __name__ == "__main__":
    arithmetic_arranger(["21 + 5","2 - 100"],True)
    