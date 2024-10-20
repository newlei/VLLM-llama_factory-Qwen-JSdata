# VLLM-llama_factory-Qwen-JSdata
VLLM(部署模型，运行调用qwen大模型)，llama_factory（LoRA训练模型），Qwen2.5（基础的大模型），JSdata（数据集）



## 使用llama_factory（LoRA训练模型）

### 安装llama_factory
  
``` 
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git

cd LLaMA-Factory

pip install -e ".[torch,metrics]"
``` 



### 构建数据集

- 运行下面的代码就行：
```
python data_generate.py
```

- 将生成的js1.json copy到./LLaMA-Factory/data/文件夹中
  
- 更多的alpaca style data，见下面的[链接](https://raw.githubusercontent.com/tatsu-lab/stanford_alpaca/refs/heads/main/alpaca_data.json)
  
https://raw.githubusercontent.com/tatsu-lab/stanford_alpaca/refs/heads/main/alpaca_data.json


### 微调训练、推理、合并导出LoRa的部分

最前面的CUDA_VISIBLE_DEVICES=4，是设置使用哪张显卡

```
微调
拷贝jsqwen_lora_pretrain.yaml到，./LLaMA-Factory/examples/train_lora/文件夹中
CUDA_VISIBLE_DEVICES=4 llamafactory-cli train examples/train_lora/jsqwen_lora_pretrain.yaml

推理
拷贝jsqwen_lora.yaml到，./LLaMA-Factory/examples/inference/文件夹中
CUDA_VISIBLE_DEVICES=4 llamafactory-cli chat examples/inference/jsqwen_lora.yaml

合并导出
拷贝jsqwen_lora_merge.yaml到，./LLaMA-Factory/examples/merge_lora/文件夹中
CUDA_VISIBLE_DEVICES=4 llamafactory-cli export examples/merge_lora/jsqwen_lora_merge.yaml
```


## api 批量推理

```
API_PORT=8000 CUDA_VISIBLE_DEVICES=0 llamafactory-cli api examples/inference/jsqwen_lora.yaml 
```
启动 api 服务并运行以下示例程序进行调用：

```
# api_call_example.py
from openai import OpenAI
client = OpenAI(api_key="0",base_url="http://0.0.0.0:8000/v1")
messages = [{"role": "user", "content": "Who are you?"}]
result = client.chat.completions.create(messages=messages, model="../Qwen2.5-1.5B-Instruct")
print(result.choices[0].message)
```
