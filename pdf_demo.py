import os
import requests
import time
from bs4 import BeautifulSoup
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as ReportImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie": "night=1; _ga=GA1.1.303251830.1726056748; Hm_lvt_1251eb70bc6856bd02196c68e198ee56=1726056749; HMACCOUNT=5AB760526FFCFFF6; cf_clearance=YMCN3aqFtBYCeytGjRuE.362vTbakmtc2lR9vmAtZQY-1726056744-1.2.1.1-v3jpYoSPfIXDPkaHjaFki71p087Aj59zCvbpaXQ8XLeXuctKbeTcD9kW7wSFgl5Sk4NMneT6kTWhg0K8XrXFaPVKi99kjgDin51TPeUWSCkW.vmEnbTZ_9XTyxoQhUInK_whgU1oPdqt97slihRnXiksk1upcG7.WFL.ITGvPW4d4ottz1KSFrWedsAWRtMV2d501j9TTiC2BnRLwr9GHRrrfIGkuL07Qtgyvn4rz4Up7IvUhEIBizqJAb7tj1Qu69_yCzQPXxc5d3rbJCfyAA8nNFQ3Jdl0m1TJKoSdfN4JZT_65lN8tfnZSmDY6BFlQtJE0yBCMzjOOdlfObCspyeiLLuRoMG6vx2YqK54rM1CXnYy.xO65OIl6AF7lLj7ttt.ElswLp24STwkOwfSQA; jieqiVisitId=article_articleviews%3D3095; _ga_NG72YQN6TX=GS1.1.1726056748.1.1.1726056765.0.0.0; Hm_lpvt_1251eb70bc6856bd02196c68e198ee56=1726056766; __gads=ID=df178e8b15ad9650:T=1726056761:RT=1726056761:S=ALNI_MZ4TZbj3HoBFCpcBLeXXLwby4W-UQ; __gpi=UID=00000efa5b0489d5:T=1726056761:RT=1726056761:S=ALNI_MYrW1R5rmjG_utUlpNTIUZ-FtByKw; __eoi=ID=1925341d2679fe78:T=1726056761:RT=1726056761:S=AA-Afjbrc4i-cghGcGDUEsunw_HR; FCNEC=%5B%5B%22AKsRol9ha-JxjUcgrSwiF6laRORvudvSaiNjEzb9s3ThwLrjodI4H2ZnST9Tx_DQaKHm9U-NXyds81y-YCkC4oe4ssbwfjLiplC_48wDsiiQnC5yV1jtSgXa4UbHGz_IxSyZbPZnjYiTgKi94k23Ji0ik1h-Rxo4cg%3D%3D%22%5D%5D",
    "Referer": "https://tw.linovelib.com/novel/3095/catalog"
}

# PDF 字體設置
pdfmetrics.registerFont(TTFont('notoR', "static/NotoSansTC-Regular.ttf"))
pdfmetrics.registerFont(TTFont('notoB', "static/NotoSansTC-Bold.ttf"))
styles = getSampleStyleSheet()
styleNormalCustom = ParagraphStyle(
    'styleNormalCustom', fontName='notoR', fontSize=10, leading=20)
styleTitleCustom = ParagraphStyle(
    'styleTitleCustom', fontName='notoB', fontSize=20)


# 載入 HTML 文件
with open('scrape/bil_novel/demo.html', 'r', encoding='utf-8') as f:
    file = f.read()

soup = BeautifulSoup(file, "html5lib")
text = soup.find('div', class_='acontent')

# 移除不需要的元素
for script in text(["script", "style", "center", "div"]):
    script.decompose()

# PDF 文件設置
fileName = "demo.pdf"
pdfTemplate = SimpleDocTemplate(fileName, pagesize=A4)
story = []
a4_width, a4_height = A4

page_width = a4_width
page_height = a4_height

for i in text.find_all(True):
    if i.get('src'):
        # 下載圖片
        pic_url = i.get('src')
        pic_resp = requests.get(url=pic_url, headers=header)
        image_path = f'scrape/bil_novel/demo.jpg'
        with open(image_path, 'wb') as f:
            f.write(pic_resp.content)
        time.sleep(0.1)

        try:
            # 打開圖片並獲取尺寸
            with PILImage.open(image_path) as img:
                img_width, img_height = img.size

                # 計算縮放比例
                scale_factor = max(img_width / page_width,
                                   img_height / page_height)+1
                scaled_width = img_width / scale_factor
                scaled_height = img_height / scale_factor

                # 使用 Pillow 縮小圖像
                img = img.resize((int(scaled_width), int(
                    scaled_height)), PILImage.Resampling.LANCZOS)
                resized_image_path = f'scrape/bil_novel/resized_demo.jpg'
                img.save(resized_image_path)

            # 將調整後的圖像添加到 PDF
            img = ReportImage(resized_image_path,
                              width=scaled_width, height=scaled_height)
            story.append(img)
            story.append(PageBreak())
        except Exception as e:
            print(f"處理圖片時出錯：{e}")
            story.append(Paragraph(f"圖片加載失敗：{pic_url}", styleNormalCustom))
    else:
        story.append(Paragraph(i.get_text(), styleNormalCustom))

# 生成 PDF
pdfTemplate.build(story)
