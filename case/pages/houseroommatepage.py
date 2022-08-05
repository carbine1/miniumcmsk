import threading

from case.base.basepage import BasePage
from case.base import route


class HouseRoommatePage(BasePage):
    locators = {
        "HOUSEROOMATE_TITLE": "view.index-module__titleContain___1KXaD",
        "HOUSE_LIST": "view.index-module__container___ciAuV",
        "MINE_BENEFIT": "view.index-module__benefits___2v3oM",
        "MINE_HOME": "view.index-module__container___3i8fz.index-module__container___RtJpO",
        "MINE_HOTLINE": "view.index-module__menu___2MIUN",
        "MINE_ORDER": "text.index-module__title___BYafr"

    }
    select_house_button = ("text.index-module__label___2i5Wc", "选择房屋")
    city_company_button = ("view.list-module__item___Ke4Wv", "深圳公司")
    project_search_text_area = ("input.index-module__input___3SyUn", "深圳招商局广场")
    project_button = ("view.list-module__item___Ke4Wv", "深圳招商局广场")
    building_button = ("view.list-module__item___Ke4Wv", "招商局广场")
    unit_button = ("view.list-module__item___Ke4Wv", "/")
    room_button = ("view.list-module__item___Ke4Wv", "中集集团财务有限公司")
    owner_input_area = ("input.index-module__inputName___3pwMU", "朱婷")
    submit_button = ("view.index-module__submitBtn___jMxPJ", "下一步")
    not_commfirt_button = ("view.index-module__submitBtn___jMxPJ", "联系业主核实房屋")

    def check_roommate_page_path(self):
        self.mini.assertEqual(self.current_path(), route.roommatepage_route)

    def check_roommate_page_base_element(self):
        # 校验页面元素
        self.mini.assertTrue(self.mini.page.element_is_exists(HouseRoommatePage.locators['HOUSE_CHECKIN']))

    def add_housemate_apply(self):
        self.mini.page.get_element(str(self.select_house_button[0]),
                                   inner_text=str(self.select_house_button[1])).click()
        self.mini.page.get_element(str(self.city_company_button[0]),
                                   inner_text=str(self.city_company_button[1])).click()
        el = self.mini.page.get_element(str(self.project_search_text_area[0]))
        callback_args = None
        callback_called = threading.Semaphore(0)
        def callback(args):
            nonlocal callback_args
            callback_args = args
            callback_called.release()
            """
            hook 参数要对应bind**的值 如：
            <input id="username" bindinput="userNameInput" type="text"/>
            则 self.mini.hook_current_page_method("userNameInput", callback)

            """
        self.mini.hook_current_page_method("aaa", callback)
        el.input(str(self.project_search_text_area[1]))
        self.mini.page.get_element(str(self.project_button[0]),
                                   inner_text=str(self.project_button[1])).click()
        self.mini.page.get_element(str(self.building_button[0]),
                                   inner_text=str(self.building_button[1])).click()
        self.mini.page.get_element(str(self.unit_button[0]),
                                   inner_text=str(self.unit_button[1])).click()
        self.mini.page.get_element(str(self.room_button[0]),
                                   inner_text=str(self.room_button[1])).click()

