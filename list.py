# list與string用同樣邏輯index儲存，只不過list可以直接對內容物做改變

list1 = [1, 2, 3]
list1 = ["1", "2", "3"]
list1 = ["1", 2, "神功護體"]
list1 = [1, [2, 3]]
print(list1)
# list內容,可以是任何object,並且可以混用

print(list1[0])
# list叫出內容方式，也是index

print(list1[0:])
# index任何模式一樣都可以套用

list1[1] = "掃地神僧"
print(list1)
# 不同於string，list可以直接指定內容作改變

list2 = ["html", "css", "javascript", "node.js"]
list3 = ["python", "flask", "django"]
list4 = list2 + list3
print(list4)
# 一樣支持串接concatenation

list5 = []
list5 = list()
# 空list的兩種定義，但要注意一件事情，只有後者可以定義更改object類型為list


list5.append("令狐沖")
list5.append("獨孤九劍")
print(list5)
# .append()新增內容，設定為新增至index -1的位置，也就是最後一個位置，big-O(1)

list5.pop()
print(list5)
# .pop()移除內容，可以在括號內定義index參數，如果沒有輸入，預設為-1

list5.pop(0)
print(list5)
# 選擇index移除

list5.append("風清揚")
list5.append("獨孤九劍")
mr_wind = list5.pop(0)
print(mr_wind, list5)
# 被pop的value可以賦予變數定義，這在資料結構的某些實踐，很好用
# "風清揚"依然被移除於list5

list6 = [7, 5, 3, 1, 75, 69, 56, 23, 73]
list7 = ["z", "c", "l", "a", "e"]
list8 = ["b", "z", "A", "i", "E"]
list6.sort(), list7.sort(), list8.sort()

print(list6), print(list7), print(list8)
# .sort()排序內容，不管是數字或英文字母，英文字母，優先排列大寫，再排小寫
# 排列順序，預設是以小到大
# python可以在一排做指令

list9 = list6.sort()
print(list9)
# 要注意的是，.sort()，並不會回傳新的值，他只是更改原本的變數
# 如果你想要回傳新的值，而不影響原本的變數呢?

list9 = sorted(list6)
print(list9)
# sorted()，這個function做的事，跟list內建method .sort()一樣，但她可以回傳新的值
# sorted()是獨立function，所以他可以用在list以外的object

list7.reverse()
print(list7)
# .reverse()反轉內容

list6.sort(reverse=True)
list10 = sorted(list8, reverse=True)
print(list6, list10)
# .sort()與sorted()，也有內建參數可以直接反轉
