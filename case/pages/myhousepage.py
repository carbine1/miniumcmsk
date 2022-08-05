from case.base.basepage import BasePage
from case.base import route


class MyHousePage(BasePage):
    locators = {
        "HOUSE_CHECKIN": "view.index-module__checkInfo___1nd2x",
        "HOUSE_LIST": "view.index-module__houseList___IOvmA",
        "MINE_BENEFIT": "view.index-module__benefits___2v3oM",
        "MINE_HOME": "view.index-module__container___3i8fz.index-module__container___RtJpO",
        "MINE_HOTLINE": "view.index-module__menu___2MIUN",
        "MINE_ORDER": "text.index-module__title___BYafr"

    }