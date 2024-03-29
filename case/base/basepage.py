from main import minium_init
from minium.miniprogram.base_driver.element import BaseElement

mini = minium_init()


class BasePage(BaseElement):
    def __init__(self, mini):
        self.mini = mini

    def navigate_to_open(self, route):
        """以导航的方式跳转到指定页面,不允许跳转到 tabbar 页面,支持相对路径和绝对路径, 小程序中页面栈最多十层"""
        self.mini.app.navigate_to(route)

    def redirect_to_open(self, route):
        """关闭当前页面，重定向到应用内的某个页面,不允许跳转到 tabbar 页面"""
        self.mini.app.redirect_to(route)

    def switch_tab_open(self, route):
        """跳转到 tabBar 页面,会关闭其他所有非 tabBar 页面"""
        self.mini.app.switch_tab(route)

    @property
    def current_title(self) -> str:
        """获取当前页面 head title, 具体项目具体分析,以下代码仅用于演示"""
        return self.mini.page.get_element("XXXXXX").inner_text

    def current_path(self) -> str:
        """获取当前页面route"""
        return self.mini.page.path

    def scroll_to_element(self, selector, duration=300):
        """
        滚动到指定位置,页面使用，非scroll-view组件使用
        :param selector:  选择器,注意，仅支持id和class，及两者组合，传tag不起作用
        :param duration:  滚动时长
        :return:
        """
        self.mini.app.call_wx_method("pageScrollTo", [{"selector": selector, "duration": duration}])

    def call_function(self, func, args):
        self.call_func(func, args)
