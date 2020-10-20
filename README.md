# 트위치 알람
## 필요 패키지
- requests
- urllib
## 실행법
- 이 프로젝트를 clone합니다. 이 명령어로 clone할 수 있습니다: ``` https://github.com/okhash/twitch_alart.git```
- 이 명령어로 프로젝트 폴더로 이동합니다:```cd twitch_alart```
- 또한, requests를 설치합니다:```pip install requests```
- urllib도 설치해야 합니다:```pip install urllib```
- 그 후, options.py, secret.py 파일를 열어 변수를 설정합니다. 초기 변수 설정 문단을 확인하시기 바랍니다.
- 이 명령어를 이용해 프로그램을 실행합니다:```python3 main.py```
- 간혹 에러가 걸릴 수 있습니다. 그러면 위 명령어 대신 이 명령어로 실행하시기 바랍니다:```python main.py```
- 그 후, URL이 출력됩니다. 이것을 웹브라우저에 입력해 접속합니다.
- 네이버 로그인이 뜰 것입니다. 로그인 후 선택 항목까지 꼭 체크하시고 동의합니다.
- http://localhost 로 시작하는 사이트에 자동으로 접속할 것입니다. 그 사이트의 URL 전체를 콘솔에 입력 후 엔터를 누르세요.
- 이제 끝났습니다. 그 프로그램이 꺼지면, 더 이상 알람을 보낼 수 없으니 주의하세요.
### 초기 변수 설정
#### options.py
- debug:True,False 값을 가지는 변수입니다. True로 하면 디버그 모드를 켜서 에러를 더 쉽게 찾아내는 대신, 콘솔 창이 난잡해지고 엔터를 눌러 수동으로 확인해야 합니다.
- cafe_clubid:정수값을 가지는 문자열입니다. clubid를 알고싶은 카페에가서 메뉴에 마우스 오른쪽, 속성보기를 하시면 해당 메뉴의 풀주소가 나옵니다. 여기서 clubid= 다음에 나오는 숫자입니다.
- cafe_menuid:정수값을 가지는 문자열입니다. clubid와 같은 방식으로 menuid= 다음에 나오는 숫자입니다.
- debug_cafe_clubid:디버그 모드 활성화 시 사용하는 clubid입니다.
- debug_cafe_menuid:디버그 모드 활성화 시 사용하는 menuid입니다.
- streamer:대상 스트리머의 트위치 ID입니다.
#### secret.py
- naver_id:네이버가 발급하는 ID입니다. NAVER Developers에서 네아로, 카페 API를 사용해야 하며, 서비스 환경은 서비스 URL/Callback URL이 모두 ```http://localhost/``` 인 PC 웹이여야 합니다.
- naver_secret:네이버가 발급하는 시크릿입니다.
- twitch_id:트위치가 발급하는 ID입니다. 응용 프로그램이며, 리디렉션 URL은 ```http://localhost/```이여야 합니다.
- twitch_secret:트위치가 발급하는 시크릿입니다.
