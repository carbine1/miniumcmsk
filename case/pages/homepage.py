from case.base.basepage import BasePage
from case.base import route
from main import minium_init

class HomePage(BasePage):
    # def __init__(self, mini):
    #     self.mini = mini
    """小程序首页公共方法"""

    locators = {
        "BASE_TITLE": "text.index-module__title___2mxTG",
        "BASE_BANNER": "view.index-module__banner___2utnr",
        "BASE_TAG": "view.list-module__flxeWidth___ET-2x",
        "BASE_TILE": "image.index-module__container___GN1pF.index-module__tileImage___ktufQ",
        "BASE_MESSAGE": "view.index-module__container___3oG-z",
        "BASE_LIVE": "view.index-module__bottomContainer___1i1hV",
        "BASE_ACTIVITY": "view.index-module__container___24IAY.index-module__container___272eS",
        "BASE_HOTTOPIC": "view.index-module__container___1xZpW",
        "BASE_MALLITEM": "view.index-module__container___24IAY.index-module__container___2BsKY"
    }
    # 首页点击官方补贴的"更多"按钮
    city_select_button = ('view.index-module__city___3CrKD', "更多")

    """
    校验页面路径
    """
    def check_homepage_path(self):
        self.mini.assertEqual(self.current_path(), route.homepage_route)
    """
    校验页面的基本元素
    """
    def check_homepage_base_element(self):
        # 校验页面是否包含TITLE
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_TITLE']))
        # 校验页面banner位置
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_BANNER']))
        # 校验页面图标
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_TAG']))
        # 校验页面tile
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_TILE']))
        # 校验页面消息
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_MESSAGE']))
        # 校验页面直播
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_LIVE']))
        # 校验页面热门活动
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_ACTIVITY']))
        # 校验页面热门话题
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_HOTTOPIC']))
        # 校验页面商城商品
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_MALLITEM']))
    """
    获取官方补贴，点击"更多"按钮跳转
    """
    # def get_subsidy_element(self):
    #     self.mini.page.get_element(str(self.subsidy_more_button[0]),
    #                                inner_text=str(self.subsidy_more_button[1])).click()
    """
    点击打开城市选择页面
    """
    def get_city_select_element(self):
        self.mini.page.get_element(str(self.city_select_button[0])).click()
