if "pyhton":
    print("Hello, World!")

    print(bool("python"))
    print(bool(0))

if True:
    print("코드 1")
if True:
    print("코드 2")

if True:
    print("코드 1")
elif True:
    print("코드 2")
    

x=1
y=77
z=0
result = x if x > y  else y
print(result)

result = x if x>y else y if y > z else z
print(result)