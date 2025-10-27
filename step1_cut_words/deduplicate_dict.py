# 简单的字典文件去重工具

# 文件路径
file_path = "e:/analysis/step1_cut_words/dict/dict_baidu_utf8.txt"

# 读取文件内容
print("读取字典文件...")
f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()

# 统计原始行数
original_count = len(lines)
print("原始行数:", original_count)

# 去重
unique_lines = []
seen = set()
for line in lines:
    # 去除换行符
    clean_line = line.rstrip('\n')
    if clean_line and clean_line not in seen:
        seen.add(clean_line)
        unique_lines.append(clean_line)

# 统计去重后的行数
unique_count = len(unique_lines)
print("去重后行数:", unique_count)
print("移除重复项:", original_count - unique_count)

# 写入文件
print("写入去重后的内容...")
f = open(file_path, "w", encoding="utf-8")
for line in unique_lines:
    f.write(line + "\n")
f.close()

print("字典文件去重完成！")