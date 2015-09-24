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
    },
)

auth_json = json.load(auth_response.text)
import pdb;pdb.set_trace()
#companies_reponse = session.post(
#    url='https://api.jiheup.com/v1/companies',
#    data={
#        'access_token': auth_response.text["access_token"],
#        'page': 1,
#        'per_page': 10,
#    }
#)
#
#print companies_response.text
