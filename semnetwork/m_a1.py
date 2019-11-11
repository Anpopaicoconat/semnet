# -*- coding: utf-8 -*-
import pymorphy2
import nltk
import string
morph = pymorphy2.MorphAnalyzer()

def splitcomplex(list, i):
        index = i.find(',')
        l1 = i[index+1:]
        l2 = i[:index]
        list.append(l2)
        list.append([l1])

def splithomo(list, i):#dobavit simvol_
    new = i.replace(',', " _")
    list.append ([new])

def rekurs(list, key):
        for i in list:
            if type(i) is str:
                
                if zpt(i):#если есть запятая
                    print('zpt')
                    if spp(i):#скорее всего сложноподчиненное
                        print('скорее всего сложноподчиненное')
                        splitcomplex(list, i)
                    elif ssp(i):#сложносочиненное или однородные
                        print('сложносочиненное или однородные')
                        splitcomplex(list, i)
                        splithomo(list, i)
                    else:#сложное безсоюзное или осложненное
                        print('сложное безсоюзное или осложненное')
                        splitcomplex(list, i)
                        splithomo(list, i)
                        pass
                else:#если нет запятой
                    if str_sentences_d[key] == '':
                        str_sentences_d[key] = 'простое, неососложенное'


            else:
                rekurs(i, key)
        return list




def zpt(i):
    if ',' in i:
        return True
    else:
        return False



def ssp(i):
    token = nltk.word_tokenize(i)
    if token[token.index(',')+1] in ssps_list:
        return True
    else:
        return False

def spp(i):
    token = nltk.word_tokenize(i)#переписать через трай
    index1 = 0
    if len(token)-token.index(',')>6:#если после запятой больше 6 слов
        r = 6
    else:
        r = len(token)-token.index(',')

    for i in range(r):
        index1+=1
        soius = token[token.index(',')+1:token.index(',')+index1+1]
        s = ' '.join(soius)
        print('s=', s)
        if s in spps_set:
            return True

    else:
        return False


ssps_list = ['и', 'да', 'тоже', 'также', 'а', 'но', 'зато', 'зато', 'или', 'либо']

spps_list1=['ибо', 'чтобы', 'чтоб', 'дабы', 'если', 'раз', 'ли', 'ежели', ' коли', 'кабы', ' хотя', \
    'хоть', 'пусть', 'пускай', 'как', 'покуда', 'чуть', 'что', 'чем', 'поскольку'] #требуется дороботка

spps_list2 = ['так как', 'потому что', 'оттого что', 'ввиду того что', 'благодаря тому что',\
'вследствие того что', 'в связи с тем что', 'в силу того что', 'ибо', 'затем что', 'так что', 'а то',\
'а не то', 'чтобы', 'чтоб', 'для того чтобы', 'с тем чтобы', 'затем чтобы', 'дабы', 'если', 'если бы',\
'если б', 'раз', 'ли', 'коль скоро', 'коли', 'кабы', 'когда бы', 'когда б', 'хотя',\
'хоть', 'даром что', 'только бы', 'лишь бы', 'несмотря на то что', 'невзирая на то что', 'хотя бы', 'хоть бы', 'пусть',\
'пускай', 'в то время как', 'между тем как', 'тогда как', 'добро бы', 'пускай бы', 'только', 'правда', 'едва',\
'едва только', 'как только', 'как', 'когда', 'лишь', 'лишь только', 'по мере того как', 'после того как',\
'с тех пор как', 'пока', 'пока не', 'покамест', 'покамест не', 'покуда', 'покуда не', 'прежде нежели',\
'прежде чем', 'только', 'только что', 'чуть лишь', 'чуть', 'чуть только', 'до того как', 'в то время как',\
'как', 'что', 'будто', 'будто бы', 'как будто', 'как будто бы', 'словно', 'подобно тому как', 'точно',\
'чем', 'нежели', 'что', 'чтобы', 'будто бы', 'как']
spps_set={'в связи с тем что', 'как только', 'покамест', 'несмотря на то что', 'когда', 'для того чтобы', 'затем что', 'пока', 'покуда не', 'прежде нежели', 'хоть бы', 'дабы', 'даром что', 'только', 'а то', 'оттого что', 'когда б', 'пускай бы', 'лишь только', 'словно', 'нежели', 'в то время как', 'покамест не', 'пока не', 'хотя', 'по мере того как', 'будто', 'пускай', 'только что', 'коль скоро', 'коли', 'с тех пор как', 'покуда', 'чем', 'ввиду того что', 'правда', 'точно', 'так как', 'хотя бы', 'хоть', 'кабы', 'так что', 'а не то', 'лишь бы', 'только бы', 'едва', 'благодаря тому что', 'как будто', 'невзирая на то что', 'затем чтобы', 'если', 'чуть', 'что', 'когда бы', 'лишь', 'как будто бы', 'если б', 'прежде чем', 'чтоб', 'ибо', 'как', 'добро бы', 'чуть лишь', 'в силу того что', 'если бы', 'пусть', 'подобно тому как', 'между тем как', 'потому что', 'после того как', 'раз', 'чуть только', 'будто бы', 'до того как', 'ли', 'едва только', 'с тем чтобы', 'чтобы', 'тогда как', 'вследствие того что'}


str_sentences_d={"я пошел, поскольку было холодно":None}
print(rekurs(["я сказал, что на улице холодно и идет дождь"], "я сказал, что на улице холодно и идет дождь"))