# 📝 2022/05/20


`pystaParser04`

```
         170706 function calls (168402 primitive calls) in 0.083 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.035    0.035    0.052    0.052 pystaParser04.py:68(division_strings)
  768/256    0.012    0.000    0.026    0.000 pystaParser04.py:263(_get_dicts)
    513/1    0.009    0.000    0.030    0.030 pystaParser04.py:295(_get_arrays)
    11777    0.007    0.000    0.010    0.000 pystaParser04.py:52(_switch_symbol_token)
     9729    0.005    0.000    0.006    0.000 pystaParser04.py:251(_convert_value)
    20993    0.005    0.000    0.005    0.000 pystaParser04.py:23(__init__)
    61441    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
    49507    0.002    0.000    0.002    0.000 {method 'isspace' of 'str' objects}
     2562    0.002    0.000    0.002    0.000 pystaParser04.py:237(_setup_nest)
        1    0.001    0.001    0.083    0.083 <string>:1(<module>)
     4096    0.001    0.000    0.001    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
   1281/1    0.001    0.000    0.030    0.030 pystaParser04.py:317(_get_json_obj)
     3072    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
     4960    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.083    0.083 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 pystaParser04.py:70(<listcomp>)
        1    0.000    0.000    0.000    0.000 pystaParser04.py:70(<lambda>)
        1    0.000    0.000    0.083    0.083 pystaParser04.py:326(parse)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

# 📝 2022/05/18

属性関係をインクルード

```
         179105 function calls (176801 primitive calls) in 0.086 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.036    0.036    0.052    0.052 pystaParser03.py:98(division_strings)
  768/256    0.012    0.000    0.029    0.000 pystaParser03.py:348(_get_dicts)
    513/1    0.009    0.000    0.033    0.033 pystaParser03.py:380(_get_arrays)
    11777    0.006    0.000    0.009    0.000 pystaParser03.py:34(_switch_symbol_token)
     9729    0.006    0.000    0.009    0.000 pystaParser03.py:335(_convert_value)
    20993    0.006    0.000    0.006    0.000 pystaParser03.py:23(__init__)
    61478    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
    49507    0.002    0.000    0.002    0.000 {method 'isspace' of 'str' objects}
     2562    0.002    0.000    0.002    0.000 pystaParser03.py:266(_setup_nest)
     4096    0.001    0.000    0.003    0.000 re.py:180(search)
     4096    0.001    0.000    0.001    0.000 re.py:287(_compile)
        1    0.001    0.001    0.086    0.086 <string>:1(<module>)
     4096    0.001    0.000    0.001    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
   1281/1    0.001    0.000    0.033    0.033 pystaParser03.py:402(_get_json_obj)
     3072    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
     4993    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.086    0.086 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 sre_compile.py:483(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_parse.py:470(_parse)
        2    0.000    0.000    0.000    0.000 sre_compile.py:251(_optimize_charset)
        4    0.000    0.000    0.000    0.000 enum.py:802(__and__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:379(<listcomp>)
        2    0.000    0.000    0.000    0.000 sre_parse.py:846(parse)
       10    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
       14    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 sre_compile.py:558(compile)
        2    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
        9    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        8    0.000    0.000    0.000    0.000 enum.py:266(__call__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:224(_compile_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:377(_mk_bitmap)
        2    0.000    0.000    0.000    0.000 sre_compile.py:543(_code)
        3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
        2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        8    0.000    0.000    0.000    0.000 enum.py:516(__new__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:65(_compile)
        2    0.000    0.000    0.000    0.000 sre_parse.py:77(__init__)
        4    0.000    0.000    0.000    0.000 sre_parse.py:82(groups)
        2    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        2    0.000    0.000    0.000    0.000 sre_parse.py:408(_parse_sub)
        1    0.000    0.000    0.000    0.000 pystaParser03.py:100(<listcomp>)
        1    0.000    0.000    0.085    0.085 pystaParser03.py:411(parse)
        1    0.000    0.000    0.000    0.000 sre_compile.py:394(_generate_overlap_table)
        4    0.000    0.000    0.000    0.000 sre_compile.py:540(isstring)
        2    0.000    0.000    0.000    0.000 sre_parse.py:112(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
        7    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        2    0.000    0.000    0.000    0.000 sre_parse.py:830(fix_flags)
        1    0.000    0.000    0.000    0.000 pystaParser03.py:100(<lambda>)
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 sre_compile.py:415(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:442(_get_charset_prefix)
        2    0.000    0.000    0.000    0.000 sre_parse.py:172(append)

```

`get_tokens` 設計を変えてみた

```
         222378 function calls (220074 primitive calls) in 0.164 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.065    0.065    0.067    0.067 pystaParser02.py:329(_get_nest2indent_list)
        1    0.023    0.023    0.038    0.038 pystaParser02.py:155(division_strings)
  768/256    0.012    0.000    0.029    0.000 pystaParser02.py:378(_get_dicts)
    20993    0.011    0.000    0.011    0.000 pystaParser02.py:296(_setup_nest)
    513/1    0.009    0.000    0.033    0.033 pystaParser02.py:410(_get_arrays)
        1    0.007    0.007    0.022    0.022 pystaParser02.py:311(_set_attributes)
    11777    0.007    0.000    0.010    0.000 pystaParser02.py:34(_switch_symbol_token)
     9729    0.006    0.000    0.009    0.000 pystaParser02.py:365(_convert_value)
    20993    0.005    0.000    0.005    0.000 pystaParser02.py:23(__init__)
    20993    0.004    0.000    0.004    0.000 pystaParser02.py:306(_setup_objkey)
    65321    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.003    0.003    0.003    0.003 pystaParser02.py:358(_set_indent)
    49507    0.002    0.000    0.002    0.000 {method 'isspace' of 'str' objects}
        1    0.002    0.002    0.002    0.002 pystaParser02.py:321(_get_index2indent_dict)
     4096    0.001    0.000    0.003    0.000 re.py:180(search)
     4096    0.001    0.000    0.001    0.000 re.py:287(_compile)
        1    0.001    0.001    0.164    0.164 <string>:1(<module>)
     4096    0.001    0.000    0.001    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
   1281/1    0.001    0.000    0.033    0.033 pystaParser02.py:432(_get_json_obj)
     3072    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
     4994    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 pystaParser02.py:332(<listcomp>)
        1    0.000    0.000    0.163    0.163 pystaParser02.py:441(parse)
        1    0.000    0.000    0.164    0.164 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 sre_parse.py:470(_parse)
        2    0.000    0.000    0.000    0.000 sre_compile.py:251(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_parse.py:846(parse)
        2    0.000    0.000    0.000    0.000 sre_compile.py:558(compile)
        2    0.000    0.000    0.000    0.000 sre_compile.py:379(<listcomp>)
        2    0.000    0.000    0.000    0.000 sre_compile.py:483(_compile_info)
        8    0.000    0.000    0.000    0.000 enum.py:516(__new__)
        4    0.000    0.000    0.000    0.000 enum.py:802(__and__)
        2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        2    0.000    0.000    0.000    0.000 sre_compile.py:65(_compile)
        2    0.000    0.000    0.000    0.000 sre_compile.py:224(_compile_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:377(_mk_bitmap)
        2    0.000    0.000    0.000    0.000 sre_compile.py:543(_code)
        2    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        9    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
       14    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:408(_parse_sub)
       10    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        8    0.000    0.000    0.000    0.000 enum.py:266(__call__)
        1    0.000    0.000    0.000    0.000 sre_compile.py:394(_generate_overlap_table)
        4    0.000    0.000    0.000    0.000 sre_parse.py:82(groups)
        7    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 pystaParser02.py:157(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 sre_compile.py:415(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:442(_get_charset_prefix)
        4    0.000    0.000    0.000    0.000 sre_compile.py:540(isstring)
        2    0.000    0.000    0.000    0.000 sre_parse.py:77(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:112(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
        3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        2    0.000    0.000    0.000    0.000 sre_parse.py:830(fix_flags)
        1    0.000    0.000    0.000    0.000 pystaParser02.py:157(<lambda>)
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
        7    0.000    0.000    0.000    0.000 sre_parse.py:249(match)

```

# 📝 2022/05/16

## 計測

`_set_indent` を`get_tokens` 内に

```
         192994 function calls (190690 primitive calls) in 1.027 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.960    0.960    0.993    0.993 pystaParser.py:98(get_tokens)
  768/256    0.012    0.000    0.029    0.000 pystaParser.py:239(_get_dicts)
    513/1    0.009    0.000    0.033    0.033 pystaParser.py:271(_get_arrays)
     4352    0.007    0.000    0.010    0.000 pystaParser.py:59(_get_strings_step)
    11777    0.006    0.000    0.009    0.000 pystaParser.py:34(_switch_symbol_token)
    20993    0.006    0.000    0.006    0.000 pystaParser.py:23(__init__)
     9729    0.006    0.000    0.009    0.000 pystaParser.py:226(_convert_value)
     3328    0.005    0.000    0.006    0.000 pystaParser.py:75(_get_numbers_step)
    61478    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
    40707    0.002    0.000    0.002    0.000 {method 'isspace' of 'str' objects}
     2562    0.002    0.000    0.002    0.000 pystaParser.py:157(_setup_nest)
     1536    0.001    0.000    0.002    0.000 pystaParser.py:86(_get_bools2null_step)
     9216    0.001    0.000    0.001    0.000 {method 'join' of 'str' objects}
     4096    0.001    0.000    0.003    0.000 re.py:180(search)
     4096    0.001    0.000    0.001    0.000 re.py:287(_compile)
        1    0.001    0.001    1.027    1.027 <string>:1(<module>)
     4096    0.001    0.000    0.001    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
     9249    0.001    0.000    0.001    0.000 {built-in method builtins.len}
   1281/1    0.001    0.000    0.033    0.033 pystaParser.py:293(_get_json_obj)
     3072    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    1.026    1.026 pystaParser.py:302(parse)
        1    0.000    0.000    1.027    1.027 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 sre_compile.py:251(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_parse.py:846(parse)
        2    0.000    0.000    0.000    0.000 sre_compile.py:483(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_parse.py:470(_parse)
        4    0.000    0.000    0.000    0.000 enum.py:802(__and__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:558(compile)
        2    0.000    0.000    0.000    0.000 sre_compile.py:377(_mk_bitmap)
        2    0.000    0.000    0.000    0.000 sre_compile.py:379(<listcomp>)
        9    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 sre_parse.py:408(_parse_sub)
       14    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        8    0.000    0.000    0.000    0.000 enum.py:266(__call__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
        2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        2    0.000    0.000    0.000    0.000 sre_compile.py:224(_compile_charset)
        2    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
        7    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        6    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 sre_compile.py:65(_compile)
        2    0.000    0.000    0.000    0.000 sre_compile.py:543(_code)
        2    0.000    0.000    0.000    0.000 sre_parse.py:112(__init__)
        3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 pystaParser.py:106(<listcomp>)
       10    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        8    0.000    0.000    0.000    0.000 enum.py:516(__new__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:415(_get_literal_prefix)
        4    0.000    0.000    0.000    0.000 sre_compile.py:540(isstring)
        2    0.000    0.000    0.000    0.000 sre_parse.py:77(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:830(fix_flags)
        1    0.000    0.000    0.000    0.000 pystaParser.py:106(<lambda>)
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
        1    0.000    0.000    0.000    0.000 sre_compile.py:394(_generate_overlap_table)
        1    0.000    0.000    0.000    0.000 sre_compile.py:442(_get_charset_prefix)
        4    0.000    0.000    0.000    0.000 sre_parse.py:82(groups)
        2    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
```

`_setup_nest` を`get_tokens` 内に

```
         227051 function calls (224747 primitive calls) in 1.094 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.941    0.941    0.983    0.983 pystaParser.py:98(get_tokens)
        1    0.065    0.065    0.067    0.067 pystaParser.py:178(_get_nest2indent_list)
  768/256    0.012    0.000    0.029    0.000 pystaParser.py:226(_get_dicts)
    11777    0.010    0.000    0.010    0.000 pystaParser.py:143(_setup_nest)
    513/1    0.009    0.000    0.033    0.033 pystaParser.py:257(_get_arrays)
     4352    0.007    0.000    0.010    0.000 pystaParser.py:59(_get_strings_step)
    11777    0.007    0.000    0.010    0.000 pystaParser.py:34(_switch_symbol_token)
    20993    0.006    0.000    0.006    0.000 pystaParser.py:23(__init__)
     9729    0.006    0.000    0.009    0.000 pystaParser.py:214(_convert_value)
     3328    0.005    0.000    0.007    0.000 pystaParser.py:75(_get_numbers_step)
        1    0.004    0.004    0.008    0.008 pystaParser.py:158(_set_attributes)
    20993    0.004    0.000    0.004    0.000 pystaParser.py:153(_setup_objkey)
    65321    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
        1    0.002    0.002    0.002    0.002 pystaParser.py:207(_set_indent)
    40707    0.002    0.000    0.002    0.000 {method 'isspace' of 'str' objects}
        1    0.002    0.002    0.002    0.002 pystaParser.py:170(_get_index2indent_dict)
     9216    0.001    0.000    0.001    0.000 {method 'join' of 'str' objects}
     1536    0.001    0.000    0.002    0.000 pystaParser.py:86(_get_bools2null_step)
     4096    0.001    0.000    0.003    0.000 re.py:180(search)
     4096    0.001    0.000    0.001    0.000 re.py:287(_compile)
        1    0.001    0.001    1.094    1.094 <string>:1(<module>)
     4096    0.001    0.000    0.001    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
     9250    0.001    0.000    0.001    0.000 {built-in method builtins.len}
   1281/1    0.001    0.000    0.033    0.033 pystaParser.py:279(_get_json_obj)
     3072    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    1.093    1.093 pystaParser.py:288(parse)
        1    0.000    0.000    0.000    0.000 pystaParser.py:181(<listcomp>)
        1    0.000    0.000    1.094    1.094 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 sre_parse.py:846(parse)
        2    0.000    0.000    0.000    0.000 sre_compile.py:251(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_parse.py:470(_parse)
        4    0.000    0.000    0.000    0.000 enum.py:802(__and__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:558(compile)
        2    0.000    0.000    0.000    0.000 sre_compile.py:483(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:379(<listcomp>)
        9    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 sre_compile.py:224(_compile_charset)
        2    0.000    0.000    0.000    0.000 sre_parse.py:408(_parse_sub)
        8    0.000    0.000    0.000    0.000 enum.py:266(__call__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:377(_mk_bitmap)
        2    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
       10    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
        2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        2    0.000    0.000    0.000    0.000 sre_compile.py:65(_compile)
        2    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
       14    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        8    0.000    0.000    0.000    0.000 enum.py:516(__new__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:830(fix_flags)
        1    0.000    0.000    0.000    0.000 pystaParser.py:106(<listcomp>)
        1    0.000    0.000    0.000    0.000 pystaParser.py:106(<lambda>)
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 sre_compile.py:394(_generate_overlap_table)
        1    0.000    0.000    0.000    0.000 sre_compile.py:442(_get_charset_prefix)
        4    0.000    0.000    0.000    0.000 sre_compile.py:540(isstring)
        2    0.000    0.000    0.000    0.000 sre_compile.py:543(_code)
        2    0.000    0.000    0.000    0.000 sre_parse.py:77(__init__)
        4    0.000    0.000    0.000    0.000 sre_parse.py:82(groups)
        2    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
        7    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
        7    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 sre_compile.py:415(_get_literal_prefix)
        2    0.000    0.000    0.000    0.000 sre_parse.py:112(__init__)
        3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
```

# 📝 2022/05/15

処理があまりにも遅いので計測

```
自分のやつ
file name: sample04.json
	01回目: 1.0980810000037309
	02回目: 1.1035174169810489
	03回目: 1.1014316669898108
	04回目: 1.0957911669975147
	05回目: 1.096645042009186
	06回目: 1.0955302919901442
	07回目: 1.1065528329927474
	08回目: 1.0968597079918254
	09回目: 1.0980925830081105
	10回目: 1.0968300420208834
平均: 1.0989331750985003
```

```
ビルドイン json
file name: sample04.json
	01回目: 0.0014894999912939966
	02回目: 0.0016257090028375387
	03回目: 0.0016498749901074916
	04回目: 0.0015635419986210763
	05回目: 0.0015682909870520234
	06回目: 0.0011102090065833181
	07回目: 0.001141209009801969
	08回目: 0.0011617919954005629
	09回目: 0.0011355419992469251
	10回目: 0.001093458995455876
平均: 0.0013539127976400778

```

`cProfile` というのを[見つけた](https://docs.python.org/ja/3.6/library/profile.html)

`run` の引数で、`sort=1` を指定すると`Ordered by: internal time`

```
         295170 function calls (292866 primitive calls) in 1.130 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.942    0.942    1.004    1.004 pystaParser.py:88(get_tokens)
        1    0.065    0.065    0.067    0.067 pystaParser.py:164(_get_nest2indent_list)
    11778    0.024    0.000    0.041    0.000 pystaParser.py:35(_get_symbol_dict)
    79884    0.020    0.000    0.020    0.000 pystaParser.py:23(__init__)
  768/256    0.012    0.000    0.029    0.000 pystaParser.py:213(_get_dicts)
    20993    0.011    0.000    0.011    0.000 pystaParser.py:127(_setup_nest)
    513/1    0.009    0.000    0.033    0.033 pystaParser.py:245(_get_arrays)
     4352    0.007    0.000    0.010    0.000 pystaParser.py:53(_get_strings_step)
        1    0.007    0.007    0.022    0.022 pystaParser.py:142(_set_attributes)
     9729    0.006    0.000    0.009    0.000 pystaParser.py:200(_convert_value)
     3328    0.005    0.000    0.006    0.000 pystaParser.py:67(_get_numbers_step)
    20993    0.004    0.000    0.004    0.000 pystaParser.py:137(_setup_objkey)
    65322    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
        1    0.003    0.003    0.003    0.003 pystaParser.py:193(_set_indent)
    40708    0.002    0.000    0.002    0.000 {method 'isspace' of 'str' objects}
        1    0.002    0.002    0.002    0.002 pystaParser.py:156(_get_index2indent_dict)
     1536    0.001    0.000    0.002    0.000 pystaParser.py:76(_get_bools2null_step)
     9216    0.001    0.000    0.001    0.000 {method 'join' of 'str' objects}
     4096    0.001    0.000    0.003    0.000 re.py:180(search)
     4096    0.001    0.000    0.001    0.000 re.py:287(_compile)
        1    0.001    0.001    1.130    1.130 <string>:1(<module>)
     4096    0.001    0.000    0.001    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
     9251    0.001    0.000    0.001    0.000 {built-in method builtins.len}
   1281/1    0.001    0.000    0.033    0.033 pystaParser.py:267(_get_json_obj)
     3072    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    1.129    1.129 pystaParser.py:277(parse)
        1    0.000    0.000    0.000    0.000 pystaParser.py:167(<listcomp>)
        1    0.000    0.000    1.130    1.130 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 sre_parse.py:470(_parse)
        2    0.000    0.000    0.000    0.000 sre_compile.py:251(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:558(compile)
        2    0.000    0.000    0.000    0.000 sre_parse.py:846(parse)
        8    0.000    0.000    0.000    0.000 enum.py:516(__new__)
        4    0.000    0.000    0.000    0.000 enum.py:802(__and__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:379(<listcomp>)
        2    0.000    0.000    0.000    0.000 sre_compile.py:483(_compile_info)
        1    0.000    0.000    0.000    0.000 sre_parse.py:295(_class_escape)
        2    0.000    0.000    0.000    0.000 sre_compile.py:377(_mk_bitmap)
        2    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
       10    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
       10    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
       14    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 sre_compile.py:543(_code)
        2    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
        8    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 pystaParser.py:96(<listcomp>)
        4    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        8    0.000    0.000    0.000    0.000 enum.py:266(__call__)
        2    0.000    0.000    0.000    0.000 sre_compile.py:65(_compile)
        2    0.000    0.000    0.000    0.000 sre_compile.py:224(_compile_charset)
        4    0.000    0.000    0.000    0.000 sre_compile.py:540(isstring)
        2    0.000    0.000    0.000    0.000 sre_parse.py:77(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:112(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
        3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        2    0.000    0.000    0.000    0.000 sre_parse.py:408(_parse_sub)
        2    0.000    0.000    0.000    0.000 sre_parse.py:830(fix_flags)
        6    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
        1    0.000    0.000    0.000    0.000 sre_compile.py:394(_generate_overlap_table)
        2    0.000    0.000    0.000    0.000 sre_compile.py:415(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:442(_get_charset_prefix)
        8    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
        1    0.000    0.000    0.000    0.000 pystaParser.py:96(<lambda>)
        2    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 sre_parse.py:82(groups)
```

```
         13 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 __init__.py:303(loads)
        1    0.000    0.000    0.001    0.001 decoder.py:335(decode)
        1    0.001    0.001    0.001    0.001 decoder.py:346(raw_decode)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'end' of '_sre.SRE_Match' objects}
        2    0.000    0.000    0.000    0.000 {method 'match' of '_sre.SRE_Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
```

[youkidearitai / my-json-parser](https://github.com/youkidearitai/my-json-parser/)

```
         336219 function calls (327771 primitive calls) in 0.088 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    35842    0.011    0.000    0.012    0.000 speedMeasurement.py:59(whitespace)
     9728    0.011    0.000    0.016    0.000 speedMeasurement.py:216(<listcomp>)
     4352    0.009    0.000    0.011    0.000 speedMeasurement.py:70(value_string)
   158730    0.009    0.000    0.009    0.000 {built-in method builtins.chr}
   7425/1    0.009    0.000    0.088    0.088 speedMeasurement.py:263(value)
     6145    0.007    0.000    0.011    0.000 speedMeasurement.py:271(<listcomp>)
     4608    0.007    0.000    0.023    0.000 speedMeasurement.py:207(digit)
    74309    0.005    0.000    0.005    0.000 {built-in method builtins.next}
  768/256    0.005    0.000    0.086    0.000 speedMeasurement.py:23(value_object)
    513/1    0.004    0.000    0.088    0.088 speedMeasurement.py:43(value_array)
     3328    0.002    0.000    0.028    0.000 speedMeasurement.py:206(value_number)
     3328    0.001    0.000    0.023    0.000 speedMeasurement.py:228(fraction)
     4352    0.001    0.000    0.002    0.000 speedMeasurement.py:312(is_nextarray)
     3328    0.001    0.000    0.026    0.000 speedMeasurement.py:240(exponent)
      768    0.001    0.000    0.001    0.000 speedMeasurement.py:190(value_null)
     3072    0.001    0.000    0.001    0.000 speedMeasurement.py:149(colon)
     3072    0.001    0.000    0.001    0.000 speedMeasurement.py:333(is_nextobject)
      352    0.001    0.000    0.001    0.000 speedMeasurement.py:158(value_false)
      416    0.001    0.000    0.001    0.000 speedMeasurement.py:174(value_true)
     4352    0.001    0.000    0.001    0.000 speedMeasurement.py:303(is_emptyarray)
     3072    0.000    0.000    0.000    0.000 speedMeasurement.py:324(is_emptyobject)
     4352    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.088    0.088 <string>:1(<module>)
        1    0.000    0.000    0.088    0.088 {built-in method builtins.exec}
        1    0.000    0.000    0.088    0.088 speedMeasurement.py:9(parse)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 speedMeasurement.py:16(<listcomp>)
```

## 私のアホアホ設計

1. `pathlib` で、`.json` 取得
   1. `read_text(encoding='utf-8')` でテキスト取得
1. 文字列を`list` に
1. `list` の長さで`for` で回す。`Token`化し、文字列分 index を進める
   1. 各型に振り分け
      - `symbols`
        - `[` `{` `:` `,` とか
      - `bool` `null`
      - `str`
        - 最初の`"` を検知して、エスケープを除いた`"` までを取得
      - `number`
      - 空白
1. `Token` のリストを返す
1. `[`, `{`, `]`, `}` を検知して、`nest` を設定
1. `:` を検知して、index の`-1` を`obj_key` に設定
1. `nest` 設定されている`Token` の開始と終了の index を取得
1. `nest` の深さと合わせて`list` で返す
1. `nest` の終始に合わせて、間の`Token` に、`indent` を付与
   - 入れ子構造になっている内部の深さを指定してる
   - 深さが上がる場合に次の要素でしか判断できない
     - ex: 深さが 5 ある場合には、5 の深さの`Token` は、5 回書き換えがある
1. 深さに合わせて、各々のオブジェクトをつくる
   - `_get_arrays` か、`_get_dicts` を起点として再帰的に処理をしてく

# 📝 2022/05/14

Pycharm 先生に怒られてる

```
class TokenType(Enum):
  NUMBER = auto()  # 数値
  STRING = auto()  # 文字列
  BOOLEAN = auto()  # true or false
  NULL = auto()  # null

  L_BRACKET = auto()  # [
  R_BRACKET = auto()  # ]
  L_BRACE = auto()  # {
  R_BRACE = auto()  # }
  COLON = auto()  # :
  COMMA = auto()  # ,

```

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

- 型の付け方適当だけど、あとでちゃんとやる

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
- JSON の BNF
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

テストとして、文字列で json を直接書いていた

```.py
str_json = '{json}'
```

```.py
str_json = r'{json}'
```

`raw` を文字列に直接だと問題がないが、変数扱いだとどうなるだろうかと`raw` の関数がないか調査した。

`repr` があったが、トリプルクオーテーションでは、処理の結果が違っていたりしたので(詳細が適当)

`.json` から読み取ってみることにしている

ぐぬぬ、、、やはり、Python 文字列上でテストするには、raw 文字列つけるの必須かもな。。。

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

```.py
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

JSON の字句解析器みたいなもの

書いていただいた！！！

## 文字列

一旦分割してみる？
