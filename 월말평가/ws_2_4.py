information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

'''
- 작가와 작품 목록 참고
- 허균 : 홍길동전, 장생전, 도문대작
- 임제 : 수성지, 백호집, 원생몽유록
- 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
'''

information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[2]
information[authors[4]] = books[0]

for k,v in information.items():
    print(f'{k} : {v}')
    
#딕셔너리의 키와 값을 이해한다
#딕셔너리의 items() 메서드를 이해한다