# Keras BERT API Demo

# import sys
import numpy as np
from keras_bert import (
    load_vocabulary,
    load_trained_model_from_checkpoint,
    Tokenizer,
    get_checkpoint_paths,
)
from keras_bert.datasets import get_pretrained, PretrainedList

# 導入已訓練中文模型
model_path = get_pretrained(PretrainedList.chinese_base)
paths = get_checkpoint_paths(model_path)
model = load_trained_model_from_checkpoint(
    paths.config, paths.checkpoint, training=True, seq_len=None
)
model.summary(line_length=120)
# 導入字典
token_dict = load_vocabulary(paths.vocab)
token_dict_inv = {v: k for k, v in token_dict.items()}
# 要測試的字串
# 舉例 : CLS 台 北 是 MASK MASK 的 首 都 SEP
# MASK = 要猜的字串
tokens = ["[CLS]"]
mask = ["[MASK]", "[MASK]"]
text1 = "北京是"
text2 = "的首都"
tokens.extend(list(text1))
tokens.extend(mask)
tokens.extend(list(text2))
tokens.append("[SEP]")
print("Tokens to predict:", tokens)
indices = np.array([[token_dict[token] for token in tokens]])
segments = np.array([[0] * len(tokens)])
# 要預測的位置為1 其它為0
judge=[]
for i in tokens:
    if i == "[MASK]":
        judge.append(1)
    else :
        judge.append(0)
masks = np.array([judge])
predicts = model.predict([indices, segments, masks])[0].argmax(axis=-1).tolist()
print("Fill with: ", list(map(lambda x: token_dict_inv[x], predicts[0][4:6])))