from case.base.basepage import BasePage
from case.base import route


class CitySelectPage(BasePage):
    locators = {
        "current_city": "text.index-module__selectedCity___kmXXG",

    }
    peking_city = ("view.index-module__atIndexesListNameInner___20dLK", "北京")

    """
        校验页面路径
        """

    def check_cityselectpage_path(self):
        self.mini.assertEqual(self.current_path(), route.citySelectpage_route)

    """
    校验当前城市
    """

    def check_current_city(self):
        self.mini.assertEqual(self.mini.page.get_element(CitySelectPage.locators['current_city']), '深圳市')

    """
    切换北京
    """

    def peking_city_click(self):
        self.mini.page.get_element(CitySelectPage.peking_city[0], inner_text=CitySelectPage.peking_city[1]).click()

    """
    检查城市列表是否显示，只需检查某一城市元素是否出现即可
    """

    def peking_city_exists(self):
        self.mini.assertEqual(True, self.mini.page.element_ie_exists(CitySelectPage.peking_city[0],
                                                                     inner_text=CitySelectPage.peking_city[1],
                                                                     max_timeout=5))
    """
    选择定位城市
    """
    def location_city_click(self):
        self.mini.page.get_element(CitySelectPage.locators['current_city']).click()
