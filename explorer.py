"""
    TODO: 
        * 디렉터리 탐색 알고리즘 구현 
        * 정규식을 이용한 파일 탐색 구현

"""

from ast import arg
from pathlib import Path
import struct
import os
from sys import argv, exit

import magic


file_name = './test/test.hwp'
pinfo = {}

wrong_file_list = []


# 파일 타입 구하기
def get_ft(file_name):
    if file_name is None:
        return False

    try:
        file_type = magic.from_file(file_name)   # 매직 넘버를 기반으로 파일 타입 확인
    except:
        wrong_file_list.append(file_name) 
        print("파일의 시그니쳐를 얻어오지 못했습니다.")
    else:
        print(f"file path:{file_name}")
        print(f"file type:{file_type}")
    
    return file_type 
