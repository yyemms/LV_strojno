br = float()

while True:
        try:
            br = float(input("Unesite broj iz intervala [0.0 , 1.0]"))
            if(br >= 0.0 and br <= 1.0):
                break;
            else:
                print("Niste unijeli broj iz zadanog intervala")
        except:
            print("Došlo je do greške, nije unesen broj")
            exit()

if br >= 0.9:
    print("A")
elif br >= 0.8:
    print("B")
elif br >= 0.7:
    print("C")
elif br >= 0.6:
    print("D")
if br < 0.6:
    print("E")
