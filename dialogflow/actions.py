from .crawlings import 상한가_크롤링, 테마별_시세_크롤링


def stock_search(stock_search_term):
    if stock_search_term == '상한가 종목':
        speech = 상한가_크롤링()

    elif stock_search_term == '테마별 시세':
        speech = 테마별_시세_크롤링()
    else:
        speech = '다시 입력해 주세요'

    return speech