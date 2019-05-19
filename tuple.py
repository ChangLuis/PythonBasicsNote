#tuple，其實就跟list很像，只不過tuple用的是圓括號，而且一旦建立好內容，以後都不能更改，這部分跟string一樣

tuple1 = (1,2,3,4,"this is five.")
print(type(tuple1))
# ans: class tuple

tuple1[4]
# ans: "this is five." 叫出內容方式也與list、string一樣

tuple1.count(3)
# ans: 1

tuple1.index(4)
# ans: 3
# tuple 只有.count()與.index()這兩個method

tuple2 = ("just one element",)
type(tuple2)
# class tuple ，如果建立的tuple內部只有一個內容，你要在後面加一個逗號，python才會認為是tuple，
# 因為圓括號，邏輯的順位很低，基本上只要內容物沒有其他邏輯符號，圓括號本身不具任何意義
# 因此，你只加圓括號，而沒有逗點，python會認為內容物本身即是你要宣告的object


