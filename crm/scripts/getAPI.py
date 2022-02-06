import requests
from amocrm.v2 import tokens


def getAPI(selection="leads"):
    tokens.default_token_manager(
        client_id="bfe9fcdb-88c5-4d99-95a5-9aa88529202f",
        client_secret="HRqmShlj1NygsuWGU9yoheBlZgnM6V2olsv9ZM9TpHn5aK18mzZk9jieteYEoFQT",
        subdomain="aleeexgerttt",
        redirect_url="https://example.com",
        storage=tokens.FileTokensStorage(),
    )
    tokens.default_token_manager.init(
        code="def50200b13854cc2364320bc9335f5e3b91ae99578207cc2b8b32a5e769c077a5ef64bd1976b3f9649b48a181e27f668d441001582cb6bc9596b8fbcb4408a333358ae0b790c1e1363aa0182a3ed03de5e8173256e8a53f12c7c226d5e306850e8aabe82324485ed283eb27beb749994d3750f2ed9aa8252e0058c6f90af5dcef550e4dd6fcb888720e75e67f737dd5c263c15fb239b8e579267f84003356bd0d72b18da6e0e9a667a57ea1297e44ca16b47fa1fd8ae5e4ec862446d6166d4b517e65b0a39ef0459c9d13be15b2da4f0245e458089f4a2d0f3f25ab30fa374e27407c981e755a5d56020c364d899eb4c541a3ae2e8a00ac956586adee63dba3c37fbb35a6749ffe9a6918d4c1d6242dec22602af12a82fa3d415f0058c0f07f607a47248e0b3329f4e750c70f15c6a3aa516f73ccf85d9d86445d971fdef0fe218ac3c6733a81ee4d824028c41da4c1a4eadd112840d3261f7f6ec6cd1ebab136067c9687159e3f500ad9224f2c9fe52f810e60563bc0e5104a3b09200b94aa88f8934c1c2bc55bf2a3c78258a1fd0efb3f95b64e3bc32e0f022893e1edb151fb6fc63165baf205f20b22d7f8fa59fe91599f9896209505b25eb3905e",
        skip_error=True)

    token = tokens.default_token_manager.get_access_token()
    link = 'https://aleeexgerttt.amocrm.ru'

    headers = {
        'Authorization': 'Bearer ' + token
    }

    res_leads = requests.get(link + f"/api/v4/{selection}", headers=headers)

    return res_leads
