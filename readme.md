

# 기록


1116(수)
Front , back pjt 설치 후 django를 이용해서 영화 데이터를 받아서 보여주도록 하였다.
pjt-back에 Movies , accounts, community 앱을 생성하였다.
Movies에는 전체 영화를 보여주는 index , 평점순 탑 10위를 보여주는 recommend , 영화의 세부사항을 보여주는 detail을 구현하였다.
accounts에는 회원가입을 할 수 있도록 signup , 로그인과 로그아웃을 하도록 login. , logout , 회원의 정보를 볼 수 있도록 profile , 회원을 follow할 수 있도록 follow를 구현하였다.
community에는 회원들이 영화에대해 리뷰를 달 수 있는 게시판을 만들도록 하였다.
게시글 목록을 보여주기 위한 index , 만들기위한 create , 세부사항을 보여주도록 detail을 구현하였다. 또한 detail에서 댓글을 달 수 있도록 하고 , 대댓글 , 댓글 좋아요 까지 구현을 하였다.

django부분을 완성시킨 후 vue를 이용하여 페이지를 보여주도록 vue의 구성을 설계하는 과정까지 진행하였다.
