# -*- coding: utf-8 -*-

from pymmseg import mmseg

mmseg.dict_load_defaults()
text = "今天很开心大家好"
algor = mmseg.Algorithm(text)
for tok in algor:
    print '%s [%d...%d]' % (tok.text, tok.start, tok.end)
