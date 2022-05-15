from pystaParser import parse

if __name__ == '__main__':
  from pathlib import Path
  import json
  
  import cProfile
  #import profile
  import time

  json_path = Path('./sample04.json')
  json_str = json_path.read_text(encoding='utf-8')
  
  cProfile.run("parse(json_str)", sort=1)
  #cProfile.run("json.loads(json_str)")
  #main = profile.run(json_path.read_text(encoding='utf-8'))
  '''
  print('file name: sample04.json')
  ave_num = 0.0
  all_num = 10
  for i in range(all_num):
    start_time = time.perf_counter()
    #main_json = parse(json_str)
    main_sample = json.loads(json_str)
    end_time = time.perf_counter()
    result_time = end_time - start_time
    print(f'\t{i+1:02}回目:', result_time)
    ave_num += result_time
  #main_sample = json.loads(json_str)
  #print(main_json == main_sample)
  print('平均:', ave_num / float(all_num))
  '''
  


