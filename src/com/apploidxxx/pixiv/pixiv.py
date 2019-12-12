#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.apploidxxx.config import PIXIV_USERNAME as P_USERNAME, PIXIV_PASSWORD as P_PASSWORD

from com.apploidxxx.pixiv import illustration
from pixivpy3 import *


class Pixiv:

    api = None

    def __init__(self):
        sni = False
        if not sni:
            self.api = AppPixivAPI()
        else:
            self.api = ByPassSniApi()
            self.api.require_appapi_hosts()

        self.api.login(P_USERNAME, P_PASSWORD)

    def get_recommends(self, count: int = 1) -> [illustration.Illustration]:
        json_result = self.api.illust_recommended()
        illustrations = []
        for idx, illust in enumerate(json_result.illusts[:count]):
            # image_url = illust.meta_single_page.get('original_image_url', illust.image_urls.large)
            image_url = illust['image_urls']['large']
            illustrations.append(
                illustration.Illustration(
                    illust['title'],
                    illust['user']['name'],
                    image_url,
                    f"https://www.pixiv.net/member.php?id={illust['user']['id']}"))

        return illustrations

