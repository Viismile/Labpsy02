#Langkah-langkah:
- Pertama kita membuat perintah untuk menginput bilangan pertama sampai ketiga. Dengan perintah:
```python
a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))
```
- Lalu kita membuat program dengan menggunakan statement if dan operators logical dan comparison. Contoh:
```python
if a>b and a>c:
    print(a, "adalah bilangan terbesar")
elif b>a and b>c:
    print(b, "adalah bilangan terbesar")
elif c>a and c>b:
    print(c, "adalah bilangan terbesar")
```
Dalam program ini, jika bilangan a lebih besar dari b dan c, maka outputnya adalah a. Dan jika bilangan b lebih besar dari a dan c, maka outputnya adalah b. Jika a dan b bukan bilangan terbesar, maka outputnya adalah c.