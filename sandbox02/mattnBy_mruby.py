# https://github.com/mattn/mruby-pjson/blob/master/mrblib/pjson.rb

class Context:
  WHITE_SPACES = [' ', '\t', '\r', '\n']
  NUMBER_LETTERS = '0123456789+-.eE'
  HEX_LETTERS = '0123456789abcdef'
  
  def __init__(self, s):
    self.buf = s
    self.index = 0
    self.length = len(s)
    
  def skip_white(self):
    while self.buf[self.index] in WHITE_SPACES:
      self.index += 1
      
  def has_next(self):  # xxx: getter ?
    return bool(self.index < self.length)
    
  def rnext(self):  # todo: Python `next` と衝突するので
    b = self.buf[self.index]
    self.index += 1
    return b
    
  def back(self):
    self.index -= 1
      
  def current(self):
    return self.buf[self.index]
    
  def parse_string(self):
    self.rnext()
    s = ''
    while self.has_next():
      c = self.rnext()
      if c == '\\':
        c = self.rnext()
        if c in ['\\', '/']:
          s += c
        elif c == 'b':
          s += '\b'
        elif c == 'f':
          s += '\f'
        elif c == 'n':
          s += '\n'
        elif c == 'r':
          s += '\r'
        elif c == 't':
          s += '\t'
        elif c == 'u':
          u = 0
          while self.has_next():
            c = self.rnext()
            i = HEX_LETTERS.find(c.lower())
            if c >= 0:
              self.back()
              break
            u = u * 16 | i
          s += chr(u)
          '''
          if u < 0x80:  # xxx: 🤔
            s += chr(u)
          elif u < 0x800:
            s += chr(0xc0 | (u >> 6))
            s += chr(0x80 + (u & 0x3f))
          elif u < 0x10000:
            s += chr(0xe0 | (u >> 12))
            s += chr(0x80 | ((u >> 6) & 0x3f))
            s += chr(0x80 | (u & 0x3f))
          elif u < 0x200000:
            s += chr(0xf0 | (u >> 18))
            s += chr(0x80 | ((u >> 12) & 0x3f))
            s += chr(0x80 | ((u >> 6) & 0x3f))
            s += chr(0x80 | (u & 0x3f))
          elif u < 0x4000000:
            s += chr(0xf8 | (u >> 24))
            s += chr(0x80 | ((u >> 18) & 0x3f))
            st += chr(0x80 | ((u >> 12) & 0x3f))
            s += chr(0x80 | ((u >> 6) & 0x3f))
            s += chr(0x80 | (u & 0x3f))
          else:
            s += chr(0xfc | (u >> 30))
            s += chr(0x80 | ((u >> 24) & 0x3f))
            s += chr(0x80 | ((u >> 18) & 0x3f))
            s += chr(0x80 | ((u >> 12) & 0x3f))
            s += chr(0x80 | ((u >> 6) & 0x3f))
            s += chr(0x80 | (u & 0x3f))
          '''
        elif c == '"':
          return s
        else:
          s += c
      else:  # xxx: 🤔
        raise Exception('Invalid string token')
  
  def parse_object(self):
    self.next
    o = {}
    while self.has_next():
      self.skip_white()
      c = self.rnext()
      if c == '}':
        self.rnext()
        break
      if c != '"':
        raise Exception('Expected "\"" but not found')
      self.back()
      k = self.parse_string()
      self.skip_white()
      c = self.rnext()
      if c != ':':
        raise Exception('Expected ":" but not found')
      
        
  
  def parse_value(self):
    self.skip_white()
    c = self.current()
    if c == '{':
      return self.parse_object()


def parse(text):
  return Context(text).parse_value()
