#!/usr/bin/env python
# coding: utf-8
import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import collections
import re

# 读取《三国演义》
text = open('sgyy.txt','r',encoding='UTF-8').read()

#此处排除关羽、张飞在一起时简称“关、张”的情形
text = re.sub("关","关羽",text)
text = re.sub("张","张飞",text)

#开始分词
words = jieba.cut(text)
r_words = ""
for word in words:
    #归一化处理
    if word in ["孟德","丞相"]:
        r_words += "曹操 "
    elif word in ["玄德","玄德曰"]:
        r_words += "刘备 "
    elif word in ["关公","云长"]:
        r_words += "关羽 "
    elif word in ["益德","飞曰"]:
        r_words += "张飞 "
    elif word in ["诸葛亮","孔明曰"]:
        r_words += "诸葛孔明 "
    elif word in ["子龙"]:
        r_words += "赵云 "
    #把这些人挑出来
    elif word in ["刘备","关羽","张飞","赵云","曹操","诸葛孔明","孙权","吕布","周瑜","黄忠","司马懿","马超","庞统","鲁肃","许攸","徐庶","袁绍","董卓","貂蝉","孙策","大乔","小乔"]:
        r_words += word + ' '
    elif word in ["将军","却说","荆州","大将","赶来","人马","二人","不可","于是","今日","不能","如此","主公","商议","如何","不敢","魏兵","军士","然后","百姓","不如","天子","后人","先生"] or len(word) ==  1:
        continue
cut_word = [item.strip() for item in r_words.split(" ") if item != '']
#得到人名列表，我们可以直接用counter()函数进行统计，然后将统计信息传入Wordcloud函数生成词云
wordcounts = collections.Counter(cut_word)
wordcountstop = wordcounts.most_common()
print(wordcountstop)

(
    WordCloud(opts.InitOpts(width="100%",height="900px"))
    .add(series_name="人物分析", data_pair=wordcountstop, word_size_range=[30, 100])
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("wordcloud.html")
)
