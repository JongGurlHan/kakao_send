from PySide2.QtWidgets import QMessageBox

 

# QMessageBox를 msgBox로 저장하여, 필요한 내용들을 setting 한다.


msgBox = QMessageBox()

msgBox.setWindowTitle("Alert Window") # 메세지창의 상단 제목

msgBox.setWindowIcon(QtGui.QPixmap("info.png")) # 메세지창의 상단 icon 설정

msgBox.setIcon(QMessageBox.Information) # 메세지창 내부에 표시될 아이콘

msgBox.setText("This is title") # 메세지 제목

msgBox.setInformativeText("This is content") # 메세지 내용

msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel) # 메세지창의 버튼

msgBox.setDefaultButton(QMessageBox.Yes) # 포커스가 지정된 기본 버튼

 

msgBox.exec_() # 클릭한 버튼 결과 리턴