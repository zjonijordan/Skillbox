print("Введите координаты монетки:")
x = float(input("x: "))
y = float(input("y: "))
R = float(input("Ведите радиус: "))

if (x or y) >= R or (x or y) <= -R:
    print("Монетки в области нет")
else:
    print("Монетка где-то рядом")