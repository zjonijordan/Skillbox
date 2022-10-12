N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))
listing = []

for i in range(N):
    listing.append(0)

for i in range(K):
    print(i + 1, "расписка")
    index_in = int(input("Кому: ")) - 1
    index_out = int(input("От кого: ")) - 1
    HM = int(input("Сколько: "))
    listing[index_in] -= HM
    listing[index_out] += HM

print("\nБаланс друзей: ")
for t in range(N):
    print(str(t + 1) + " :",  listing[t])
