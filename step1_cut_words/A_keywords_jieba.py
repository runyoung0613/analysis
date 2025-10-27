from jieba import analyse
import os

# 获取当前脚本文件所在目录的绝对路径，确保后续拼接文件路径时不受工作目录影响
script_dir = os.path.dirname(os.path.abspath(__file__))

def extract_key(file1,file2):
    tfidf = analyse.extract_tags
    # 使用with语句安全地处理文件，并使用"w+"模式确保每次运行都重写文件内容
    with open(file2, "w+", encoding="utf8") as fo:
        for line in open(file1, encoding="utf8"):
            if line.strip()=='':
                continue
            text = line
            #tfidf 仅仅从词的统计信息出发，而没有充分考虑词之间的语义信息
            keywords = tfidf(text, allowPOS=('ns','nr','nt','nz','nl','n', 'vn','vd','vg','v','vf','a','an','i'))
            result=[]

            for keyword in keywords:     
                result.append(keyword)
            #print(result[0])
            for j in result:
                fo.write(j)
                fo.write(' ')
            fo.write('\n')

    print("Keywords Extraction Done!")

if __name__ == '__main__':
    
    # file1 是输入文件（原始文本），file2 是输出文件（提取出的关键词）
    file1 = os.path.join(script_dir, "temp data", "contents_full.dat")
    file2 = os.path.join(script_dir, "temp data", "contents_keywords.dat")
    print("关键词提取开始...")    
    extract_key(file1,file2)
        
    print("Done!")