# 自然语言处理 基础分词接口


## 分词工具：哈工大ltp算法包
## 启动服务：python3 ltp.py

## 请求地址
访问：http://host:8082/ltp/f


f = seg/pos/ner/parse/srl

分词：seg
词性标注：pos
实体识别：ner
依存句法分析：parse
语义角色标注: srl

辅助分词词典：lexicon

传参格式{"text" : "..."}

返回数据格式：字符串
