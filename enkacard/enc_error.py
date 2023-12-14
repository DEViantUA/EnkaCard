# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
class EnkaNetworkCardError(BaseException):
    def __init__(self, code, message):
        super().__init__(f"[{code}] {message}")
        self.code = code
        self.message = message

class ENCardError(EnkaNetworkCardError):
    pass