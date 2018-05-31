a = input("숫자를 입력하세요 : ")
a = int(a)

if a < 10 :
    for i in range(1, 10):
        print(a, "*", i, "=", a*i)
else :
    print("10보다 작은 숫자를 입력해주세요")
