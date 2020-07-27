def func_name():
    print("call func")

print(func_name())

def progression(n,step=1):
    x=1
    while x<=n:
        print(x)
        x+=step
progression(10)

def kw_func(year,month,day):
    print("오늘은",year, "년",month,"월", day,"일 입니다.")

#일반적인 인수 전달 방법(위치 인수 전달 방법)
kw_func(2020,7,22)

def return_test(a,b,c,d):
    print(a+b)
    return b+c

outData =77
def func_1(parm):
    parm =parm+23
    print(parm)
func_1(outData)
print(outData)

def func2():
    global outData
    outData =outData+23
    print(outData)

func2()
print(outData)