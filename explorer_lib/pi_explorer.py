import olefile 
import re



def find_pi(file_name, file_type, regexp_li):
    regexp_li = regexp_li
    
    
    

    if 'Hangul' in file_type: 
        result = find_pi_hwp(file_name)
        return result

    elif 'doc' in file_type:
        result = find_pi_msword(file_name)
        return result

    elif 'pdf' in file_type:
        result = find_pi_pdf(file_name)
        return result

    elif 'excel' or 'csv' in file_type:
        result = find_pi_excel(file_name)
        return result

    elif 'doc' in file_type:
        result = find_pi_ppt(file_name)
        return result

    elif 'doc' in file_type:
        result = find_pi_txt(file_name)
        return result

    else:
        print(f'{file_type}은 지원되지 않는 문서 형식 입니다.')
        return False
        
    
    
    


def find_pi_hwp(file_name):
    file = olefile.OleFileIO(file_name)
    encoded_text = file.openstream('PrvText').read()
    decoded_text = encoded_text.decode('utf-16')
    
    
    

def find_pi_msword(file_name):
    pass


def find_pi_pdf(file_name):
    pass


def find_pi_excel(file_name):
    pass


def find_pi_ppt(file_name):
    pass


def find_pi_txt(file_name):
    pass



if __name__ == '__main__':
    file_name = './test/test.hwp'
    file_type ='Hangul'

    find_pi(file_name, file_type)