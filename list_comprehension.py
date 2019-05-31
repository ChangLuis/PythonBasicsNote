#這是python獨有的list模式

array1 = []
into_array = [0,1,3,4,5,6,7]
for num in into_array:
    array1.append(num)
print(array1)
# 這是一般的流程加入新的內容進空的list裡面

array2 = [num for num in into_array]
print(array2)
# 這就是list_comprehension，直接在list裡面做for回圈

into_array_nest = [9,8]
array3 = [x*y for x in into_array for y in into_array_nest]
print(array3)
# 也可以像這樣用巢狀的list，前面的for回圈，是外層，後面的for回圈，是內層，
