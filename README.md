# jjwxcNovelProfile
爬取晋江文学城小说简介和封面
# 用法
 调用函数 search_jj_novel(book_keywork,author_keywork,search_pages,savepath)
## 参数
  - book_keywork：小说关键字
  - author_keywork：作者名字
  - search_pages：搜索页数
  - savepath：保存路径
# 补充
可以作者author_keywork设置为""进行全查找。
保存地址：
- 小说简介：TOC_file="%s/%s - %s - 简介.txt"%(savepath,apicont["novelName"],apicont["authorName"])
- 封面图片：img_file="%s/%s - %s - 封面.jpg"%(savepath,apicont["novelName"],apicont["authorName"])
- 
我以"savepath/作者"作为具体的保存路径，所以有时作者被封，名字就会带星号"\*"，使用img_file.replace("\*","x")将星号改为了x。
此外也可以去除apicont["novelName"]改为只保存在savepath路径下。
