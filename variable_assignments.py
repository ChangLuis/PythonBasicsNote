a = 10
#a變數定義為10

a = 20
#a變數重新定義為20
#python 是動態語言，同樣的變數可以重複定義

a = a + a
#a變數，重新定義為兩個原本的a變數相加

a += a
#a變數，另一種重新定義為兩個原本a變數相加的寫法

type(a)
#type() function 是辨認變數型態，但此行並沒有將此結果儲存在某變數，這會在後面無法重新使用

b = type(a)
#這樣就定義b代表type(a)的結果，後續可以重複使用這個結果

通話時間_每秒 = 100
計算金額_每秒_新台幣 = 0.1
總通話時間金額 = 通話時間_每秒 * 計算金額_每秒_新台幣
#python可以直接用中文字當作變數