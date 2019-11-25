python3中字符有两种类型：

- str
- bytes

凡是通过`unicode`编码的都为`str`类型， 其他编码为`bytes`类型，python3默认编码格式为`unicode`， 它们可以相互转化
> str类型编码转化为bytes类型：

>		>>>s = ’你好'
>		>>>type(s)
>		str
>		>>>ss = s.encode('utf8')
>		>>>type(ss)
>		bytes
>		>>>print(ss)
>		b'\xe4\xbd\xa0\xe5\xa5\xbd'
> 编码成utf格式时中文会编码成`utf8`格式而英文会编码成`ascii`格式。

> bytes类型解码成str类型：

>		>>>sd = ss.decode('utf8')
>		>>>sd
>		'你好'
>		type(sd)
>		str

我们可以通过`chardet`来识别bytes类型的编码格式：

	>>>import chardet
	>>>chardet.detect(ss)
	{'confidence': 0.7525, 'encoding': 'utf-8'}
	# confidence为置信度， 表明判断的准确性
	
**len()**

`str`类型时，`len()`计算的是字符个数：

	>>>len('abc')
	3
	>>>len('你好')
	2

如果换成`bytes`：

	>>>len(b'ABC')
	3
	>>>'你好'.encode('utf8')
	b'\xe4\xbd\xa0\xe5\xa5\xbd'
	>>>len(b'\xe4\xbd\xa0\xe5\xa5\xbd')
	6

这里便计算的是是字节数。

	
如果bytes中只有一小部分无效的字节，可以传入`errors='ignore'`忽略错误的字节：

	>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
	'中'
### requests获取html中文乱码问题

在requests库中请求页面时有时会出现中文不能显示的问题，只是由于编码格式的问题，有些页面没有设置`charset`于是requests库便使用默认的编码格式`ISO-8859-1`

	>>>r.encoding
	'ISO-8859-1'
	
我们在使用`r.text`时html页面中不会显示中文。这时我们可以通过设置：

	>>>r.encoding = 'utf8'
	
另外我们可以通过requests提供的`response.content`来解决, 由于content是HTTP相应的原始字节串二进制信息，我们可以通过解码成`unicode`的方式来实现：
	
	>>>type(rep.content)
	bytes
	>>>r.content.decode(r.apparent_encoding)
	...

### apparent_encoding和encoding

requests提供了两种方法获取编码信息

- r.encoding ： 从http header中猜测的响应内容编码方式
- r.apparent_encoding ： 从内容中分析出的响应内容编码方式（备选编码方式）

由于有些不规范的网页没有指定charset，所以requests采用默认的编码方式`ISO-8859-1`来编码，以至于出现中文时出现乱码。但是`apparent_encoding`是通过`chardet.detect`来判断，所以说`apparent_encoding`比`encoding`更准确一些，编码可以指定：

	>>>r.encoding = r.apparent_encoding
	
### 总结

了解了以上的信息之后我们就会知道requests对编码怎样处理:

- requests获取网页后检测charset，如果没有就采用默认编码

- 然后采用猜测的编码模式对网页进行解码成unicode编码，也就是str类型

由于采用了错误的编码模式自然会出现乱码，这样我们也可以这样处理：

	>>>r.text.encode(r.encoding).decode(r.apparent_encoding)
	
先用requests采用的编码模式对解码后的`unicode`进行编码成`r.encoding`编码模式, 然后再用原本页面采用的编码模式`apparent_encoding`进行第二次解码成`unicode`，这样乱码问题一样能解决。


	

	
