#Chapter02-1 print 사용법

#기본 출력
print('hi')
print("hi")
print() #줄바꿈
print('''hi''')
print("""hi""")
print()

#separator 옵션
print('P','Y','T','H','O','N',sep='|')
print('010','7777','7777',sep='-')
print()

#end 옵션
print('Welcome to',end='        ')
print('IT News',end='     ')
print('Web Site')
print()

#file옵션
import sys
print('Learn Python',file=sys.stdout)
print()

#format 사용(d : 3, s : 'python' , f : 3.1444443)
print('%s %s' %('one','two'))
print('{0} {1}'.format('one','two'))
print('{1} {0}'.format('one','two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%5s' % ('nicenice'))
print('%.5s' % ('nicenice'))
print('{:10.5}'.format('pythonsutdy'))


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))


# %f
print('%1.3f' % (3.14141414141141414))
print('{:1.3f}'.format(3.141414141414))

print('%06.2f' % (3.123456767782))
print('{:06.2f}'.format(3.141414141414))

print()
