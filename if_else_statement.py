# if elif else條件句 Python讓人舒服的地方在於，不須分號在尾，條件式只有冒號，條件句內容以縮排表示，簡潔，舒暢

if True:
    print("I always a man follow my heart.")

if 9 > 1:
    print("Number nine is more than number one.")

location = "store"
if location == "store":
    print("Goods is fine.")
elif location == "pool":
    print("Swimming is great.")
elif location == "shop":
    print("Stuff is good.")
else:
    print("Rest.")
