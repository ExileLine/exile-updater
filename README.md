# exile-updater

用于初始化 `FastAPI` 项目骨架的 CLI 脚本仓库。

## 用法

```bash
chmod +x init_fastapi_project.sh
./init_fastapi_project.sh --name exile_updater --target /tmp/demo
```

## 参数

- `-n, --name`：项目包名，默认 `exile_updater`
- `-t, --target`：输出目录，默认当前目录
- `--force`：覆盖脚本生成的已有文件
- `--dry-run`：仅打印将执行的初始化动作
- `-h, --help`：查看帮助

## 常用示例

```bash
./init_fastapi_project.sh
./init_fastapi_project.sh --dry-run
./init_fastapi_project.sh --name demo_service --target /tmp/demo_service
./init_fastapi_project.sh --force
```

## 当前会生成的内容

- `app/api/v1/endpoints`、`app/core`、`app/db`、`app/models`、`app/tasks` 等基础目录
- `app/main.py`、`lifespan`、中间件、异常处理、权限、分页、响应等基础模块
- `SQLAlchemy` 模型基类、`Admin`、`ApsTask` 等示例模型
- `Celery`、`APScheduler`、`Redis`、数据库会话等基础集成样板
- `.env.example`、`.env.development`、`.env.test`、`.env.staging`、`.env.production`
- `pyproject.toml`、`scripts/dev.sh`、`local_run.py`、`tests/test_health.py`

## 建议

- 如果只是检查会生成什么，先使用 `--dry-run`
- 如果在已有目录中重新生成，只有在确认要覆盖文件时再使用 `--force`
