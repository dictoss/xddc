# webサイトについて

## ツール

- pelicanというツールを使っています
  - pip3 install pelican==4.2.0

## 記事の作成手順

- 雛形ファイルをコピーします。
  - cp blog-template.rst content/yyyy-mm-dd_{イベント名}.rst
- 記事を書きます
  - editor content/yyyy-mm-dd_{イベント名}.rst
  - ファイル上部のメタデータ情報
    - 解説： https://docs.getpelican.com/en/stable/content.html
    - slug は 拡張子を除いたファイル名を書いてください
      - 後述の make html を実行したときに生成される html ファイルのファイル名に使われます。
  - 記事部分の書き方
    - rst形式で書いてください。
- 記事をビルドしてhtmlファイルを生成します。
  - make html
- 記事の内容を確認します
  - make serve
    - ローカル環境でwebサーバが起動します
  - http://localhost:8000 へwebブラウザで見て確認します

## 記事のコミットと公開方法

- リポジトリの /docs/ ディレクトリにあるファイルを github pages で公開する仕組みになっています。
- make htmlで生成したhtmlファイルを /docs/ 配下へコピーしてcommit、pushします。
- https://dictoss.github.io/xddc/ でコンテンツが公開されます。
