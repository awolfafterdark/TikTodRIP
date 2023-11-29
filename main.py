#!/usr/bin/env python3
import os
import random
import requests
import threading
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"


def GetProxy():
    response = requests.get(
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt"
    )
    if response.status_code == 200:
        if os.path.exists("proxies.txt"):
            os.remove("proxies.txt")
        with open("proxies.txt", "w") as f:
            print(f"\n\t{GREEN}{'SUCCESS':<10}{RESET}|\tGot {len(response.text.splitlines())} proxies from elliottophellia/yakumo\n")
            f.write(response.text)
            f.close()
    else:
        print(f"\n\t{RED}{RED}{'ERROR':<10}{RESET}{RESET}|\tFailed to get proxies\n")
        quit()


def GetUserID(username):
    try:
        headers = {
            "authority": "www.tiktok.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "msToken=cxfL0lxGWTg_UmhgLz8U_Nv3ecxsgvBu5OJ1FtmVgMd3cHWoFCxQnyHSUzoCzEMMh0XeZzSw_gjF8XhG8Qp9qiE7yi9Yjm5B64hK4qdEMnhOvQCK6bL2bP8h6pAAVdphB3w_yBje2nj3iFw=",
            "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        response = requests.get(f"https://www.tiktok.com/@{username}", headers=headers)
        return response.text.split('"id":"')[1].split('"')[0]
    except:
        print(f"\n\t{RED}{RED}{'ERROR':<10}{RESET}{RESET}|\tFailed to get user ID\n")
        quit()


def Report(userId, use_proxy=False):
    headers = {
        "authority": "www.tiktok.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "referer": "https://www.tiktok.com/",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }
    reason = random.randint(0, 12000)
    try:
        if use_proxy:
            proxy = random.choice(open("proxies.txt", "r").read().splitlines())
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            response = requests.get(
                "https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={}&owner_id={}&reason={}".format(
                    userId, userId, reason
                ),
                headers=headers,
                proxies=proxies,
                timeout=15,
            )
        else:
            response = requests.get(
                "https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={}&owner_id={}&reason={}".format(
                    userId, userId, reason
                ),
                headers=headers,
                timeout=15,
            )
        if response and response.text:
            try:
                if response.json()["status_message"] == "Thanks for your feedback":
                    print(
                        f"\t{GREEN}{'SUCCESS':<10}{RESET}|\t{userId:<15}\t|\t{proxy if use_proxy else 'No Proxy Used':<20}\t|"
                    )
                else:
                    print(
                        f"\t{RED}{'ERROR':<10}{RESET}|\t{userId:<15}\t|\t{proxy if use_proxy else 'No Proxy Used':<20}\t|"
                    )
            except ValueError:
                print(
                    f"\t{RED}{'ERROR':<10}{RESET}|\t{userId:<15}\t|\t{proxy if use_proxy else 'No Proxy Used':<20}\t|\tEmpty response"
                )
    except requests.exceptions.RequestException as e:
        print(
            f"\t{RED}{'ERROR':<10}{RESET}|\t{userId:<15}\t|\t{proxy if use_proxy else 'No Proxy Used':<20}\t|\t{e.__class__.__name__}"
        )


def main():
    try:
        print(f"""{RED}
        \t  |''||''|  ||  '||      |''||''|              '||  '||''|.   '||' '||''|.  
        \t     ||    ...   ||  ..     ||      ...      .. ||   ||   ||   ||   ||   || 
        \t     ||     ||   || .'      ||    .|  '|.  .'  '||   ||''|'    ||   ||...|' {RESET}
        \t     ||     ||   ||'|.      ||    ||   ||  |.   ||   ||   |.   ||   ||      
        \t    .||.   .||. .||. ||.   .||.    '|..|'  '|..'||. .||.  '|' .||. .||. 
        \t                 - TikTok Mass Report With Proxy Rotator -
        \t                           Code by {YELLOW}@elliottophellia{RESET}
        \t               https://github.com/elliottophellia/TikTodRIP
        """)
        print("\t" + "="*94)
        username = GetUserID(input(f"\t{YELLOW}{'INPUT':<10}{RESET}|\t{'Username (USERNAME)':<25} > "))
        loop = int(input(f"\t{YELLOW}{'INPUT':<10}{RESET}|\t{'Loop (NUMBER)':<25} > "))
        proxy = input(f"\t{YELLOW}{'INPUT':<10}{RESET}|\t{'Proxy (YES/NO)':<25} > ")
        print("\t" + "="*94) 
        if proxy.lower() == "yes" or proxy.lower() == "y":
            proxy = True
            GetProxy()
            print("\t" + "="*94) 
        else:
            proxy = False
        threads = []
        for _ in range(loop):
            thread = threading.Thread(target=Report, args=(username, proxy))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        print("\t" + "="*94) 
        print(f"\n\t{GREEN}{'DONE':<10}{RESET}|\t{'All Threads Completed':<25}\n")
        print("\t" + "="*94) 
        print(f"""
        \t                        Please kindly buy me a coffee
        \t                      https://saweria.co/elliottophellia  
        \t                      https://paypal.me/elliottophellia
        """)
        print("\t" + "="*94) 
        if os.path.exists("proxies.txt"):
            os.remove("proxies.txt")
    except Exception as e:
        print(f"\t{RED}{'ERROR':<10}{RESET}|\t{str(e)}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print(f"\n\n\t{RED}{'ERROR':<10}{RESET}|\t{e.__class__.__name__}\n")
        quit()
