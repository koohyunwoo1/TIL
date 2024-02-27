list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    # '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    # '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    # '난중일기',
    '홍길동전',
    '만복자서포기',
]

missing_book = [book for book in rental_book if book not in list_of_book]
# print(missing_book)
if missing_book:
    # missing_book에 값이 있다?
    for missing in missing_book:
        print(f'{missing} 이 책 없다.')
else:
    # missing_book이 비었다?
    print('책 다있음')
# for missing in missing_book:
#     print(f'{missing}책 없다.')
# else:
#     print('책 다 있음')