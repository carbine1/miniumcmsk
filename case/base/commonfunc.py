#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: lockerzhang
@LastEditors: lockerzhang
@Description: 小程序页面
@Date: 2019-03-11 14:42:29
@LastEditTime: 2019-06-05 17:04:02
"""
import re
from minium.framework.exception import MiniElementNotFoundError, MiniAppError
import typing
from minium.miniprogram.base_driver.element import *
# from .element import *
from minium.miniprogram.base_driver.minium_object import MiniumObject
from minium.utils.utils import timeout
from minium.miniprogram.base_driver.connection import Command


class PageFunction(MiniumObject):
    def __init__(self, page_id, path, query, connection):
        """
        初始化页面
        """
        super().__init__()
        self.page_id = page_id
        # 处理下path，普通page以"/"开头，插件以"plugin://" 或 "plugin-private://"开头
        self.plugin_appid = None
        match = re.search(r"^(plugin://|plugin-private://|__plugin__/)(\w+)/", path)
        if match:
            self.plugin_appid = match.group(2)
        elif not path.startswith("/"):
            path = "/" + path
        self.path = path
        self.query = query
        self.connection = connection
        self.is_webview = None  # None: 未知，true: 是，false: 否

    def __repr__(self):
        return "Page(id={0}, path={1}, query={2})".format(self.page_id, self.path, self.query)


