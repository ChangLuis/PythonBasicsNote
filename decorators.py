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
# 這邊為什麼沒有括號？，居然可以成功呼叫內容？
# 其實是因為我在new_func裡面，直接return inside_func()，直接定義好一定要呼叫導致的
# 如果一開始return時，你沒有括號，那下面這個呼叫就需要加括號，可以自己選擇


def new_func_with_pars(parser_func):
    def inner_func(give):
        print("This is inner part.")
        parser_func(give)
    return inner_func


@new_func_with_pars
def inside_func(age):
    print(f'I am {age} years old.')

inside_func(29)
# 如果你要decorate的函式有包含參數，你就要特別注意，上面的new_func_with_pars，
# 裡面的return，你就不能加括號，因為括號內必須傳參數，你在這邊如果直接打return inner_func(give)
# 外部的new_func_with_pars他不認得give這個東西是什麼，這個give是內部inner_func定義的
# 因此外部func能做的就是回傳指向內部func
