---
title: 리뷰 요청 방법
sort: 1
published: true
---

# 리뷰 요청 방법

리뷰 요청 전 검출된 OSS 정보를 정제하는 방법을 안내드립니다.

## 검출된 OSS 정제

리뷰 요청 전 아래 항목을 확인하고 정제합니다.

1. 배포에 포함되지 않는 Row는 삭제합니다. (예: Build Script 등)
2. 실제 사용한 오픈소스가 아닌 오검출 Row는 삭제합니다.
3. `Download location`이 비어 있는 Row에는 실제 소스코드를 다운로드할 수 있는 경로를 입력합니다.
4. **Download location**이 입력된 상태에서 OSS Name, License 정보를 채우거나, 실제 DB에 저장된 값으로 변경하고 싶은 경우에 각 탭에서 [`Pre-review > Open Source, License`](https://fosslight.org/hub-guide/tips/1_common/2_pre_review/)를 수행합니다.
5. `New Version`의 warning의 경우 commit hash가 아닌 공식 release 버전으로 입력합니다. Semver형식(예: v3.2.1 → 3.2.1)에 맞춰 입력해 주시고, Git 기반의 경우는 공식 태그가 있다면, 해당 버전을 사용하시길 권장합니다. 
6. 그 외 빨간색 warning message 위주로 [`Warning message`](https://fosslight.org/hub-guide/tips/1_common/5_warning_message/)를 검토합니다.

## 리뷰 요청 절차

- SBOM 탭에서 **Save** 버튼을 클릭합니다.
  - 3rd Party, SRC, DEP, BIN 탭에 작성한 OSS List를 취합합니다.
- Request 버튼을 클릭하여 리뷰 요청을 합니다.
  - 단, 빨간색 Warning Message가 있을 경우 리뷰 요청이 불가합니다.
