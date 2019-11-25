
### 快速获取cookies

如果在响应中包含一些cookies，你能够快速的访问它们：

	>>> url = 'http://example.com/some/cookie/setting/url'
	>>> r = requests.get(url)

	>>> r.cookies['example_cookie_name']
	'example_cookie_value'
	
发送你自己的cookies到服务器， 你能够使用cookies参数：

	>>> url = 'http://httpbin.org/cookies'
	>>> cookies = dict(cookies_are='working')

	>>> r = requests.get(url, cookies=cookies)
	>>> r.text
	'{"cookies": {"cookies_are": "working"}}'
	
cookies在`RequestsCookieJar`返回， 它的作用类似于字典但也提供了更完整的接口，适用多个域和路径， `cookie jars`能被传入到request：

	>>> jar = requests.cookies.RequestsCookieJar()
	>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
	>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
	>>> url = 'http://httpbin.org/cookies'
	>>> r = requests.get(url, cookies=jar)
	>>> r.text
	'{"cookies": {"tasty_cookie": "yum"}}'
	
### cookies在session中

session对象允许你在请求中保存某些参数，还在session实例所做的所有请求中保存cookies。

让我们从请求中保存一些cookies：

	s = requests.Session()

	s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
	r = s.get('http://httpbin.org/cookies')

	print(r.text)
	# '{"cookies": {"sessioncookie": "123456789"}}'
	
这里实例化了一个Session类，在请求url`s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')`时，取得了cookies，在下次的请求中便自动填充了实例的cookies到请求中。

接下来：

	In [72]: s.get('http://www.baidu.com')
	Out[72]: <Response [200]>

	In [73]: s.cookies
	Out[73]: <RequestsCookieJar[Cookie(version=0, name='BDORZ', value='27315', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1522568345, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)]>

	In [74]: s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
	Out[74]: <Response [200]>

	In [75]: s.cookies
	Out[75]: <RequestsCookieJar[Cookie(version=0, name='BDORZ', value='27315', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1522568345, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='sessioncookie', value='123456789', port=None, port_specified=False, domain='httpbin.org', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)]>
	
	In [77]: s.cookies.items()
	Out[77]: [('BDORZ', '27315'), ('sessioncookie', '123456789')]
	
这里实例会保存所有请求中的cookies。

### cookies文件的加载和保存

**文件保存**

这里可以利用`LWPCookieJar`来实现：

	import requests
	from http import cookiejar

	r = requests.session()    # 实例化一个session类
	r.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')   # 实例化session类的cookies为LWPCookieJar类，并设置文件路径和名称

	s = r.get('http://www.zhihu.com')
	print(s.status_code)

	r.cookies.save()   # 保存cookies为文件cookies.txt
	
运行完成后会保存一个`cookies.txt`文件在当前文件夹。

**文件加载**

	r.cookies.load(ignore_discard=True)
	
