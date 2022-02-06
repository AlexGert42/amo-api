import requests
from amocrm.v2 import tokens


def getAPI(currentIntegration, selection):

    tokens.default_token_manager(
        client_id=currentIntegration['key_client_id'],
        client_secret=currentIntegration['key_client_secret'],
        subdomain=currentIntegration['key_subdomain'],
        redirect_url=currentIntegration['key_redirect_url'],
        storage=tokens.FileTokensStorage(),
    )
    tokens.default_token_manager.init(
        code=currentIntegration['key_code'],
        skip_error=True
    )

    token = tokens.default_token_manager.get_access_token()
    link = currentIntegration['key_link']

    headers = {
        'Authorization': 'Bearer ' + token
    }

    res_leads = requests.get(link + f"/api/v4/{selection}", headers=headers)

    return res_leads
