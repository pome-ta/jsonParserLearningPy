# 📝 2022/05/12


## ビルドインのモジュールを見る

Pythonista 内のと


[リポジトリ](https://github.com/python/cpython/tree/main/Lib/json) のやつ


## メモ


- `raise`
  - エラー発生さす
- 正規表現
  - `FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL`
    - ビット演算でフラグ管理してる




# 📝 2022/05/11


## sandbox01

とりあえず、パースはできた


考え方とか、メモでも良いから書き落とさないと、、、


## 清書

- 変数名
- Parse の用語
- 型
- モジュール化
- エラー処理

を考えて、やってく



# 📝 2022/05/08

## メタ文法のお勉強

### キーワード用語のベタ書き

- BNF
- 左側規則名、右側本体
- 非終端記号
  - 最後が何かを参照
- 規則
- JSON のBNF
- シンプルであるが、再帰的に定義されてる
- 構文解析器

- GoF(Gang of Four) パターン
- `Composite`




## json の同じキー


Python の`json` モジュールだと、しれっと上書きされてるぽい


最後に取得したキー



# 📝 2022/05/07

分割はできたけども、オブジェクト化するのがゴタゴタしてる

[asciidwango / parser_book](https://github.com/asciidwango/parser_book/blob/master/SUMMARY.md)

これ読んでみる



## JSON BNF

```
json = object;
object = LBRACE RBRACE | LBRACE {pair {COMMA pair} RBRACE;
pair = STRING COLON value;
array = LBRACKET RBRACKET | LBRACKET {value {COMMA value}} RBRACKET ;
value = STRING | NUMBER | object | array | TRUE | FALSE | NULL ;

STRING = ("\"\"" / "\"" CHAR+ "\"") S;
NUMBER = (INT FRAC EXP | INT EXP | INT FRAC | INT) S;
TRUE = "true" S ;
FALSE = "false" S;
NULL = "null" S;
COMMA = "," S;
COLON = ":" S;
LBRACE = "{" S;
RBRACE = "}" S;
LBRACKET = "[" S;
RBRACKET = "]" S;

S = ( [ \f\t\r\n]+
  | "/*" (!"*/" _)* "*/"
    / "//" (![\r\n] _)* [\r\n]
    )* ;

CHAR = (!(["\\]) _) | "\\" [\\"/bfnrt] | "u" HEX HEX HEX HEX ;
HEX = `[0-9a-fA-F]` ;
INT = ["-"] (`[1-9]` {`[0-9]`} / "0") ;
FRAC = "." [0-9]+ ;
EXP = e `[0-9]` {`[0-9]`} ;
E = "e+" | "e-" | "E+" | "E-" | "e" | "E" ;
```

そもそも、オブジェクトの変換について考えないと(プログラムの処理的な話だとおもう)



# 📝 2022/05/04


## 辞書の順番


 Pythonista は、3.6 だから
 
 順番変わる問題は気にしなくていい？
 
 
 2.6 で実行すると、順番が変だった


# 📝 2022/05/03

## `Enum` 使うかな？


うーん、列挙型のメリットが理解できていない、、、

(js の移植も考えた時に) としても、js にも列挙型あるしねぇ


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


そもそも、json ってところから始める



## `[` `]` について

サンプルで、`[` があるものとないものがある？




JSON RPC v2.0 形式


`'` シングルではなく`"` ダブルの必要がある



簡易パーサー作成後、json へか？



## 正規表現


結局諦めた

``` .py
pattern = compile(r'(\[|\]|\{|\}|:|,|\n)')
slice_data = pattern.split(json_data)
```



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

