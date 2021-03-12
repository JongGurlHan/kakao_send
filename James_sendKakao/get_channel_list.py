# -*- coding: utf-8 -*-
import requests
import json
from get_token import genToken

token = genToken()

basic_send_url = 'https://kakaoapi.aligo.in/akv10/profile/list/' 

sms_data={
        'apikey': '3csnnuqcuivb8p0gxylnk1bsrvlaance', #api key
        'userid': 'jameshan', # 알리고 사이트 아이디
        'token': token, # 생성한 토큰
        'plusid': '@퍼포마스', # 카카오채널 아이디(@포함)
        'authnum': '917026', # 발신프로필 인증번호(senderkey)
        'phonenumber': '01084222789', # 카카오채널 알림받는 관리자 핸드폰 번호       
}

request_enrollment_response = requests.post(basic_send_url, data=sms_data)
wholeChannel_list = request_enrollment_response.json()['list']

def get_channel_list():
    for list in wholeChannel_list:
        return list['uuid']





