#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 1999-2018 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from mars.tensor.expressions.datasource import ones
from mars.tests.core import calc_shape


class Test(unittest.TestCase):
    def testReshape(self):
        a = ones((10, 20, 30), chunk_size=5)
        b = a.reshape(10, 600)

        b.tiles()

        self.assertEqual(calc_shape(b), b.shape)
        self.assertEqual(calc_shape(b.chunks[0]), b.chunks[0].shape)
        self.assertEqual(tuple(sum(s) for s in b.nsplits), (10, 600))

        a = ones((10, 600), chunk_size=5)
        b = a.reshape(10, 30, 20)

        b.tiles()

        self.assertEqual(calc_shape(b), b.shape)
        self.assertEqual(calc_shape(b.chunks[0]), b.chunks[0].shape)
        self.assertEqual(tuple(sum(s) for s in b.nsplits), (10, 30, 20))

        a = ones((10, 600), chunk_size=5)
        a.shape = [10, 30, 20]

        a.tiles()

        self.assertEqual(calc_shape(b), b.shape)
        self.assertEqual(calc_shape(b.chunks[0]), b.chunks[0].shape)
        self.assertEqual(tuple(sum(s) for s in a.nsplits), (10, 30, 20))
