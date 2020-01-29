# 基于python3.7版本
FROM python:3.7
  
# 设置代码文件夹工作目录 /app
WORKDIR /app
  
# 复制当前代码文件到容器中 /app
ADD . /app
  
# 安装所需的包，使用清华源加速安装
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  
# 运行程序
CMD ["python", "main.py"]
