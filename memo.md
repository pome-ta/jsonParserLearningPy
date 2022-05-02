# 📝 2022/05/02


## エスケープシーケンス

テストとして、文字列でjson を直接書いていた

``` .py
str_json = '{json}'
```

``` .py
str_json = r'{json}'
```

`raw` を文字列に直接だと問題がないが、変数扱いだとどうなるだろうかと`raw` の関数がないか調査した。

`repr` があったが、トリプルクオーテーションでは、処理の結果が違っていたりしたので(詳細が適当)

`.json` から読み取ってみることにしている


ぐぬぬ、、、やはり、Python 文字列上でテストするには、raw文字列つけるの必須かもな。。。


### Python の文字列処理

エスケープシーケンスを入れた文字列は、その手前で処理しないといけなそう


`'"\""'` が、しれっと`\` が消えてしまう

`b'{json}'` でも結果変わらずだった(当たり前か。。。)


## `path` の扱い

Pythonista だと、実行ファイル位置がカレントディレクトリになってる(ぽい)

処理段階で、挙動を変更することを考えておく


まずは、カジュアルにでもカタチにすることを目指す




# 📝 2022/05/01


エスケープの書き方にもにゃる


# 📝 2022/04/30

## 例外処理？


いまは、考えなくていいのか？


そもそも、エラーになる構造だと取得結果があかんけど

まずは、正義であるでいいのかな？




## 文字列分割

`while` は筋が良くない(Python 処理的に)気がして

分割の長さから、インデックスで処理する？


(もちろん、処理の計測は必要)


## 数値

### ルール

`:` (配列であれば`,` )の後に登場



`key` で数値はないよね？




# 📝 2022/04/29

[PickledChair / json_token.py](https://gist.github.com/PickledChair/77b5a06d18f7274a0761f3ea26851911)

JSONの字句解析器みたいなもの

書いていただいた！！！



## 文字列


一旦分割してみる？
