import os
import requests
import time
import re
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as ReportImage, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import shutil


def get_web(link):
    nurl = f'https://tw.linovelib.com{link}'
    resp = requests.get(url=nurl, headers=headers, cookies=cookies)
    if resp.status_code == 200:
        with open('demo.html', 'w', encoding='utf-8')as f:
            f.write(resp.text)
    return resp


pdfmetrics.registerFont(TTFont('notoR', "font/NotoSansTC-Regular.ttf"))
pdfmetrics.registerFont(TTFont('notoB', "font/NotoSansTC-Bold.ttf"))
styles = getSampleStyleSheet()
styleNormalCustom = ParagraphStyle(
    'styleNormalCustom', fontName='notoR', fontSize=10, leading=20)
styleTitleCustom = ParagraphStyle(
    'styleTitleCustom', fontName='notoB', fontSize=20, alignment='center')

cookies = {
    'night': '0',
    'jieqiRecentRead': '3095.154933.0.1.1726474874.0',
    '_ga': 'GA1.1.1416571014.1726474881',
    'Hm_lvt_1251eb70bc6856bd02196c68e198ee56': '1726474881',
    'Hm_lpvt_1251eb70bc6856bd02196c68e198ee56': '1726474881',
    'HMACCOUNT': '4A2F0EB4ECC25C40',
    '__gads': 'ID=a141ee4cfc528692:T=1726474876:RT=1726474876:S=ALNI_MaRDRzwsopeMvFGrVKXqh66_jpYSQ',
    '__gpi': 'UID=00000f0b65ede236:T=1726474876:RT=1726474876:S=ALNI_MaFhNAYGKBgXkhicxh1IdLvFzDzyg',
    '__eoi': 'ID=5eca0adf9c691b85:T=1726474876:RT=1726474876:S=AA-AfjZJ5OuoYJ5NLen4qrE8rz8Q',
    'cf_clearance': 'xjlXLdnpWDUjcrUodZlsPAZtd7wI0DUT7JzVR17drOg-1726474877-1.2.1.1-pMs1nqGe859oR.G53wisfeTb9o9ZjEsEGzpr1l7msTlVA_5kwnDR80xjIAx4Do_akKvCmwm1ZL7jsS0QXrMh7WNnfOK2gv2qxf3hosP6N8pGQpLoZoixBh3Elg2ihe30eTLvzNojWFmpBSUlakYXImREzPDezTMPKOTNncMJKC9aTEdMx3SNDxbfNYaNYz9.Znx66fi9CXSnBfc3kP2NYdgm4tSL1wn2K23E.BR0lvvFE2wsZqCvYKRqybiT0zUyAuJ4iKRHIBE8O53D8qqJcsgZ7cYpH2kj6.kSAghJ80Kssl1pOCxzLpxz9dV8OPZSKxVzVXiuviQZVl7i6uVFC3h.hl6_u.y5ExPAJwJsxvOyj_RcORsAQBbgKrJ8wFCSUSRivZuFEJEOzJGlyKSopw',
    'FCNEC': '%5B%5B%22AKsRol8837Jn4emUAOxDObggzIBf2zmWIbsNP3jnk3ccCpakEHrIOlV0YG6b2chX7PGKZ6rwl-b5KggBj6idgCahkaqL20o6a5X357ha9uDZgecxGstAxGKaMymAwE8zqGlEjm5bA8dsacvE8C0sPrnkxcIphXsbRA%3D%3D%22%5D%5D',
    '_ga_NG72YQN6TX': 'GS1.1.1726474881.1.0.1726474893.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9',
    'cache-control': 'no-cache',
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


url = 'https://tw.linovelib.com/novel/3095/154931.html'
resp = requests.get(url=url, headers=headers, cookies=cookies)
print(resp.status_code)
if resp.status_code == 200:
    with open('demo.html', 'w', encoding='utf-8')as f:
        f.write(resp.text)
expdir = ''
for i in range(1, 10000):

    soup = BeautifulSoup(resp.text, "html5lib")
    try:
        exp = soup.find('h3').get_text()
        if exp != expdir:
            try:
                os.mkdir(f'episode/{exp}')
            except:
                pass
            expdir = exp
        title = soup.find('h1', id="atitle").get_text()
        safe_title = re.sub(r'[<>:"/\\|?*]', '', title).strip()
        text = soup.find('div', class_='acontent')
    except:
        break
    for script in text(["script", "style", "center", "div"]):
        script.decompose()

    fileName = f"episode/{exp}/{f'{exp} {safe_title}'}.pdf"
    pdfTemplate = SimpleDocTemplate(fileName, pagesize=A4)
    story = []
    a4_width, a4_height = A4
    page_width = a4_width
    page_height = a4_height

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        "Referer": 'https://tw.linovelib.com/novel/3095/154933.html',
        'Cookie': 'night=0; _ga=GA1.1.1416571014.1726474881; Hm_lvt_1251eb70bc6856bd02196c68e198ee56=1726474881; HMACCOUNT=4A2F0EB4ECC25C40; cf_clearance=xjlXLdnpWDUjcrUodZlsPAZtd7wI0DUT7JzVR17drOg-1726474877-1.2.1.1-pMs1nqGe859oR.G53wisfeTb9o9ZjEsEGzpr1l7msTlVA_5kwnDR80xjIAx4Do_akKvCmwm1ZL7jsS0QXrMh7WNnfOK2gv2qxf3hosP6N8pGQpLoZoixBh3Elg2ihe30eTLvzNojWFmpBSUlakYXImREzPDezTMPKOTNncMJKC9aTEdMx3SNDxbfNYaNYz9.Znx66fi9CXSnBfc3kP2NYdgm4tSL1wn2K23E.BR0lvvFE2wsZqCvYKRqybiT0zUyAuJ4iKRHIBE8O53D8qqJcsgZ7cYpH2kj6.kSAghJ80Kssl1pOCxzLpxz9dV8OPZSKxVzVXiuviQZVl7i6uVFC3h.hl6_u.y5ExPAJwJsxvOyj_RcORsAQBbgKrJ8wFCSUSRivZuFEJEOzJGlyKSopw; __gads=ID=a141ee4cfc528692:T=1726474876:RT=1726475329:S=ALNI_MaRDRzwsopeMvFGrVKXqh66_jpYSQ; __gpi=UID=00000f0b65ede236:T=1726474876:RT=1726475329:S=ALNI_MaFhNAYGKBgXkhicxh1IdLvFzDzyg; __eoi=ID=5eca0adf9c691b85:T=1726474876:RT=1726475329:S=AA-AfjZJ5OuoYJ5NLen4qrE8rz8Q; FCNEC=%5B%5B%22AKsRol_umO9yaedP5_W3fAoE5LIBIvKtB5UCTqCTE6AoRhCtvVovCEUt4-VqGAUQ9ZlhriP9fMBIejTqkR5r5HLNdGCXEY0xn082j8jACDX7VYFUiw1JKFuOvjXwg44sWsYHBdeEahFI_IiQETzpPc9wdSrZXe_j8A%3D%3D%22%5D%5D; jieqiRecentRead=3095.154931.0.1.1726475331.0; _ga_NG72YQN6TX=GS1.1.1726474881.1.1.1726475336.0.0.0; Hm_lpvt_1251eb70bc6856bd02196c68e198ee56=1726475336'
    }

    for i in text.find_all(True):
        if i.get('src'):
            pic_url = i.get('src')
            if 'https://' not in pic_url:
                pic_url = i.get('data-src')
            pic_resp = requests.get(
                url=pic_url, headers=header)
            demo_path = f'pic/demo{time.time()}.jpg'
            image_path = demo_path
            with open(image_path, 'wb') as f:
                f.write(pic_resp.content)
            time.sleep(0.1)
            try:
                img = Image(demo_path)
                img_width, img_height = img.wrap(0, 0)  # 獲取原始圖片大小
                if img_width > page_width or img_height > page_height:
                    scale_factor = max(img_width / page_width,
                                       img_height / page_height)+1
                    img.drawWidth = img_width / scale_factor
                    img.drawHeight = img_height / scale_factor
                story.append(img)
                story.append(PageBreak())
            except Exception as e:
                print(f"處理圖片時出錯：{e}")
                story.append(Paragraph(f"圖片加載失敗：{pic_url}", styleNormalCustom))
        else:
            story.append(Paragraph(i.get_text(), styleNormalCustom))

    pdfTemplate.build(story)
    time.sleep(1.5)

    ans = re.findall(
        'nextpage="(.*?)";', resp.text)[0]
    resp = get_web(ans)
    print(ans)

time.sleep(1)
shutil.rmtree('pic')
time.sleep(1)
os.mkdir('pic')
