#1.A.Test case 1
a = int(input("Masukkan awal deret: "))
b = int(input("Masukkan akhir deret: "))
for count in range(a, b):
    if count%6 != 0 and count%3 != 0 and count%2 ==1:
        print(count)

#1.B.Test case 2
a = int(input("Masukkan awal deret: "))
b = int(input("Masukkan akhir deret: "))
for count in range(a, b):
    if count%6 != 0 and count%3 != 0 and count%2 ==1:
        print(count)
