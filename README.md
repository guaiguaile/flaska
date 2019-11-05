>目录结构:
```text
flaska/
├── app
│   └── __init__.py
├── app.py
├── common
│   └── __init__.py
├── conf
│   ├── dev_config.py
│   ├── pro_config.py
│   └── test_config.py
├── __init__.py
├── requirements.txt
├── routes
│   └── __init__.py
├── services
│   └── __init__.py
├── settings.py
├── .gitignore
├── requirements.txt
└── README.md
```

>目录说明:
```text
- Directory
app: 放置项目的基础代码
common: 项目的公共代码
conf: 不同运行环境的配置文件
routes: 项目的路由代码
services: 项目引用的相关服务代码

- File
app.py 项目主入口文件 
__init__.py 项目初始化文件
README.md 项目说明文件
settings.py 配置读取文件
.gitignore git上传过滤文件
requirements.txt 包依赖文件
```