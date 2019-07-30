---
title: pipenv使用
date: 2019/07/26 14:24:00
tags: [Python,pipenv]
categories: Python
---
<!-- more -->

# Pipenv的使用

下载安装
pip install pipenv
创建虚拟环境(pipenv可以根据Python的不同版本创建)
pipenv --three/two
pipenv --python 2.7
pipenv --python 3.7

文件介绍
创建虚拟环境之后，项目目录中会有两个新的文件
Pipfile 文件是TOML格式，存放当前虚拟环境的配置信息，包括Python版本,pypi源以及依赖包等
Pipfile.lock 该文件是对Pipfile的锁定

激活虚拟环境
pipenv shell 进入虚拟环境
exit 退出虚拟环境

环境分离与添加
pipenv install的多重作用
1.如果虚拟环境存在，则安装Pipfile中的依赖包
2.如果虚拟环境不存在，但Pipfile存在，则根据Pipfile中python版本创建虚拟环境并安装依赖包;
3.如果虚拟环境与Pipefile都不存在，则根据系统Python版本创建虚拟环境
4.指定requirements.txt 文件安装环境

```text
强烈建议以编辑模式安装任何版本控制依赖，如下示例：
# 安装requests
pipenv install -e git+https://github.com/requests/requests.git@v2.19#egg=requests
```


https://blog.csdn.net/haiyanggeng/article/details/82382993