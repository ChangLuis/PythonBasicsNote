from collections import Counter as C

# 我們現在要引入collections models裡面其中一個module,稱作Counter
# 這個Counter是方便你統計內容數量用的，
# 排序方式是由數量最多到最少，decreasing sort
# 因為collections有好幾個module,所以你直接import collections會直接載入多個module
# 要呼叫來操作時，也挺麻煩的，必須寫成，例如，collections.Counter()

list1 = [1, 1, 2, 3, 4, 5, 1, 2, 2, 3, 4, 5, 7, 9]
result1 = C(list1)
print(result1)

list2 = ['asdasdasfasdasdasdfasdf']
result2 = C(list2[0])
print(result2)

list3 = 'asdasdasdasfsfasdfasdfasdf'
result3 = C(list3)
print(result3)

list4 = ['a', 'b', 'w', 'a', 'b']
result4 = C(list4)
print(result4)

list5 = 'How many times does word shows up in this statement word word'
split_list5 = list5.split()
result5 = C(split_list5)
print(result5)
print(result5['word'])
# Counter() 操作模式就是dict,但object是Counter

print(result5.most_common())
print(result5.most_common(3))
# most_common() method可以自己決定出現次數最多前幾個
# 如果沒有選擇，他就會輸出全部，
# most_common(),格式會轉成list!!

print(result5.most_common(5)[::-1])
# 如果你想要increasing輸出，可以這麼做

print(dict(result5))
# 轉成純字典

print(list(result5))
# 轉成list,但只會出現key的部分

print(result5.values())
# 純粹輸出value，用法就跟dict一樣

print(sum(result5.values()))

print(type(C()))
