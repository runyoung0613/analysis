from jieba import analyse
import os

# 获取脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))


def extract_key(file1,file2):
    tfidf = analyse.extract_tags
    for line in open(file1,encoding="utf8"):
        if line.strip()=='':
            continue
        text = line
        #tfidf 仅仅从词的统计信息出发，而没有充分考虑词之间的语义信息
        keywords = tfidf(text,allowPOS=('ns','nr','nt','nz','nl','n', 'vn','vd','vg','v','vf','a','an','i'))
        result=[]

        for keyword in keywords:     
            result.append(keyword)
        #print(result[0])
        fo = open(file2, "a+")
        for j in result:
            fo.write(j)
            fo.write(' ')
        fo.write('\n')
    fo.close()

    print("Keywords Extraction Done!")

if __name__ == '__main__':
    
    # 构建输入输出文件的绝对路径
    file1 = os.path.join(script_dir, "temp data", "contents_full.dat")
    file2 = os.path.join(script_dir, "temp data", "contents_keywords.dat")
    print("关键词提取开始...")     
    extract_key(file1,file2)
        
    print("Done!")