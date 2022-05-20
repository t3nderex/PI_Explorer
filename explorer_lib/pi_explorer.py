"""
    TODO: 
        * 이미지가 존재한다면 OCR로 이미지 추출하기
"""

import olefile 
import re
from docx import Document


class PI_Explorer():
    def __init__(self):
        pass
        

    def find_pi(self, file_name, file_type, regexp_li):
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
        """ 한글 문서 내 문자열 추출

        Args:
            file_name (str): 한글 문서의 경로

        Returns:
            list: 문서 내 텍스트 데이터

        TODO:
            * 표 내의 글 읽기
            * 이미지 읽기 -> OCR 처리
            
        """
        file = olefile.OleFileIO(file_name)
        
        encoded_data = file.openstream('PrvText').read()
        decoded_data = encoded_data.decode('utf-16')

        # img = file.openstream('PrvImage').read()
        return decoded_data 


    def __find_pi_msword(self, file_name):
        """ doc, docx 파일 내 문자열 추출
        
        Args:
            file_name (str): 문서의 경로

        Returns:
            list: 문서 내의 모든 텍스트

        TODO:
            * 이미지 읽기 -> OCR처리
        """
        data = []
        doc = Document(file_name)
        text_data = [paragraph.text for paragraph in doc.paragraphs]

        tables = doc.tables
        tables_data = []
        table_data = [cell.text for table in tables for row in table.rows for cell in row.cells]
        
        for txt_data in text_data:
            data.append(txt_data)
        for tb_data in table_data:
            data.append(tb_data)

        return data
        

    def __find_pi_pdf(self, file_name):
        pass


    def __find_pi_excel(self, file_name):
        pass


    def __find_pi_ppt(self, file_name):

        pass

    def __find_pi_txt(self, file_name):
        pass



if __name__ == '__main__':
    file_name = './test/test.hwp'
    file_type ='Hangule'
    regexp_li = ''

    

    


    px = PI_Explorer()
    
    temp = px.find_pi(file_name, file_type, regexp_li)

    print(temp)


    

    
