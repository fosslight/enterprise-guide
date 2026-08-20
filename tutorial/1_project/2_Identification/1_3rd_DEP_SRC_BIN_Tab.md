---
sort: 1
published: true
---

# 3rd Party/DEP/SRC/BIN Tab
<div class="note">
분석 결과 Report를 Upload 하거나 Confirm된 Project 또는 3rd Party를 Load 할 수 있습니다.
</div>  

## 작성 Process
{: .left-bar-title }
- [FOSSLight Scanner](https://fosslight.org/fosslight-guide/scanner/)의 분석 결과 업로드
- [**Warning message 검토**](https://fosslight.org/hub-guide/tips/1_common/5_warning_message)

## OSS Table에 수기로 작성
{: .left-bar-title }
OSS Table의 좌측 상단 + 버튼을 클릭하여 OSS 정보를 기입합니다.

## 분석 Report Upload
{: .left-bar-title }
1. Upload 영역의 + 버튼을 클릭합니다. (처음 Upload를 하는 경우는 2번 화면이 보이게 됩니다.)
<img src="images/1_upload_report1.png" alt="select" class="styled-image">
2. Upload Analysis Result를 선택 한 후, Upload 버튼 클릭하여 FOSSLight Report 파일을 업로드합니다.  
Report는 Excel, SPDX, CycloneDX 형식의 문서가 업로드 가능합니다.
<img src="images/1_upload_report2.png" alt="select" class="styled-image">
3. 좌측에 sheet 목록이 표시되고, 우측에서 업로드할 탭을 선택합니다.  
한 sheet는 한 탭에만 매핑되며, 탭 이름으로 시작하는 sheet가 기본 선택됩니다. 로드하지 않을 sheet는 체크를 해제합니다.
<img src="images/1_select_sheet.png" alt="select" class="styled-image">
4. Save 클릭시, 업로드한 report 파일의 data가 하단의 OSS Table에 로드되면서 저장됩니다.

## Project/3rd Party Search
{: .left-bar-title }
Status가 Confirm 상태인 Project 또는 3rd Party를 Load합니다.  

1. Upload 영역의 + 버튼을 클릭합니다. (처음 Load를 하는 경우는 2번 화면이 보이게 됩니다.)
<img src="images/1_upload_report1.png" alt="select" class="styled-image">
2. Project Search 또는 3rd Party를 Search를 선택합니다.  
Project/3rd party Name, ID로 불러올 Project 또는 3rd Party를 검색합니다.
<img src="images/1_project_search.png" alt="select" class="styled-image">
<img src="images/1_3rd_search.png" alt="select" class="styled-image">
3. Load할 탭을 선택합니다. 선택한 탭과 동일한 이름의 탭에만 데이터가 로드됩니다. (예: SRC 선택 시 SRC 탭에만 로드)
<img src="images/1_select_tab.png" alt="select" class="styled-image">
4. Save 클릭시, 하단의 OSS Table에 선택한 project 또는 3rd party의 data가 로드되면서 저장됩니다.


## Upload / Load된 데이터 표시
{: .left-bar-title }
<img src="images/1_loaded_item.png" alt="select" class="styled-image">
1. Load된 3rd party
2. Load된 project
3. Upload된 report 파일
4. Total : Upload된 Report 파일 수와 Load된 project, 3rd party 수
OSS Components : 각 탭에 로드된 oss component 수

<img src="images/1_oss_component_comment.png" alt="select" class="styled-image">
- OSS Table의 Comment Column에 출처가 표시됩니다. 

## Delete
{: .left-bar-title }
<img src="images/1_delete1.png" alt="select" class="styled-image">

1. 삭제하고자 하는 하나의 row만을 선택하여 휴지통 아이콘을 클릭하면 아래의 팝업이 뜹니다.
<img src="images/1_delete2.png" alt="select" class="styled-image">
2. OK 클릭시, 선택한 row가 삭제되고 선택한 row로 부터 load된 하단의 OSS Table 데이터가 모두 삭제되고 저장됩니다.
3. 이때 아무것도 선택하지 않거나 두개 이상의 row를 선택시 아래의 팝업이 뜹니다.
<img src="images/1_delete3.png" alt="select" class="styled-image">

## Reset
{: .left-bar-title }
<img src="images/1_reset1.png" alt="select" class="styled-image">
1. Reset 버튼을 클릭합니다.
2. Upload, load된 모든 row가 체크가 되고 모든 데이터가 삭제된다는 팝업이 뜹니다.
<img src="images/1_reset2.png" alt="select" class="styled-image">
3. OK 클릭시 선택된 모든 row가 삭제되고 OSS Table의 모든 데이터가 삭제되고 저장됩니다.
4. 각 탭을 개별로 reset을 하길 원하는 경우, 각 탭 내에 위치한 reset 버튼을 클릭하면 됩니다.
