# 发博人
creen_name = jd['data']['cards'][count]['mblog']['user']['screen_name']
result['微博用户'].append(screen_name)
# 这部分是获取微博用户的文本内容
# 发表时间
a = ('\''+jd['data']['cards'][count]['mblog']['created_at']+'\'').count('-')
if a == 2:
date = datetime.strptime(jd['data']['cards'][count]['mblog']['created_at'],'%Y-%m-%d')
datesrt = date.strftime('%Y-%m-%d')
if a == 1:
date = datetime.strptime(jd['data']['cards'][count]['mblog']['created_at'],'%m-%d')
datesrt = date.strftime('2018'+'-%m-%d')
if a == 0:
datesrt = '今天或昨天'
result['发博日期'].append(datesrt)

def PageData(url,cookie,header):
    #提交请求获取要抓取的页面信息
    res = requests.get(url=url, cookies=cookie, headers=header)
    #读取页面内容
    jd = json.loads(res.text)
    count = -1
    result = {}
    result['id'] = []
    result['微博用户'] = []
    result['发博日期'] = []
    result['微博文本'] = []
    result['附带图片链接'] = []
    result['微博链接'] = []
    result['点赞数'] = []
    result['评论数'] = []
    result['转发数'] = []
    
    for i in jd['data']['cards']:
        count = count + 1
        if jd['data']['cards'][count]['card_type'] == 9:
            #发博人
            screen_name = jd['data']['cards'][count]['mblog']['user']['screen_name']
            result['微博用户'].append(screen_name)
            #发表时间
            a = ('\''+jd['data']['cards'][count]['mblog']['created_at']+'\'').count('-')
            if a == 2:
                date = datetime.strptime(jd['data']['cards'][count]['mblog']['created_at'],'%Y-%m-%d')
                datesrt = date.strftime('%Y-%m-%d')
            if a == 1:
                date = datetime.strptime(jd['data']['cards'][count]['mblog']['created_at'],'%m-%d')
                datesrt = date.strftime('2018'+'-%m-%d')
            if a == 0:
                datesrt = '今天或昨天'
            result['发博日期'].append(datesrt)
            #微博内容
            text = jd['data']['cards'][count]['mblog']['text']
            text = filter_emoji(text,restr='')
            soup = BeautifulSoup(text,'html.parser')
            text = soup.get_text()
            result['微博文本'].append(text)
            #微博所附图片链接
            if 'original_pic' in jd['data']['cards'][count]['mblog'].keys():
                original_pic = jd['data']['cards'][count]['mblog']['original_pic']
            else:
                original_pic = '无图片链接'
            result['附带图片链接'].append(original_pic)
            #微博网页链接
            html = jd['data']['cards'][count]['scheme']
            result['微博链接'].append(html)
            #点赞数量
            attitudes_count = jd['data']['cards'][count]['mblog']['attitudes_count']
            result['点赞数'].append(attitudes_count)
            #评论数量
            comments_count = jd['data']['cards'][count]['mblog']['comments_count']
            result['评论数'].append(comments_count)
            #转发数量
            reposts_count = jd['data']['cards'][count]['mblog']['reposts_count']
            result['转发数'].append(reposts_count)
    return result
