from argparse import FileType
import magic
import os


def get_ft(file_name):
    if file_name is None:
        return False

    try:
        file_type = magic.from_file(file_name)   # 매직 넘버를 기반으로 파일 타입 확인
    except:
        print("파일의 시그니쳐를 얻어오지 못했습니다.")
        file = {file_name:file_type}
        return file 
    return file_type


def search_dir(dir_path):
    files = os.listdir(dir_path)
    return files


def zz():
    print(zz)