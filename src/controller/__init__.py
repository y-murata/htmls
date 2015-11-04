# encoding:utf-8

import os
from datetime import datetime


def git_commit():
    os.system("git add ../../sites/")
    os.system("git commit -a -m 'auto commit : %s : %s'" % (url, nowDate))
    os.system("git push origin master")


def wget_list():
    os.system("wget --recursive --quiet --accept=html --wait=1 --random-wait --force-directories --directory-prefix=../../sites/ " + url)


def file_encode():
    os.system("nkf -Xw --overwrite ../../sites/**/*.html")


for url in open("../work/company.csv", "r"):
    print(url)

    # html取得
    wget_list()

    # 文字コード変換
    file_encode()

    # 現在日時の取得
    nowDate = datetime.now().strftime("%Y/%m/%d")

    # wgetによる変更をプッシュ
    git_commit()