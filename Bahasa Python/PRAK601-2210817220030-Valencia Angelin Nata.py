baris, kolom = map(int, input().split())
angka=[]
a = 0
isi = list(map(int, input().split())); print("\n")
for i in range (baris):
    angka.append(isi[a:a+kolom])
    a = a + kolom
for baris in angka:
    for isi in baris:
        print(isi, end=' ')
    print()