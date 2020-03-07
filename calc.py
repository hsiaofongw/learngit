# author: sam
# last_modified: 2020-03-08T01:47:51+08:00

# 加法
def add(x, y):
    return x + y

# 减法
def sub(x, y):
    return x - y

# 乘法
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

# 除法
def div(x: int, y: int) -> str:
    try:
        answer = x // y
        return str(answer)
    except ZeroDivisionError:
        return str("Error: y shoudn't be zero")
