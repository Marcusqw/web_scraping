import pandas as pd
import json
from markdownify import markdownify as md

input_file_path = r'C:\Users\Razer\Desktop\爬蟲\supreme_court_toc.jsonl'  # 输入文件路径
output_file_path = r'C:\Users\Razer\Desktop\爬蟲\output.jsonl'  # 输出文件路径

# Read the JSON Lines file
data = []
with open(input_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line.strip()))

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 确保只选择需要的列
if 'path' in df.columns and 'content' in df.columns:
    df['path'] = df['path'].str.replace(r'\t', '', regex=True)  # 移除所有制表符
    df['path'] = df['path'].str.replace(r'\s+', '_', regex=True)  # 将一个或多个空格替换成下划线
    
    df['content'] = df['content'].apply(lambda x: md(x))
    
    # 将DataFrame转换回字典
    transformed_data = df.to_dict(orient='records')
    
    # 写入新的JSON Lines文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for item in transformed_data:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')
    
    print(f"Processed JSON Lines file has been saved as {output_file_path}")