###Scrapy的元素选择器Xpath

response.xpath('//span//table')
跳级定位：符号“//”表示跳级定位，即对当前元素的所有层数的子元素（不仅是第一层子元素）进行查找

###提取元素或元素的属性值
a=response.xpath('//a[contains(text(),"闻")]').extract()
//提取被定义的元素对象


1，url字符串中如果带有中文的编码，要使用url时。先将中文部分编码由gbk译为utf8

然后在urllib.quote(str)

才可以使用url正常访问打开，否则编码会出问题。

2，同样如果从url中取出相应中文字段解码时，需要先unquote，然后在decode，具体按照gbk或者utf8，视情况而定。


