#物件導向，換句話講，通常來講，就是class去繼承另一個class的內容，讓你可以方便使用另一個class的內容
#那為什麼要這樣子操作?
#之前就有講過，class基本上就是一堆function的集合體，有很多的function基本上要被重複使用時，有繼承這個方式，可以讓世界更美好!
#一堆function會被重複使用，代表這兩個class，要處理的內容範圍，基本上可以說是在同一個領域，
#因此，也會有人這麼解釋，class繼承模式就像生物學的界門綱目科數種，被繼承的class，代表他的內容物越容易被廣泛的使用
#去繼承的class，就越分門別類，內容也越專精在某個範圍

class Animal():
    def __init__(self):
        print("The creature is an animal.")
    
    def who_am_I(self):
        return "I am an aniaml."
    
    def eat(self):
        return "Maybe vegetable or meat."

sample_animal = Animal()
print(sample_animal)
print(sample_animal.eat())
# __init__被定義不能return 任何內容，但你可以用print


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("The creature is a dog.")
    
    def who_am_I(self):
        return "I am a dog."
    
    def eat_food(self):
        return "I want to eat meat."

the_dog = Dog()
print(the_dog)
print(the_dog.who_am_I())
# 與被繼承的class，如果有相同名稱的func，會被當前的func覆寫，只會執行當前的func內容，
# 當然你也可以在當前的func裡面對被繼承裡面相同名稱的func做呼叫，這樣你可以使用

print(the_dog.eat())
# 可以直接操作被繼承的func
print(the_dog.eat_food())

class Puppy(Dog):
    def __init__(self,name):
        self.name = name
    
    def who_am_I(self):
        return f'My name is {self.name} and I am cute Dog.'

    def eat_food(self,choice):
        Dog.eat_food(self)
        return f"But now I want to drink {choice}."
# 這個Dog.eat_food(這個self一定要打)，只要是class裡面的func，最前面的參數，都一定要打self，
# python規定class裡面的func，第一個參數位置一定要聲明所屬權限

mypuppy = Puppy("Jack")
print(mypuppy.who_am_I())
print(mypuppy.eat_food("milk"))
