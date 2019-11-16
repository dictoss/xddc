# webサイトについて

## ツール

- pelicanというツールを使っています
  - pip install pelican

## 記事の作成手順

- 雛形ファイルをコピーします。
  - cp blog-template.rst content/yyyy-mm-dd_{イベント名}.rst
- 記事を書きます
  - editor content/yyyy-mm-dd_{イベント名}.rst
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
