# jjwxcNovelProfile
**爬取晋江文学城小说的简介和封面**

# 用法
 调用函数 search_jj_novel(book_keywork,author_keywork,search_pages,savepath)

## 参数
  - book_keywork：小说关键字
  - author_keywork：作者名字
  - search_pages：搜索页数
  - savepath：保存路径
  - 
# 补充
可以作者author_keywork设置为""进行全查找。
保存地址：
- 保存路径：savepath = os.path.join(savepath,apicont["authorName"]).replace("*","x")
- 小说简介：TOC_file="%s/%s - %s - 简介.txt"%(savepath,apicont["novelName"],apicont["authorName"])
- 封面图片：img_file="%s/%s - %s - 封面.jpg"%(savepath,apicont["novelName"],apicont["authorName"])

我以"savepath/作者"作为具体的保存路径，所以有时作者被封，名字就会带星号"\*"，使用img_file.replace("\*","x")将星号改为了x。

此外也可以注释掉"savepath = os.path.join(savepath,apicont["authorName"]).replace("\*","x")"，改为只保存在savepath路径下。

# 实例

 # 小说界面
![image](https://user-images.githubusercontent.com/57182325/157384580-35822da5-236f-4510-bbcb-22673ae4d3df.png)

 # 运行代码
 - 运行目录结构：![image](https://user-images.githubusercontent.com/57182325/157384794-fe5da6cf-cdec-44b3-9e9f-62c9b4465fc2.png)
 - 调用函数：![image](https://user-images.githubusercontent.com/57182325/157385155-88a3eb33-e1ef-4016-aab5-f9b0b5e0e5cc.png)

 # 爬取结果
 - 小说：![image](https://user-images.githubusercontent.com/57182325/157384830-d11d09cb-6376-4ef6-86d3-248641c99cc7.png)
 - 封面：![image](https://user-images.githubusercontent.com/57182325/157384846-6f3b14cc-da91-4a0d-8210-b3cfb08ed51b.png)
