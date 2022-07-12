from case.base.basepage import BasePage
from case.base import route
from main import minium_init


class MallPage(BasePage):

    locators = {
        "MALL_WEB": "web-view"
    }
    """
    H5页面,不适用minium自动化
    """
    # BasePage.navigate_to_open(BasePage,route.mallpage_route)
    # def __init__(self):
    #     self.navigate_to_open(route.mallpage_route)

    def go_mallpage(self):
        self.mini.app.switch_tab(route.mallpage_route)

    def check_mallpage_path(self):
        self.mini.assertEqual(self.current_path(), route.mallpage_route)



