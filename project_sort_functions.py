#-*- coding:utf-8 -*-

from project_functions import *

sort_map=[
    ('번호순', sort_by_num),
    ('이름순', sort_by_name),
    ('점수내림차순', sort_by_reverse_score),
    ('점수오름차순', sort_by_score)
    ]

sort_list=[x[0] for x in sort_map]
