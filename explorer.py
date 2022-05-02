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


# 현재 디렉터리 탐색
def search_directroy(directory):
    pass


# 정규식을 통한 파일 내 개인정보 탐색 
def search_pi(file):
    type = get_ft(file)
    pass


if __name__ == '__main__':    
    if len(argv) == 1:
        print("-> [specific reason] 실행인자가 없습니다. \'-h, -help\'를 통해 사용법을 확인하세요.")
        exit()

    elif len(argv) == 2:
        if argv[1] == '-h' or '-help':
            print('-r : 개인정보를 탐색할 범위를 지정합니다. \'-r [file]or[dircetory]\' 형태로 사용합니다.')
            exit()

        if argv[1] == '-r' or '-range':
            print("전체 디렉터리")
    
    elif len(argv) == 3:
        if argv[1] == '-r' or '-range':
            if argv[2] == 'all':
                print('전체 경로 탐색을 시작합니다.')
                # 탐색 함수 추가
            else:
                if os.path.isfile(argv[2]) is True:
                    print(f'{argv[2]}파일을 탐색합니다.')
                    # 탐색 함수 추가
                elif os.path.isfile(argv[2]) is False:
                    print(f'{argv[2]} 디렉터리를 탐색합니다.')
                    # 탐색 함수 추가                          
                else:
                    print('알 수 없는 파일 또는 디렉터리 입니다.')
                    exit()

    else:
        print('[exit] wrong arguments.')
        exit()
# python dev.py -r all
# python dev.py -r "[dir_path]"
# python dev.py -r "[file_path]"