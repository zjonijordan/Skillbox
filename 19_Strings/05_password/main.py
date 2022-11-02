flag = True
numbers = '0 1 2 3 4 5 6 7 8 9'.split()
abc = 'A, E, I, O, U, Y, B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z'.split(", ")
while flag == True:
    password = input("Придумайте пароль: ")
    numbers_in_password = [i for i in password for k in numbers if i == k]
    words_in_password = [i for i in password for k in abc if i == k or i == k.lower()]
    Upper = [i for i in words_in_password if i == i.upper()]
    for i in words_in_password:
        if len(Upper) >= 1 and len(numbers_in_password) > 3 and len(password) >= 8:
            print("Это надёжный пароль!")
            flag = False
            break
        else:
            print("Пароль ненадёжный. Попробуйте ещё раз.")
            break