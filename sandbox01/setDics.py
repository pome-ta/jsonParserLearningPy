'''
sample_str = '{"hoge": "fuga"}'

s_lbr = '{'
s_key = 'hoge'
s_cm = ':'
s_value = 'fuga'
s_rbr = '}'


dic = {'piyo': 'baa'}
obj_dic = {s_key: s_value}
dic.update(obj_dic)
'''

dic1 = {'d': 1}
dic2 = {'b': 2}
dic1.update(**dic2)

lll = [[1,2],[4,2],[1,5]]
#llr = [l for l in lll]
llr = lll
llr[2] = 'a'



print(lll)
print(*lll)


class Hoge:
  def __init__(self, *lis):
    self.lis = lis


hoge = Hoge('a')

