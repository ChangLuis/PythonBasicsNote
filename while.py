# while迴圈，他也是迴圈，只不過他迴圈的條件，你可以自己設定，while迴圈，可以再最後設定一個else條件式，邏輯就跟if else一樣

x = 0
while x < 10:
    print(f"Now the x value is {x}.")
    x += 1

y = 0
while y < 10:
    print(f"Now the y value is {y}.")
    y += 1
else:
    print(f"Now the y value {y} is more than the 10.")


for i in range(10):
    if i == 5:
        continue
    print(f"Now the i value {i} is not five.")
# continue 是特殊的指令，你可以設定一個條件，只要成立，我就跳過下面的code，直接執行下一個迴圈

for i in range(10):
    if i == 5:
        break
    print(f"Now the i value {i} is less than five.")
# break ，是當你的條件式成立時，我就直接跳出這整個迴圈，不會在繼續往下執行code，也不會再繼續迴圈

for i in range(10):
    pass
# pass，當python看到pass，他會直接跳去下一個迴圈，這pass指令，通常是用來幫助你建構程式邏輯時用的，
# 你可能目前只是在建構程式內容，還沒有要對內部作詳細的寫法，此時你就可以先在內容環境先寫一個pass，這樣python就不會對你的code做不正確的顯示
