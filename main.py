import time, argparse, subprocess

# Class 호출.
from app.data_crawling import DataCrawling
from app.data_logging import logging

# 명령줄에서 설정한 인자를 파싱하는 함수.
def parse_args() -> argparse.Namespace:
    '''
    Args:
        None.
    Returns:
        argparse.Namespace: 명령줄 인자를 속성으로 가지는 객체.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_uri',
        type=str,
        required=True,
        help='재생목록이 실행된 Youtube Music URI.'
    )
    return parser.parse_args()

# 메인 함수.
def main():
    # 기록을 위한 logger 생성.
    logger = logging._get_log()

    # 명령줄의 인자를 파싱.
    args = parse_args()

    # 크롤링 클래스의 인스턴스 생성.
    crawling = DataCrawling(uri=args.input_uri)

# 실행 코드.
if __name__ == '__main__':
    main()