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




wrong_file_list = []


# 파일 타입을 구하기
# 매개변수로 들어온 파일을 바이너리로 변환 후, 파일 타입 확인 후 반환
# rtype: str
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


# 정규식을 통한 파일 내 PI(Personal Information) 탐색
# 탐색된 개인정보를 딕셔너리로 반환 
# rtype = dict
def find_pi(file_name, file_type):
    
    
    if file_type is 'Hangul (Korean) Word Processor File 5.x':
        pass

    
    return searched_pi


if __name__ == '__main__':
    file_name = ''
    pinfo = {}

    # 매개변수가 없는 경우
    if len(argv) == 1:
        print("매개변수를 입력하세요. \'-h, -help\'를 통해 사용법을 확인하세요.")
        exit()


    # 매개변수가 1개인 경우
    elif len(argv) == 2:
        if argv[1] == '-h' or '-help':
            print('-r : 개인정보를 탐색할 범위를 지정합니다. \'-r [file]or[dircetory]\' 형태로 사용합니다.')
            exit()

        if argv[1] == '-r' or '-range':
            print("전체 디렉터리")
    
    # 매개변수가 2개인 경우
    elif len(argv) == 3:
        if argv[1] == '-r' or '-range':
            if argv[2] == 'all':
                print('전체 경로 탐색을 시작합니다.')
                # 탐색 함수 추가
            else:
                file_name = argv[2]
                
                try:
                    is_file = os.path.isfile(file_name)

                except:
                    print('알 수 없는 파일 또는 디렉터리입니다. 경로 또는 이름을 다시 확인하세요.')
                    exit()
                else:
                    if is_file is True: # 파일인 경우
                        file_type = get_ft(file_name)
                        searched_pi = find_pi(file_name, file_type)    
                        
                        exit()
                
                    else:               # 디렉터리인 경우
                        print(f'{argv[2]} 디렉터리를 탐색합니다.')
                        search_directroy()  # 디렉터리 탐색
                        exit()    
                finally:
                    exit()
                    print('[exit] Exception occurred')
                    
        else:
            print('[exit] wrong arguments')
            exit()
    else:
        print('[exit] wrong arguments')
        exit()
