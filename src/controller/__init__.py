# encoding:utf-8

import os
from datetime import datetime

for url in open("../work/company.csv", "r"):
    print(url)

    # html取得
    os.system("wget --recursive --quiet --accept=html --wait=1 --random-wait --force-directories --directory-prefix=../../sites/ " + url)

    # 文字コード変換
    os.system("nkf -Xw --overwrite ../../sites/**/*.html")

    # 現在日時の取得
    nowDate = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    # wgetによる変更をプッシュ
    os.system("git add ../../sites/")
    os.system("git commit -a -m 'auto commit_%s %s'" % (url, nowDate))
    os.system("git push origin master")