## python ------- re方法

[TOC]

### match(*pattern*, *string*, *flags=0*)

> 如果 *string* 从开始的时候匹配到了正则表达式样式，就返回一个相应的 `匹配对象`。 如果没有匹配，就返回 `None` ；

```python
st = '123-456-789'
print(re.match('-\d+', st))   # None
print(re.match('\d+', st))   # <re.Match object; span=(0, 3), match='123'>
```

### search(*pattern*, *string*, *flags=0*)

> 扫描整个 `字符串`找到匹配样式的第一个位置，并返回一个相应的 匹配对象。如果没有匹配，就返回一个 `None` ； 

```python
st = '123-456-789'
re.search('-\d+', st)   # <re.Match object; span=(3, 7), match='-456'>
```

### group(n),  groups()

>group()方法或者返回所有匹配对象或是根据要求返回某个特定子组。(用圆括号(()) 组建组),如果一个组参数n值为 0，相应的返回值就是整个匹配字符串
>
>groups()则很简单，它返回一个包含唯一或所有子组的元组。
>
>如果正则表达式中没有子组的话， groups() 将返回一个空元组，而 group()仍会返回全部匹配对象

```python
st = '123-456-789'
r = re.search('(\d+)-(\d+)-(\d+)', st)
r.group()   #   '123-456-789'
r.group(0)   #   '123-456-789'
r.group(1)   # '123'
r.group(2)   # '456'
r.group(3)   # '789'
r.groups()   # ('123', '456', '789')
```

### findall(*pattern*, *string*, *flags=0*)

> 对 *string* 返回一个不重复的 *pattern* 的匹配列表， *string* 从左到右进行扫描，匹配按找到的顺序返回。如果样式里存在一到多个组，就返回一个`组合列表`；就是一个元组的`列表`（如果样式里有超过一个组合的话）。没有找到匹配的部分，会返回空列表；
>

```python
st = '123-456-789'
re.findall('(\d+)-(\d+)-(\d+)', st)   # [('123', '456', '789')]
re.findall('\d+', st)   # ['123', '456', '789']
```

