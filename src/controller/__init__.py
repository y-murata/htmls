# encoding:utf-8

import os
os.system("git commit -a -m pywget1")
os.system("git push origin master")

"""
with open("../work/company.csv") as f:
    url = f.read()

    # html取得
    os.system("wget --recursive --quiet --accept=html --wait=1 --random-wait --force-directories --directory-prefix=../../sites/ " + url)

    # 文字コード変換
    os.system("nkf -Xw --overwrite ../../sites/**/*.html")

    # 変更をコミット
    os.system("git commit -a")
"""