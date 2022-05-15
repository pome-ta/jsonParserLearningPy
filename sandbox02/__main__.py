from pystaParser import parse

if __name__ == '__main__':
  from pathlib import Path
  import json

  json_path = Path('./sample04.json')
  json_str = json_path.read_text(encoding='utf-8')
  main_json = parse(json_str)
  main_sample = json.loads(json_str)
  print(main_json == main_sample)

