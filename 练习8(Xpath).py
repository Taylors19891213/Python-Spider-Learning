#xpath 是在XML文档中搜索内容的一门语言
#html是XML的一个子集
#靠节点之间的关系来查找


#   /表示层级关系，第一个/是根节点
#   //表示后代
#   *表示任意的节点:通配符


#安装lxml模块
#pip install lxml -i xxxxx

# from lxml import etree
# xml = "......"
# tree = etree.Xml(xml)
# result = tree.xpath("/book//name/text(")   #text() 拿文本
# print(result)


from lxml import etree
tree = etree.parse("b.html")    #解析处理（文件）

# result = tree.xpath("/html/body/ul/li[1]/a/text()")   #[  ]表示索引，xpath是从1开始数
# result = tree.xpath("/html/body/ol/li/a[@href = 'dapao']/text()")  #[@xxx = xxx]表示属性的筛选定位

ol_li_list = tree.xpath("/html/body/ol/li")

for li in ol_li_list:
    result = li.xpath("./a/text()")       #li中继续去查找，相对查找
    print(result)
    rusult2 = li.xpath("./a/@href")       #拿到属性值，/@a
    print(rusult2)

print(tree.xpath("/html/body/ul/li/a/@href"))

print(tree.xpath("/html/body/div[1]/text()"))     #tips:页面检查复制xpath路径