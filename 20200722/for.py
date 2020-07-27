# for i in range(10):
#     print(i)


# my_dict ={'a':1,'b':2,'c':3}
# for k in my_dict:
#     print(k,my_dict[k])
# for k, v in my_dict.items():
#     print(k,v)

# Eng_dir =['a','b','c','d','e','f','g']
# Num_dir=[1,2,3,4,5,6,7]
# Kor_dir=['가','나','다']

# for e in Eng_dir:
#     print(e)
# for n in Num_dir:
#     print(n)
# for k in Kor_dir:
#     print(k)


# coin_box=[500,500,10,50,10,50]
# for c in coin_box:
#     if c==100:
#         print("100원 찾았다!")
#         break
#     else:
#         print("100원 아님")

# for c in coin_box:
#     if c!=100:
#         continue
#     print("100원을 찾았습니다")
#     break
        
# else:
#     print("100원이 상자에 없다.")

my_list=[]

for x in range(1,10):
    my_list.append(x)

print(my_list)

list_for = [x for x in range(1,10)]

print(list_for)

list_for = [x for x in range(1,10) if x%2 == 0]
print(list_for)

info=[1,2,8,22,3,5,20,6,99,22,76]
info = ['짝' if x%2==0 else '홀' for x in info if x<70]
print(info)

info = [(x,y) for x in range(1,10) for y in range(1,10)]
print(info)

info=[(x,y) for x in range(1,10) for y in "가나다라마바사아자차"]
print(info)