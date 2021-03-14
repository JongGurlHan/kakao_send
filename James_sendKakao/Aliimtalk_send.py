from flask import Flask, request, render_template, redirect
from datetime import datetime, timedelta
import requests
import json

from Alimtalk_checkList import getTemplateMessage
from get_token import genToken  #token 생성

app = Flask("__name__")

@app.route('/alimtalk')
def index_alimtalk():

    token = genToken()

    ###템플릿 조회#####
    basic_send_url = 'https://kakaoapi.aligo.in/akv10/template/list/'

    sms_data={'apikey': '3csnnuqcuivb8p0gxylnk1bsrvlaance', #api key
            'userid': 'jameshan', # 알리고 사이트 아이디
            'token': token, # 생성한 토큰
            'senderkey': 'ef751be96a47782edfe6f483fb2460ab216596a5' # 발신프로필 키
    }
    template_list_response = requests.post(basic_send_url, data=sms_data)
    wholeTemplateInfo = template_list_response.json() #전체 템플릿 정보 조회 
    wholeTemplateList = wholeTemplateInfo['list'] #템플릿 컨텐츠 리스트 조회   
        
    return render_template('Alimtalk_sendForm.html', lists = wholeTemplateList)



@app.route('/sendAlimtalk', methods = ['POST'])
def sendMessage1():
        
    token = genToken()
    sender = request.form['sendNum'] 
        
    receiver1 = request.form['receiveNum1']
    receiver2 = request.form['receiveNum2']
    receivers = [receiver1, receiver2]


    tpl_code = request.form.get('template')
    message_1 = getTemplateMessage(tpl_code)


    senddate =""

    if request.form["sendingtime"] == "timeNow":
        pass
    else: 
        senddate = request.form['date']+request.form['hour']+request.form['min']+"00"
        
        #====Show error page if user input wrong time====
        send_year = int(request.form['date'][:4])
        send_mon = int(request.form['date'][4:6])
        send_date = int(request.form['date'][6:8])
        send_hour = int(request.form['hour'])
        send_min = int(request.form['min'])
        send_sec = int("00")
        
        timeInput = datetime(send_year, send_mon, send_date, send_hour, send_min, send_sec)
        timeNow = datetime.now()
        timeDiff = (timeInput - timeNow).seconds
        if timeDiff < 600:
            return render_template('wrongdate_Alimtalk.html')

    basic_send_url = 'https://kakaoapi.aligo.in/akv10/alimtalk/send/' # 요청을 던지는 URL, 알림톡 전송

    button_info = {'button': [{'name':'name', # 버튼명
                        'linkType':'WL', # DS, WL, AL, BK, MD
                        'linkTypeName' : '웹링크', # 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개
                        'linkM':'https://smartsms.aligo.in/ ', # WL일 때 필수
                        'linkP':'https://smartsms.aligo.in/ ', # WL일 때 필수
                        #'linkI': 'IOS app link', # AL일 때 필수
                        #'linkA': 'Android app link' # AL일 때 필수
                }]}

       
    for i in range(len(receivers)):
        
        #button_info = json.dumps(button_info) # button의 타입은 JSON 이어야 합니다.
        sms_data={'apikey': '3csnnuqcuivb8p0gxylnk1bsrvlaance', #api key
            'userid': 'jameshan', # 알리고 사이트 아이디
            'token': token, # 생성한 토큰
            'senderkey': 'ef751be96a47782edfe6f483fb2460ab216596a5', # 발신프로파일 키
            'tpl_code': tpl_code, # 템플릿 코드
            'sender' : sender, # 발신자 연락처,
            #'senddate': '19000131120130', # YYYYMMDDHHmmss
            'receiver_1': receivers[i], # 수신자 연락처
            #'recvname_1': '홍길동1', # 수신자 이름
            'subject_1': 'Join', # 알림톡 제목 - 수신자에게는 표기X
            'message_1': message_1, # 알림톡 내용 - 등록한 템플릿이랑 개행문자 포함 동일하게 입력.
            # 'button_1': button_info, # 버튼 정보
            #'failover': 'Y or N', # 실패시 대체문자 전송 여부(템플릿 신청시 대체문자 발송으로 설정하였더라도 Y로 입력해야합니다.)
            #'fsubject_1': '대체문자 제목', # 실패시 대체문자 제목
            #'fmessage_1': '대체문자 내용', # 실패시 대체문자 내용
            #'testMode': 'Y or N' # 테스트 모드 적용여부(기본N), 실제 발송 X
        }
            
        alimtalk_send_response = requests.post(basic_send_url, data=sms_data)
        print(alimtalk_send_response.json())
    
 

    return sms_data

if __name__ == '__main__':
    app.run(port=5050, debug=True)