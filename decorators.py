# decorator，是在function裡面包function，然後呼叫外部的function來叫出內部funciton的寫法


def outside_func():
    def inside_func():
        return "Hello everybody!"
    return inside_func()

check_func = outside_func()
print(check_func)

check_func_wait_call = outside_func
print(check_func_wait_call())

# 不管怎麼叫出都可以，但重點是外部的func回傳的是內部的func


def hello():
    return "Hi I am luis."


def greet(put_in):
    print("Hello everybody!")
    print(put_in)

greet(hello())
# 這是最基本的寫法，鑲嵌別的func


def check_out():
    print("It's mosiac")


def new_func(original_func):
    def inside_func():
        print("It's inside part.")
        original_func()
    return inside_func()

new_func(check_out)
# 把代入的func，放進內部的func叫出
# 上述這種情況，python有一個語法糖可以簡單的操作


@new_func
def show_message():
    print("Wow! It's impressive.")

show_message
