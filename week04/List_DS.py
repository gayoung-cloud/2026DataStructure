# artists = []
artists = list()
print(artists)
artists.append("리센느") # append는 list의 맨 뒤에 새로운 데이터를 추가하는 기능 상자
print(artists)
artists.append("핑클")
print(artists)
artists.append("데이식스")
print(artists)
print(artists.pop(1)) # 언제나 0부터 시작이므로 핑클 뽑아내 삭제
print(artists)