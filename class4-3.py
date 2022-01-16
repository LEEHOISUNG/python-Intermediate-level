# 일급 함수 (일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(래퍼런스) 복사 후 저장 -> 후에 접근 (액세스) 가능
# 파이썬 변수 범위(scope)

## Closure 사용

def closure_ex1():
    series = []
    # Free variable
    # 클로저 영역
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closere1 = closure_ex1()

print(avg_closere1(10))
print(avg_closere1(20))
print(avg_closere1(30))

print()
print()

# function inspection
print(dir(avg_closere1))
print()
print(dir(avg_closere1.__code__))
print(avg_closere1.__code__.co_freevars)
print(avg_closere1.__closure__[0].cell_contents)

## 잘못된 클로저 사용

print()
print()
def closure_ex2():
    #Free varialbe
    cnt = 0 
    total = 0
    def averager(v):
        cnt = 1
        total += v
        return total / cnt
    return  averager


avg_closere2 = closure_ex2()

print()
print()
def closure_ex3():
    #Free varialbe
    cnt = 0 
    total = 0
    def averager(v):
        nonlocal cnt, total
        cnt = 1
        total += v
        return total / cnt
    return  averager


avg_closere3 = closure_ex3()
print(avg_closere3(15))
print(avg_closere3(35))
print(avg_closere3(45))
