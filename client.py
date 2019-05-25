# Copyright 2019 The crowdcompute:crowdengine Authors
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

from jsonrpcclient.clients.http_client import HTTPClient
import json

CC_DEFAULT_RPC_PORT = 8085


class Client(object):
    def __init__(self, host='localhost', port=CC_DEFAULT_RPC_PORT, version="2.0", tls=False):
        self.version = version
        self.host = host
        self.port = port
        self.tls = tls
        scheme = 'http'
        if self.tls:
            scheme += 's'
        url = '{}://{}:{}'.format(scheme, self.host, self.port)
        self.http_client = HTTPClient(url)
    
    def _call(self, method, parameters, id=1):
        payload = {
            "method": method,
            "params": parameters,
            "jsonrpc": self.version,
            "id": id,
        }
        response = self.http_client.send(json.dumps(payload))
        return response.data.result

    # ACCOUNTS
    def create_account(self, passphrase):
        if not isinstance(passphrase, str):
            raise TypeError('Parameter "passphrase" must be a string')
        return self._call("accounts_createAccount", [passphrase])

    def unlock_account(self, acc, passphrase):
        if not isinstance(acc, str):
            raise TypeError('Parameter "acc" must be a string')
        if not isinstance(passphrase, str):
            raise TypeError('Parameter "passphrase" must be a string')
        return self._call("accounts_unlockAccount", [acc, passphrase])


    def lock_account(self, account, token):
        self.http_client.session.headers.update({"Authorization": "Bearer " + token})
        if not isinstance(account, str):
            raise TypeError('Parameter "account" must be a string')
        if not isinstance(token, str):
            raise TypeError('Parameter "token" must be a string')
        return self._call("accounts_lockAccount", [account])

    def delete_account(self, acc, passphrase):
        if not isinstance(acc, str):
            raise TypeError('Parameter "acc" must be a string')
        if not isinstance(passphrase, str):
            raise TypeError('Parameter "passphrase" must be a string')
        return self._call("accounts_deleteAccount", [acc, passphrase])

    def list_accounts(self):
        return self._call("accounts_listAccounts", [])

    # BOOTNODES
    def get_bootnodes(self):
        return self._call("bootnodes_getBootnodes", [])

    def set_bootnodes(self, nodes):
        if not isinstance(nodes, list):
            raise TypeError('Parameter "nodes" must be given in a list form')
        return self._call("bootnodes_setBootnodes", [nodes])

    # SWARM SERVICE
    def run_swarm_service(self, service, nodes):
        if not isinstance(nodes, list):
            raise TypeError('Parameter "nodes" must be given in a list form')
        if not isinstance(service, dict):
            raise TypeError('Parameter "service" must be a dictionary')
        return self._call("service_run", [json.dumps(service), nodes])


    def leave_swarm_service(self, nodes):
        if not isinstance(nodes, list):
            raise TypeError('Parameter "nodes" must be given in a list form')
        return self._call("service_leave", [nodes])

    def leave_swarm_service(self, serviceName):
        if not isinstance(serviceName, str):
            raise TypeError('Parameter "serviceName" must be given in a string form')
        return self._call("service_removeService", serviceName)

     # DISCOVER NODES
    def discover_nodes(self, num):
        if not isinstance(num, int):
            raise TypeError('Parameter "num" must a positive integer')
        return self._call("discovery_discover", [num])


    # DOCKER IMAGE MANAGER
    def load_image_to_node(self, node_id, image_hash, token):
        self.http_client.session.headers.update({"Authorization": "Bearer " + token})
        if not isinstance(node_id, str):
            raise TypeError('Parameter "node_id" must be a string')
        if not isinstance(image_hash, str):
            raise TypeError('Parameter "image_hash" must be a string')
        return self._call("imagemanager_pushImage", [node_id, image_hash])

    def execute_image(self, node_id, dock_image_id):
        if not isinstance(node_id, str):
            raise TypeError('Parameter "node_id" must be a string')
        if not isinstance(dock_image_id, str):
            raise TypeError('Parameter "dock_image_id" must be a string')
        return self._call("imagemanager_runImage", [node_id, dock_image_id])

    def inspect_container(self, node_id, dock_cont_id):
        if not isinstance(node_id, str):
            raise TypeError('Parameter "node_id" must be a string')
        if not isinstance(dock_cont_id, str):
            raise TypeError('Parameter "dock_cont_id" must be a string')
        return self._call("imagemanager_inspectContainer", [node_id, dock_cont_id])

    def list_node_images(self, node_id, token):
        self.http_client.session.headers.update({"Authorization": "Bearer " + token})
        if not isinstance(node_id, str):
            raise TypeError('Parameter "node_id" must be a string')
        return self._call("imagemanager_listImages", [node_id])

    def list_node_containers(self, node_id, token):
        self.http_client.session.headers.update({"Authorization": "Bearer " + token})
        if not isinstance(node_id, str):
            raise TypeError('Parameter "node_id" must be a string')
        return self._call("imagemanager_listContainers", [node_id])

    # LEVEL DB
    def lvldb_stats(self):
        return self._call("lvldb_getDBStats", [])

    def lvldb_select_image(self, image_id):
        if not isinstance(image_id, str):
            raise TypeError('Parameter "image_id" must be a string')
        return self._call("lvldb_selectImage", [image_id])

    def lvldb_select_image_account(self, image_hash):
        if not isinstance(image_hash, str):
            raise TypeError('Parameter "image_id" must be a string')
        return self._call("lvldb_selectImageAccount", [image_hash])

    def lvldb_select_type(self, typeName):
        if not isinstance(typeName, str):
            raise TypeError('Parameter "typeName" must be a string')
        return self._call("lvldb_selectType", [typeName])

    def lvldb_select_all(self):
        return self._call("lvldb_selectAll", [])