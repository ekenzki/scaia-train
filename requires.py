#!/usr/bin/python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import Endpoint
from charms.reactive import when, when_not
from charms.reactive import set_flag, clear_flag
from charms.reactive import data_changed


class ScaniaTrainigClient(Endpoint):

    @when('endpoint.{endpoint_name}.changed.ready')
    def new_signal(self):
        set_flag(self.expand_name('endpoint.{endpoint_name}.new-signal'))
        clear_flag(self.expand_name('endpoint.{endpoint_name}.changed.ready'))

    @when_not('endpoint.{endpoint_name}.joined')
    def broken(self):
        clear_flag(self.expand_name('endpoint.{endpoint_name}.new-signal'))


    def are_backends_ready(self):
        for relation in self.relations:
            for unit in relation.units:
                ready = unit.received['ready']
                if ready != "true":
                    return False
        return True
