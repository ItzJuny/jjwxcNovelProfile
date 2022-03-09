from genericpath import exists
from json.tool import main
from base64 import encode
from lxml import etree
import requests
import re,os
import json
import urllib.parse


def parse_jj_novel(req_url,savepath):
    nid = req_url.split('=')[1]
    apireq = 'https://app.jjwxc.net/androidapi/novelbasicinfo?novelId=' + nid
    apires = requests.get(apireq)
    apicont = json.loads(apires.text)
    savepath=os.path.join(savepath,apicont["authorName"])
    os.makedirs(savepath,exist_ok=True)
    cover = apicont["novelCover"]
    TOC=""
    TOC+="书名："+apicont["novelName"]+"\tID："+apicont["novelId"]+"\n"
    TOC+="作者："+apicont["authorName"]+"\tID："+apicont["authorId"]+"\n"
    TOC+="源网址："+req_url+"\n"
    TOC+="封面地址："+apicont["novelCover"]+"\n"
    TOC+="全文字数："+apicont["novelSize"]+"\t文章进度："+apicont["series"]+"\n"
    TOC+="评分："+apicont["novelReviewScore"]+"\t排名："+apicont["ranking"]+"\n"
    TOC+=apicont["protagonist"]+"\t"+apicont["costar"]+"\n"
    TOC+="作品视角："+apicont["mainview"]+"\t作品风格："+apicont["novelStyle"]+"\n"
    TOC+="文案：\n"
    intro = apicont["novelIntro"].replace("&lt;","").replace("&gt;","").split("br/")
    # print(intro)
    for i,j in enumerate(intro):
        if (j != ""):
            TOC+="\t"+j+"\n"
    TOC+="一句话简介："+apicont['novelIntroShort']+"\n"
    fo=open("%s/%s - %s - 简介.txt"%(savepath,apicont["novelName"],apicont["authorName"]),'w',encoding='utf-8')
    fo.write(TOC)
    fo.close()
    if cover != '':
        pres = requests.get(cover)
        img = pres.content
        with open("%s/%s - %s - 封面.jpg"%(savepath,apicont["novelName"],apicont["authorName"]), 'wb') as pic:
            pic.write(img)

            
def search_jj_novel(book_keywork,author_keywork,search_pages,savepath):
    encode_keywork = urllib.parse.quote(book_keywork.encode('gbk'))
    find_dict={}
    for page in range(1,search_pages):
        search_url="http://www.jjwxc.net/search.php?kw=%s&t=1&p=%d&ord=novelscore"%(encode_keywork,page)
        try:
            res = requests.get(search_url).content
            res_utf=res.decode("GB18030","ignore").encode("utf-8","ignore").decode('utf-8')
            from lxml import etree
            ress = etree.HTML(res_utf)
            for i in range(2,27):
                book_name=ress.xpath("//*[@id='search_result']//div[%d]/h3/a//text()"%i)
                book_url=ress.xpath("//*[@id='search_result']//div[%d]/h3/a/@href"%i)
                author=ress.xpath("//*[@id='search_result']//div[%d]/div[2]/a/span/text()"%i)
                book_name = "".join(book_name).replace(" ","").replace("\n","").replace("\r","")
                book_url = "".join(book_url).replace(" ","").replace("\n","").replace("\r","")
                author = "".join(author).replace(" ","").replace("\n","").replace("\r","")
                if author_keywork in author :
                    find_dict[book_name+"-"+author]=book_url
        except:
            pass
    if len(find_dict)==0:
        print("没有找到，增加搜索页数或者检查关键词输入。")
    else:
        print("找到%d条记录："%len(find_dict))
        for i in find_dict.keys():
            print("  书名：%s，作者：%s，小说地址：%s"%(i.split("-")[0],i.split("-")[1],find_dict[i]))
            parse_jj_novel(find_dict[i],savepath)
