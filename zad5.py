naziv = input("Unesite ime datoteke:\n")
dat = open(naziv)
rjecnik={}
br=0

for line in dat:
    r=line.split( )

    for rijec in r:
        if rijec in rjecnik:
            rjecnik[rijec] += 1
        else:
            rjecnik[rijec] = 1

for rijeci in rjecnik:
    if rjecnik[rijeci]==1:
        br+=1

print(rjecnik)
print(br)