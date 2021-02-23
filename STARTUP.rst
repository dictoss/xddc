=====================================
CDDC を初めるための準備
=====================================

メーリングリスト
--------------------------------------------------

- 条件

  - 公開状態で運用する
  - 匿名投稿は不可
  - メールサーバを運用したくない

- 選定候補

  - Google Groups

- 例

  - tracプロジェクトはGoogle Groupsで運営している

    - https://groups.google.com/forum/#!forum/trac-dev


ソースコード、wiki等のデータの保管場所
----------------------------------------------------------

- 条件

  - 公開状態で運用する
  - gitリポジトリへのコミットはメンバのみ
  -

- 選定候補

  - github.com

    - `料金プラン <https://github.co.jp/pricing>`_
    - 無料枠は3名まで。**枠が足りない。**
  - gitlab.com

    - `料金プラン <https://www.gitlab.jp/pricing/#gitlab-com>`_
    - Freeプランで人数に関係なく、無料で使える。
    - CI/CDのサーバもついている
    - **候補先としてはこれがよいかも。**
  - bitbucket (Atlassian.com)

    - `Atlassian Community License Request <https://www.atlassian.com/software/views/community-license-request>`_

      - 申請枠に団体のwebサイトのURLを提示するところが必須入力になっている。**まだwebサイトがないので困った。**


webサイト
--------------------------------

- 要件

  - 静的HTMLファイルをビルドして公開するやり方にしたい
  - ブログはmarkdownかreStructuredTextで書いて、静的なHTMLとしてビルドしてブログをやりたい
  - できればソースコード管理しているところで、静的HTMLをホスティングしているところがいい

- 中身をどうつくるか

  - 自作する必要あり
  - ただwebアプリ開発者がメンバにいないため、web周りは苦手

- プロトタイプ

  - https://dictoss.github.io/cddc/

    - source code: https://github.com/dictoss/cddc/tree/master/docs
