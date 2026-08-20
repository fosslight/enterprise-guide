---
sort: 2 
published: true
title: 2.Identification 
---


# Identification 
<div class="note">
배포하는 Project에 대하여 Open Source Software 분석 결과를 작성하고, OSPO의 리뷰를 받습니다.
</div>

{% include list.liquid all=true %}

## 일반 Project의 Identification Process
{: .left-bar-title }
- **3rd Party, DEP 탭, SRC, BIN 탭 작성 → SBOM 탭**에서 **Request** 버튼을 클릭하여 리뷰 요청  
        - [**3rd Party, DEP, SRC, BIN**](https://fosslight.org/hub-guide/tutorial/1_project/2_Identification/1_3rd_DEP_SRC_BIN_Tab.html): 분석 결과 Report를 업로드 하거나 Confirm된 Project, 3rd Party를 Load합니다.  
        - [**SBOM**](https://fosslight.org/hub-guide/tutorial/1_project/2_Identification/2_SBOM_Tab.html): 다른 탭에 작성된 OSS List를 취합하고 Warning message를 검토한 후 리뷰 요청을 합니다.  

## (LGE Only) Platform-generated Project의 Identification Process
{: .left-bar-title }
- BIN(Android), BIN(Yocto) Tab : 각 탭 작성 → Request 버튼을 클릭하여 리뷰 요청합니다.  
        - BIN(Android) : [Android binary 분석](https://fosslight.org/fosslight-guide/android/) 결과를 작성합니다.  
        - BIN(Yocto) : [Yocto 분석](https://fosslight.org/fosslight-guide/yocto/) 결과를 작성합니다.  