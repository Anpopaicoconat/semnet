# -*- coding: utf-8 -*-
import pymorphy2
import nltk
import string
morph = pymorphy2.MorphAnalyzer()
soiusi=['что', 'и', 'или']
def podlejashee(word):
    pass


class _text():
    def __init__(self, text):
        self.str_sentences_list = text.split('.')#список предложений в строковом типе
        self.cls_sentences_list = []#список объектов класса _sentence
        for str_sentence in self.str_sentences_list:
            cls_sentence = _sentence(str_sentence)
            self.cls_sentences_list.append(cls_sentence)

    

        



class _sentence():
    def __init__(str_in):#в качестве ключа для словаря тагов предложения использовать кортеж словоб индексс тк слова могут повторяться
        self.sentence = []
        self.invariants=[]
        tokens = nltk.word_tokenize(str_in)
        self.tag_dict = {}#словарь тк у одинаковых токенов один и тот же тэг
        for token in sentence:
            p = morph.parse(token)
            self.tag_dict[token] = []
            for itag in p:
                ru_tag = itag.tag.cyr_repr
                self.tag_dict[token].append(ru_tag)
        def rec(sentence):
            tokens = nltk.word_tokenize(sentence)

            

            #анализ сложности предложения
            if ',' in tokens:#предложение содержит запятую
                next = tokens[tokens.index(',')+1]#токен после запятой
                if 'СОЮЗ' in self.tag_dict[next]:#если после запятой стоит союз 
                    if next in pod: #сложноподчиненное предложение
                        list = sentence.text_split(',')#выделяем известную нам клаузу
                        self.sentence.append(list[0])#заносим ее в список клауз предложения
                        rec(list[1])#проверяем остальную часть предложения
                    else: #ССП или простое осложненное
                        if 'а' or 'но' in next: 
                            pass #Спорный момент либо простое осложнённое, либо ССП
                        else:
                            for token in tokens:
                                tags = tag_sentence([token])
                                for tag in tags:
                                    pass
                else:#предложение сложное безсоюзное или простое осложненное
                    pass
            else:#предложение простое
                pass
            
            self.tokens = tokens


        





    def tag_sentence(self):
        out = {}
        for token in sentence:
            p = morph.parse(token)
            out[token] = []
            for itag in p:
                ru_tag = itag.tag.cyr_repr
                out[token].append(ru_tag)
        return out 



print('start')
pod = ['так как', ' потому что', ' поскольку', ' оттого что', ' ввиду того что', ' благодаря тому что',\
   ' вследствие того что', ' в связи с тем что', ' в силу того что', ' ибо', ' затем что', ' так что', ' а то',\
  ' а не то', ' чтобы', ' чтоб', ' для того чтобы', ' с тем чтобы', ' затем чтобы', ' дабы', ' если', ' если бы',\
 ' если б', ' раз', ' ли', ' коль скоро', ' ежели (бы', ' б)', ' коли', ' кабы', ' когда бы', ' когда б', ' хотя',\
' хоть; даром что; только бы', ' лишь бы; несмотря на то что', ' невзирая на то что; хотя бы', ' хоть бы', ' пусть',\
' пускай; в то время как', ' между тем как', ' тогда как; добро бы', ' пускай бы; только', ' правда', ' едва',\
' едва только', ' как только', ' как', ' когда', ' лишь', ' лишь только', ' по мере того как', ' после того как',\
' с тех пор как', ' пока', ' пока не', ' покамест', ' покамест не', ' покуда', ' покуда не', ' прежде нежели',\
' прежде чем', ' только', ' только что', ' чуть лишь', ' чуть', ' чуть только', ' до того как', ' в то время как',\
' как', ' что', ' будто', ' будто бы', ' как будто', ' как будто бы', ' словно (как)', ' подобно тому как', ' точно',\
' ровно (как)', ' чем', ' нежели', ' что', ' чтобы', ' будто бы', ' как']





predicat = []
subject = []
text = 'Какой бы интересной ни была домашняя и школьная жизнь ребенка, не прочти он драгоценных книг – он обделён. Такие утраты невосполнимы. Это взрослые могут прочесть книжку сегодня или через год – разница невелика. В детстве счет времени ведется иначе, тут каждый день – открытия. И острота восприятия в дни детства такова, что ранние впечатления могут влиять потом на всю жизнь. Впечатления детства – самые яркие и прочные впечатления. Это фундамент будущей духовной жизни, золотой фонд.'
text_test1 = 'Какой бы интересной ни была бы жизнь ребёнка, не прочти он книг, его жизнь будет неполной. Взрослые могут прочитать книгу сегодня или завтра, а в детстве время идёт совсем иначе. Каждый день - это целое открытие. Так что прочитанная книга может оказать влияние на всю оставшуюся жизнь.'
text_test2 = '''На цирковую арену выбежала девочка с синими синими глазами а вокруг них были длинные ресницы она была в 
серебряном платье и также у этой девочки были длинные руки она вскочила на огромный шар который стоял посередине и 
вдруг побежала. Шар начал крутится в разные стороны девочка бегала по этому шару назад налево в общем куда она хотела 
так девочка остановилась какое-то мгновение ей подали разные браслеты она надела их себе на руки и стала танцевать 
тут потушили свет и все удивились потому что девочка светилась в темноте'''
text_s = 'что и когда или а но да'






sentences = text_split(text)
for sentence in sentences:
    print(sentence)

print('\n\n\n\ntags\n')
for sentence in sentences:
    print('\n\n=============================================================================\
    new sentence==========================================================================')
    predicat = []
    subject = []
    tags = tag_sentence(sentence)
    for token in tags:
        for gramem in tags[token]:
            gramem = gramem.split(',')

            if 'им' in gramem and 'СУЩ' in gramem and token.lower() != 'и':
                subject.append(token)
            if 'ГЛ' in gramem or token =='–':
                predicat.append(token)
        print(token, tags[token], '\n')
    print('\nsubject=', subject, '\n\npredicat=', predicat)



#for i in morph.parse('помидор'):
    #print(i.tag.cyr_repr)
    