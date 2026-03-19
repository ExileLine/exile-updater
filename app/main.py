# -*- coding: utf-8 -*-
# @Time    : 2026-03-19 17:55:21
# @Author  : yangyuexiong
# @File    : main.py

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.router import api_router
from app.core.config import get_config
from app.core.exception_handlers import register_exception_handlers
from app.core.lifespan import lifespan
from app.core.middleware import MyMiddleware

project_config = get_config()


def create_app():
    debug = project_config.DEBUG
    kw = {
        "debug": debug
    }

    app = FastAPI(
        title=project_config.DOCS_TITLE,
        description=project_config.DOCS_DESCRIPTION,
        summary=project_config.DOCS_SUMMARY,
        version=project_config.DOCS_VERSION,
        openapi_url=project_config.DOCS_OPENAPI_URL,
        lifespan=lifespan,
        **kw
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.add_middleware(
        MyMiddleware,
        log_headers=debug,
        log_body=debug,
        exclude_paths=["/docs", "/openapi.json", "/redoc", "/static*"],
        sensitive_headers=project_config.SENSITIVE_HEADERS,
        mask_sensitive_headers=project_config.MASK_SENSITIVE_HEADERS,
    )

    register_exception_handlers(app, debug)
    app.include_router(api_router)

    static_dir = Path(__file__).resolve().parent / "static"
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    @app.get("/")
    async def root_redirect():
        return {
            "status": "ok",
        }

    return app


app = create_app()