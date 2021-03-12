# -*- coding: utf-8 -*-
import requests
import json
from get_token import genToken

token = genToken()

basic_send_url = 'https://kakaoapi.aligo.in/akv10/template/list/' # 요청을 던지는 URL, 등록된 템플릿 리스트

sms_data={'apikey': '3csnnuqcuivb8p0gxylnk1bsrvlaance', #api key
        'userid': 'jameshan', # 알리고 사이트 아이디
        'token': token, # 생성한 토큰
        'senderkey': 'ef751be96a47782edfe6f483fb2460ab216596a5' # 발신프로필 키
}

template_list_response = requests.post(basic_send_url, data=sms_data)


wholeTemplateInfo = template_list_response.json() #전체 템플릿 정보 

wholeTemplateList = wholeTemplateInfo['list'] #템플릿 컨텐츠 리스트


def getTemplateMessage(tpl_code):
        for list in wholeTemplateList:
                if tpl_code == list.get('templtCode'):                       
                        return (list.get('templtContent'))
        





