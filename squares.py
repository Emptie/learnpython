squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

#数到20
for i in range(1,21):
    print(i)

#计算1~1000000之和
L = [i for i in range(1,1000001)]
print(min(L))
print(max(L))
print(sum(L))

#打印1~20间的奇数
L = [i for i in range(1,20,2)]
print(L)

#打印3~30之间可以被3整除的数
L = [i for i in range(3,30,3)]
print(L)

#1~10的立方列表
print([i**3 for i in range(1,11)])