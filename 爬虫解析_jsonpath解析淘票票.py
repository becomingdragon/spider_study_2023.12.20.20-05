import urllib.request
import  json
import jsonpath

url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1703072210714_120&jsoncallback=jsonp121&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"

headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cookie':'t=949698ce07b1457be8af8bf6814e7a93; cookie2=119bdd1ddb22376b0fd52237a2b8f7d5; v=0; _tb_token_=53b435051673e; xlly_s=1; isg=BIaGbrF1HxNkXMt3CI9THXfW13wI58qhTtX2QXCuNal2cySN2HZfsZFFS6-_XMK5; l=fBjIMGMrPKXEfnF8BO5Cnurza77tqIObz1PzaNbMiIEGa6thth6gmNCOgcPwSdtjgT55_etPx-igEd3w-A4LRE9ZrVSzKtyuJAJ6ReM3N7AN.; tfstk=ecnX3scr3sfX1abcNI9rOdz1T4E6LjtF1OwtKAIVBoEYChGZatkqQmu7BflkIKqqB5Gsa7c_SKVa65GZBqJyYHkmnlqTfB-eYjvKUbOFeuJJaxqgXQWPXe-InX-Z9bjYTa_H2QMWNgI5fLDcIWfU9Wi7hzLrH7E3Ady0lNkbZGdiP-s39xF5XGIzRMPIbkb1Fyj_FWJWFNbG0GwI_1sH4MaYE8oeFL1fSreuFWJWFNbgk82z8L95GNf..',
'Referer':'https://dianying.taobao.com/',
'Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'document',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content=content.split('(')[1].split(')')[0]

with open('爬虫解析_jsonpath解析淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('爬虫解析_jsonpath解析淘票票.json','r',encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)