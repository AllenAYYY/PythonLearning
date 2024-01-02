# -*- encoding: utf-8 -*-
"""

@File    :   python_test.py  
@Modify Time : 2023/12/30 22:36 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : 介绍Python基础知识

"""
# 变量
float_variable = 1.0 # 浮点型
int_variable = 1 # 整形
string_variable = "Hello, i am fine."

print(f"float_variable 是:{float_variable}, int_variable 是:{int_variable}，二者相加结果是:{float_variable+int_variable}")

# 字符串运算
str_original = "I come from China."
# 空格也算字符，会占位
# 最大取值范围不包括该值
# 第三个参数代表步长step，可以省略
print(str_original[1:5:2])
print(str_original[-5:-1])

str_original_2 = "What about u?"

# 字符串相关操作
print(str_original + str_original_2)
print(str_original * 2)
print("*" in str_original)
print("I" in str_original)

# 字符串函数操作

# 统计子字符串在原字符串中出现次数
print(str_original.count("come"))
print(str_original.find("me"))
print(len(str_original))
print(str_original.upper())
print(str_original.replace("come","coooool"))
print(str_original.split(" "))

# 列表
list_A = ['i','am',123,[1,2,3]]
print(list_A)
print(list_A * 3)
print([1,2] * 3)
print( 3 in [1,2,3])
for x in [1,2,3]:
    print(x,end=" ")
print()
# 列表操作函数

# 列表末尾添加对象
list_A.append("1")
print(list_A)

# 统计某个元素在列表中出现的次数
print(list_A.count(123))

# 在列表中扩展另一个列表中的元素
list_A.extend([1,2,3])
print(list_A)

# 从列表中找出某一个值第一个匹配项索引的位置
print(list_A.index(1))

# 将对象插入列表
list_A.insert(0,"Yang")
print(list_A)

# 弹出列表元素
pop_value = list_A.pop(2)
print(pop_value)
print(list_A)

# 排序
list_string = ['a','cb','ca']
list_string.sort()
print(list_string)
list_num = [3,2,5,7,9]
list_num.reverse()
print(list_num)
list_num.sort(reverse=False)
print(list_num)
list_num.sort(reverse=True)
print(list_num)

# 字典变量
# 字典形式为 key=>value，键:值
dict_lastName = {1:"Yang",2:"Wang",3:"Yu",'haha':"Kong",5:"Zhao"}
dict_lastName[100] = 'Cat'
print(dict_lastName['haha'])
dict_lastName['haha'] = "123456"
print(dict_lastName)

# 删除键
del dict_lastName[1]
print(dict_lastName)

# 打包创建字典
dict_test = {}
list_key = ['name','phone','address']
list_value = ['Allen',123,'China']
key_value_pairs = zip(list_key,list_value)
dict_result = dict(key_value_pairs)
print(dict_result)

# get返回值,找到name1键则返回name1键对应的值，不然返回后面的默认值
print(dict_result.get('name1',"aaa"))

# 删除字典里的值
item = dict_result.pop('name')
print(item)
print(dict_result)


# match case 用法
status = 40
match status:
    case 400:
        print("status is 400")
    case 401:
        print("status is 401")
    case 402:
        print("status is 402")
    case 403:
        print("status is 403")
    case _:
        print("wrong")

# while else用法
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# for else用法
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# break和continue
# break直接跳出所有循环
# continue只跳过当前轮次，继续进行后续的循环
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

# 推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3 and name != 'Jerry']
print(new_names)
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

# 函数，返回更大的值
# 这里面的a,b是形式参数
def max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = 4
num2 = 5
print(max(num1, num2))

# lambda表达式，lambda 参数1,参数2: 运算
x = lambda a, b : a * b
print(x(5, 6))

# map联用，对列表里每一个元素应用函数运算
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# filter过滤
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce对list元素进行累计计算
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

