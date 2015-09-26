from requests import Session
from oauth2client.client import OAuth2WebServerFlow
import simplejson as json

session = Session()

auth_response = session.post(
    url='http://api-qa.jihub.com:80/oauth/token',
    data={
        'client_id': 'eE0MRGsAnNsjy0ZQ83Kz8S6xM1oYIGcW3RBwJdbcIBgAUaIe6jnSc+h41j8dc1LX.dist',
        'client_secret': 'xqUAQbAc/H0OiqVMEYSne+2QxabFUGRW2l94lAg0hujaCb5Kx40YYqzeRa8jKSr6.dist',
        'grant_type': 'client_credentials',
        'scope': 'board.read'
    },
)

auth_json = json.loads(auth_response.text)
companies_reponse = session.get(
    url='http://api-qa.jihub.com:80/v1/positions',
    data={
        'access_token': auth_json['access_token'],
        'page': 1,
        'per_page': 10,
    }
)

print companies_reponse.text


