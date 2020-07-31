#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from encryptLib import et

print('md5 ==>', et.md5('Hello World'))
print('sha1 ==>', et.sha1('Hello World'))
print('sha224 ==>', et.sha224('Hello World'))
print('sha224 ==>', et.sha224('Hello World'))
print('sha224 ==>', et.sha224('Hello World'))
print('sha224 ==>', et.sha224('Hello World'))
print('sha224 ==>', et.sha224('Hello World'))

password = '123456'

salt = et.generate_salt()
print('bcrypt生成盐值 ==>', salt)

salt = et.md5('username + phone + timestamp')
print('自定义盐值 ==>', salt)

pw_hash = et.generate_password_hash(password, salt)
print('bcrypt加密 ==>', pw_hash)

pw_check = et.check_password_hash(password, salt, pw_hash)
print('bcrypt校验 ==>', pw_check)
