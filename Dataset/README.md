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
  + Train Dataset
    + 3191장의 6개 클래스에 대한 각각의 단일 이미지
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
       
* **2nd Training**
  + Train Dataset
    + 3191장의 6개 클래스에 대한 각각의 단일 이미지 + 250장의 2개 클래스 조합 이미지
  + Iterations
     + 12000번
  + Result
     + 첫 번째 트레이닝에서 2개 이상의 클래스들을 붙여 놓았을 때 인식하지 못하던 것들을 인식하는 것을 볼 수 있다. 하지만 아직 객체를 잘 인식하지 못하는 현상을 발견할 수 있다. 따라서 더 많은 조합의 데이터셋을 만들어 다음 트레이닝을 진행했다.
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90867509-7393f300-e3d0-11ea-9051-0e99532a22a9.png" width="320" height="240"/>
       <img src="https://user-images.githubusercontent.com/55565351/90867546-81497880-e3d0-11ea-8224-ed9c2137a3ba.png" width="320" height="240"/>
       </div>
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90867568-8b6b7700-e3d0-11ea-9a55-70658783c852.png" width="320" height="240"/>
       <img src="https://user-images.githubusercontent.com/55565351/90867591-958d7580-e3d0-11ea-8069-a153b9f1b51c.png" width="320" height="240"/>
       </div>
       
* **3rd Training**
  + Train Dataset
    + 3191장의 6개 클래스에 대한 각각의 단일 이미지 + 1704장의 2~6개 클래스 조합 이미지
  + Iterations
     + 12000번
  + Result
     + 두 번째 트레이닝에서 인식하지 못하던 것들을 인식하는 것을 볼 수 있다. 하지만 아직 어떠한 조합은 객체를 잘 인식하지 못하는 현상을 발견할 수 있다. 더 많은 데이터셋을 만들어 트레이닝을 시켜야 인식할 것으로 보인다.
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90867509-7393f300-e3d0-11ea-9051-0e99532a22a9.png" width="320" height="240"/>
       <img src="https://user-images.githubusercontent.com/55565351/90868016-32501300-e3d1-11ea-8833-f7b05a5365e6.png" width="320" height="240"/>
       </div>
     + <div>
       <img src="https://user-images.githubusercontent.com/55565351/90868067-4431b600-e3d1-11ea-86a0-d8780357bde3.png" width="320" height="240"/>
       <img src="https://user-images.githubusercontent.com/55565351/90868092-4bf15a80-e3d1-11ea-9cef-cc67785ceaab.png" width="320" height="240"/>
       </div>

* **결론**
  + Test Dataset
    + 576장의 단일 및 조합 이미지
  + 1st Training
     + Precision = 0.58, Recall = 0.34, mAP(@IoU=0.5) = 40.32%
  + 2nd Training
     + Precision = 0.90, Recall = 0.73, mAP(@IoU=0.5) = 80.78%
  + 3rd Training
     + Precision = 0.98, Recall = 0.97, mAP(@IoU=0.5) = 98.52%
  + Conclusion
     + 단일 이미지 데이터셋을 학습시킨 것만으로는 여러 객체를 한 번에 인식하는 데는 한계가 있다. 하나의 객체는 인식을 잘 하지만 붙어있는 객체도 하나로 인식하는 경우가 발생한다. 한 번에 여러 객체를 인식하려면 붙어 있는 객체 이미지를 데이터셋으로 만들어 학습을 시켜줘야 인식률이 올라간다. 2개 객체 조합의 이미지 데이터셋 만을 넣어줘도 mAP가 2배나 증가하는 것을 볼 수 있다. 2개 객체 조합뿐만 아니라 3~6개 객체 조합의 데이터셋을 넣어줬을 때는 mAP가 98%까지 올라가는 것을 볼 수 있다. 
     + 여기서 알 수 있는 사실은 한 번에 여러 객체를 따로따로 정확하게 인식하려면 객체 하나에 대해서만 학습을 하는 것이 아니라 여러 객체와 함께 있는 모습에 대해서도 학습을 해야지만 인식을 잘 할 수 있다는 것이다. 
     + 아쉬운 점은 반복 학습 횟수에 대한 객체 인식률의 변화를 실험하지 못한 것이다. 
