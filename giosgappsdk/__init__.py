import jwt
import urlparse

from .giosg_api import GiosgApiMixin


class GiosgAppSDK(GiosgApiMixin):
    REQUEST_TYPE_CHAT_START = 'chat_start'
    REQUEST_TYPE_CHAT_END = 'chat_end'
    REQUEST_TYPE_CONSOLE_LOAD = 'console_load'
    REQUEST_TYPE_MANUAL_DIALOG = 'manual_dialog'
    REQUEST_TYPE_MANUAL_NAV = 'manual_nav'

    def __init__(self, url_or_req=None, app_secret=None):
        if not url_or_req:
            raise ValueError('%s requires either full request url with "token" and "data" query parameters or django request object.' % self.__class__.__name__)

        self._protocol = 'http'
        self._secret = app_secret
        self.url = self.get_url(url_or_req)

        self._access_token = self.get_token_from_url(self.url)
        self._data_token = self.get_data_from_url(self.url)

        print self._access_token
        print self._data_token
        self.data = {}
        if self._data_token and self._access_token:
            self.data = self.get_data(self._data_token)

    @property
    def is_app_request(self):
        keys = self.data.keys()
        return (keys > 0 and self.request_type is not None)

    @property
    def request_type(self):
        req_type = self._get_params_from_url(self.url).get('type')
        return req_type[0] if req_type else None

    @property
    def chat_id(self):
        return self.data.get('chat_id')

    @property
    def organization_id(self):
        return self.data.get('org_id')

    @property
    def user_id(self):
        return self.data.get('user_id')

    @property
    def visitor_id(self):
        return self.data.get('visitor_id')

    @property
    def app_instance_id(self):
        return self.data.get('inst_id')

    @property
    def app_id(self):
        return self.data.get('app_id')

    def get_url(self, url_or_req):
        if isinstance(url_or_req, basestring):
            return url_or_req
        else:
            return self.get_url_from_request(url_or_req)

    def get_url_from_request(self, request):
        if hasattr(request, 'get_full_path'):
            return request.get_full_path()
        elif hasattr(request, 'url'):
            return request.url
        else:
            raise ValueError("%s was initialized with request object but it doesn't seem to be django or flask request!" % self.__class__.__name__)

    def _get_params_from_url(self, url):
        parsed = urlparse.urlparse(url)
        return urlparse.parse_qs(parsed.query)

    def get_token_from_url(self, url):
        token = self._get_params_from_url(url).get('token')
        return token[0] if token else None

    def get_data_from_url(self, url):
        data = self._get_params_from_url(url).get('data')
        return data[0] if data else None

    def get_data(self, jwt_str):
        return jwt.decode(jwt_str, self._secret, verify=True)

    def get_auth_header(self):
        return {'Authorization': 'GIOSGAPP %s %s' % (self._access_token, self._secret)}
