# bdictParser
百度词典(.bdict)解析。Python3编写。

### 使用
```
from bdictParser import bdictParser

# 从文件
words = bdictParser.parse_file('热门游戏.bdict')
print(words)

# 从数据
with open('热门游戏.bdict') as f:
    words = bdictParser.parse(f.read())
print(words)
```

### 说明
借鉴了[buaahsh/bdictDecoder](https://github.com/buaahsh/bdictDecoder)
