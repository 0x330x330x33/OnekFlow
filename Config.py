#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 20:49:47
# 描述: todo ...



G_SQL_URL = "http://localhost:81/?id="
G_SQL_KEYWORD = "036d8f414f8340"
G_TMP_DIR = "onek_tmp"
G_DEV_SIZE = 20
G_KEYWORDS = ['flag', 'key', 'password','pin','admin','shell','exec','system','login','hacker','pass','root','PRIVATE KEY','PUBLIC KEY']

G_REPORT_HEAD = f"""
# 数据流分析报告

[TOC]

## 简报

```
文件名： %s
过滤语句： %s
数据包数量: %d
```

"""

keyfile_signatures = {
    "zip": ["504b0506", "504b", "5040708","504b4c495445", 
            "504b4c4f434b", "504b537058", "504b1200", "504b0102",
            "504b070b4c4f4e", "504b4c4954450100", "4c4954451a00", 
            "504b4c495445160d", "504b42214", "504b4c4954450d0a", "4b0304", "4b0506", "4b0708", "4b0102"],
    "rar": ["526172211a0700"],
    "7z": ["377abcaf271c"],
    "tar": ["7573746172"],
#    "gzip": ["1f8b08"],
    "bzip2": ["425a68"],
    "pdf": ["25504446"],
    "jpeg": ["ffd8ff"],
    "png": ["89504e47"],
 #   "bmp": ["424d"],
    "gif": ["47494638"],
    "tiff": ["49492a00", "4d4d002a"],
    "mp3": ["494433"],
    "wav": ["52494646"],
    "flac": ["664c614300000022"],
    "ogg": ["4f676753"],
    "avi": ["52494646"],
    "mp4": ["00000020667479706d70"],
    "mov": ["0000002066747970450"],
    "mkv": ["1a45dfa3"],
    "wmv": ["3026b2758e66cf11"],
    "flv": ["464c5601"],
    "mpg": ["000001ba","000001b3"],
    "mpeg": ["000001ba","000001b3"],
    "doc": ["d0cf11e0a1b11ae1"],
    "xls": ["d0cf11e0a1"],
    "ppt": ["d0cf11e0a1b11ae1"],
    "docx": ["504b0304"],
    "xlsx": ["504b0304"],
    "pptx": ["504b0304"],
    "rtf": ["7b5c727466"],
#    "html": ["68746d6c3e"],
    "xml": ["3c3f786d6c"],
    "exe": ["4d5a"],
    "dll": ["4d5a"],
    "bat": ["0d0a406563686f20686"],
    "jar": ["cafebabe"],
    "class": ["cafebabe"],
    "py": ["696d706f7274"],
    "cpp": ["0a232050726f6772616d"],
    "c": ["0a232050726f6772616d"],
    "java": ["cafebabe"],
    "txt": ["746578742f706c61696e"],
    "md": ["232062726966"],
#    "csv": ["2c"],
    "json": ["7b226572726f"],
#    "yaml": ["2dd"],
    "sql": ["2d2d2d2d2d2053494d50"],
    "db": ["5374616e64617264204a6574204442"],
    "mdb": ["5374616e64617264204a6574204442"],
    "accdb": ["5374616e64617264204a6574204442"],
    "apk": ["504b0304"],
    "ipa": ["504b0506"],
    "iso": ["4344303031"],
    "img": ["454353a01a"],
    "vmdk": ["7801730d626260"],
    "vhd": ["636f6e6563746978"],
    "bak": ["5c57696e646f7773"],
    "log": ["5b696e666f5d"],
    "bak": ["2d2d2d2d2d424547494e"],
    "psd": ["38425053"],
#    "pkl": ["636c617373"],
    "pk": ["04034b50"],
    "key": ["2d2d2d2d2d424547494e"],
    "cer": ["2d2d2d2d2d424547494e"],
    "pem": ["2d2d2d2d2d424547494e"],
    "csr": ["2d2d2d2d2d424547494e"]
}



G_HTML_HEAD = """
<!DOCTYPE html>

<html lang="zh-cn">

<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />

<style type="text/css">
body {
    font-family: Helvetica, arial, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    padding-top: 10px;
    padding-bottom: 10px;
    background-color: white;
    padding: 30px; }

body > *:first-child {
    margin-top: 0 !important; }
body > *:last-child {
    margin-bottom: 0 !important; }

a {
    color: #4183C4; }
a.absent {
    color: #cc0000; }
a.anchor {
    display: block;
    padding-left: 30px;
    margin-left: -30px;
    cursor: pointer;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0; }

h1, h2, h3, h4, h5, h6 {
    margin: 20px 0 10px;
    padding: 0;
    font-weight: bold;
    -webkit-font-smoothing: antialiased;
    cursor: text;
    position: relative; }

h1:hover a.anchor, h2:hover a.anchor, h3:hover a.anchor, h4:hover a.anchor, h5:hover a.anchor, h6:hover a.anchor {
    background: url("../../images/modules/styleguide/para.png") no-repeat 10px center;
    text-decoration: none; }

h1 tt, h1 code {
    font-size: inherit; }

h2 tt, h2 code {
    font-size: inherit; }

h3 tt, h3 code {
    font-size: inherit; }

h4 tt, h4 code {
    font-size: inherit; }

h5 tt, h5 code {
    font-size: inherit; }

h6 tt, h6 code {
    font-size: inherit; }

h1 {
    font-size: 28px;
    color: black; }

h2 {
    font-size: 24px;
    border-bottom: 1px solid #cccccc;
    color: black; }

h3 {
    font-size: 18px; }

h4 {
    font-size: 16px; }

h5 {
    font-size: 14px; }

h6 {
    color: #777777;
    font-size: 14px; }

p, blockquote, ul, ol, dl, li, table, pre {
    margin: 15px 0; }

hr {
    background: transparent url("../../images/modules/pulls/dirty-shade.png") repeat-x 0 0;
    border: 0 none;
    color: #cccccc;
    height: 4px;
    padding: 0; }

body > h2:first-child {
    margin-top: 0;
    padding-top: 0; }
body > h1:first-child {
    margin-top: 0;
    padding-top: 0; }
body > h1:first-child + h2 {
    margin-top: 0;
    padding-top: 0; }
body > h3:first-child, body > h4:first-child, body > h5:first-child, body > h6:first-child {
    margin-top: 0;
    padding-top: 0; }

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
    margin-top: 0;
    padding-top: 0; }

h1 p, h2 p, h3 p, h4 p, h5 p, h6 p {
    margin-top: 0; }

li p.first {
    display: inline-block; }

ul, ol {
    padding-left: 30px; }

ul :first-child, ol :first-child {
    margin-top: 0; }

ul :last-child, ol :last-child {
    margin-bottom: 0; }

dl {
    padding: 0; }
dl dt {
    font-size: 14px;
    font-weight: bold;
    font-style: italic;
    padding: 0;
    margin: 15px 0 5px; }
dl dt:first-child {
    padding: 0; }
dl dt > :first-child {
    margin-top: 0; }
dl dt > :last-child {
    margin-bottom: 0; }
dl dd {
    margin: 0 0 15px;
    padding: 0 15px; }
dl dd > :first-child {
    margin-top: 0; }
dl dd > :last-child {
    margin-bottom: 0; }

blockquote {
    border-left: 4px solid #dddddd;
    padding: 0 15px;
    color: #777777; }
blockquote > :first-child {
    margin-top: 0; }
blockquote > :last-child {
    margin-bottom: 0; }

table {
    padding: 0; }
table tr {
    border-top: 1px solid #cccccc;
    background-color: white;
    margin: 0;
    padding: 0; }
table tr:nth-child(2n) {
    background-color: #f8f8f8; }
table tr th {
    font-weight: bold;
    border: 1px solid #cccccc;
    text-align: left;
    margin: 0;
    padding: 6px 13px; }
table tr td {
    border: 1px solid #cccccc;
    text-align: left;
    margin: 0;
    padding: 6px 13px; }
table tr th :first-child, table tr td :first-child {
    margin-top: 0; }
table tr th :last-child, table tr td :last-child {
    margin-bottom: 0; }

img {
    max-width: 100%; }

span.frame {
    display: block;
    overflow: hidden; }
span.frame > span {
    border: 1px solid #dddddd;
    display: block;
    float: left;
    overflow: hidden;
    margin: 13px 0 0;
    padding: 7px;
    width: auto; }
span.frame span img {
    display: block;
    float: left; }
span.frame span span {
    clear: both;
    color: #333333;
    display: block;
    padding: 5px 0 0; }
span.align-center {
    display: block;
    overflow: hidden;
    clear: both; }
span.align-center > span {
    display: block;
    overflow: hidden;
    margin: 13px auto 0;
    text-align: center; }
span.align-center span img {
    margin: 0 auto;
    text-align: center; }
span.align-right {
    display: block;
    overflow: hidden;
    clear: both; }
span.align-right > span {
    display: block;
    overflow: hidden;
    margin: 13px 0 0;
    text-align: right; }
span.align-right span img {
    margin: 0;
    text-align: right; }
span.float-left {
    display: block;
    margin-right: 13px;
    overflow: hidden;
    float: left; }
span.float-left span {
    margin: 13px 0 0; }
span.float-right {
    display: block;
    margin-left: 13px;
    overflow: hidden;
    float: right; }
span.float-right > span {
    display: block;
    overflow: hidden;
    margin: 13px auto 0;
    text-align: right; }

code, tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid #eaeaea;
    background-color: #f8f8f8;
    border-radius: 3px; }

pre code {
    margin: 0;
    padding: 0;
    white-space: pre;
    border: none;
    background: transparent; }

.highlight pre {
    background-color: #f8f8f8;
    border: 1px solid #cccccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px; }

pre {
    background-color: #f8f8f8;
    border: 1px solid #cccccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px; }
pre code, pre tt {
    background-color: transparent;
    border: none; }
</style>
</head>

<body>
"""
