---
name: 전국 공공 박물관·미술관 지도
description: 도로표지판의 규율을 그대로 가져온 공공 안내 지도 — 면색 한 판, 그림자 없음, 나머지는 전부 조용하다
colors:
  sign: "#6E3B1F"
  sign-ink: "#FFFFFF"
  sign-wash: "#F3ECE7"
  bg: "#F7F7F5"
  panel: "#FFFFFF"
  ink: "#1A1A18"
  ink-muted: "#5F5E58"
  line: "#DCDBD4"
  free: "#176B5B"
  paid: "#8A4B12"
  kind-1: "#8A5024"
  kind-2: "#E3B577"
  kind-3: "#4C7A55"
  kind-4: "#2E1A0C"
  kind-5: "#6B7C9B"
  kind-6: "#A8A093"
typography:
  display:
    fontFamily: "Do Hyeon, IBM Plex Sans KR, sans-serif"
    fontSize: "1.40rem"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  title:
    fontFamily: "IBM Plex Sans KR, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "1.40rem"
    fontWeight: 600
    lineHeight: 1.3
  headline:
    fontFamily: "IBM Plex Sans KR, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "1.12rem"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "IBM Plex Sans KR, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Sans KR, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "0.80rem"
    fontWeight: 500
    lineHeight: 1.45
  numeric:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "1.40rem"
    fontWeight: 700
    fontFeature: "tabular-nums"
rounded:
  tag: "4px"
  control: "8px"
  card: "10px"
  panel: "12px"
  sheet: "16px 16px 0 0"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  tap: "44px"
components:
  sign-header:
    backgroundColor: "{colors.sign}"
    textColor: "{colors.sign-ink}"
    typography: "{typography.display}"
    rounded: "{rounded.panel}"
    padding: "8px 56px 8px 12px"
    height: "52px"
  panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: "12px"
  pill:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0 14px"
    height: "44px"
  pill-active:
    backgroundColor: "{colors.sign}"
    textColor: "{colors.sign-ink}"
    rounded: "{rounded.pill}"
  facility-card:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "12px"
  facility-card-hover:
    backgroundColor: "{colors.sign-wash}"
  input-search:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "8px 12px"
    height: "44px"
  tag-free:
    backgroundColor: "{colors.free}"
    textColor: "{colors.panel}"
    rounded: "{rounded.tag}"
    padding: "3px 8px"
  tag-paid:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.paid}"
    rounded: "{rounded.tag}"
    padding: "3px 8px"
  button-sign:
    backgroundColor: "{colors.sign}"
    textColor: "{colors.sign-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "44px"
  button-outline:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.control}"
    padding: "0 12px"
    height: "44px"
---

# Design System: 전국 공공 박물관·미술관 지도

> 이 문서는 **실제 빌드에서 뽑아낸** 파일럿 기록이다(토큰 frontmatter + `.impeccable/design.json` 사이드카 포함).
> 7개 앱을 가로지르는 정본은 `daitmap/DESIGN.md`에 있고, 나머지 6개 앱은 그 사본을 갖는다.
> 값이 어긋나면 정본의 **유도 규칙**을 따르고, 이 문서의 값은 그 규칙을 이 앱에 적용한 결과로 읽는다.

## Overview

**Creative North Star: "길가의 갈색 표지판"**

이 시스템은 도로표지판의 규율을 화면으로 옮긴 것이다. 표지판에는 그라디언트도 그림자도 없다. 색이 있는 면(面) 한 판과 흰 글자, 그리고 판을 판으로 만드는 얇은 테두리가 전부다. 이 앱의 헤더는 그 판이고, 나머지 화면은 판이 읽히도록 조용히 물러난다. 면색은 도로표지규칙 제8조 — 문화재·관광 안내는 갈색 바탕에 흰 글자 — 에서 그대로 유도했다.

밀도는 휴대폰 기준으로 짜여 있다. 모바일 우선 스타일시트 하나가 640px과 901px 두 번만 갈라지고, 데스크톱은 같은 판을 넓게 펼친 것이지 다른 디자인이 아니다. 사진도 로고도 없는 앱이므로 시각적 무게는 전부 면색·활자·픽토그램이 진다. 장식으로 존재하는 요소는 이 빌드에 하나도 없다.

이 시스템은 워크스페이스의 지도 PWA 7종이 공유하는 **파일럿**이다. 앱 사이에서 달라지는 축은 정확히 세 개(`--sign` / `--sign-ink` / `--sign-wash`)와 `--kind-*` 램프뿐이고, 나머지 토큰·컴포넌트·규칙은 7개가 같은 값을 쓴다. 그러므로 아래의 값보다 **유도 규칙**이 정본이다. 값만 복사하면 면색이 밝은 앱(노랑 계열)에서 곧바로 어긋난다.

**Key Characteristics:**
- 면색 한 개가 앱의 정체성 전부를 진다 — 표지판·활성 필터·마커에만 나온다
- 위계 표현에서 `box-shadow`를 완전히 뺐다. 깊이는 1px 괘선과 면색으로만 만든다
- 1.250 Major Third 6단계 밖의 글자 크기를 쓰지 않는다
- 아이콘은 두 계열뿐 — 헤더 픽토그램은 면 채움, 컨트롤은 1.8 선. 유니코드 글리프·이모지는 쓰지 않는다
- 터치 타깃 44px, 입력 글자 16px이 물러설 수 없는 하한이다
- 브라우저가 그리는 표면(선택 영역, 스크롤바, 캐럿, accent)까지 팔레트 안에 있다

## Colors

흙빛 갈색 한 축에 무채색 종이, 그리고 정보를 나르는 색 두 개. 그 밖의 색은 지도 마커 램프에만 존재한다.

### Primary
- **표지 갈색 / Sign Brown** (`{colors.sign}`): 헤더 판 바탕, 활성 필터 pill, 지도 팝업 버튼, 상세 모달의 지도 버튼, 포커스 링, 찜 켜짐 상태, 리포트 막대 채움. 화면에서 이 색이 나오는 자리는 목록화할 수 있을 만큼 적어야 한다.
- **표지 흰 글자 / Sign Ink** (`{colors.sign-ink}`): 면색 판 위 녹아웃 텍스트와 픽토그램. 면색 위에서는 예외 없이 이 색만 쓴다.
- **표지 옅은 바닥 / Sign Wash** (`{colors.sign-wash}`): 면색의 아주 옅은 톤. 카드 hover 바닥, 리포트 표 행 hover, 지역 막대 활성 바닥. 면색을 쓸 수 없는 자리에서 "면색 계열임"만 알리는 최소 신호다.

### Secondary
- **무료 청록 / Free Teal** (`{colors.free}`): "무료" 태그의 면 채움. 부모가 목록에서 스캔하는 단 하나의 값이라서 유일하게 채워진 태그다.
- **유료 흙갈 / Paid Umber** (`{colors.paid}`): "유료" 태그의 외곽선과 글자. 채우지 않는다.

### Tertiary
지도 마커·범례 램프 `{colors.kind-1}` ~ `{colors.kind-6}`. `app.js`의 `KIND_ORDER`와 1:1로 대응하며, 색값은 CSS가 소유하고 JS는 `getComputedStyle`로 읽어 쓰기만 한다. 램프는 값이 아니라 유도 규칙이 정본이다(아래 Named Rules).
- **박물관 갈색** (`{colors.kind-1}`) — 265곳, 과반이라 중간 명도
- **미술관 모래** (`{colors.kind-2}`) — 90곳
- **과학·생태 이끼** (`{colors.kind-3}`) — 18곳, 면색 계열 밖으로 나간 이탈 중 하나
- **역사·민속 흑갈** (`{colors.kind-4}`) — 87곳, 램프에서 가장 어둡게
- **문학관 청회** (`{colors.kind-5}`) — 9곳, 개체 수가 가장 적어 이탈이 허용된 자리
- **전시·기타 회갈** (`{colors.kind-6}`) — 36곳

### Neutral
- **종이 / Paper** (`{colors.bg}`): 페이지 바탕. 흰색이 아니라 아주 옅은 회백이라 흰 판이 판으로 보인다.
- **판 흰색 / Panel White** (`{colors.panel}`): 카드·필터바·입력·지도 프레임의 바탕.
- **먹 / Ink** (`{colors.ink}`): 본문·제목·값. 모달 오버레이도 이 색의 45% 투명이다.
- **흐린 먹 / Muted Ink** (`{colors.ink-muted}`): 주의 문구, 라벨, 보조 수치, 태그 기본색, placeholder.
- **괘선 / Rule Line** (`{colors.line}`): 모든 테두리·구분선·스크롤바 썸. 이 시스템에서 깊이를 만드는 유일한 재료다.

### Named Rules

**The Sign-Only Rule.** 면색은 표지판(헤더), 활성 상태(선택된 필터·찜 켜짐), 지도 마커, 그리고 단 하나의 주 행동 버튼에만 나온다. 카드·태그·패널 바탕으로 면색이 새는 순간 표지판은 표지판이기를 그만둔다. 무료/유료 태그가 "무료만 채우고 유료는 외곽선"인 것은 이 규칙의 직접 결과다.

**The Carrying-Color Rule.** 색은 정보를 나를 때만 붙는다. 기본 태그는 무채색이고, 색이 붙은 태그는 그 색이 곧 의미다(청록=무료, 흙갈=유료). 같은 정보를 두 번 칠하지 않는다.

**The Kind-Ramp Derivation Rule.** `--kind-*` 램프는 값을 베끼는 것이 아니라 규칙으로 다시 유도한다. (1) 과반을 차지하는 범주는 중간 명도에 둔다. (2) 최암 범주는 명도로 확실히 분리한다. (3) 명도가 인접한 두 범주는 색상으로 갈라낸다. (4) 면색 계열 밖으로의 색상 이탈은 개체 수가 가장 적은 범주에만 허용한다. (5) 검증은 스와치가 아니라 지도 전면 렌더로 한다.

## Typography

**Display Font:** Do Hyeon (fallback: IBM Plex Sans KR, sans-serif)
**Body Font:** IBM Plex Sans KR (fallback: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif)
**Numeric Font:** JetBrains Mono (fallback: ui-monospace, monospace)

**Character:** Do Hyeon은 각지고 굵기 변화가 없는 표지판 활자라 앱 이름 한 줄에만 쓴다. 본문은 IBM Plex Sans KR가 전부 받고, 숫자는 JetBrains Mono가 `tabular-nums`로 자리를 지킨다 — 표지판의 거리 표기처럼. 세 활자는 상위 브랜드 다있맵과 동일하다.

### Hierarchy
- **Display** (Do Hyeon 400, `--fs-l` 1.40rem → ≥640px `--fs-xl` 1.75rem, line-height 1.15, letter-spacing -0.01em): 헤더 표지판의 앱 이름. 이 앱에서 Do Hyeon이 쓰이는 유일한 자리다. `word-break: keep-all` + `text-wrap: balance`로 어절 단위 줄바꿈만 허용한다.
- **Numeric** (JetBrains Mono 700, `--fs-l` → ≥640px `--fs-xl`, tabular-nums): 헤더의 시설 수, 리포트 타일 수치. 단위(`곳`)는 `--fs-s`에 불투명도 0.8로 낮춘다.
- **Title** (600, `--fs-l` 1.40rem, line-height 1.3): 카드 시설명, 모달 제목.
- **Headline** (600, `--fs-m` 1.12rem, line-height 1.3): 지도 팝업 시설명, 리포트 섹션 제목.
- **Body** (400, `--fs-base` 1rem, line-height 1.5–1.6): 카드 정보, 상세 항목, 입력·pill·버튼 텍스트.
- **Label** (500, `--fs-s` 0.80rem, line-height 1.45): 주의 문구, 필터 라벨, 태그, 결과 수, 푸터, 작은 pill.

### Named Rules

**The Six-Step Rule.** 글자 크기는 1.250 Major Third 6단계(`--fs-xxl` 2.19 / `--fs-xl` 1.75 / `--fs-l` 1.40 / `--fs-m` 1.12 / `--fs-base` 1 / `--fs-s` 0.80rem) 안에서만 고른다. 새 크기가 필요하다는 느낌은 거의 항상 위계 설계가 틀렸다는 신호다. (`--fs-xxl`은 이 앱에서 아직 어떤 규칙도 차지하지 않았다. 공유 스케일의 상단으로 남겨 둔 것이지 미배정 슬롯을 채우라는 뜻이 아니다.)

**The 16px Floor Rule.** 입력 가능한 요소(`input`, `select`)의 `font-size`는 `--fs-base`(16px) 아래로 내려가지 않는다. iOS Safari가 포커스 시 페이지를 확대해 버려 한 손 조작이 깨진다. 작아 보이고 싶으면 크기가 아니라 색과 여백으로 낮춘다.

**The Standing Number Rule.** 사용자가 비교하는 숫자는 JetBrains Mono + `font-variant-numeric: tabular-nums`로 자리를 고정한다. 리포트 표 전체에도 같은 처리가 걸려 있다.

## Layout

컨테이너는 최대 1200px 중앙 정렬, 좌우 여백은 모바일 12px / ≥640px 16px이다. 여백 리듬은 4px 배수를 기본으로 하되 8·10·12·14가 실제 사용 단위이고, 판 사이 간격은 12px(≥640px에서 패널 내부 패딩 14px), 카드 그리드 간격은 10px(≥640px 12px)이다. 안전 영역은 `env(safe-area-inset-*)`을 `max()`로 감싸 상단·하단에서 최소값을 보장한다 — PWA standalone 실행이 실제 조건이기 때문이다.

브레이크포인트는 두 개뿐이다.

- **기본(모바일)**: 단일 컬럼. 검색이 한 줄을 다 쓰고 시군구·필터 토글이 다음 줄로 내려간다. 카드 그리드 1열, 지도 높이 `62dvh`(최소 320px). 지도/목록은 토글로 한 번에 하나만 보인다.
- **≥640px**: 표지판이 커진다(min-height 64px, 픽토그램 32px, 제목·수치 한 단계 위로). 카드 그리드가 `auto-fill minmax(240px, 1fr)`로 바뀌고, 모달이 바텀시트에서 가운데 카드(최대 520px)로 되돌아간다.
- **≥901px**: 지도와 목록을 `55% / 1fr` 2열로 나란히 둔다. 뷰 토글이 사라지고 지도 pane이 `sticky`로 붙으며 높이가 `calc(100dvh - 140px)`가 된다. 필터바는 모든 폭에서 `top: 8px`에 sticky다.

**The One-Hand Rule.** 누를 수 있는 것은 전부 최소 44px(`--tap`)이다. 시각적으로 작아야 하는 컨트롤(찜 버튼, 작은 pill, 뷰 토글)은 크기를 줄이는 대신 음수 마진으로 히트 영역만 넓힌다.

**The Pointer-Gated Hover Rule.** hover 스타일은 `@media (hover: hover)` 안에만 존재한다. 터치 기기에서 탭 뒤 hover가 고착되어 상태가 거짓말을 하는 것을 막는다.

## Elevation & Depth

**이 시스템에는 그림자가 없다.** 위계는 오직 (1) 1px `--line` 괘선, (2) 종이(`--bg`)와 판(`--panel`)의 밝기 차, (3) 면색 판의 존재로만 만든다. 떠 있는 것처럼 보이는 요소는 하나도 없고, 그것이 표지판 세계의 조건이다. `box-shadow` 속성이 스타일시트에 세 번 나오지만 어느 것도 깊이를 만들지 않는다 — 표지판 안쪽 흰 테두리, 토글 버튼 사이 1px 구분선, 그리고 독도 라벨에서 Leaflet 기본 그림자를 끄는 `none`이다.

### Shadow Vocabulary
- **표지판 안쪽 테두리** (`box-shadow: inset 0 0 0 2px rgba(255,255,255,.9)`): 헤더 판에만. 실제 도로표지판의 흰 테두리이며, 면색 판을 판으로 마감한다. 다른 요소에 복제하지 않는다.
- **인접 구분선** (`box-shadow: inset 1px 0 0 var(--line)`): 뷰 토글에서 붙어 있는 pill 사이 경계. 테두리를 그릴 수 없는 자리의 괘선 대체물이다.

**The No-Lift Rule.** 어떤 요소도 그림자로 떠오르지 않는다. 상승감이 필요하다고 느껴지면 괘선을 쓰거나, 바탕을 `--sign-wash`로 바꾸거나, 면색 테두리로 상태를 알린다.

## Shapes

모서리는 네 단계다: 태그 4px, 컨트롤·작은 판 8px, 카드 10px, 큰 판 12px. pill과 진행 막대·그랩 핸들만 999px 완전 원형이고, 모바일 모달은 위쪽만 16px 둥근 바텀시트다. 크기가 클수록 반경이 커지는 단순한 순서라서 새 요소의 반경은 크기만 보면 정해진다.

형태 언어는 전부 **테두리로 만든 사각 판**이다. 판은 흰 바탕 + 1px 괘선 + 반경 조합 하나로 정의되고, 상태는 그 테두리 색이 `--sign`으로 바뀌는 것으로 표현한다. 지도 마커만 예외적으로 원(반지름 8px, 흰 테두리 2px, 채움 불투명도 0.9)이고, 범례 점이 같은 형태를 10px로 축소해 반복한다.

**The Border-Not-Fill Rule.** 상태 변화의 1차 수단은 채움이 아니라 테두리다. hover는 테두리를 `--sign`으로, 선택은 테두리와 채움을 동시에 `--sign`으로 바꾼다. 채움까지 가는 것은 "선택됨"에만 허용된다.

## Components

### Buttons
- **Shape:** 컨트롤 반경 8px(`{rounded.control}`), 필터류는 완전 원형 pill(999px)
- **Sign(주 행동):** 면색 바탕 + 흰 글자. 지도 팝업의 "자세히 보기", 상세 모달의 지도 버튼. 한 화면에 하나만 둔다
- **Outline(기본):** 흰 바탕 + `--line` 테두리 + 먹 글자. "지도에서 보기", 상세 링크 버튼
- **Hover / Focus:** 포인터 기기에서만 테두리가 `--sign`으로. 포커스는 전역 `:focus-visible` 규칙 — `--sign` 2px 아웃라인, 오프셋 2px, 반경 4px
- **Icon-only:** 44×44 투명 버튼(공유, 모달 닫기). 눌림은 배경 흰색 16% 투명으로만 표시한다

### Chips
- **Style:** 흰 바탕, `--line` 1px 테두리, 원형(999px), 높이 44px, 좌우 패딩 14px, 본문 크기
- **State:** 선택되면 바탕·테두리가 `--sign`, 글자가 `--sign-ink`. "초기화"는 파괴적 행동이 아니라 흐린 먹 글자로 낮춘다. 결과 수 줄의 작은 pill은 크기는 `--fs-s`로 줄이되 높이 44px는 유지한다

### Cards / Containers
- **Corner Style:** 카드 10px, 패널 12px
- **Background:** 흰 판(`--panel`), 페이지는 종이(`--bg`)
- **Shadow Strategy:** 없음 (Elevation & Depth 참조)
- **Border:** 1px `--line`. hover 시 테두리 `--sign` + 바탕 `--sign-wash`
- **Internal Padding:** 12px(≥640px 패널 14px), 내부 요소 간격 7px

### Inputs / Fields
- **Style:** 흰 바탕, 1px `--line`, 반경 8px, 최소 높이 44px, 패딩 8/12, 글자 16px
- **Focus:** 기본 아웃라인을 끄고 테두리를 `--sign`으로 바꾼다. 키보드 포커스는 전역 `:focus-visible` 아웃라인이 따로 받는다
- **Select:** `min-width: 0`이 필수다. 없으면 가장 긴 옵션 텍스트만큼 벌어져 좁은 화면에서 옆 버튼을 다음 줄로 밀어낸다
- **캐럿·선택 영역:** `caret-color`, `accent-color`, `::selection`이 모두 면색에서 나온다

### Navigation
이 앱에는 내비게이션 바가 없다. 이동을 담당하는 것은 (1) 필터바(sticky, `top: 8px`)와 (2) ≤900px에서만 나타나는 지도/목록 뷰 토글이다. 토글은 원형 테두리 하나 안에 두 pill을 이어 붙이고 사이를 inset 괘선으로 가른다.

### 표지판 헤더 (Signature)
면색 판 하나에 픽토그램(26px, ≥640px 32px) · 앱 이름 · 시설 수를 한 줄로 앉히고, 안쪽 흰 테두리로 마감한다. 판 우측 56px은 링크복사 버튼 자리로 비워 둔다. 판 바깥 아래에 흐린 먹으로 참고용 주의 문구가 붙는다 — 이 문구는 판 안으로 들어가지 않는다. 판은 정보를, 문구는 신뢰도를 말하는 서로 다른 층이다.

### 지도 마커·범례 (Signature)
마커는 반지름 8px 원, 채움은 `--kind-*`, 흰 테두리 2px, 채움 불투명도 0.9. 범례는 지도 좌하단에 흰색 94% 투명 판으로 얹히고 10px 원 점이 같은 색을 반복한다. 점에는 흰 테두리 1.5px + 검정 18% 아웃라인이 붙어 밝은 타일 위에서도 경계가 남는다. **색값은 CSS가 소유하고 JS는 읽어 쓰기만 한다.**

### 아이콘
- **`.sign-mark`** — 헤더 표지판 픽토그램. 면으로 채운다(`fill: currentColor`). 이 계열은 헤더에만 존재한다
- **`.ico`** — 컨트롤 아이콘. 선으로 그린다(`fill: none`, `stroke: currentColor`, `stroke-width: 1.8`, 둥근 끝·이음). `pointer-events: none`으로 클릭 판정이 항상 버튼에 잡히게 한다. 예외는 찜 켜짐(`.fav-btn.on .ico`)뿐 — 선 계열이 면으로 채워지는 것 자체가 상태 신호다

## Do's and Don'ts

### Do:
- **Do** 새 앱을 파생할 때 `--sign` / `--sign-ink` / `--sign-wash` 세 줄과 `--kind-*` 램프만 바꾼다. 나머지 토큰은 7개 앱 공통이다.
- **Do** `--kind-*`를 값 복사가 아니라 The Kind-Ramp Derivation Rule로 다시 유도하고, 지도 전면 렌더로 검증한다.
- **Do** 글자 크기를 6단계 토큰 안에서만 고른다.
- **Do** 위계를 1px `--line` 괘선과 바탕 밝기 차이로 만든다.
- **Do** 누를 수 있는 모든 것에 44px(`--tap`)을 준다. 작아 보여야 하면 음수 마진으로 히트 영역만 넓힌다.
- **Do** 입력 요소의 글자 크기를 16px 이상으로 유지한다.
- **Do** `prefers-reduced-motion: reduce`에서 `transition: none !important`를 쓴다. `transition-duration: .01ms` 스니펫은 `transition-property`가 `all`인 채로 남아 배경·테두리·transform 같은 상태 변화가 시작값에 고정돼 아예 렌더되지 않는다 — 이 빌드에서 실제로 발생했던 결함이다.
- **Do** hover 규칙을 `@media (hover: hover)` 안에 가둔다.
- **Do** 브라우저가 그리는 표면(`::selection`, 스크롤바, `caret-color`, `accent-color`)도 팔레트에서 테마한다.
- **Do** 지도 마커·범례 색을 CSS 커스텀 프로퍼티에서 읽어 쓴다. 색값을 JS에 복제하지 않는다.

### Don't:
- **Don't** 위계 표현에 `box-shadow`를 쓰지 않는다. 이 시스템에서 허용된 `box-shadow`는 헤더 안쪽 흰 테두리와 인접 pill 구분선, 두 가지 inset뿐이다.
- **Don't** 그라디언트를 쓰지 않는다. 면은 단색이다.
- **Don't** 면색을 카드·태그·패널 바탕으로 흘리지 않는다. 유료 태그를 채우고 싶어지는 순간이 규칙이 깨지는 지점이다.
- **Don't** 유니코드 글리프나 이모지를 아이콘으로 쓰지 않는다. 아이콘은 인라인 SVG 두 계열(면 픽토그램, 1.8 선)뿐이다.
- **Don't** 6단계 밖의 `font-size`를 새로 만들지 않는다.
- **Don't** 표지판의 앱 이름을 말줄임(`text-overflow: ellipsis`)으로 자르지 않는다. 좁으면 어절 단위로 두 줄이 된다.
- **Don't** 정보를 나르지 않는 색을 추가하지 않는다. 새 색을 넣기 전에 그 색이 무엇을 말하는지 한 문장으로 적을 수 있어야 한다.
- **Don't** `select`에서 `min-width: 0`을 빼지 않는다.
