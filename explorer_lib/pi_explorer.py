"""
    TODO: 
        * 이미지가 존재한다면 OCR로 이미지 추출하기
"""

import olefile 
import re



class PI_Explorer():
    def __init__(self):
        pass
    

    def find_pi(self, file_name, file_type, regexp_li):
        
        print(file_name)
        print(file_type)

        if 'Hangul' in file_type: 
            result = self.__find_pi_hwp(file_name)
            
            return result

        elif 'doc' in file_type:
            result = self.__find_pi_msword(file_name)
            
            
            return result

        elif 'pdf' in file_type:
            result = self.__find_pi_pdf(file_name)
            
            
            return result

        elif 'excel' in file_type or 'csv' in file_type:
            result = self.__find_pi_excel(file_name)
                        
            return result

        elif 'ppt' in file_type:
            result = self.__find_pi_ppt(file_name)
            return result

        elif 'txt' in file_type:
            result = self.__find_pi_txt(file_name)
            return result

        else:
            print(f'{file_type}은 지원되지 않는 문서 형식 입니다.')
            return False
        

    def __find_pi_hwp(self, file_name):
        file = olefile.OleFileIO(file_name)
        
        encoded_data = file.openstream('PrvText').read()
        decoded_data = encoded_data.decode('utf-16')
        # img = file.openstream('PrvImage').read()
        return decoded_data 


    def __find_pi_msword(self, file_name):
        pass
        

    def __find_pi_pdf(self, file_name):
        pass


    def __find_pi_excel(self, file_name):
        pass


    def __find_pi_ppt(self, file_name):
        pass

    def __find_pi_txt(self, file_name):
        pass



if __name__ == '__main__':
    file_name = './test/test.docx'
    file_type ='doc'
    regexp_li = ''




    px = PI_Explorer()

    temp = px.find_pi(file_name, file_type, regexp_li)
    
    print(temp)


    

    

