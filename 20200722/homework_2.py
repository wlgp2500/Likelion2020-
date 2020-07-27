class human:
    def eating(self,name,time="맛있는"):
        print(name,"은 ",time," 식사를 합니다.")
    def cooking(self,name):
        print(name,"은 요리를 합니다.")
    def studying(self,name):
        print(name,"은 공부를 합니다.")
    def exerciising(self,name):
        print(name,"은 운동을 합니다.")

class student(human):
    def studying(self,name):
        print(name,"은 시험 공부를 합니다.")

class chef(human):
    def cooking(self,name):
        print(name,"은 맛있는 요리를 합니다.")
        
class athlete(human):
    def execising(self,name):
        print(name,"은 훈련을 합니다.")

adult=human()
adult.eating("어른","저녁")

child1=student()
child1.studying("아이1")

child2=chef()
child2.cooking("아이2")

child3=athlete()
child3.execising("아이3")


