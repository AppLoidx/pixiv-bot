from com.apploidxxx.pixiv.pixiv import Pixiv
from com.apploidxxx.vk.handler.vk_request_handler import AbsRequestHandler
from com.apploidxxx.vk.vk_client import VkClient


class DefaultPixivRequestHandler(AbsRequestHandler):
    pixiv = None

    def __init__(self, pixiv_pi: Pixiv):
        self.pixiv = pixiv_pi

    def handle(self, message: str, user_id: int, vk: VkClient) -> None:
        if message == 'Случайное изображение':

            DefaultPixivRequestHandler._send_wait_a_second_message(user_id, vk)

            illustration = self.pixiv.get_recommends(1)[0]

            print(illustration.get_image_url())

            attachment = vk.prepare_photos_attachment([illustration.get_image_url()])

            message = f"title: {illustration.get_title()}\n" \
                      f"Artist name: {illustration.get_artist()}\n" \
                      f"Source: Pixiv\n" \
                      f"Artist Profile: {illustration.get_artist_url()}\n"

            vk.write_msg(user_id, message, attachment)
        elif message == 'несколько пожалуйста':

            DefaultPixivRequestHandler._send_wait_a_second_message(
                user_id, vk,
                "\nЧем больше картинок, тем больше времени уходит на их загрузку")

            illustrations = self.pixiv.get_recommends(10)
            urls = []
            for i in illustrations:
                urls.append(i.get_image_url())

            attachment = vk.prepare_photos_attachment(urls)

            message = "Source: Pixiv"

            vk.write_msg(user_id, message, attachment)

    @staticmethod
    def _send_wait_a_second_message(user_id: int, vk: VkClient, additional_text: str = ""):
        vk.write_msg(user_id, "Секундочку..." + additional_text)
