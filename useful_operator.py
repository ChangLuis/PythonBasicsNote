#常會用到的operator

for i in range(10):
    print(i)
# 這在之前有介紹過，range() func，可以直接指定範圍做迴圈，也可以指定起始位置與間隔跳行


array1 = ["a","b","c","d","e"]
for idx,char in enumerate(array1):
    print(idx)
    print(char)
# enumerate() func 可以一邊迴圈出index的值，也可以迴圈出index的位置，非常方便，
# 規則是，第一個參數，代表index，第二個則是值


for charator in enumerate(array1):
    print(charator)
#當然，你可以只用一個變數，但這個變數就會自動含有index與值，輸出會發現，以tuple方式呈現


array2 = ["first","second","third","forth","fifth"]
for match in zip(array1,array2):
    print(match)
# zip() func 可以直接合併list的內容，依照index位置，並不限兩個，你可以好幾個，不同長度的list，以最短list長度為基準合併


for char1,char2 in zip(array1,array2):
    print(char1)
    print(char2)
# 你也可以像這樣，分開輸出，通常會用這種方法，去做for迴圈，執行內容的邏輯或修改!!


array3 = list(zip(array1,array2))
print(array3)


"a" in array1
# ans: True
# in 可以單獨使用，不一定要跟著for迴圈，in 只是單純來確認前方內容是否存在於後方內容，輸出的值，為boolean

min(array1)
# min() func 可以幫你快速查找出最小的值，字串與數字都可以


max(array1)
# max() func 可以幫你快速查找最大的值，字串與數字都可以


from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
shuffle(mylist)
print(mylist)
# shuffle() func 可以幫你對內容洗牌，但要記得，他不會回傳新的值，他是直接改變原本mylist的值


from random import randint
print(randint(0,10))
# randint() func 可以在你指定的範圍內，隨機叫出一個數字


input("Input one number : ")
# input() func 可以讓user輸入值，你可以把值記下來，做程式運算，或判斷
# 當然，你要給予一個變數，存取才能操作

result = input("Choosing a number : ")
# 但你要注意一件事情，input() func輸入的值，型態都是string，即便輸入的是數字，型態也是string，所以如果需要計算，都需要轉型態

str_num = "500"
type(str_num)
# ans: class str

int(str_num)
# ans: 500   將string型態的"500"，轉成integer的500

