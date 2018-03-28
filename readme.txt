信件 受信人的识别


分词工具：哈工大ltp算法包
启动服务：python3 recognize.py

受信人请求地址
访问：http://host:8083/sxr

来信人请求地址
访问：http://host:8083/lxr

访问：http://host:8082/extract_id

调用身份证号识别接口 ： extract_id
调用手机号识别接口： extract_tel

地址识别：address
组织机构识别：org
9

传参格式{"text" : "..."}

返回数据格式：字符串