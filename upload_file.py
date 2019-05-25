# Copyright 2018 The crowdcompute:crowdengine Authors
# This file is part of the crowdcompute:crowdengine library.
#
# The crowdcompute:crowdengine library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The crowdcompute:crowdengine library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with the crowdcompute:crowdengine library. If not, see <http://www.gnu.org/licenses/>.

import requests

CC_DEFAULT_UPLOAD_PORT = 8085

class UploadClient(object):
    def __init__(self, host='localhost', port=CC_DEFAULT_UPLOAD_PORT):
        self.url = 'http://{}:{}/upload'.format(host, port)

    def upload_file(self, file, token):
        extra_headers = {'Authorization': 'Bearer {0}'.format(token)}
        files = {'file': open(file, 'rb')}
        # with requests.Session() as s:
        #     s.headers.update(extra_headers)
        resp = requests.post(self.url, files=files,headers=extra_headers)
        return resp.text