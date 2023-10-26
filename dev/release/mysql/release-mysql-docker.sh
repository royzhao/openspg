#!/usr/bin/env bash

#
# Copyright 2023 Ant Group CO., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
#

docker buildx build -f Dockerfile --platform linux/arm64/v8,linux/amd64 --push -t baifuyu/openspg-mysql:0.0.1-beta1 -t baifuyu/openspg-mysql:latest .

