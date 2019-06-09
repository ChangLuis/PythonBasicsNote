# map funciton 不是python獨有的的函式，大部分的語言，基本上也都有map()


def square(num):
    return num ** 2

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 假設我現在要將list1裡面的數值，全部做square的函式，照之前的方式，基本上大概會這樣子做

for idx, num in enumerate(list1):
    list1[idx] = square(num)
print(list1)

for i in range(len(list1)):
    list1[i] = square(list1[i])
print(list1)

list1 = [square(num) for num in list1]
print(list1)
# 基本上可以用上述三種型式做解決

list1 = list(map(square, list1))
print(list1)
# 但現在你也可以用map()來達到一樣的效果，map(),就是幫你組合你想做的事情，以及初始值。
# 前面放的是function，後面放的是初始值，你要做怎樣的變化，用function包起來放在map()第一個參數位置，第二個則是你的初始值
# 但你要注意一件事情，map()他本身只是一個object，不會自動回傳值，所以你要搭配其他func叫出，
# 這裡我當然還是要以list形式叫出，所以在外面加一個list()，將值存成list

print(map(square, list1))
# 像這樣直接叫出，python會直接回傳 map object at xxxxxxxxx位置


# filter(),使用邏輯與map()一樣，他必須搭配其他func叫出，它的作用，是幫你篩選內容，你的條件，也適用func包起來放在前面

def check_even(num):
    return num % 2 == 0


def check_odd(num):
    if num % 2 != 0:
        return num

list2 = list(filter(check_even, list1))
print(list2)
list3 = list(filter(check_odd, list1))
print(list3)
# 要記得，filter() func，前面判斷function，一定要有True False的條件判斷，畢竟他是在幫你篩選內容


# lambda function，匿名函式，簡單講，就是這個函式不用名稱

lambda_square_root = lambda num: num**0.5
list4 = list(map(lambda_square_root, list1))
print(list4)
# lambda func，寫法很簡單，用lambda代替def，然後不用定義名稱，後面就直接寫上參數名，冒號後面就是內容，不用寫return
# 匿名函式，有一些操作限制，他只能寫在一行，所以內容寫法被限制，只能做一些單行內容

list5 = list(map(lambda num: num ** 0.5, list1))
print(list5)
# 當然，如果這個lambda不會重複使用，你就可以像這樣，直接寫在裡面

list6 = list(filter(lambda num: num % 2 == 0, list1))
print(list6)
