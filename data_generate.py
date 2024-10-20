# for generating Alpaca-style-Dataset

import json
import pandas as pd
import pdb
import math

# 读取excel的某一个sheet
df = pd.read_excel('./papers.xlsx', sheet_name='Sheet1')
data = []
instruction = "您是一个总结出关键词的助手。"
for ind in df.index:
    # print(df['abstract'][ind], df['keyword'][ind])
    # pdb.set_trace() 
    text = df['abstract'][ind]
    output = df['keyword'][ind]
    # print(text,output)
    if len(str(text))<4:
        continue
    if len(str(output))<4:
        continue
    data.append({
            "instruction": instruction,
            "input": text,
            "output":output
        })

output_file = './LLaMA-Factory/data/js_problem.json'

with open(output_file, 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')


