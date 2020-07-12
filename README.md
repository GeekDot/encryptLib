<h2 align= center> encrypLib 常用加密算法库 </h2>

<h5 align=right> 极客点儿 </h5>
<p align=right> 2019-09-11 </p>

### 一、概述

`encrypLib` 是常用加密算法库，依赖 `hashlib`、`base64` 库，`encrypLib` 是对常用加密算法库进行二次封装，使用更加方便简洁，只用一行就可以解决绝大部分的问题，不需要考虑编码、格式、类型等无关问题

下面是对 `encrypLib` 的详解，如想快速使用，请移步 `demo.py` 模块，里面有 `encrypLib` 的使用 `demo`

### 二、安装

`encrypLib` 是以源码的方式呈现，使用的时候直接导入即可

	from encrypLib import dt
    
### 三、使用

`encrypLib` 所有的功能都是 `ep` 的方法，它们的返回值都是 `string` 类型，`encrypLib` 包括 `7` 类功能

#### 1. `md5`

    ep.md5('Hello World')

#### 2. `sha1`

    ep.sha1('Hello World')

#### 3. `sha224`

    ep.sha224('Hello World')

#### 4. `sha256`

    ep.sha256('Hello World')

#### 5. `sha384`

    ep.sha384('Hello World')

#### 6. `sha512`

    ep.sha512('Hello World')

#### 7. `base64`

    ep.base64('Hello World')
