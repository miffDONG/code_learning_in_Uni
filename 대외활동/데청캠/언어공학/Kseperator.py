# 초성이 되는 자음 목록
choseong_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성이 되는 모음 목록
joongseong_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성의 경우 자음도 되고, 이중자음도 가능하며 없을 수도 있음.(공백)
jongseong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def decompose(word):
    # 분리한 자모를 저장할 빈 배열
    word_list = []
    for letter in list(word.strip()): # 공백 제거 필요
        if '가' <= letter <= '힣':
            # 588개마다 초성이 바뀜.
            char1 = (ord(letter) - ord('가')) // 588
            # 중성은 28가지 종류
            char2 = ((ord(letter) - ord('가')) - (588 * char1)) // 28
            char3 = ((ord(letter) - ord('가')) - (588 * char1)) - 28 * char2
            # 분리한 자모를 word_list에 추가
            # 초성, 중성, 종성을 각각 저장
            word_list.append([choseong_list[char1], joongseong_list[char2], jongseong_list[char3]])
        else:
            word_list.append([letter])
    return word_list

def compose(word):
    word_list = []
    for char_list in word:
        # 문자열 리스트에서 자모를 추출
        char1, char2, char3 = char_list[0], char_list[1], char_list[2]
        if char1 in choseong_list and char2 in joongseong_list and char3 in jongseong_list:
            # 자모를 조합하여 문자로 변환 후 word_list에 추가
            char_code = ord('가') + (choseong_list.index(char1) * 588) + (joongseong_list.index(char2) * 28) + jongseong_list.index(char3)
            character = chr(char_code)
            word_list.append(character)
        else:
            word_list.append(char_list[0])

        print(word_list)
    composed_word = ''.join(word_list)
    return composed_word

# string = input('자모를 해체할 문자열을 입력하세요: ')

# print(decompose(string))

# print(compose(decompose(string)))