# Weibo-crawler
How to crawl Sina Weibo data?

As part of the code contains account, database and other information, only part of the Python is shown here. students who need it can contact me (database building code is not included, because part of the operation is directly based on Navicat visual database software).

## Step 1: Analysis of the web structure

This link is the most basic part and the more important part. The key is to find the information you want in the complex web structure. The web version of the mobile weibo crawl is chosen here, at https://m.weibo.cn/.

First of all, we use Google Chrome to login to our Weibo account and open a blogger's Weibo page randomly to observe the web structure. Here we take Jerry_寅子's Weibo page as an example. First of all, we browse his Weibo page and find that as we swipe the mouse, new pages will be loaded. This is asynchronous loading. Each new content loaded is equivalent to a new page, and such content is often not placed in the Doc of Network as described in the tutorial, but in the Js file of XHR, where Js is the XML-based asynchronous JavaScript (AJAX) file.

Open the background controller of Google Chrome (right click at the page - check), tap XHR in Network, refresh the interface and reload it, tap Perview interface, you can see the JS code, one layer after another, you will see the place where the microblogging information is located. This is the information we need to crawl.

<img width="1337" alt="image" src="https://user-images.githubusercontent.com/114042177/191410053-d14eb4ae-f1d8-42c2-99ab-4076bebca500.png">

## Step 2: Simulate login to get JS
This part of the python code can be found in file **Step2**

After getting familiar with the structure of JS, all we have to do is to make the code access to simulate a real login to capture the JS. there are two methods here, one is to simulate a login and the other is to simulate a browser.

Simulated login: In the login screen of Weibo on the mobile side, enter your username and password to login to Weibo mobile.

The other one is to simulate browser login, using browser cookies information, which can be easily found in the backend control of the web page, taking care to store it in a variable in the form of a dictionary. [Cookies example (can be found in Header Requests in XHR's JS)]
```
#微博内容抓取页URL
  url_init = url_base+'&page={}'
    #设置Cookie的内容
  cookie={
        'MLOGIN':'1',
        'M_WEIBOCN_PARAMS':'luicode%3D10000011%26lfid%3D100103type%253D3%2526q%253D%25E5%25AF%2585%25E5%25AD%2590%2526t%253D0%26featurecode%3D20000320%26oid%3D3900004206849232%26fid%3D1005053628359543%26uicode%3D10000011&page={}',
        'SCF':'AkhONeuuFcGAlAz0kgavz1wRbp1fz7ZGn0Xn_zPHzoa0B_VbPTNxInVDSaycKttiCUPGwlxaxxqJG',
        'SUB':'_2A252C9fsDeRhGeNI41QZ-CrEyzqIHXVV9_mkrDV6PUJbkdAKLW_CkW1NSDUIJok_9iLiEAocyWlucWgHT-UKNQiO',
        'SUHB':'0A0JidXol5dQPP',
        'WEIBOCN_FROM':'1110006030',
        '_T_WM':'28789df2dacda9b86d0a2ffa60adbfe8',
    }
```
Generally speaking, simulating a browser takes less time than simulating a login.

Another key to this part is to pay attention to the law of the URL, that is, the URL of the page to be visited. For this kind of asynchronous loading, generally the front page is fixed and only the back page will be different. This rule can be expressed by using url_init = url_base+'&page={}'.

## Step 3: Get specific content

After getting the content of the web page, the next step is to parse the web page format to get the specific content. Since JS JSON files are dictionary-like and very regular, it is very easy to get the content. Use jd = json.loads(res.text) to parse the web page content into JSON format, and then get the content according to different fields.

The file **Step3** is about getting the date of posting the blog. The reason why a lot of judgments are used is the way it presents time. In Sina Weibo, there are non-standard time expressions like "1 hour ago", "today", "5 days ago" and so on. (The standard way is xxxxx year xx month xx day)

Other fields will be handled in a similar way.

## Step 4: Organize the data and enter the database

Step 3 will get the information organized into the dictionary, the next is based on the fields to write the database. This part involves more knowledge of the database. Because it is complicated to use pymysql to build a table here, it is easy to make mistakes, so the table building process is done in navicat.

As shown by the code in file **Step4**, first link the database, then organize the data stored in the dictionary, and then execute the operation to store the data into the database. This code is applicable to all web version mobile Weibo data crawling.

## Appendix 1: Solution to the problem that the full text of Weibo text cannot be displayed

When we crawl Weibo, we will encounter a problem that some bloggers have sent a long text, and when we actually browse Weibo, we need to click the "Full text" button to view the full text. So the data we crawl is only the content after being collapsed.

The solution to this problem is much the same as the solution to asynchronous loading, because clicking the full text button is equivalent to loading a new page. The key is to find the link to the jump page.

See the pic for the code that is determined to be collapsed. Since the links to the jump pages are relatively regular, it is enough to jump directly to the Weibo interface to get the full text.
<img width="1231" alt="image" src="https://user-images.githubusercontent.com/114042177/191411328-228bcc26-e602-49a1-b6d6-49e273841d88.png">

## Appendix 2: Filtering of Emjio expressions

In the first attempt to enter the data into the database, we found that the text with Emjio emoji will report an error. This is due to the encoding problem. Normally we use utf encoding, but emjio emoticons are utfbm4, and their encoding bits are longer than utf. In principle, this problem can be solved by changing the encoding, but I encountered various problems when configuring the environment, so I finally took the approach of filtering it out. The code is shown in the file **Appendix**.

If there are mistakes or misunderstanding, I hope you can correct it. After all, the code is relatively long ago, some details are not clear ~
