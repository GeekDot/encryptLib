<h2 align= center> encrypLib 常用加密算法库 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2019-09-11 </p>

### 一、概述

`encryptLib` 是常用加密算法库，依赖 `hashlib`、`base64` 库，`encryptLib` 是对常用加密算法库进行二次封装，使用更加方便简洁，只用一行就可以解决`99%`的问题，不需要考虑编码、格式、类型等无关问题。

下面是对 `encryptLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `encryptLib` 的使用 `demo`。

### 二、安装

`encryptLib` 是以源码的方式呈现，使用的时候直接导入即可。

	from encryptLib import et
    
### 三、使用

`encryptLib` 所有的功能都是 `et` 的方法，它们的返回值都是 `string` 类型，`encryptLib` 包括 `10` 类功能。

#### 1. `md5`

    et.md5('Hello World')

#### 2. `sha1`

    et.sha1('Hello World')

#### 3. `sha224`

    et.sha224('Hello World')

#### 4. `sha256`

    et.sha256('Hello World')

#### 5. `sha384`

    et.sha384('Hello World')

#### 6. `sha512`

    et.sha512('Hello World')

#### 7. `base64`

    et.base64('Hello World')
    
#### 8. `bcrypt`生成盐值
    
    salt = et.generate_salt()

#### 9. `bcrypt`加密

	password = '123456'
	salt = et.md5('username + phone + timestamp')

	pw_hash = et.generate_password_hash(password, salt)
	
`generate_password_hash` 有三个参数

- `password`： 密码，必须参数

- `salt`： 盐值，必须参数

- `rounds`： 成本因子，默认是 8，可以修改大小，一般默认，非必须参数

#### 10. `bcrypt`校验

	pw_check = et.check_password_hash(password, salt, pw_hash)

`check_password_hash ` 有三个参数

- `password`： 密码，必须参数

- `salt`： 盐值，必须参数

- `pw_hash`：密文，必须参数