from abc import ABC, abstractmethod

import argon2


class BasePasswordHandler(ABC):
    @abstractmethod
    def encode(self, row_password):
        pass

    @abstractmethod
    def verify(self, row_password, crypto_password):
        pass


class Argon2Handler(BasePasswordHandler):
    def __init__(self):
        self.ph = argon2.PasswordHasher()

    def encode(self, row_password):
        return self.ph.hash(row_password)

    def verify(self, row_password, crypto_password):
        try:
            return self.ph.verify(crypto_password, row_password)
        except argon2.exceptions.VerifyMismatchError:
            return False
