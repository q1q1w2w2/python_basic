# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) -> 불변
# 수정되면 안되는 값

# 선언

a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 10000, 'Ace', 'Base', 'Captine')
e = (100, 10000, ('Ace', 'Base', 'Captine'))
print(type(a), type(b)) # 튜플로 인식시키려면 콤마 필요

# 인덱싱
print('>>>>>')
print('d - ',d[1])
print('d - ',d[0] + d[1] + d[1])
print('d - ',d[-1])
print('e - ',e[-1])
print('e - ',e[-1][1])
print('e - ',list(e[-1][1])) # 리스트 형 변환

# 수정x
# d[0] = 1500 -> 수정 안된다는 에러 발생

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing, Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t
print(type(t))
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)