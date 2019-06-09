# 一般我們程式碼，如果出錯，執行後，就會停止，並且出現錯誤訊息
# 如果我們是要弄一個操作介面，總不能輸入有問題，就讓程式停下來，我們必須讓程式一直跑著
# 又或者，我們要特別處理一些特殊的錯誤，要讓它出現我們自訂的錯誤訊息，都可以用try except


def input_data():
    try:
        answer = int(input("Please input the number:"))
        print(f"Your input is correct.")
    except:
        print("Your input is not number.")

input_data()
# 這是最基本的寫法，只要try裡面有內容是不對的，就會跳去except裡面執行代碼


def input_data2():
    try:
        answer = int(input("Please input the number:"))
    except:
        print("Your input is not number!")
    else:
        print("Your input is correct.")

input_data2()
# else部分，則是try裡面的代碼都沒有問題，執行完try的內容，就會跳進else裡面執行


def input_data3():
    try:
        answer = int(input("Input the number :"))
    except:
        print("Check your input.")
    else:
        print("Correct!")
    finally:
        print("I always present!")

input_data3()
# finally部分，就是不管如何，他到最後一定會執行


def input_data4():
    try:
        answer = int(input("Number:"))
        print("Yeah!")
    except TypeError:
        print("Your input is not correct type!")
    except ValueError:
        print("Your input value is not correct!")

input_data4()
# except部分，我還可以因應不同的錯誤格式做不同的輸出，
# 至於你要客製化哪一種編譯錯誤訊息，可以官網tutorial Error and Exception\Built-in Exception 尋找名稱

import time


def input_data5():
    while True:
        try:
            answer = int(input("Nums:"))
            if answer == 0:
                print("The program will stop in two-second.")
                time.sleep(2)
                break

        except:
            print("You need input the number,try again!")

        else:
            print("The program will restart in two-second.")
            time.sleep(2)

input_data5()
# 你可以製作一個無限while來讓某個程式一直持續下去
