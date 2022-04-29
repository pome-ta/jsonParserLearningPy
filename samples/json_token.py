# https://gist.github.com/PickledChair/77b5a06d18f7274a0761f3ea26851911

from dataclasses import dataclass
from enum import Enum, auto
from typing import Union


class TokenKind(Enum):
    # リテラル
    BOOLEAN = auto()  # true または false
    INTEGER = auto()  # 整数値
    FLOAT = auto()    # 浮動小数点数値
    STRING = auto()   # 文字列
    NULL = auto()     # null
    
    # 記号
    COMMA = auto()    # ,
    COLON = auto()    # :
    LBRACE = auto()   # {
    RBRACE = auto()   # }
    LBRACKET = auto() # [
    RBRACKET = auto() # ]


@dataclass
class Token:
    kind: TokenKind
    value: Union[int, float, str, None] = None

    def __str__(self):
        if self.kind == TokenKind.COMMA:
            return ","
        elif self.kind == TokenKind.COLON:
            return ":"
        elif self.kind == TokenKind.LBRACE:
            return "{"
        elif self.kind == TokenKind.RBRACE:
            return "}"
        elif self.kind == TokenKind.LBRACKET:
            return "["
        elif self.kind == TokenKind.RBRACKET:
            return "]"
        elif self.kind == TokenKind.STRING:
            return f"\"{self.value}\""
        else:
            return str(self.value)


# { "name": "太郎", "age": 24, "hobby": ["釣り", "サイクリング"] }
tokens = [
    Token(TokenKind.LBRACE),
    Token(TokenKind.STRING, "name"),
    Token(TokenKind.COLON),
    Token(TokenKind.STRING, "太郎"),
    Token(TokenKind.COMMA),
    Token(TokenKind.STRING, "age"),
    Token(TokenKind.COLON),
    Token(TokenKind.INTEGER, 24),
    Token(TokenKind.COMMA),
    Token(TokenKind.STRING, "hobby"),
    Token(TokenKind.COLON),
    Token(TokenKind.LBRACKET),
    Token(TokenKind.STRING, "釣り"),
    Token(TokenKind.COMMA),
    Token(TokenKind.STRING, "サイクリング"),
    Token(TokenKind.RBRACKET),
    Token(TokenKind.RBRACE),
]


string = ""
for token in tokens:
    string += str(token)
print("tokens:", string)


def tokenize(s, tokens):
    """ 字句解析器（もどき）"""
    if len(s) == 0 or s.isspace():
        return tokens

    while s[0].isspace():
        s = s[1:]

    if s[0] == ",":
        tokens.append(Token(TokenKind.COMMA))
        return tokenize(s[1:], tokens)
    elif s[0] == ":":
        tokens.append(Token(TokenKind.COLON))
        return tokenize(s[1:], tokens)
    elif s[0] == "{":
        tokens.append(Token(TokenKind.LBRACE))
        return tokenize(s[1:], tokens)
    elif s[0] == "}":
        tokens.append(Token(TokenKind.RBRACE))
        return tokenize(s[1:], tokens)
    elif s[0] == "[":
        tokens.append(Token(TokenKind.LBRACKET))
        return tokenize(s[1:], tokens)
    elif s[0] == "]":
        tokens.append(Token(TokenKind.RBRACKET))
        return tokenize(s[1:], tokens)
    elif s[0] == "\"":
        s = s[1:]
        value = ""
        while s[0] != "\"":
            value += s[0]
            s = s[1:]
        tokens.append(Token(TokenKind.STRING, value))
        return tokenize(s[1:], tokens)
    elif s[0].isdigit():
        str_value = ""
        while s[0].isdigit():
            str_value += s[0]
            s = s[1:]
        tokens.append(Token(TokenKind.INTEGER, int(str_value)))
        return tokenize(s, tokens)


s = '{ "name": "太郎", "age": 24, "hobby": ["釣り", "サイクリング"] }'
result = tokenize(s, [])
print("result == tokens:", result == tokens)

