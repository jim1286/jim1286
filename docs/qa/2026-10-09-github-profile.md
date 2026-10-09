# QA 리포트 — GitHub 프로필 포트폴리오

## 1. 최종 판정

GitHub 프로필 소개·웹사이트·README·고정 저장소·사진·제품 이미지·기여 요약 확인 범위 통과.
실행 날짜: 2026-10-09 KST. 앱 자체 기능을 새로 검증한 작업은 아니다.

## 2. 대상과 이력

- 대상: https://github.com/jim1286 및 jim1286/jim1286, main.
- 최초 콘텐츠 0df3bc112e44bbca427a3aa5f109b5823941e8f1, 후속 콘텐츠 93180109f0203e224d055f6e4d8b23f8acabf37b.
- GitHub API로 main에 직접 반영했다. 고정 저장소와 사진은 Aside의 소유자 로그인 브라우저에서 저장했다.
- bio·website·README·pins가 비어 있던 프로필에 개발자 소개·포트폴리오·공용 디자인 시스템을 연결했다.
- 사용자 지적으로 처음 복사한 아이콘이 사이트의 옛 자산임을 확인했다. 실제 제품 설정의 원본 7개로 교체하고,
  Diairy·Spint·Utilverse와 Unairplane Android를 포함했다. Utilverse는 개발 중으로 구분한다.
- 사용자 제공 KakaoTalk_Photo_2026-08-03-19-03-30.png를 새 프로필 사진으로 저장하고 공개 화면에서 확인했다.

## 3. 환경과 검증 범위

macOS, Aside Browser 소유자 세션과 Codex 인앱 브라우저의 로그아웃 프로필.
공개 화면은 다크 테마, 기본 940×1294px에서 직접 확인했다. 두 SVG 팔레트는 로컬 렌더로 확인했다.
실제 REST/GraphQL과 공개 스토어·서비스 URL을 사용했다. 합성 기여 데이터는 사용하지 않았다.

## 4. 확인 결과와 문제

| 시나리오 | 실제 결과 | 판정 |
| --- | --- | --- |
| 프로필 | 새 사진·소개·포트폴리오·README 표시 | 통과 |
| 이미지 | 배너 1·앱 아이콘 7·활동 카드 1, 9개 모두 로드 | 통과 |
| 고정 저장소 | HJM, portfolio 순서의 공개 저장소 2개, GraphQL 일치 | 통과 |
| README·자산 | REST/git tree와 로컬 UTF-8/PNG/SVG 바이트 비교 | 통과 |
| 공개 상품 | 6개 스토어 연결 제품과 개발 중 Utilverse | 통과 |
| 기여 요약 | 실제 달력 합계 4,411·활동 215일·최근 30일 2,543·월별 총계 | 통과 |
| 활동 링크 | GitHub의 실제 user-content ID를 사용, 구역 이동 확인 | 통과 |
| 사진 | 원본 인물·가운데 얼굴 크롭을 공개 프로필에서 직접 확인 | 통과 |

초기 Aside 일회성 REPL 변수를 다음 호출에서 재사용할 수 없어 실패했다. 지속 세션으로 저장하고 화면·API로 확인했다.
GitHub의 첫 이미지 관찰은 로드 직후 pending이었다. 로드 후 전체 이미지와 실제 활동 카드 표시를 확인했다.
프로필 fragment의 기본 heading 주소가 이동하지 않는 환경이 있어 실제 GitHub user-content ID로 연결했다.

## 5. 기여 UI와 원천

GitHub의 기본 Contributions·Contribution activity는 GitHub가 소유하는 UI여서 README로 직접 재설계할 수 없다.
README에 자체 SVG 요약과 Recent public work를 추가했다. 실제 GitHub 달력의 날짜별 합계와 totalContributions를
교차 확인하고 월별·최근30일·활동일을 계산한다. build_activity.py가 재사용 생성기다.
카드는 2026-10-09의 명시된 snapshot이며 자동 갱신되지 않는다. 프로필 커밋 자체가 기본 기여 수를 늘리므로
기본 그래프와 요약의 이후 숫자 차이는 snapshot 경계다. 이를 실시간 통계나 앱 이용 성과로 주장하지 않는다.

아이콘은 제품 설정의 launcher 원본과 SHA-256 manifest를 확인한 뒤 복사한다. build_assets.py가 사이트 동기화
검사를 먼저 수행한다. PNG 7개와 자체 SVG를 profile repo에서 제공하며 외부 통계 이미지 서비스나 workflow는 추가하지 않았다.
Apple lookup의 6개 앱 레코드, Diairy·Unairplane Google Play 및 웹을 확인했다. Spint Android 404 링크는 넣지 않았다.
공개 HTTP/스토어 레코드는 로그인·설치·결제·제품 내부 동작 성공을 뜻하지 않는다.

사용자 요청에 따라 [antfu](https://github.com/antfu), [DenverCoder1](https://github.com/DenverCoder1),
[sindresorhus](https://github.com/sindresorhus)를 살펴봤다. 간결한 링크 허브·제품 소개·활동 구성을 참고했고 문구/자산은 복제하지 않았다.
기본 기여 표시 경계는 [GitHub 안내](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile)를 확인했다.

## 6. 미확인 범위

모든 브라우저 조합·실기기·앱 내부 흐름·GitHub 라이트 테마 전체 화면은 검사하지 않았다.
포트폴리오 사이트는 별도 main 커밋 bfd3d09a0491b0d93c10a36c4e4d653347bd71d5에 최신 제품·아이콘·포슬이
마케팅 사례 통합을 구현하고 로컬 검사했다. 사용자 지시로 사이트 push와 배포는 수행하지 않았다.

## 7. 보관·정리

README·SVG·PNG·재사용 생성기와 이 리포트를 보존한다. 원시 API JSON·중간 작업 로그/사진 캡처는 제거한다.
최종 profile-preview.png, activity-preview.png, portfolio-marketing-preview.png는 사용자 전달용 발표 이미지로
Documents/Codex에 보존하며 공개 repo에 불필요한 캡처를 올리지 않는다. 사용자 사진 원본은 보존한다.
새 브랜치·워크트리·clone은 만들지 않았다. profile은 main 하나, 열린 PR 없음, 관련 임시 checkout 없음.
사이트도 main 단일 checkout이며 작업용 브랜치·워크트리 정리 대상은 없다. 자체 Vite만 종료하고 기존 앱 실행은 유지한다.
