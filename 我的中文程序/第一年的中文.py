#[character, pin1yin1, part of speech, lesson, definition, notes]
import pandas as 熊猫
'''
中字 = 熊猫.read_csv(filepath_or_buffer = '第一年的中文.csv', sep = '     ', index_col = 0, encoding = 'UTF-8', engine='python')
数据库 = 熊猫.read_json(filepath_or_buffer = database, sep = '     ', index_col = 0, encoding = 'UTF-8', engine='python')
'''
儿子 = 熊猫.read_json('汉字数据库.json', index_col = 0, encoding = 'UTF-8')
print(儿子)

def charcount():
    uniquechar = []
    儿子 = 熊猫.read_json('汉字数据库.json')
    charvocab = 儿子.loc[儿子['character']]
    for item in charvocab:
        for char in item:
            if char not in uniquechar:
                uniquechar = uniquechar + [char]
    return(len(uniquechar))
print(charcount())

#暑假 shu3jia4 & 寒假 han3jia4, database, places, activity, nature, most, healthy  所有的词汇
#vocab https://mandarinwow.wordpress.com/2020/07/04/parts-of-speech-in-mandarin-%EF%BC%88%E8%AF%8D%E7%B1%BB%EF%BC%89/
'''
https://www.sinosplice.com/life/archives/2006/03/20/chinese-parts-of-speech
Content Words (实词 shi2ci2)
    Nouns (名词 ming2ci2)
    Pronouns (代词 dai4ci2)
    Verbs (动词 dong4ci2)
    Auxiliary Verbs (助动词 zhu4dong4ci2)
    Adjectives (形容词 xing2rong2ci2)
    Adverbs (副词 fu4ci2)
    Number Words (数词 shu4ci2)
    Quantifiers (量词 liang4ci2)
    Interjections (叹词 tan4ci2)
    Onomatopoeias (象声词 xiang4shengci2)

Function Words (虚词 xu1ci2)
    Conjunctions (连词 lian2ci2)
    Prepositions (介词 jie4ci2)
    Particles (助词 zhu4ci2)
'''