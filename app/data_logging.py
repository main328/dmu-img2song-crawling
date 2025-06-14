import os, logging
from datetime import datetime

class DataLogging:
    def __init__(self):
        # log 파일의 이름을 '생성일자_생성시간_log'로 생성.
        self._time = datetime.now().strftime('%Y%m%d%H%M%S')
        self._path = 'statements/logs'
        self._name = f'{self._path}/{self._time}.log'

        # 디렉토리가 없으면 생성.
        if not os.path.exists(self._path):
            os.makedirs(self._path)

        # Logger 인스턴스화 진행.
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        # 인스턴스화 진행 시 설정 함수 자동 실행.
        self._set_log()
    
    def _set_log(self):
        # log 출력 형식 지정.
        format_log = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        # 콘솔 핸들러 생성 및 설정.
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(format_log)
        # 파일 핸들러 생성 및 설정.
        file_handler = logging.FileHandler(self._name, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(format_log)
        # 생성한 handler를 logger에 연결.
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)
    
    def _get_log(self):
        return self._logger

logging = DataLogging() # type: ignore