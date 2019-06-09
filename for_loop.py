# for loop 迴圈的使用，基本上與其它的程式差不多，差別在於，python內建的for迴圈，已經非常的簡潔

array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for num in array:
    print(num)
# num 代表每一個array的index值，從index 0開始，
# 當完成內部的code之後，自動疊加1位，也就是index 1的內容，然後又做一輪內部的code，
# in array，代表，所有在array的數值，
# 所以從頭到尾解釋一遍，就是，輪遍在array這個list裡面的所有index的值，每個值以num代表

for check in array:
    print(check)
# 代表的變數，可自行隨意更改，只要自己看得懂就好，不過最好養成一個習慣，代表的變數，最好取一個有意義的名字，
# 這樣過一陣子你回來看，會比較清楚

for num in array:
    print("hello")
# 並沒有人規定你用這個array，就一定要操作這個array裡面的值，你可以像這樣，單純的只是調用這個array的長度，
# 然後輸出別的內容，不過通常這種情況很少見

number = 0
for i in range(10):
    number += i
print(number)
# range()是一種特殊的func，它可以在裡面設定一個範圍，然後用for迴圈叫出，像這裡就是叫出內容0,1,2,3,4,5,6,7,8,9，順著累加進number這個變數
# range()實際上可以輸入三個參數，一個起始位置，一個是終了範圍，一個是跳躍的範圍
# 像此例子range(10)，在python看起來，是range(0,10,1)

sum_number = sum(range(10))
print(sum_number)
# 你可以利用sum()這個func，直接做上面的行為
