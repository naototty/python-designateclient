# Copyright 2012 Managed I.T.
#
# Author: Kiall Mac Innes <kiall@managedit.ie>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from monikerclient.v1 import domains
from monikerclient.v1 import records
from monikerclient.v1 import servers


class Client(object):
    """ Client for the Moniker v1 API """

    def __init__(self):
        self.domains = domains.Controller()
        self.records = records.Controller()
        self.servers = servers.Controller()