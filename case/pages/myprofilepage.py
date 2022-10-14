import time

from case.base.basepage import BasePage
from case.base import route


class MyProfilePage(BasePage):
    locators = {
        "MINE_AVATAR": "image.index-module__avatarImg___2N6Qf",
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

    def check_myprofile_page_path(self):
        # self.mini.app.switch_tab(route.minepage_route)
        self.mini.page.wait_for(MyProfilePage.locators['MINE_HOTLINE'])
        self.mini.assertEqual(self.current_path(), route.myProfile_route)

    """
        校验页面的基本元素
    """

    def check_mine_page_base_element(self):
        pass