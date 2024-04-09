# 장고 MTM 필드는 어떻게 작동하는가.

- 예약 정보 테이블 구조

  | PK | PRIMARY KEY |
  |---|---|
  | 의사_id | FOREIGN KEY |
  | 환자_id | FOREIGN KEY |
  
- 의사 테이블 구조
  
  | PK | PRIMARY KEY |
  |---|---|
  | 이름 | TEXT |
  | 분야 | TEXT | 

- 환자 테이블 구조
  
  | PK | PRIMARY KEY |
  |---|---|
  | 이름 | TEXT |
  | 나이 | INT | 

---

- 각 테이블들의 정보를 models.py에서 class로 정의한다면,
  ```python
  from django import models

  class Doctor(models.Model):
    name = models.TextField()
    medical = models.TextField()

  class Patient(models.Model):
    name = models.TextField()
    age = models.IntegerField()

  class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  ```

## 중개 모델 사용시 발생하는 불편함
1. 의사 입장에서 진료 예정인 환자 정보를 탐색하려면?
   1. 의사 테이블에는 환자와 관련된 정보를 저장하는 곳이 없음.
   2. 환자 테이블에도 참조 중인 의사 정보는 없음.
   
2. 환자와 의사 정보를 모두 저장 할 수 있는 class는 Reservation
   1. 따라서, 환자와 의사 관계를 새롭게 정의하려면 Reservation class를 통해서만 가능
   ```python
   # 관게를 맺을 doctor1 정보 조회
   doctor1 = Doctor.objects.get(pk=1)
   # 관계를 맺을 patient1 정보 조회
   patient1 = Patient.objects.get(pk=1)
   # 의사와 환자 정보를 Reservation 테이블에 추가
   Reservation.objects.create(doctor=doctor1, patient=patient1)
   ```  
3. 반대의 경우도 마찬가지.

## MTMField 를 사용한다면?
- 둘 중, 한 곳에만 MTMField 정의
- 필요하다면, related_name 작성 (역참조 매니저 명)
```python
class Patient(models.Model):
# ManyToManyField 작성
  doctors = models.ManyToManyField(Doctor, related_name='patients')
  name = models.TextField()
```

1. 환자는 `doctors` 매니저를 통해 직접 관계 형성 가능
2. 의사는 `parients` 매니저를 통해 직접 관계 형성 가능
