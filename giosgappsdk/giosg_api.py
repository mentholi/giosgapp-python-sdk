import requests


class GiosgApiMixin(object):
    URL_USERS = '/api/v3/customer/personnel'

    def build_request_url(self, base, page_size=25, page=1):
        domain = self.data.get('sub')
        return '%s://%s%s?page_size=%s&page=%s' % (self._protocol, domain, base, page_size, page)

    def get_users(self, page=1, page_size=25):
        return requests.get(self.build_request_url(self.URL_USERS, page_size, page), headers=self.get_auth_header())
