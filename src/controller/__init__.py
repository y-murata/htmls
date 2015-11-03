# encoding:utf-8

import os

with open("../work/company.csv") as f:
    url = f.read()
    print(url)

    # html取得
    os.system("wget --recursive --quiet --accept=html --wait=1 --random-wait --force-directories --directory-prefix=../../sites/ " + url)

    # 文字コード変換
    os.system("nkf -Xw --overwrite ../../sites/**/*.html")

    # wgetによる変更をプッシュ
    os.system("git add ../../sites/")
    os.system("git commit -a -m 'auto commit'")
    os.system("git push origin master")
