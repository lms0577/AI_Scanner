# YOLO format dataset 생성 툴
<div>
<img src="https://user-images.githubusercontent.com/55565351/90864418-97086f00-e3cb-11ea-9bbc-f180db242b3b.png" width="400" height="300"/>
</div>

## 툴 개요
* YOLO 포멧의 데이터셋을 만들기 위한 툴
* 이미지의 객체에 바운딩 박스를 그리고 레이블을 표시한다.
* 이미지에 대한 바운딩 박스와 레이블 정보를 .txt 파일로 저장한다.
* 훈련시킬 모든 이미지에 대한 경로를 .txt 파일로 저장한다.

## 실행 환경
제목 | 내용
--------- | --------
OS | Windows(Anaconda) & Linux
언어 | Python 3.6
라이브러리 | OpenCV 4.2.0

## 사용 방법
* **1st**
  + config.txt 파일 설정
    + classes:	 클래스(레이블)의 개수 설정
    + name:	 클래스(레이블)의 각각 이름 설정
    + img_path: 	 이미지가 있는 폴더 경로 설정(절대 경로로 설정)
    + train_txt_path: 훈련시킬 모든 이미지에 대한 경로 파일을 저장할 위치 설정
  + 예제 사진
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90866254-991ffd00-e3ce-11ea-8922-ac10ca46c21a.png" width="320" height="240"/>
       </div>

* **2nd**
  + generate_yolo_dataset.py 파일 실행
    + python generate_yolo_dataset.py
    + 실행 후 이미지에서 훈련시킬 객체를 마우스를 이용하여 바운딩 박스를 그린다.
  + 예제 사진
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90866254-991ffd00-e3ce-11ea-8922-ac10ca46c21a.png" width="320" height="240"/>
       </div>

* **사용 매뉴얼**
  + 마우스 컨트롤
    + 버튼 | 설명
       --------- | --------
       Left | 누른 상태에서 박스를 그린다.
       Right | 이미지에 대한 바운딩 박스와 레이블 정보를 .txt 파일로 저장
 
  + 키보드 컨트롤