players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
perem = list()
for name, score in players.items():
    perem += [tuple(name[0:] + tuple(score)[0:])]
print(perem)
