import jieba
import os

# 获取脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 使用绝对路径加载词典文件
jieba.load_userdict(os.path.join(script_dir, "dict", "SogouLabDic.txt"))
jieba.load_userdict(os.path.join(script_dir, "dict", "dict_baidu_utf8.txt"))
jieba.load_userdict(os.path.join(script_dir, "dict", "dict_pangu.txt"))
jieba.load_userdict(os.path.join(script_dir, "dict", "dict_sougou_utf8.txt"))
jieba.load_userdict(os.path.join(script_dir, "dict", "dict_tencent_utf8.txt"))
#jieba.load_userdict(os.path.join(script_dir, "dict", "my_dict.txt"))

def get_data(file,file2):
    # 使用绝对路径加载停用词表
    stopwords_file = os.path.join(script_dir, "Stopword.txt")
    stopwords = {}.fromkeys([ line.rstrip() for line in open(stopwords_file, 'r', encoding='utf8') ])
    result =[]
    f = open(file,"r")
    data = f.readlines()
    f.close()
    print(len(data))
    for line in data:
        if not len(line):
            continue
        seg = jieba.cut(line)
        for i in seg:
            if i not in stopwords:  
                result.append(i)

        fo = open(file2, "a+",encoding='utf8')
        for j in result:       
           fo.write(j)
           fo.write(' ')
        fo.write('\n')
        result=[]
    fo.close()
    print("转换完成!")

if __name__ == '__main__':
    
    # 构建输入输出文件的绝对路径
    #可以修改为评论或则新闻本身
    # file = os.path.join(script_dir, "raw data", "comments.txt")
    # file2 = os.path.join(script_dir, "temp data", "comments_full.dat")
    file = os.path.join(script_dir, "raw data", "contents.txt")
    file2 = os.path.join(script_dir, "temp data", "contents_full.dat")
    print("转换开始...")     
    get_data(file,file2)
        
    print("Done!")






