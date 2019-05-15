#利用format方式，使print輸出時，比較井然有序，不需要用一堆+號

print("This is a {} {}.".format("first","line"))
# {}內是你要代入的內容，內容則定義在.format()裡面

print("This is a {0} {1}.".format("second","line"))
# 你可以定義位置,format裡面的參數，預設就是0,1,2,3,4......

print("This is a {1} {0}.".format("line","third"))
# 也可以像這樣，做變化

print("This is a {a} {b}.".format(a = "fourth",b = "line"))
# 也可以像這樣自行定義變數，然後擺上位置

value = 17/3
print("The result is {}.".format(value))
# ans: The result is 5.666666666666667.   這樣會有很長的float內容，通常不會想要看到這種內容

print("The result is {:1.2f}.".format(value))
# ans: The result is 5.67.   在{}裡面定義float的長度，這裡設置最多兩個，會自動四捨五入

print("The result is {:1.4f}.".format(value))
# ans: he result is 5.6667. 這行定義float長度為四

print("The result is {r:1.2f}.".format(r =value))
# 定義變數表示  

name = "Jack"
print(f"My name is {name}.")
# 這是python3.6以後新增的format方式，比較簡短，更方便

print(f"The result is {value:1.2f}.")
# 是不是比較簡單，format格式，看起來就像dictionary

num = 516
print(f"This number is {num:0>5d}")
# ans: This number is 00516  這是自動補零，總深度depth為5個單位

