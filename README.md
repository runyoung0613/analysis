# news-analyst
## 项目关键词
Word2Vec
## 文件说明
### step1_cut_words
**dict：停用词表**
dict_baidu_utf8.txt：百度停用词表
dict_pangu.txt：盘古停用词表
dict_sougou_utf8.txt：搜狗停用词表
dict_tencent_utf8.txt：腾讯停用词表
my_dict.txt：自定义停用词表
SogouLabDic.txt：搜狗实验室停用词表
**raw data:原始文件**
comments_utf8.txt：utf-8编码的评论文件
conments.txt：原始评论文件
contents.txt：预处理后的评论文件
**temp data**
contents_full.dat: 提取关键词后的文件
contents_.dat: 提取关键词后的文件
contents_keywords.dat：textrank提取关键词后的文件

- A_csv2txt_comment.py：将contents_keywords.dat文件转换为contents_keywords.txt文件
- A_csv2txt_data.py：将contents_full.dat文件转换为contents_.txt文件
- A_csv_words.py：将contents_keywords.dat文件转换为contents_keywords.txt文件
- A_keywords_jieba.py：使用jieba库对contents_keywords.txt文件进行分词处理，得到contents_keywords_jieba.txt文件
- Stopword.txt：停用词表文件
- test.py：测试文件，用于测试分词效果

### step2_word_cloud
- wordcloud.py：使用wordcloud库生成词云图
- wordcloud_chinese.py：使用wordcloud库生成中文词云图

### step3_sentimentAnalysis
**data**
deal.py：数据预处理文件，包括去重、去停用词、分词等
neg.csv：消极评论文件
pos.csv：积极评论文件
neutral.csv：中性评论文件
**lstm**
comments_sentiment.txt：lstm模型情感分析结果文件
lstm_train.py：lstm模型训练文件
lstm_test.py：lstm模型测试文件
test.py：测试文件，用于测试lstm模型的情感分析效果
word2index.txt：词到索引的映射文件，用于将词语转换为索引
**model**
lstm.h5：lstm模型文件
lstm.yml：lstm模型配置文件，包括模型参数、词向量维度、窗口长度、学习率等
Word2vec_model.pkl：word2vec模型文件，用于将词语转换为向量表示
- requirements.txt：项目依赖文件，包含了项目所需的Python库和版本
- step3_README.md：step3情感分析模块的说明文档，介绍了情感分析的流程、算法、数据集、模型训练、测试和评估等内容

### step4_clustering
**data**
clustering.py：聚类分析文件，包括数据预处理、聚类模型训练、聚类结果可视化等
clustering_result.txt：聚类分析结果文件，包含了每个评论所属的聚类类别
**tmp**
    ***AP_with_emb***
    ***AP_without_emb***
    - data_with_embedding.json：包含词向量的评论文件
    - data_with_id.json：包含评论id的文件
    - data_with_lable.json：包含情感标签的文件
    - data.json：包含评论id、情感标签、评论内容的文件
    - used_embedding_50.txt：包含已使用的词向量文件，每行一个词向量，词向量维度为50
- step1_data_process.py：数据预处理文件，包括去重、去停用词、分词等
- step2_load_word2vec.py：加载word2vec模型文件，用于将词语转换为向量表示
- step3_doc_embedding.py：文档嵌入文件，用于将文档转换为向量表示
- step4_AP.py：AP聚类分析文件，包括数据预处理、聚类模型训练、聚类结果可视化等
- step5_select_sentence.py：选择情感分析结果为积极的评论文件，用于后续的情感分析任务
tfidf-ap.py：tf-idf聚类分析文件，包括数据预处理、聚类模型训练、聚类结果可视化等

## 使用步骤


## 词云展示涉及的算法：

Tf-idf:提取句子中关键词
tf-idf提取关键词是一种简单有效的提取关键词的方法.其思想主要在于预先统计在语料中出现的所有词的词频,计算出idf值,
然后再针对要提取关键词的文章或句子的每个词计算出tf值,乘起来便是tf-idf值.值越大表示作为关键词的优先级越高.

TextRank：提取文档中关键词构建词云
tf-idf是纯粹用词频的思想，完全没有用到词之间的关联性. 而textrank用到了词之间的关联性(将相邻的词链接起来),
以词为节点，以共现关系建立起节点之间的链接.即文本进行分词，去除停用词或词性筛选等之后，设定窗口长度为K，即
最多只能出现K个词，进行窗口滑动，在窗口中共同出现的词之间即可建立起无向边。

## 情感分析涉及的算法：

Word2Vec算法:通过Word2Vec算法得到每个词语的高维向量（词向量，Word Embedding）表示，词向量把相近意思的词
语放在相近的位置。我们只需要有大量的某语言的语料，就可以用它来训练模型，获得词向量.词向量可以方便做聚类，用
欧氏距离或余弦相似度都可以找出两个具有相近意思的词语。

LSTM三分类模型:LSTM是一种特定的循环神经网络，增加了记忆单元c、输入门i、遗忘门f及输出门o，这些门及记忆单元组合
起来大大提升了循环神经网络处理长序列数据的能力。将一个句子中所有词向量输入到LSTM神经网络中，得到最后时刻的输出
用于分类即可判断句子的情感极性（消极，积极、中性）

## 观点抽取涉及的算法：

AP聚类算法进行文本聚类：
AP(Affinity Propagation)算法,称为仿射传播聚类算法、近邻传播聚类算法、亲和传播聚类算法，是根据数据点之间的相似
度来进行聚类，可以是对称的，也可以是不对称的。 该算法不需要先确定聚类的数目，而是把所有的数据点都看成潜在意义上
的聚类中心（exemplar）。这里通过词向量和词向量对应的tf-idf 值构建文本向量表示，文本之间的相似性通过两个文本向
量的余弦相似性得到。最后通过AP聚类算法得到观点数量，并从观点中筛选典型评论