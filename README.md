# 프로그라피 사전과제

> 사전과제 목표

- Django를 이용한 REST API 개발

- 필수 요구사항

  1. Django REST framework(https://www.django-rest-framework.org/)를 이용해 아래의 기능을 개발해주세요. __(완료)__
  2. 테이블 구조(Django model)
     - subscriber, title, content, created, updated 로 구성
#### 1. 게시물 목록을 반환하는 API를 개발해주세요. 각 게시물에는 아래의 항목이 필수적으로 있어야합니다. __(완료)__

- 게시물 ID : id
- 게시물의 제목 : title
- 게시물의 내용 : content
- 게시물 작성 날짜 : created
- 유저 ID : subscriber __(추가)__

**기능 상세**

- 게시물 목록은 게시물 작성 날짜를 기준으로 최신 날짜로 정렬하세요.
- (추가) url : https://youdongkwan.herokuapp.com/boardList/

![image](https://user-images.githubusercontent.com/26649731/75650332-e5e50f80-5c98-11ea-826c-6f4c7787a544.png)

#### 2. 게시물 상세 정보를 반환하는 API를 개발해주세요. __(완료)__

- https://youdongkwan.herokuapp.com/boardList/1
  - 보안기능 추가로 접속 불가능.
  - admin에서 Token 인증 추가해줘야 접근 가능하게 설정하였다.

![image](https://user-images.githubusercontent.com/26649731/75650396-1167fa00-5c99-11ea-9777-dd36677832fc.png)

#### 3. 게시물 작성, 수정, 삭제를 수행하는 API를 개발해주세요. __(완료)__

- (추가) https://youdongkwan.herokuapp.com/api/doc/
- 유저가 아니라면 CRUD 불가능하도록 제작
- admin에서 등록해주어야 함.

![image](https://user-images.githubusercontent.com/26649731/75654124-5ba1a900-5ca2-11ea-9906-274dc7f5d811.png)

- 선택 요구사항

  선택 요구사항은 필수사항을 모두 개발한 뒤 남는 시간에 진행해주세요.

  - 기본 디렉토리에 README.md를 추가하여 과제에 대한 피드백을 남겨주세요. __(완료)__
  - 본인이 작성한 API를 서버에 배포하여 접근 가능하도록 해주세요. __(완료)__
  - 게시물 목록, 상세, 작성, 수정, 삭제에 사용자 권한을 추가로 적용해보세요.__(완료)__
    - 게시글 소유자가 아닌 경우 수정 불가능하도록 권한 부여 __(추가 완료)__

