#class 你可以視class為一堆要處理類似問題的function結合體

class sample():
    pass

print(sample)
print(sample())
# 第一個print，我們只是要印出class sample是甚麼，
# 第二個print，則是開啟這個class sample，所以python會印出導入記憶體的位置
# ()在之前就有講過，他就是執行的意思

mysample = sample()
print(mysample)
# 通常要用class，都要先實體化，也就是用一個變數代表，要不然無法重複使用

class animal1():
    def __init__(self,breed):
        self.breed = breed
# class，基本上是一堆function的集合體，那一開始通常也是要代入參數，
# python的class，特別定義了一個__init__ function，讓你可以定義這些參數，也方便你可以重複使用這些參數帶入不同的子funciton裡面
# 但要注意，class裡面的所有funciton，()內，最初的位置，都要打self，代表這是內部的func，
# self.xxx，就是內部其他的子func，呼叫參數的方式，
# self.breed = breed，等號後面的breed，當然是代表參數breed
# self."breed"的breed，是你定義要呼叫breed這個參數的入逕名，實際上，你可以不需要定義一樣的名稱，
# 你也可以換不同名稱定義，例如self.para1 = breed，只不過基本上會用同樣名稱代表
# 最上面animal旁邊的()，其實可以不用打，因為python強制定義用__init__ func代表你要填入的參數
# 最後我必須要講，function並沒有一定要強制使用參數，因此class其實也不一定要定義__init__，如果你class本身並沒有要用甚麼參數的話，可以不打

myanimal = animal1("lab")
print(myanimal.breed)
# 這樣就可以直接叫出參數，為什麼breed後面沒有括號?，需要括號代表內容必須透過呼叫才能操作，string本身不是func，不用呼叫，
# 如果你說，我要呼叫這個breed的內容啊!?，如果你這樣想就不太行，
# 我們是用self.breed當作變數，refer to breed這個參數，並不是呼叫!!

class animal2:
    species = "mammal"
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

myanimal = animal2("lab","jojo")
print(myanimal.species)
# 我們也可以直接在class裡面弄一個變數，在外部refer
# 其實不用把class想得太複雜，class基本上就是一個容器而已

class animal3:
    def __init__(self,breed,name,age):
        self.breed = breed
        self.name = name
        self.age = age
    
    def check(self):
         return f"This is class of animal3 and the breed is {self.breed},the name is {self.name} and the age is {self.age} "

myanimal = animal3("lab","jojo","18")
print(myanimal.check())

class animal4:
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    def check(self,age):
        return f"This is class of animal3 and the breed is {self.breed},the name is {self.name} and the age is {age} "

myanimal = animal4("lab","jojo")
print(myanimal.check(18))
# 如果某一個參數只會使用在某一個func裡面，你可以只在這個func定義需要這個參數，然後呼叫這個func時，再打入參數
# 就跟一般的function一個樣