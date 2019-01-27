#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostIntegerConan(base.BoostBaseConan):
    name = "boost_integer"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_integer"
    lib_short_names = ["integer"]
    header_only_libs = ["integer"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_static_assert"
    ]
