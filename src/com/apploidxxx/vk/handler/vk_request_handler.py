from abc import ABC, abstractmethod


class AbsRequestHandler(ABC):

    @abstractmethod
    def handle(self, message: str, user_id: int, vk) -> None:
        """
        Handle received message text

        :param message: text of message from VK
        :param user_id: id of user which sent this message
        :param vk: Object for VK management. See: com.apploidxxx.vk.vk_client.VkClient
        :return: None
        """

        pass
