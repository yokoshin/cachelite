# -*- coding: utf-8 -*-
import os
import unittest
from pathlib import Path
from tempfile import gettempdir
from unittest import TestCase

import shutil

from cachelite import CacheLite


class TestCacheLite(TestCase):

    def setUp(self):
        self._temp_dir = gettempdir() + os.sep + "cache_lite_test"
        self._cachelite = CacheLite(dir=self._temp_dir)

    def tearDown(self):
        self._cachelite.clear()
        self._cachelite = None
        delattr(self, "_cachelite")
        if Path(self._temp_dir).exists():
            shutil.rmtree(self._temp_dir)

    def test_getitem(self):
        self._cachelite["abc"] = "def"
        self.assertEqual("def", self._cachelite["abc"])

        with self.assertRaises(KeyError):
            xyz = self._cachelite["xyz"]

    def test_setitem(self):
        self._cachelite["abc"] = "def"
        self.assertEqual("def", self._cachelite["abc"])

        self._cachelite["abc"] = "xyz"
        self.assertEqual("xyz", self._cachelite["abc"])

    def test_len(self):
        self._cachelite["abc"] = "def"
        self.assertEqual(1, len(self._cachelite))

        self._cachelite["hij"] = "lmn"
        self.assertEqual(2, len(self._cachelite))

        self._cachelite["hij"] = 3
        self.assertEqual(2, len(self._cachelite))

        self._cachelite["opq"] = 15
        self.assertEqual(3, len(self._cachelite))

        del self._cachelite["abc"]
        self.assertEqual(2, len(self._cachelite))

        del self._cachelite["hij"]
        self.assertEqual(len(self._cachelite), 1)

        self._cachelite["xyz"] = "def"
        self.assertEqual(2, len(self._cachelite))

        self._cachelite.clear()
        self.assertEqual(0, len(self._cachelite))

        with self.assertRaises(KeyError):
            xyz = self._cachelite["abc"]

        with self.assertRaises(KeyError):
            xyz = self._cachelite["xyz"]

    def test_iterator(self):
        self._cachelite["abc"] = "def"
        it = self._cachelite.__iter__()
        self.assertEqual("abc", next(it))

        self._cachelite["opq"] = "stu"
        it = self._cachelite.__iter__()
        value1 = next(it)
        value2 = next(it)
        self.assertEqual(set(["abc", "opq"]), set([value1, value2]))

        with self.assertRaises(StopIteration):
            next(it)

    def test_keys(self):
        self._cachelite["abc"] = "def"
        self._cachelite["opq"] = "stu"

        keys = list(self._cachelite.keys())
        self.assertEqual(set(["abc", "opq"]), set([keys[0], keys[1]]))

    def test_values(self):
        self._cachelite["abc"] = "def"
        self._cachelite["opq"] = "stu"

        keys = list(self._cachelite.values())
        self.assertEqual(set(["def", "stu"]), set([keys[0], keys[1]]))


if __name__ == '__main__':
    unittest.main()
