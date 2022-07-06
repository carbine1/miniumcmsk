from case.base.basepage import BasePage
from case.base import route


class MallPage(BasePage):
    locators = {
        "MALL_WEB": "web-view"
    }
    """
    H5页面,不适用minium自动化
    """
    def check_mallpage_path(self):
        self.mini.assertEqual(self.current_path(), route.mallpage_route)
