asli = input()
palsu = input()
kode = len(asli)
pesan = len(palsu)
print ("\n")
x = 0
y = 0
if kode != pesan:
    print('Panjang kalimat berbeda, pesan palsu')
else:
    for i in range (kode):
        if asli[i] == palsu[i]:
            if (asli[i]==' '):
                print(" ", end =" ")
            else:
                print('*', end='')
                x+=1
        else:
            print('#', end='') 
            y+=1
    print('\n* = {}' .format(x))
    print('# = {}' .format(y))
    if x >= y:
        print('Pesan Asli')
    elif x < y:
        print('Pesan Palsu')