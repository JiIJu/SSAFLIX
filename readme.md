# ===== Final PJT =====


# 사용 기술
- Django, Vue.js, Python, CSS, HTML  
<br>

# 서비스 기획과 실제 구현
> ## 기획
    1. 영화 조회
        - 영화 검색
        - 평점순 영화
        - 개봉일 순 최신영화 조회
    2. 영화 추천
        - 유저의 선호 장르(유저 선택)에 따른 영화 추천
    3. 리뷰 게시판
        - 영화에 대한 리뷰 게시판
        - 댓글과 좋아요 기능

> ## 실제 구현
    1. 영화 조회
        - 전체 조회(랜덤)
        - 영화 개봉일과 평점순 영화 조회
        - 영화 상세 정보 조회
        - 영화 검색
    2. 영화 추천
        - 유저가 선택한 장르에 따른 영화 리스트 출력
    3. 리뷰 게시판
        - 영화에 대한 리뷰를 작성하는 게시판 생성
        - 댓글과 좋아요 기능 생성

> # 프로젝트 진행  
    > ## 1. Front, back pjt 설치, django를 이용해 영화 데이터를 받아 보여주기
   - pjt-back : Movies, accounts, community 앱 생성
     - Movies
       - index => 전체 영화조회
       - recommend => 평점순 탑 10
       - detail => 영화 세부사항
     - accounts
       - signup => 회원가입
       - login, logout => 로그인과 로그아웃
       - profile => 회원 정보 관리
       - follow => 회원 팔로우 기능
     - community : 영화에 대한 리뷰를 달 수 있는 게시판
       - index => 게시글 목록
       - create => 게시글 만들기
       - detail => 세부사항(댓글 및 댓글 좋아요 추가)

> ## 2. DB 생성
    `TMDB` 사이트의 `API key`를 통해서 데이터를 받아온 후, json 파일을 만들어 loaddata해 사용

> ## 3. django를 완성시킨 후 vue를 이용해 페이지 구성 설계
  - pjt-front : components와 router를 이용해 프론트 설계
    - MovieListView => TMDB_API에서 반환된 영화리스트를 출력
    - DetailView => 영화의 세부 설명 페이지
    - RecommendView =>  TOP 10 영화 페이지
    - LatestMovieView => 최신영화를 보여주는 페이지
 - ### 메인
   - 로그인 후 영화 전체 리스트의 출력 및 메뉴의 선택 가능
     - 장르 선택을 통해 선호하는 장르의 영화만을 출력 가능
     - 평점 순 TOP 10의 영화 출력
     - 개봉일에 따른 최신 영화 출력
 - ### MoviesListView
   - 영화의 전체 리스트 페이지
     - 정렬 없이 랜덤으로 출력
 - ### DetailView
   - 포스터 클릭시 영화의 상세 페이지 출력
     - 영화의 줄거리 및 평점, 포스터를 출력
 - ### community
   - 영화의 리뷰 작성 페이지 출력
     - 리뷰의 댓글 및 좋아요 기능 구현






![ERD](./img/ERD.jpg)

