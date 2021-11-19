# 「Pythonで作るはじめてのElasticsearchアプリケーション」サンプルコード

「[Pythonで作るはじめてのElasticsearchアプリケーション](https://amzn.to/2PeF5Js)」のサンプルコードです。

## 目次
1. はじめに 
2. Pythonによる検索アプリケーションの完成イメージ
3. Elasticsearchとは
4. ElasticSearchのインストール
5. Kibanaのインストール
6. Elasticsearch Securityを設定する
7. Elasticsearchの概念を学ぶ
8. ドキュメントのCRUD操作を行う
9. マッピング・インデックスおよびその他主要なドキュメント操作を行う
10. Elasticsearchによる様々な検索を行う
11. アグリゲーション機能を利用して統計データを作成する
12. Pythonによる検索アプリケーションの作成
13. 最後に

## Q&A

### 1. [get_books_from_rakuten.py](https://github.com/chaingng/elasticsearch_python_tutorial/blob/master/get_books_from_rakuten.py)でエラーが発生

エラー内容

```
pipenv run python get_books_from_rakuten.py
> Traceback (most recent call last):
>   File "get_books_from_rakuten.py", line 22, in <module>
>     books.extend(data['Items'])
> KeyError: 'Items'
```

解決方法

認証エラーとなっている可能性が高いので、
RakutenDevelopersで発行された「アプリID/デベロッパーID」を
コード中の `[YOUR APPLICATION_ID]` に置き換えて記載されているかを確認

