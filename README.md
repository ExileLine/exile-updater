# exile-updater

用于初始化 `FastAPI` 项目骨架的 CLI 脚本仓库。

## 用法

- 安装uv

    ```bash
    pip install uv
    ```
- 构建项目

    ```bash
    chmod +x init_fastapi_project.sh
    ./init_fastapi_project.sh --name exile_updater --author yangyuexiong --target /tmp/demo
    ```

- 安装依赖
    ```bash
    uv sync
    ```    

- 配置(如未准备db相关配置可注释代码如下，方可正常启动);`FAST_API_ENV`默认为`development`，按需切换环境配置，查阅`/app/core/config.py`

    ```python
    # /app/core/lifespan.py
    ...
    async def startup_event() -> None:
        _log_startup_info()
        logger.info(f">>> Config初始化: {project_config.ENV}")
    
        # try:
        #     await _init_db()
        #     await _init_redis()
        #     # await _init_scheduler()
        # except Exception:
        #     logger.exception("应用启动失败，开始回收资源")
        #     await _shutdown_scheduler()
        #     await _shutdown_redis()
        #     await _shutdown_db()
        #     raise
    
    
    async def shutdown_event() -> None:
        logger.info(">>> shutdown")
        # await _shutdown_scheduler()
        # await _shutdown_redis()
        # await _shutdown_db()
    ...
    ```
- 启动
    ```bash
    uv run local_run.py
    
    # http://localhost:7769/docs#/
    ```

## 参数

- `-n, --name`：项目包名，默认 `exile_updater`
- `-a, --author`：生成文件中的作者名，默认 `yangyuexiong`
- `-t, --target`：输出目录，默认当前目录
- `--force`：覆盖脚本生成的已有文件
- `--dry-run`：仅打印将执行的初始化动作
- `-h, --help`：查看帮助

## 常用示例

```bash
./init_fastapi_project.sh
./init_fastapi_project.sh --dry-run
./init_fastapi_project.sh --author yangyuexiong
./init_fastapi_project.sh --name demo_service --target /tmp/demo_service
./init_fastapi_project.sh --name demo_service --author alice --target /tmp/demo_service
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
