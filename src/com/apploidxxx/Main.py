from com.apploidxxx.pixiv.pixiv import Pixiv
from com.apploidxxx.vk.handler.vk_default_pixiv_request_handler import DefaultPixivRequestHandler
from com.apploidxxx.vk.vk_client import VkClient


def main():
    pixiv_api = Pixiv()
    vk_client = VkClient(DefaultPixivRequestHandler(pixiv_api))

    print("-> Started")
    vk_client.run()


if __name__ == '__main__':
    print("Starting...")
    main()
