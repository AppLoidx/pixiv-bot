import random
from threading import Thread

import requests
import vk_api
from com.apploidxxx.config import VK_API_KEY as API_KEY
from vk_api.longpoll import VkLongPoll, VkEventType

from com.apploidxxx.vk.handler.vk_request_handler import AbsRequestHandler


class VkClient:

    handler = None
    session = None
    longpoll = None
    upload = None

    def __init__(self, handler: AbsRequestHandler):
        self.handler = handler
        self.vk = vk_api.VkApi(token=API_KEY)
        self.session = requests.Session()
        self.longpoll = VkLongPoll(self.vk)
        self.upload = vk_api.VkUpload(self.vk)

    def write_msg(self, user_id: int, message: str, photos=None) -> None:

        if photos is None:
            photos = []
        _attachments = photos

        attachment = ','.join(_attachments)

        self.vk.method('messages.send', {
            'message': message,
            'user_id': user_id,
            'random_id': random.randint(1, 1000),
            'attachment': attachment})

    def prepare_photos_attachment(self, photos: [str]) -> [str]:
        _attachments = []
        for _photo_url in photos:
            _photo = self.upload.photo_messages(
                photos=self.session.get(
                    _photo_url,
                    headers={'Referer': 'https://app-api.pixiv.net/'},
                    stream=True).raw)

            _photo_url = 'photo{}_{}'.format(_photo[0]['owner_id'], _photo[0]['id'])
            _attachments.append(_photo_url)
        return _attachments

    def get_handle_thread(self, user_input: str, user_id, vk_client) -> Thread:
        return HandleThread(
            "handle-thread-" + str(random.randint(1, 1000)), self.handler,
            user_input, user_id, vk_client)

    def run(self):
        for event in self.longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW:

                if event.to_me:
                    self.get_handle_thread(event.text, event.user_id, self).start()


class HandleThread(Thread):
    _name = None
    _handler = None
    _input = None
    _user_id = 0
    _vk_client = None

    def __init__(self, name: str, handler: AbsRequestHandler, user_input: str, user_id, vk_client):
        Thread.__init__(self)
        self._name = name
        self._handler = handler
        self._input = user_input
        self._user_id = user_id
        self._vk_client = vk_client

    def run(self):
        self._handler.handle(self._input, self._user_id, self._vk_client)
