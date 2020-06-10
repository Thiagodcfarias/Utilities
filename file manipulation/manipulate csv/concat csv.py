# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:28:20 2020

@author: ThiagoD
"""
import pandas as pd

path = "path/arc.csv"


entity = pd.read_csv(path)
entity_temp = pd.DataFrame()
entity_temp['value'] = entity.value.str.replace('d0','d')
entity_temp['code'] = entity['code']

entity_temp = entity_temp[entity_temp.value.str[0] == 'd']

final_csv = pd.concat([entity, entity_temp], axis=0)

final_csv.to_csv(path[:-9] + 'finalDpto.csv',index = False)
