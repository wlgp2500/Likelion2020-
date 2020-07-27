class shape():
    def draw_shape(self,name):
        self.name=name
        print(self.name,"모양을 그립니다")
    def fill(self, color):
        self.color=color
        print(self.name,"은",self.color,"색 입니다.")
    def shape_size(self,size):
        self.size=size
        print(self.name,"은",self.size,"크기 입니다.")

def draw_shape(name):
        print(name,"모양을 그립니다")
def fill(name,color):
    print(name,"은",color,"색 입니다.")
def shape_size(name,size):
    print(name,"은",size,"크기 입니다.")
triangle=shape()

triangle.draw_shape("삼각형")

class solidShape(shape):
    def draw_shape(self,name):
        self.name=name
        print("나는 3D",self.name,"모양을 그립니다.")
square =solidShape()
square.draw_shape("사각형")
square.fill("노랑")
square.shape_size(5)