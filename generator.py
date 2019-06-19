# 當你在操作list時，常常會遇到生值，然後暫存的過程


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**2)
    return result

print(create_cubes(10))

# 正常會這樣做，先開一個空的list，然後將所有生成的值存入，這個情況就會暫存值得情況


def create_cubes_yield(n):
    for x in range(n):
        yield x**2

print(create_cubes_yield(10))

# yield是一個產生器，當你真的要執行裡面的內容時，他才會操作，正常來講一次只做一次操作，
# 這邊我用一個for迴圈，讓他連續操作，像上述這樣直接呼叫這個func，python只會回傳這是一個generator object
# 真正要輸出裡面的內容時，他才會操作yield

for i in create_cubes_yield(10):
    print(i)

# 上述這樣做就是連續操作內容，並且打印
# 那如果我一次只要操作一次的內容呢？

print(next(create_cubes_yield(10)))

# 必須用next()來操作一次性的generate

result = list(create_cubes_yield(10))
print(result)

# 你也可以像這樣，強制生成所有值，然後存成list
# generator基本上是對可以迭代的內容做產生，那如果理論上他是不可以迭代的呢？
# 例如，Srting他在python裡面並不歸類為可以迭代的object，那我們可以用yield，來產生嗎？

string1 = "Hello"
iter_string = iter(string1)
print(next(iter_string))

# 我們可以利用 iter()這個method對他進進行格式轉換，這樣就可以用next()
