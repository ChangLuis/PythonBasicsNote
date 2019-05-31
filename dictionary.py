#字典，以捲曲的括號{}，來代表，list是靠index來搜尋內容，而字典則是靠關鍵字來搜尋內容，關鍵字key可以自己定義，內容value也是自己定義
#字典沒有所謂的順序，未來你會學到collections module，裡面會有一個orderdict()，會記住dict的順序

dict0 = {}
dict0 = dict()
# 新建一個空的dictionary的兩種方式，但要注意，如果是要去改變別的object的type變成dict，需要用後者

dict1 = {"key1":"value1","key2":"value2","key3":"value3"}
# 冒號前，表示key，冒號後，表示value

dict2 = {1:"1",2:"2",3:"3"}
dict3 = {"k1":999,"k2":[6,9,2],"k3":{"I'm inner dict":3345678}}
# key可以是num或string，value可以是任何object

dict1_value1 = dict1["key1"]
print(dict1_value1)
# 呼叫內容的方式，用的也是list括號，但內容是輸入key

print(dict3["k3"]["I'm inner dict"])
# 多層字典呼叫，就像這樣，一層一層打入key

dict3["k4"] = "this is add line."
print(dict3)
# 增加字典內容，就是這麼簡單，打入一個新的key，後面就是輸入值

dict3["k1"] = "modified value"
print(dict3)
# 更該原字典的key and value，也是如此簡單

print(dict3.keys())
# .keys()叫出所有key

print(dict3.values())
# .values()叫出所有value

print(dict3.items())
# .items()叫出所有key and value組合




