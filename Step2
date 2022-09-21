payload = {
        'username': '156****1997',
        'password': '**********'}

    #设置请求头文件信息
    header_init = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'close',
    'Referer':'https://weibo.com/askcliff?is_all=1'
    }

    #微博登陆页URL
    url_login='https://passport.weibo.cn/signin/login'

    #设置一个会话对象
    s = requests.Session()

    #以post形式提交登陆用户名和密码
    s.post(url=url_login, data=payload, headers=header_init)
