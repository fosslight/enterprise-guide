---
sort: 1
published: true
---

# Create Self-Check Project
<div class="note">
Self-Check 프로젝트를 생성하고, 검토할 OSS 목록을 OSS 보고서를 이용하여 일괄 추가하거나 UI 상에서 하나씩 추가할 수 있습니다.  
</div>

## Self-Check Project 생성 
{: .left-bar-title }
1. Self-Check list 좌측 상단의 Add 버튼을 클릭합니다. 
![selfcheck_create_project_1](images/1_self_check_create_1.png){: .styled-image}    
2. Self-Check 정보를 기입하고, Save 합니다.
![selfcheck_create_project_2](images/1_self_check_create_2.png){: .styled-image}  
3. Self-Check List에서 새로 생성한 Self-Check Project를 확인할 수 있고, List에서 클릭 시 상세 내용을 확인할 수 있습니다.


## OSS 정보 입력 
{: .left-bar-title }

### OSS Table에 수기로 작성
{: .specific-title}  
1. OSS Table의 좌측 상단 + 버튼을 클릭하여 OSS 정보를 기입합니다.
2. 추가된 Row에 정보(OSS Name, OSS Version, License)를 입력합니다.
    - OSS Name, OSS Version을 입력하면 FOSSLight Hub에 저장된 정보인 경우 [**OSS 정보 자동 완성**](../../tips/1_common/1_oss_table/README.md)으로 정보를 불러옵니다. 


### Upload Analysis Result 
{: .specific-title}
1. Upload Analysis Result란에 OSS 리스트가 기재된 FOSSLight Report를 업로드합니다. 
  업로드 가능한 FOSSLight Report 양식은 Export 버튼을 클릭하여 다운로드 받을 수 있습니다.
  ![selfcheck_add_oss_1](images/1_self_check_file_uplad.png){: .styled-image}
2. OSS List가 작성된 Sheet를 선택하고 OK 클릭합니다.  
3. Save 버튼(<img src="images/save_button.png" width="20" height="20" />)을 클릭합니다. 


### (LGE Only) FOSSLight Scanner Service 분석 결과 Load 
{: .specific-title}
**FOSSLight Hub의 Self-check와 [FOSSLight Scanner Service](http://fs.lge.com/)는 연동되어 있습니다.**    
방법 1. URL을 선택하여 분석할 소스 링크 (wget 또는 git clone 하여 받을 수 있는 링크)를 입력하고 Send를 클릭합니다.
   ![selfcheck_add_oss_3](images/1_self_check_add_oss_url.png){: .styled-image}
방법 2. [FOSSLight Scanner Service](http://fs.lge.com/)에 분석 완료한 Project의 결과 Report를 load합니다.
   ![selfcheck_fs_list](images/1_self_check_add_prj_id.png){: .styled-image}
