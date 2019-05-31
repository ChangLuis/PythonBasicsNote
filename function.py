#function，函式的使用，為什麼需要function?，只要會重複運用的程式，你可以把他們包成function，重複使用，這樣就不用一直重複打一樣的程式碼

def hello_func():
    print("Hello!")
# python的func定義，格式就像上述這樣，先寫一個def，就是define的意思，後面打上你要給予的名稱，最後要相連一個小括號，並且寫一個冒號，

hello_func()
# 如果內容沒有要回傳值，而是像上述這樣，只是要印出內容，你就直接像這樣呼叫，有寫上小括號，就是呼叫

hello_func
# 像這樣沒有寫小括號，python只會知道，這裡有一個func，但不會做任何操作

def name_hello(name = "Luis"):
    """
    This is a simple description.
    """
    print(f"Hello {name}")
# 在括號內定義參數，並且給予default值，即便你沒有給予參數，他依然可以執行，執行的就是default的內容
# 有填入就會跑你給的參數，
# 你可以簡單打一些說明，這樣別人看到這個你自己定義的func，人家就可以用help()，來確定你這個func主要是用來幹嘛

name_hello()
name_hello("jack")
help(name_hello)
#可以利用help() func 來看看你自己寫的描述，不過windows系統，有些時候可能會出現一些問題
