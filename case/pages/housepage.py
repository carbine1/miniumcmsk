from case.base.basepage import BasePage
from case.base import route


class HousePage(BasePage):
    locators = {
        "HOUSE_CITY": "view.index-module__city___3SF-H",
        "HOUSE_PROJECTLIST": "view.index-module__item___3bBn1"
    }

    """
    校验页面路径
    """
    def check_housepage_path(self):
        self.mini.assertEqual(self.current_path(), route.housepage_route)

    """
    校验页面的基本元素
    """
    def check_housepage_base_element(self):
        # 校验页面城市元素
        self.mini.assertTrue(self.mini.page.element_is_exists(HousePage.locators['HOUSE_CITY']))
        # 校验页面项目列表
        self.mini.assertTrue(self.mini.page.element_is_exists(HousePage.locators['HOUSE_PROJECTLIST']))

    """
    点击项目呼起弹窗
    """
    def get_project_element(self):
        self.mini.page.get_elements(HousePage.locators['HOUSE_PROJECTLIST'])[1].click()
        self.mini.native.handle_modal("允许")
