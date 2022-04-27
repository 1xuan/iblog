# Unicode And Bytes

> Humans speak text. Computers speak bytes.

This article mainly focus on encoding of Python3, invovling Python2. Due to encoding is a huge subject, I can't dive deeply into everything about encoding, just try around Python as possible as I can.

(note: Defaults to Python3 unless otherwise specified, some may also work in Python2)

## Prerequisite Knowledge

- What is Unicode ?

Unicode, formally the Unicode Standard, is an **information technology standard** for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems<sup>[[1]](#1)</sup>. The Unicode standard describes how characters are represented by code points. A code point value is an integer in the range 0 to 0x10FFFF (about 1.1 million values, the actual number assigned is less than that).
    
Unicode identify every characters in all of the world, represent code point (i.e., single character) by notation hex-nubmer with prefix `U+`. The Unicode standard defines Unicode Transformation Formats (UTF): UTF-8, UTF-16, and UTF-32, and several other encodings<sup>[[1]](#1)</sup>.

And we must know **Unicode IS NOT an encoding, it is an abstract specification.**

This article [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) explains Why does Unicode exists?

- what is Byte ?
    
The byte is a unit of digital information that most commonly consists of eight bits. Historically, the byte was the number of bits used to encode a single character of text in a computer and for this reason it is the smallest addressable unit of memory in many computer architectures<sup>[[2]](#2)</sup>.

No matter what you see from computer, all of it stored in bytes,  probably in different form.

- what is difference and relation between Unicode and Byte ?
    
As for this question, giving an example would be great idea. SO, 
    
Take `utf8` and character 'a' as an example:
        
~~~

  text                   Unicode        (encode)      utf8-encoded
  +---+                 +--------+        --->        +----------+
  | a | <-------------> | U+0061 | <----------------> | 01100001 |
  +---+                 +--------+        <---        +----------+
character                code point     (decode)         bytes

~~~
        
## For Python

> "Modern programs must handle unicode -Python has excellent support for Unicode, and will keep getting better."       -GvR

Python2 and Python3 is different. The string handling part is among the greatest different parts.
    
- In Python2, `str` is a sequence of bytes, and there is separate type `unicode`.
- In Python3, `str` is contains Unicode characters(a sequence of code point, and even identifiers can be unicode characters). There is a separate type `bytes` which is same as `str` of Python2.

As for how `str` is stored in memory, We don't need to care about that much. It could be UCS-2 or UCS-4, it doesn't matter, entirely possbile being changed over time. (I find out that memory occupied by str is getting smaller, it should be Python core developers keep optimizing it.)

### encode and decode between string and bytes

~~~python
>>> my_str = '你好'
>>> type(my_str)
<class 'str'>
>>> my_utf8 = my_str.encode('utf8')
>>> my_utf8
b'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> my_utf8.decode('utf8')
'你好'


>>> my_str.decode('utf8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'decode'


>>> my_str + my_utf8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not bytes
~~~

Many things become much easier in Python3, `str` is a sequence of code points, it can contain any unicode characters, and there is no implicit conversion between `bytes` and `str`.

<details>
<summary>In Python2, it is exactly converse:</summary>

~~~python
>>> my_str = '你好'
>>> my_str
'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> type(my_str)
<type 'str'>

>>> my_unicode = my_str.decode('utf8')
>>> my_unicode
u'\u4f60\u597d'
>>> my_unicode.encode('utf8')
'\xe4\xbd\xa0\xe5\xa5\xbd'


# If I encode str
>>> my_str.encode('utf8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

# If I decode unicode
>>> my_unicode.decode('utf8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/encodings/utf_8.py", line 16, in decode
    return codecs.utf_8_decode(input, errors, True)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

~~~

Here, the last two exception info are sort of odd. It indicates Python tries to encode or decode using `ascii`. The fact is, in `my_str.encode('utf8')`, due to you want to encode bytes which already be encoded, in order to be able to enocde then Python2 tries to make implicit conversion: it coverts `my_str` to unicode using `ascii` to decode `my_str`, then exception `UnicodeDecodeError` raised.

There are some cases to make it clearer.

~~~python
>>> import sys 
>>> sys.getdefaultencoding()
'ascii'

>>> u'hello ' + 'world'
u'hello world'
>>> u'hello ' + 'world'.decode('ascii')
u'hello world'
~~~

We can see that implicit conversion exists. if you wanna mix bytes and unicode in Python2, Python2 will convert bytes to unicode using default decoding which is `ascii` (get it from `sys.getdefaultencoding()`).

~~~python
>>> my_utf8 = '世界'
>>> u"hello" + my_utf8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

>>> u"hello" + my_utf8.decode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
~~~

In above example, Python2 tries to decode `my_utf8` in mixing unicode and bytes.
but the byte in position 0 is beyond 128, so `ascii` can't recognize it. So exception raised.

Python2's implicit conversion is undoubtedly very likely to be confusing. And it is fixed in Python3. [Pragmatic Unicode, or, How do I stop the pain?](https://www.youtube.com/watch?v=sgHbC6udIqc) The Pycon talk gives more detail and suggestions(e.g., Unicode Sandwich)

</details>


### Around Unicode

In Python source code, specific Unicode code points can be written using the `\u` escape sequence, which is followed by four hex digits giving the code point. The `\U` escape sequence is similar, but expects eight hex digits, not four:

~~~python
>>> s = "a\xac\u1234\u20ac\U00008000"
... #     ^^^^ two-digit hex escape
... #         ^^^^^^ four-digit Unicode escape
... #                     ^^^^^^^^^^ eight-digit Unicode escape
>>> s
'a¬ሴ€耀'
~~~

- function `ord`

>
> ord(c, /)
>
>     Return the Unicode code point for a one-character string.

~~~python
>>> ord('你')
20320
~~~

We can get number of code point of any unicode character using `ord`.

- function `chr`

>
> chr(i, /)
>
>     Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
>

~~~python
>>> chr(20320)
'你'
~~~

Likewise, convert nubmer of code point to unicode character using `chr`.

### Around Bytes

- print bytes

In Python3, there is a separate type `bytes`. It denoted by string with prefix `b`.

~~~python
>>> type(b'a')
<class 'bytes'>
>>> type(b'你')
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
~~~

Not as you think, if you iterate bytes:

~~~python
>>> for byte in b'abc':
...     print(byte)
...
97
98
99
~~~

This would be helpful:

~~~python
>>> for byte in b'abc':
...     print(chr(byte))
... 
a
b
c
~~~

by binary otherwise:

~~~python
>>> for byte in b'abc':
...     print(bin(byte))
...
0b1100001
0b1100010
0b1100011
~~~

or:

~~~python
>>> my_bytes = '你好'.encode('utf8')
>>> my_bytes
b'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> for byte in my_bytes:
...     print(byte.to_bytes(1, 'big'))
...
b'\xe4'
b'\xbd'
b'\xa0'
b'\xe5'
b'\xa5'
b'\xbd'
~~~

- decode

If we wanna read text, we need to decode bytes. **Most important, bytes is no sense without its' encoding**.

Here, I just talk about a handful of special cases:

- if the encoding informed is not exactly correct, do [this](https://docs.python.org/3.10/howto/unicode.html#files-in-an-unknown-encoding):

~~~python
>>> my_gb2312 = '你好, world'.encode('gb2312')
>>> my_gb2312.decode('utf8')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc4 in position 0: invalid continuation byte


# this would be helpful
>>> my_gb2312
b'\xc4\xe3\xba\xc3, world'
>>> my_gb2312.decode('utf8', errors='surrogateescape')
'\udcc4\udce3\udcba\udcc3, world'
>>> my_gb2312.decode('utf8', errors='surrogateescape').encode('utf8', errors='surrogateescape')
b'\xc4\xe3\xba\xc3, world'
~~~

- if don't know encoding, use `chardet` 

~~~python
>>> my_latin1 = 'hellõ, world'.encode('iso-8859-1')
>>> chardet.detect(my_latin1)
{'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
~~~

It's not quite reliabe, just as a approach as there is no other ways. You shouldnt put yourself into the situation.

- operation on bytes

...

### Encoding Setting

Here I just talk about four parts:

<details>
<summary>- sys.getdefaultencoding()</summary>

It is `utf8` in Python3, `ascii` in Python2. Return encoding used as implicitly converting between `unicode` and `bytes`. I don't know what it's meant to in Python3.

It can't be change.

</details>
    
<details>
<summary>- sys.getfilesystemencoding()</summary>

Return the encoding used to convert unicode filenames
 
</details>

<details>
<summary>- locale.getpreferredencoding(False)</summary>

It's same as locale encoding (under normal circumstances). By the way, argument `encoding` of function `open` defaults to `locale.getpreferredencoding(False)`.
 
</details>

<details>
<summary>- sys.stdout.encoding</summary>

It's the encoding standard i/o uses currently.
 
</details>
    

the setting var:

- PYTHONIOENCODING: change std I/O encoding (few reason to change it)

- LC_CTYPE: locale encoding. It should be consistent with terminal encoding ([What is the process of a letter between text app and terminal?](https://stackoverflow.com/questions/72011302/what-is-the-process-of-a-letter-between-text-app-and-terminal) this question provides some useful info, but gets no answer for now).

- PYTHONUTF8: [Python UTF-8 mode](https://docs.python.org/3/library/os.html#python-utf-8-mode), added in Python3.7

Giving some cases next,

~~~bash
# encodings.py

import sys
import locale

print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
print(locale.getpreferredencoding())
print(sys.stdout.encoding)


$ python3.7 encodings.py
utf-8
utf-8
UTF-8
UTF-8


$ PYTHONIOENCODING=ascii python3.7 encodings.py
utf-8
utf-8
UTF-8
ascii


$ LC_CTYPE=zh_CN.GB2312 python3.7 encodings.py
utf-8
gb2312
GB2312
GB2312


$ LC_CTYPE=zh_CN.GB2312 PYTHONIOENCODING=ascii PYTHONUTF8=1 python3.7 encodings.py
utf-8
utf-8
UTF-8
ascii
~~~

The answer [How to print UTF-8 encoded text to the console in Python](https://stackoverflow.com/a/35100990/8993864) gives some details and suggestions about this.

**See Also**

- [Unicode HOWTO -Python Doc](https://docs.python.org/3.10/howto/unicode.html)


**Reference**

1. <a id='1'></a>[Unicode -wikipedia](https://en.wikipedia.org/wiki/Unicode)

2. <a id='2'></a>[Byte -wikipedia](https://en.wikipedia.org/wiki/Byte)

    
**Further Reading**

- [Travis Fischer, Esther Nam: Character encoding and Unicode in Python - PyCon 2014](https://www.youtube.com/watch?v=Mx70n1dL534)

- [The Guts of Unicode in Python -PyCon US 2013](https://pyvideo.org/pycon-us-2013/the-guts-of-unicode-in-python.html)

- [Mastering Python 3 I/O -PyCon US 2010](https://archive.org/details/pyvideo_289___mastering-python-3-i-o)

- [How is text saved in memory? -stackoverflow](https://stackoverflow.com/questions/69514467/how-is-text-saved-in-memory)

