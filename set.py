# set()裡面的內容，一定是不重複的、獨特的，所以他常常拿篩內容，你可以設一個空的set，然後慢慢加入東西
# 加入的物件只要是重複的，他只會存在一個在Set()裡面，set()跟dict()格式一樣，都是綣曲的括號，沒有順序index

my_set = set()
# 空set

my_set.add(1)
# 加入數字1進入my_set

print(my_set)
# ans: {1}

my_set.add("string")

print(my_set)
# ans: {1, 'string'}

mylist = [1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 8, 8, 9, 9]
mylist = set(mylist)
print(mylist)
# ans: {1, 2, 3, 4, 5, 6, 8, 9}

string = "around the corner"
string = set(string)
print(string)
# ans: {'e', 'u', 'n', 'a', 'h', 'r', 'c', 'o', 't', ' ', 'd'}
