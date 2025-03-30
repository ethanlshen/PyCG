#
# Copyright (c) 2020 Vitalis Salis.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from .base import BaseFormatter

class Simple(BaseFormatter):
    def __init__(self, cg_generator):
        self.cg_generator = cg_generator

    def generate(self):
        # Get the extended call graph that includes line numbers
        extended_cg = self.cg_generator.cg.get_extended()
        output_cg = {}
        
        # Process the extended call graph to include line numbers
        for src_node, data in extended_cg.items():
            output_cg[src_node] = []
            for dst_info in data['dsts']:
                # Include destination with line number
                output_cg[src_node].append({
                    "dst": dst_info["dst"],
                    "lineno": dst_info["lineno"],
                    "mod": dst_info["mod"]
                })
                
        return output_cg
