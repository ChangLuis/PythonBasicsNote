# python紀錄字串，可以利用index叫出內容

string1 = "Hello"
# 可以用雙引號

string2 = 'Hello'
# 可以用單引號

string3 = "I'm Jack."
# 可以如此錯開單引號與雙引號，保證內容正確性與施打方便度

print("Hello \n World!")
# string內的\n ，有具體意義，代表要-換行-

num1 = 123
str_num1 = str(num1)
# str() 更改型態成string的方式

len_str_num1 = len(str_num1)
print(len_str_num1)
# output: 3   len()function可以查詢類list(string)或list(array)的長度

string4 = "Jack is a painter."
# 可以利用array模式呼叫string個別index上的內容，或某範圍index內容

print(string4)
# output: Jack is a painter.  index記憶位置，假設長度為10，以左到右為順序的話，為0,1,2,3,4,5,6,7,8,9
# 如果以右到左為順序的話，0,-9,-8,-7,-6,-5,-4,-3,-2,-1 ，也可以是 -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(string4[2])
# ouput: c

print(string4[-1])
# ouput: .   最後一個的index，一定是-1,是不是很方便，不用先找出長度!!

print(string4[0:3])
# output: Jac
# # 要記住一件事，範圍的尾巴，預設是不輸出的，如果你想要輸出尾巴的內容呢?

print(string4[5:])
# output: is a painter.  尾巴不要設位置就行了，他就會預設全部輸出

print(string4[::])
# 後面一個冒號，是代表你要間隔幾個index輸出，像此行，就全部都沒有設置，就會全部為預設模式，原字串全部輸出，預設間隔距離為1

print(string4[::2])
# output: Jc sapitr 間隔2輸出

print(string4[::-1])
# output: .retniap a si kcaJ 以右到左為順序輸出

print(string4[1:11:3])
# ouput: a  p  空格在字串裡面也是佔一個index記憶體位置!!


name = "Jack"
name_part = name[1:]
renew_name = "H" + name_part
print(renew_name)
# output: Hack  字串本身不可以重新定義或者說複寫，例如 name[2] = "l",這是不允許的，It's immutable.
# 你要嘛重新定義全部的內容，或者就像上面那樣做串接

string5 = "I know that the ones who love us, will miss us."
string5 = string5.upper()
print(string5)
# string5 : I KNOW THAT THE ONES WHO LOVE US, WILL MISS US.  .upper() 會將內容全部轉成大寫

string5 = string5.lower()
print(string5)
# string5: i know that the ones who love us, will miss us.   .lower() 將內容全部轉乘小寫

string6 = string5.split()
print(string6)
# string6: ['i', 'know', 'that', 'the', 'ones', 'who', 'love', 'us,', 'will', 'miss', 'us.']
# .split() 會將字串內容依照()內的參數做分隔，並且以list模式回存，如果沒有定義參數，預設為以-空格-為分隔

string7 = string5.split("o")
print(string7)
# string7: ['i kn', 'w that the ', 'nes wh', ' l', 've us, will miss us.']
# 參數輸入"o"，以o做分隔
