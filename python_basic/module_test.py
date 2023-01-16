# 모듈 사용 실습

import sys

print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:/math_py')

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10,3))
print('-' * 15)

import chapter06_02

print(chapter06_02.add(10,23))