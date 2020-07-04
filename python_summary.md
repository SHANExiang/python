





## 各种函数

##### 默认参数值

定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后就行了。但是要注意：`默认参数的值仅仅在函数定义的时候赋值一次`。看下面的例子：

```python
def f(a, L=[]):
    L.append(a)
    return L
print f(1)  # [1]
print f(2)  # [1, 2]
print f(3)  # [1, 2, 3]
```

关于这点，文档上着重给出警告，如下：

> Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

所以，如果默认参数是一个可修改的容器比如一个列表、集合或者字典，最好使用 None 作为默认值。

```python
# Using a list as a default value
def spam(a, b=None): 
    if b is None: 
        b = [] 
    ...
```

如果不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来，可以像下面这样写:

```python
_no_value = object()
def spam(a, b=_no_value): 
    if b is _no_value: 
        print('No b value supplied')
    ... 
```





#### 1. lambda匿名函数

Python使用lambda关键字创造`匿名函数`。所谓匿名，意即不再使用def语句这样标准的形式定义一个函数。这种语句在**调用时绕过函数的栈分配，可以提高效率**。其语法是：

```python
lambda [arg1[, arg2, ... argN]]: expression
```

其中，参数是可选的，如果使用参数的话，参数通常也会在表达式之中出现。

lambda 匿名函数捕获值

lambda 表达式允许你定义简单函数,但是它的使用是有限制的。你只能指定单个表达式,它的值就是最后的返回值。也就是说不能包含其他的语言特性了，包括多个语句、条件表达式、迭代以及异常处理等等。

```Python
>>> x = 10
>>> a = lambda y: x + y
>>> x = 20
>>> b = lambda y: x + y 
```

那么 a(10) 和 b(10) 返回的结果是什么? 答案是 30，30。

这其中的奥妙在于**lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的**。因此在调用这个 lambda 表达式的时候，x 的值是执行时的值。

如果想让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可，就像下面这样:

```python
>>> x = 10
>>> a = lambda y, x=x: x + y
>>> x = 20
>>> b = lambda y, x=x: x + y 
```

这样结果就是 20，30了。下面再看两个例子，加深对lambda变量捕获机制的了解：

```python
>>> funcs = [lambda x: x+n for n in range(5)] 
>>> for f in funcs:
... print(f(0))
# 4 4 4 4 4
>>> funcs = [lambda x, n=n: x+n for n in range(5)]
>>> for f in funcs:
... print(f(0))
# 0 1 2 3 4
```

