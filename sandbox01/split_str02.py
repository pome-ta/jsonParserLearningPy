from pathlib import Path

# --- テストデータ
# todo: エスケープシーケンス指定時は、raw文字列指定
json_data = r'''{
        "k0": "\" \\ \/ \b \f \n \r \t",
        "key0": "screwsat",
        "key1": 10,
        "key2": true,
        "key3": false,
        "key4": null,
        "key5": {
            "key1": [1, 2, 3, 4, null, "togatoga"],
            "key2": "あいうえお",
            "key3": "\" \\ \/ \b \f \n \r \t"
        },
        "key6": -11.0111,
        "key7": 1e-10
}
'''


# json_data = '[{"nam e": "Taro", "age": 14, "check": true}, {"name": "Jiro", "age": 23, "check": false}, {"name": "Tom", "age": 16, "check": false}, {"name": null, "age": 14, "check": null}]'


def get_strings_step(tail_list):
  quotation_flag = False
  for n, string in enumerate(tail_list):
    if string == '"':
      # todo: 先頭`"` は、最後尾index を取得するため
      if n and tail_list[n - 1] == '\\': continue
      if quotation_flag: break
      quotation_flag = True
  str_value = ''.join(tail_list[:n + 1])
  return str_value, len(str_value)


def get_numbers_step(tail_list):
  end = [',', '}', ']', '\n']
  for n, number in enumerate(tail_list):
    if number in end: break
  num_value = ''.join(tail_list[:n])
  return num_value, len(num_value)


def get_tokens(str_list):
  tokens = []
  symbols = ['[', ']', '{', '}', ':', ',']
  index = 0

  for _ in range(len(str_list)):
    if index >= len(str_list): break

    element = str_list[index]
    if element.isspace():
      index += 1
      continue

    if element in symbols:
      tokens.append(element)
      index += 1
      continue

    if element == 't':
      # xxx: `true` 確認
      tokens.append(''.join(str_list[index:index + 4]))
      index += 4
      continue

    if element == 'f':
      # xxx: `false` 確認
      tokens.append(''.join(str_list[index:index + 5]))
      index += 5
      continue

    if element == 'n':
      # xxx: `null` 確認
      tokens.append(''.join(str_list[index:index + 5]))
      index += 4
      continue

    # string
    if element == '"':
      value, step = get_strings_step(str_list[index:])
      tokens.append(value)
      index += step
      continue

    # number
    if element:
      value, step = get_numbers_step(str_list[index:])
      tokens.append(value)
      index += step
      continue

    # xxx: ここに来てたらエラー 後で書く
    print(f'err!element: {element}')
    index += 1

  return tokens


if __name__ == '__main__':
  from pprint import pprint

  # json_path = Path('./sandbox/sample01.json')
  json_path = Path('./sample01.json')
  json_data = json_path.read_text(encoding='utf-8')
  json_chr_list = list(json_data)
  json_tokens = get_tokens(json_chr_list)
  print(json_tokens)
