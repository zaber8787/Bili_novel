import requests
from bs4 import BeautifulSoup
cookies = {
    'night': '0',
    '_ga': 'GA1.1.958722391.1726658608',
    'Hm_lvt_1251eb70bc6856bd02196c68e198ee56': '1726658609',
    'HMACCOUNT': '4AE0029338E4857C',
    'cf_clearance': 'BFKM2Lf4wzFlXom9ci1yJKoApenxgGUI1rX8RRcRQG8-1726658610-1.2.1.1-1geBX7RLdxTdstgGmIVAgRdHzSZuFKLDE3rkUHMcvUa1t7gq.Xvmj1fI63cF1D0dtUamAfxaaIxixzPKVz3BFbQDIAEGvOuuCvHHvI0qFpHNCNyXfxloqUfj8GwOESDEW93iy0NUqZDP9zUOicM1kPmfmA_Pjw3r_diw8xJxN1E68LXRBXiM7OZ8IqXPf05AoyWYs9RZEetXuA5rZI.lgFe2kcHlH4kqw5lxXwRKvCvGEAwxH5IvbbJAETNbrDC6gvh2lbhbsdqtqFg5Eo95G2dxz0Y1hoi.uQYdE9bPLsUyKK0yuUOsjRe1Dog7fvJOQUNNyENkPrrkcIJcNadIn5TxMhBt.DrN101P2MwwiTDJjAhFpqarpL2cwEkqq.l8ynmtOay4gXqhUC3aV4xrCw',
    'jieqiVisitId': 'article_articleviews%3D3095',
    '_ga_NG72YQN6TX': 'GS1.1.1726658608.1.1.1726658624.0.0.0',
    'Hm_lpvt_1251eb70bc6856bd02196c68e198ee56': '1726658624',
    '__gads': 'ID=7f2b5c19114606c4:T=1726658623:RT=1726658623:S=ALNI_Ma1KqzEjUMf7Pa0lmkABpCEBAJHDA',
    '__gpi': 'UID=00000f1035c646b5:T=1726658623:RT=1726658623:S=ALNI_MYV0K4tTZxbBZxI8KGWYL4_CZE9Fw',
    '__eoi': 'ID=790bbbcca1211a24:T=1726658623:RT=1726658623:S=AA-AfjbM3in4FrNrS2TWiZY-GbqH',
    'FCNEC': '%5B%5B%22AKsRol8PcJumq30SBS3Vj1LKxWp0fBq48fT4M86FT1JfbXzQnsEDV8unfDs8RR4ClgROg8oGk6LpXbusd7KQ7hWoO8s-sPWQ7uInswjZXZvt2TwUNgcvrqCLSIs0P77MhEVUzyTktGr3Cje571BF14DzuEZsFYaUPw%3D%3D%22%5D%5D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'night=0; _ga=GA1.1.958722391.1726658608; Hm_lvt_1251eb70bc6856bd02196c68e198ee56=1726658609; HMACCOUNT=4AE0029338E4857C; cf_clearance=BFKM2Lf4wzFlXom9ci1yJKoApenxgGUI1rX8RRcRQG8-1726658610-1.2.1.1-1geBX7RLdxTdstgGmIVAgRdHzSZuFKLDE3rkUHMcvUa1t7gq.Xvmj1fI63cF1D0dtUamAfxaaIxixzPKVz3BFbQDIAEGvOuuCvHHvI0qFpHNCNyXfxloqUfj8GwOESDEW93iy0NUqZDP9zUOicM1kPmfmA_Pjw3r_diw8xJxN1E68LXRBXiM7OZ8IqXPf05AoyWYs9RZEetXuA5rZI.lgFe2kcHlH4kqw5lxXwRKvCvGEAwxH5IvbbJAETNbrDC6gvh2lbhbsdqtqFg5Eo95G2dxz0Y1hoi.uQYdE9bPLsUyKK0yuUOsjRe1Dog7fvJOQUNNyENkPrrkcIJcNadIn5TxMhBt.DrN101P2MwwiTDJjAhFpqarpL2cwEkqq.l8ynmtOay4gXqhUC3aV4xrCw; jieqiVisitId=article_articleviews%3D3095; _ga_NG72YQN6TX=GS1.1.1726658608.1.1.1726658624.0.0.0; Hm_lpvt_1251eb70bc6856bd02196c68e198ee56=1726658624; __gads=ID=7f2b5c19114606c4:T=1726658623:RT=1726658623:S=ALNI_Ma1KqzEjUMf7Pa0lmkABpCEBAJHDA; __gpi=UID=00000f1035c646b5:T=1726658623:RT=1726658623:S=ALNI_MYV0K4tTZxbBZxI8KGWYL4_CZE9Fw; __eoi=ID=790bbbcca1211a24:T=1726658623:RT=1726658623:S=AA-AfjbM3in4FrNrS2TWiZY-GbqH; FCNEC=%5B%5B%22AKsRol8PcJumq30SBS3Vj1LKxWp0fBq48fT4M86FT1JfbXzQnsEDV8unfDs8RR4ClgROg8oGk6LpXbusd7KQ7hWoO8s-sPWQ7uInswjZXZvt2TwUNgcvrqCLSIs0P77MhEVUzyTktGr3Cje571BF14DzuEZsFYaUPw%3D%3D%22%5D%5D',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}


def catalog_url(novel: str):
    if 'https' in novel:
        tmp = novel.split('/')
        for i in tmp:
            if i.isdigit():
                url = f'https://tw.linovelib.com/novel/{i}/catalog'
                return (url)
    else:
        if novel.isdigit():
            url = f'https://tw.linovelib.com/novel/{novel}/catalog'
            return (url)
        else:
            print('這不是編號也不是網址，請重新輸入')
            novel = input('請輸入小說編號或小說目錄網址:')
            return (catalog_url(novel=novel))


def check_range(esp):
    tmp = input('請輸入你要從第幾卷載到第幾卷(使用編號)(輸入範例: 0 ~ 5): ')
    if '~' not in tmp:
        print('沒有偵測到 ~ 請重新輸入')
    else:
        tmp = tmp.strip()
        tmp = tmp.split('~')
        for i in range(len(tmp)):
            if tmp[i].isdigit() == False:
                print('錯誤，請重新輸入')
                return (check_range(esp=esp))
            else:
                tmp[i] = int(tmp[i])
                if tmp[i] >= len(esp) or tmp[i] < 0:
                    print('錯誤，請重新輸入')
                    return (check_range(esp=esp))
        tmp = tmp.sort()
        return tmp


def get_range(esp):
    num = int(input('請輸入你要下載的集數或範圍'))
    if num < 0:
        print('請根據剛剛的編號給出範圍，不會小於0喔')
        get_range(esp=esp)
    elif num > (len(esp) + 1):
        print('超出範圍，請重新選擇')
        get_range(esp=esp)
    elif num < len(esp):
        return (num, num+1)
    elif num == len(esp):
        return (0, len(esp))
    elif num == len(esp+1):
        tmp = check_range(esp=esp)
        return (tmp[0], tmp[-1])


code = input('請輸入小說編號或小說目錄網址:')
url = catalog_url(novel=code)
response = requests.get(url=url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, "html5lib")
name = soup.find('title')
print(name.get_text() + ': ')
espisode = soup.find_all('h3')
for i in range(len(espisode)):
    print(f'[{i}] ' + espisode[i].text)
print(f'[{len(espisode)}] 全部小說')
print((f'[{len(espisode)+1}] 自定義範圍'))
left, right = get_range(esp=espisode)
soup.find_all('a', class_="volume-cover-img")

with open('demo1.html', 'w', encoding='utf-8')as f:
    f.write(response.text)
