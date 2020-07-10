#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from encrypLib import ep


print(ep.md5('Hello World'))
print(ep.sha1('Hello World'))
print(ep.sha224('Hello World'))
print(ep.sha256('Hello World'))
print(ep.sha384('Hello World'))
print(ep.sha512('Hello World'))
print(ep.base64('Hello World'))
