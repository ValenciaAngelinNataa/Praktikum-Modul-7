ruangan = int(input())
isi = []
zetsu = list(map(int, input().split()));print("\n")
for i in range (ruangan):
    print((i+1)*zetsu[i], end=' ')