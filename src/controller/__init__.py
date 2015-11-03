# encoding:utf-8

import os

# html取得
os.system("xargs -P 200 -n 1 wget --recursive --quiet --accept=html --wait=1 --random-wait --force-directories --directory-prefix=../../sites/ < ../../company.csv")

# 文字コード変換
# os.system("nkf -Xw --overwrite /Users/muratayu/codebreak/sites/**/*.html")
os.system("nkf -Xw --overwrite ../../sites/**/*.html")
