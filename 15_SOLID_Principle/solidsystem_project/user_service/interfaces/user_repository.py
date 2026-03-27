from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def find(self, user_id):
        pass
