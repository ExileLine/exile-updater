# -*- coding: utf-8 -*-
# @Time    : 2026-03-19 17:55:21
# @Author  : yangyuexiong
# @File    : enums.py

from enum import Enum


class UserStatus(str, Enum):
    normal = "正常"
    disable = "禁用"