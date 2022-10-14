import threading
import time
import datetime
from case.base.basepage import BasePage
from case.base import route
from minium.framework.minitest import MiniTest
# from main import minium_init


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
        "BASE_MALLITEM": "view.index-module__container___24IAY.index-module__container___2BsKY",
        "BASE_MALL": "view.index-module__imgContainer___3MS4F"
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
        # self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_LIVE']))
        # 校验页面热门活动
        self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_ACTIVITY']))
        # 校验页面热门话题
        # self.mini.assertTrue(self.mini.page.element_is_exists(HomePage.locators['BASE_HOTTOPIC']))
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

    def scroll_page(self):
        el = self.mini.page.get_element("scroll-view.index-module__container___292Uk")
        # 等待目标元素渲染完成再下拉，否则概率出现下拉失效
        self.mini.page.wait_for(HomePage.locators['BASE_MALL'])
        # asa = threading.Semaphore()
        # scroll-view 下可使用以下方法滚动：el.scroll_to和el.call_func(func="scroll-view.scrollTo", args=[0, 1000, 1000, 1])，非scroll-view不起作用
        el.scroll_to(y=1000)
        el.call_func(func="scroll-view.scrollTo", args=[0, 1000, 1000, 1])
        # page1 = self.mini.app.get_current_page()
        # self.mini.app.call_wx_method("pageScrollTo", [{"selector": HomePage.locators['BASE_MALL'], "duration": 1000}])

        self.scroll_to_element(HomePage.locators['BASE_MALL'], 2000)
        imagename = "homescrolled%s" % datetime.datetime.now().strftime("%H%M%S%f")
        self.mini.capture(name=imagename)
        # time.sleep(20)

        # self.mini.page.wait_for()
        # self.mini.page.scroll_to(200, 300)
        # time.sleep(10)

    def cmpark_modal(self):
        self.mini.page.get_element(str(self.city_select_button[0])).click()
        self.mini.app.wait_for_page('/pages/citySelect/index')
        self.mini.page.get_element('view.index-module__atIndexesListNameInner___20dLK', inner_text='东莞').click()
        self.mini.app.wait_for_page('/pages/home/index')
        before_called = threading.Semaphore(0)  # 监听回调, 阻塞当前主线程
        after_called = threading.Semaphore(0)  # 监听回调, 阻塞当前主线程
        callback_called = threading.Semaphore(0)  # 监听回调, 阻塞当前主线程
        before_args = None
        after_args = None
        callback_args = None

        def before(args):
            nonlocal before_args
            before_called.release()
            before_args = args

        def after(args):
            nonlocal after_args
            after_called.release()
            after_args = args

        def callback(args):
            nonlocal callback_args
            callback_called.release()
            callback_args = args

        self.mini.app.hook_wx_method("showModal", before=before, after=after, callback=callback)
        # time.sleep(2)
        self.mini.page.wait_for('view.index-module__name___oj2aW')
        self.mini.page.get_element('view.index-module__name___oj2aW', inner_text="招商央畔").click()
        time.sleep(2)
        self.mini.native.handle_action_sheet("允许")
        time.sleep(5)
        # is_called = callback_called.acquire(timeout=10)
        self.mini.app.release_hook_wx_method("showModal")
        # self.mini.assertTrue(is_called, "callback called")
