import requests
from amocrm.v2 import tokens


def testApi(selection):
    tokens.default_token_manager(
        client_id="23cc3e92-8bf2-40aa-bc4f-1e2f318260d6",
        client_secret="dA0XjmwWyDfAoEAtxsfw1gG0einV5hWi1hOtUUmA0mruazu3n93KGareTZynlYuR",
        subdomain="aleeexgerttt",
        redirect_url="https://amoapibi.herokuapp.com",
        storage=tokens.FileTokensStorage(),
    )
    tokens.default_token_manager.init(
        code="def50200f27c01a9ce819d2383ad42808f3f128e6f0388b02b5a4176f8f0223239cbd4a5f91bfadfb54bdacc666475c857c2b805a35cdc35df7e7e5aae86454840e39135570a911adef95319982f3a3f1ba7df5959e6809aedfb3ba727f465f5df623e60a6141f739c812a32263dad1d625b22570467a36be3a0dc9bbe30c32bf8b2983719ae07de6b32d6da6b273355af1eb4c7bfd6bf8eacfaf8a74a25c7baca2cf4e3c2da1eb83b2572c6b518f64f365ed271be42a4967f21d61e32e9e7a722a000200d0cff4d7de638db300f0f1c3004d70d92d1d675c0a89f628b6971a0fd253c18961d5f3f63ea117c791ea8c8a9a12f1394274261bd7cc686110599a2892fa6eabe869ad73000d7ff253d6827b214ea27f5dcd1be1303b0c283f8cbf12a506c2d840501631e7b88d80c613376af938a44a0acee482592572debcf77e2b78c5ae2f8edde042be06a86f22efd9201fe0809ceceb82c3197a9b41090af111b8bfdd9914a2e9aa5ab5ad409df26b08c9a6c4e47eee2dbffbd6388ede11c93717c84fd1020c185317ad8ddbd094b15738c33fb55c8f70787a928c29c66eadd3a41de05775fd690c3fce2fdf477ecb37ee023b991185b4effc62cf19914229254a726e6acc8352f",
        skip_error=True
    )

    token = tokens.default_token_manager.get_access_token()
    link = "https://aleeexgerttt.amocrm.ru"

    headers = {
        'Authorization': 'Bearer ' + token
    }

    res = requests.get(link + f"/api/v4/{selection}", headers=headers)

    return res