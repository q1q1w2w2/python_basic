# Chapter03-2
# 파이썬 문자형

# 문자열 생성



str1 = "I am Python"
str2 = 'Python'
str3 = """HI"""
str4 = '''gg!'''

print(type(str1),type(str2),type(str3),type(str4))
print(len(str1),len(str2),len(str3),len(str4))

# 빈 문자열
str1_t1 = ""
str2_t2 = str()

print(type(str1_t1), type(str2_t2))
print(len(str1_t1), len(str2_t2))

# 이스케이프 문자 사용

print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "What\'s on TV?"
print(escape_str2)

# 탭, 줄 바꿈

t_s1 = "Click \t Start!"
t_s2 = "New Line \nCheck!"

print(t_s1)
print(t_s2)
print()

# Raw String 출력

# raw_s = r'D:\Python\test' # 안되는데

# print(raw_s)
print()

# 멀티라인 입력

multi_str = '''
String
Multi line
Test
'''

# 역슬래시 사용
multi_str1 = \
'''
String
Multi line
Test
'''

print(multi_str, multi_str1)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print(True,type(True))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫 글자 대문자로 변환
print("endswith?: ", str_o2.endswith("e")) # 마지막 글자 확인
print("replace", str_o1.replace("thon", ' Good')) # 글자 대체
print("sorted: ", sorted(str_o1)) # 기준에 따라 정렬
print("split: ", str_o3.split(" ")) # 기준에 따라 분리
print()

# 반복(시퀀스)
im_str = "Good boy!"

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습
str_sl = "Nice Python"

print(str_sl[0:3]) # 3-1까지 나옴 -> 0, 1, 2 번 출력
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_sl[:10]
print(str_sl[1:9:2]) # str_sl[1:9] 인데 2단위
print(str_sl[-5:]) # 뒤에서부터 계산
print(str_sl[1:-2])
print(str_sl[::-1])

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))   # a 의 아스키코드 값
print(chr(122)) # 아스키코드 122의 값
