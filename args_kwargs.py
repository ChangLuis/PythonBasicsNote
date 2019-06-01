#這是兩個特殊的參數表示法，args代表參數是一般object，前面加一個星號*，代表不用特別指定參數的數量，
#kwargs代表參數是字典類的object，或說key and value的object，前面兩個星號**，也是代表不用特別指定參數的數量，
#正確寫法，*args、**kwargs
#要清楚一件事情，args與kwargs，他們本身也只是參數名，他們其實可以改變，不變的是*與**，如果沒有特殊需求，寫上args與kwargs，比較容易被識別

def func(*args):
    return args

print(func(123,456,789))
# 不需要指定輸入參數數量

def myfunc(**kwargs):
    if "water" in kwargs:
        print(f"I am thirsty，so I need {kwargs['water']} .")
    else:
        print("I am good.")
# 上述我遇到一個問題，括號內的'water'，必須用單引號，如果用雙引號，會與外面的雙引號衝突，但vscode不會自動將雙引號與雙引號match顏色，
# 導致我第一時間沒注意到...這可能要注意一下

myfunc(water = "cola")
myfunc(food = "rice")

def myfunc2(*args,**kwargs):
    print(f"The fist part is args variable {args[0]} and the second part is kwargs variable {kwargs['color']}")

myfunc2(123,"check",789,color = "red",change_color = "green")
# 你只要參數都有定義好，絕對沒有問題