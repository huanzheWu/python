# if语句
条件判断语句，格式是：

```
x = input("Please enter an inter number:")
if x < 0 :
	print("x < 0 ")
elif x >0 :
	print("x > 0 ")
else 
	print(" x= 0 ")

```
`elif`是else if的缩写.

# for 循环语句
python中的`for`语句与C语言的不同，它基于一个序列的子项来顺序迭代这个序列。这个序列可以是有范围的某种数据结构，例如数组、元组等，也可以是一串字符串。


```
def test_for():

    words = ['a','b','c','d']
    for word in words:
        print(word)

    str = "this is a string for test"
    for let in str :
        print(let)
```
那如果要实现从1到100的循环应该怎么做呢？Python提供了一个`range()`函数，它可以生成一个整数序列，作为参数传递给`list()`函数，可以产生一个整数元素的`list`，然后来进行循环：

```
    #计算0+1+2+...+100
    sum = 0
    for inter in list(range(100)):
        sum += inter
    print(sum)
```




