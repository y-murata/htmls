# encoding:utf-8

import os
from datetime import datetime


def getNowDate():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


if __name__ == '__main__':
    listFilePath = "../work/company.csv"

    # プロセス並列化をする

    for url in open(listFilePath, "r"):
        print(url)

        # ブランチを切って切り替える
        os.system("git checkout -b %s" % url)

        # wgetによりhtmlを取得
        ## オプションと説明の一覧
        os.system(
            "wget --recursive --quiet --accept=html --wait=1 --random-wait --force-directories --directory-prefix=../../sites/ " + url)

        # 取得ファイルの文字コード変換
        os.system("nkf -Xw --overwrite ../../sites/**/*.html")

        # コミットコメント用に現在日時の取得
        nowDate = getNowDate()

        # 取得したファイルをプッシュする
        os.system("git add ../../sites/")
        os.system("git commit -a -m 'auto commit_%s %s'" % (url, nowDate))
        os.system("git push -u origin %s" % url)  # ローカルブランチ:リモートブランチ

        # プルリクエスト : 要インストール : brew install hub
        os.system("git pull-request")

        # masterに移動，最新をプル
        os.system("git checkout master")
        os.system("git pull -u origin master")

        # マージする
        ## マージするときはmasterのHEADに行ってマージしないといけない
        os.system("git merge %s --no-ff" % url)

        # ブランチを削除する
        os.system("git branch -D %s" % url)
