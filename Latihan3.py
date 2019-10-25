print("===================================")
print("Menentukan Bilangan Terbesar")
print("==================================="+'\n')
print("Silahkan Masukkan Bilangan")
a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))
print('')
if a>b and a>c:
    print(a, "adalah bilangan terbesar")
elif b>a and b>c:
    print(b, "adalah bilangan terbesar")
elif c>a and c>b:
    print(c, "adalah bilangan terbesar")