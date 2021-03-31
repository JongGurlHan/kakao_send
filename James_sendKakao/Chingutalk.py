from flask import Blueprint
from flask import Flask, request, render_template, redirect, json

bp = Blueprint('chingutalk', __name__)

@bp.route("/chingutalk")
def index_chingutalk():
    return render_template('Chingutalk_sendForm.html')


@bp.route('/sendChingutalk', methods=['POST'])
def sendMessage():    
    token = genToken()

    sender = request.form['sendNum']        
    receiver1 = request.form['receiveNum1']  
    # receiver2 = request.form['receiveNum2']    
    receivers = [receiver1] #, receiver2 
    
    message = request.form['messageContents']
    
    senddate =""

    image_url = request.form['image_url']

    button = request.form.get('button')
  

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
            return render_template('wrongdate_Chingutalk.html')

    basic_send_url = 'https://kakaoapi.aligo.in/akv10/friend/send/'

# -------------------------------------------------------------------------------------------------
# BUTTON
#
# name: 버튼명, 
# linkType: 버튼 링크타입(DS:배송조회, WL:웹링크, AL:앱링크, BK:봇키워드, MD:메시지전달),
# linkTypeName : 버튼 링크 타입네임, ( 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개) 
# linkM: 모바일 웹링크주소(WL일 때 필수), linkP: PC웹링크 주소(WL일 때 필수),
# linkI: IOS앱링크 주소(AL일 때 필수), linkA: Android앱링크 주소(AL일 때 필수)

    name = request.form['btn_name']
    linkType = request.form['tplCode']


    button_info = {'button': [{'name':'name', # 버튼명
                            'linkType':'WL', # DS, WL, AL, BK, MD
                            'linkTypeName' : '웹링크', # 배송조회, 웹링크, 앱링크, 봇키워드, 메시지전달 중에서 1개
                            'linkM':'www.naver.com', # WL일 때 필수
                            'linkP':'www.naver.com', # WL일 때 필수
                            #'linkI': 'IOS app link', # AL일 때 필수
                            #'linkA': 'Android app link' # AL일 때 필수
                    }]}
    obj1 = json.dumps(button_info)

    for i in range(len(receivers)):

        sms_data={'apikey': '3csnnuqcuivb8p0gxylnk1bsrvlaance', #api key
                'userid': 'jameshan', # 알리고 사이트 아이디
                'token': token, 
                'senderkey': 'ef751be96a47782edfe6f483fb2460ab216596a5', # 발신프로파일 키
                'sender' : sender, # 발신자 연락처,
                'senddate': senddate, # YYYYMMDDHHmmss 
                #'advert': 'Y or N', # 광고분류(기본Y)
                'image_url': image_url, # 첨부이미지에 삽입되는 링크
                'receiver_1': receivers[i], # 수신자 연락처
                #'recvname_1': '홍길동1', # 수신자 이름
                'subject_1': '친구톡 제목', # 친구톡 제목 
                'message_1': message, # 친구톡 내용
                'button_1': obj1, # 버튼 정보
                #'failover': 'Y or N', # 실패시 대체문자 전송 여부(템플릿 신청시 대체문자 발송으로 설정하였더라도 Y로 입력해야합니다.)
                #'fsubject_1': '대체문자 제목', # 실패시 대체문자 제목
                #'fmessage_1': '대체문자 내용', # 실패시 대체문자 내용
                #'testMode': 'Y or N' # 테스트 모드 적용여부(기본N), 실제 발송 X
                }

         
        if request.files['file'] :
            f = request.files['file']           
            f.save("H:/HS-APP/James_sendKakao/images/" +secure_filename(f.filename))
            # image_file_name = "H:/HS-APP/James_sendKakao/images/" + secure_filename(f.filename)            
            images = {'image' : open('H:/HS-APP/James_sendKakao/images/' +secure_filename(f.filename), 'rb')} # 첨부 이미지 경로
            images.update({'fimage': open('H:/HS-APP/James_sendKakao/images/suzy.jpg', 'rb')}) # 실패시 첨부이미지 경로
            friend_send_response = requests.post(basic_send_url, data=sms_data, files=images)
            print(friend_send_response.json())
                
        else:                   #when NOTattatcehd image file
            friend_send_response = requests.post(basic_send_url, data=sms_data)
            print(friend_send_response.json())

    return  sms_data  