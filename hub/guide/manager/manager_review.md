---
title: 중간 관리자 리뷰 방법
sort: 2
published: true
---

# 중간 관리자 리뷰 방법

중간 관리자가 SBOM을 검토하고 리뷰를 완료하는 방법을 안내합니다.

## 리뷰 절차

1. SBOM 탭 우측 상단에 있는 **Review Start** 버튼을 클릭합니다.
2. 각 탭의 [`Warning message`](https://fosslight.org/hub-guide/tips/1_common/5_warning_message/)를 검토합니다.
   - 빨간색 Warning message 위주로 검토합니다.
   - `New Open Source, New Version`의 warning message가 있는 경우 사용자에게 download location의 입력을 가이드 합니다.
   - `New Version`의 경우 commit hash가 아닌 공식 release 버전으로 입력을 가이드 합니다. Semver형식(예: v3.2.1 → 3.2.1)에 맞춰 입력, Git 기반의 경우는 공식 태그가 있다면 해당 버전을 사용하도록 가이드 합니다.
3. Identification의 각 탭에서 [`Pre-review > Open Source, License`](https://fosslight.org/hub-guide/tips/1_common/2_pre_review/)를 수행합니다.
   - Download location이 입력이 되어있는 Row에 대해서 FOSSLight Hub DB, ClearlyDefined, Github, OROSI DB에서 OSS Name, License 정보를 가지고 오는 기능을 제공하고 있습니다. 
4. 앞 단계를 모두 진행하고도 `New Open Source, New Version`의 빨간색 Warning message가 남아 있는 경우, Comment를 남겨 LG 측에 리뷰를 요청합니다.
5. 빨간색 Warning message가 없는 경우 **Save**를 클릭한 후 **Confirm**을 클릭합니다.

Creator에게 재확인이 필요한 경우에는 **Reject**를 클릭하여 Status를 `Progress`로 변경합니다.
