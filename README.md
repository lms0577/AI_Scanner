# AI Scanner
<div>
<img src="https://user-images.githubusercontent.com/55565351/90864418-97086f00-e3cb-11ea-9bbc-f180db242b3b.png" width="400" height="300"/>
</div>

## 프로젝트 개요
* AI Scanner에서 영감을 받아 편의점에서 구입한 물건 6개를 객체 인식하는 프로젝트
* 직접 데이터셋을 제작 및 데이터셋을 만들기 위한 프로그램 개발

## 개발 환경
제목 | 내용
--------- | --------
OS | Ubuntu 18.04
CPU | Intel core i7-9700F
GPU | Geforce RTX 2080 SUPER
언어 | Python
카메라 | Logitech C920
프레임워크 | AlexeyAB Darknet
객체 인식 모델 | YOLOv3

## 프로젝트 결과
* **1st Training**
  + Dataset
    + 3191장의 6개의 클래스에 대한 각각의 단일 이미지
  + Iterations
     + 4000번
  + Result
     + 각각의 클래스에 대해서는 객체를 잘 인식한다. 하지만 물체를 붙여서 놓았을 때 인식하지 못하는 경우가 발생한다. 2개 이상의 클래스들을 붙여 놓은 데이터셋을 훈련 시키지 않아서 발생한 문제로 예상하고 두 번째 트레이닝을 진행했다. 
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90865951-27e04a00-e3ce-11ea-9390-6e710154d7ef.png" width="320" height="240"/>
       <img src="https://user-images.githubusercontent.com/55565351/90866174-768de400-e3ce-11ea-914b-52919b7b1678.png" width="320" height="240"/>
       </div>
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90866254-991ffd00-e3ce-11ea-8922-ac10ca46c21a.png" width="320" height="240"/>
       <img src="https://user-images.githubusercontent.com/55565351/90866358-bb197f80-e3ce-11ea-8383-4d32740572f3.png" width="320" height="240"/>
       </div>
