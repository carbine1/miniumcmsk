from case.base.basepage import BasePage
from case.base import route


class MinePage(BasePage):
    locators = {
        "MINE_AVATAR": "view.index-module__avatar___1FurM",
        "MINE_MEMBERCARD": "view.index-module__swiperContainer___2gAgK",
        "MINE_BENEFIT": "view.index-module__benefits___2v3oM",
        "MINE_HOME": "view.index-module__container___3i8fz.index-module__container___RtJpO",
        "MINE_HOTLINE": "view.index-module__menu___2MIUN",
        "MINE_ORDER": "text.index-module__title___BYafr"

    }
    point_button = ("text", "签到领积分")
    """
        校验页面路径
        """

    def check_mine_page_path(self):
        self.mini.assertEqual(self.current_path(), route.minepage_route)

    """
        校验页面的基本元素
    """

    def check_mine_page_base_element(self):
        # 校验页面会员信息元素
        self.mini.assertTrue(self.mini.page.element_is_exists(MinePage.locators['MINE_AVATAR']))
        # 校验页面会员卡元素
        self.mini.assertTrue(self.mini.page.element_is_exists(MinePage.locators['MINE_MEMBERCARD']))
        # 校验页面MINE_BENEFIT元素
        self.mini.assertTrue(self.mini.page.element_is_exists(MinePage.locators['MINE_BENEFIT']))
        # 校验页面MINE_HOME元素
        self.mini.assertTrue(self.mini.page.element_is_exists(MinePage.locators['MINE_HOME']))
        # 校验页面MINE_HOTLINE元素
        self.mini.assertTrue(self.mini.page.element_is_exists(MinePage.locators['MINE_HOTLINE']))
        # 校验页面MINE_ORDER元素
        self.mini.assertTrue(self.mini.page.element_is_exists(MinePage.locators['MINE_ORDER']))

    def click_my_profile_element(self):
        self.mini.page.get_element(MinePage.locators['MINE_AVATAR']).click()
        # 检查跳转后页面路径
        self.mini.assertEqual(self.current_path(), route.myProfile_route)
