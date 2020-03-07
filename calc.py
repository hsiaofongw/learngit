# 加法
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

# 比较两个整数x, y
# 如果x < y 返回-1
# 如果x = y 返回0
# 如果x > y 返回1
def compare(x, y):
    if (x < y):
        return -1
    elif (x == y):
        return 0
    elif (x > y):
        return 1
