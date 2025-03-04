csv-cti/
│── app/
│   ├── main.py           # 应用入口
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── routers/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user_router.py    # 用户管理 API
│   │   │   │   ├── csv_router.py     # CSV 解析 API
│   │   │   │   ├── auth_router.py    # 认证 API
│   │   │   ├── dependencies.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── settings.py    # 环境变量管理
│   │   ├── security.py    # 认证、Token
│   ├── middlewares/       # 可选：中间件
│   │   ├── __init__.py
│   │   ├── cors.py
│   │   ├── logging.py
│   │   ├── timing.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py        # 用户模型
│   │   ├── csv_data.py    # CSV 数据模型
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py        # 用户数据结构
│   │   ├── csv_data.py    # CSV 数据结构
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py        # 用户数据库操作
│   │   ├── csv_data.py    # CSV 数据操作
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py  # 用户业务逻辑
│   │   ├── csv_service.py   # CSV 解析业务逻辑
│   ├── database.py        # 数据库连接
│   ├── deps.py            # 依赖项
│── tests/
│   ├── test_main.py       # 主测试文件
│   ├── test_users.py      # 用户 API 测试
│   ├── test_csv.py        # CSV 相关测试
│── .env                   # 环境变量
│── .gitignore             # Git 忽略文件
│── Pipfile                # Pipenv 依赖管理
│── Pipfile.lock           # 依赖锁定
│── README.md              # 项目说明
