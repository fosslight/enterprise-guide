---
sort: 1
published: true
---

# Project Status  

## Project Status 이동 
{: .left-bar-title }  
- Project List에서 Project Name, OSC Process (Identification, Packaging, Distribution) 각 단계를 클릭하면 해당 단계의 tab으로 이동할 수 있습니다.  
<img src="../../images/project/status_bar/status_project.png" width="600px" height="250px" class="styled-image">  
- 각 단계의 상단 Status bar에서도 Project 상태를 확인할 수 있으며, 각 단계를 클릭하여 해당 단계의 tab으로 이동할 수 있습니다.  
<img src="../../images/project/status_bar/status_topbar.png" width="600px" height="100px" class="styled-image">  
<br><br><br>

## Self-Reject 
{: .left-bar-title }  
- Project Status가 <img src="../../images/project/status_bar/status_request_icon.png" width="60px" height="20px"> 인 상태에서 Identification과 Packaging 단계의 수정이 필요한 경우, 사용자는 Project Status를 변경할 수 있습니다.   
  1. Identification(SBOM), Packaging 단계에서 우측 상단의 <img src="../../images/project/status_bar/status_reject_icon.png" width="50px" height="20px"> 버튼을 클릭합니다.  
  <img src="../../images/project/status_bar/status_identification_reject.png" width="600px" height="150px" class="styled-image">  
  <img src="../../images/project/status_bar/status_packaging_reject.png" width="600px" height="150px" class="styled-image">  
  2. 변경이 필요한 사유를 입력하고, OK 버튼을 클릭합니다. 이때 Project Status는 <img src="../../images/project/status_bar/status_progress_icon.png" width="60px" height="20px"> 상태로 변경됩니다.  
  <img src="../../images/project/status_bar/status_reject_popup.png" width="400px" height="300px" class="styled-image">  
<br><br><br>

## Reopen 
{: .left-bar-title }  
- Project Status가 <img src="../../images/project/status_bar/status_complete_icon.png" width="60px" height="20px"> 인 경우, Reopen으로 Project Status를 <img src="../../images/project/status_bar/status_progress_icon.png" width="60px" height="20px">로 변경 요청할 수 있습니다.  
  1. Project List에서 Project Name을 클릭하여 Project Information 탭으로 이동합니다.  
  <img src="../../images/project/status_bar/status_projectname.png" width="600px" height="150px" class="styled-image">  
  2. Project Information tab 우측 상단의 <img src="../../images/project/status_bar/status_reopen_icon.png" width="50px" height="20px"> 버튼을 클릭합니다.  
  <img src="../../images/project/status_bar/status_reopen.png" width="600px" height="200px" class="styled-image">  
  3. 변경이 필요한 사유를 입력하고, 재수행이 필요한 단계(Identification 또는 Packaging)를 선택한 후 OK를 클릭합니다.  
  <img src="../../images/project/status_bar/status_reopen_popup.png" width="400px" height="300px" class="styled-image">  
<br><br><br>

## Drop & Reopen 
{: .left-bar-title }

### Drop
{: .specific-title }  
- 더 이상 Project의 OSC Process를 진행하지 않아도 되는 경우, Project를 중지할 수 있습니다.  
  1. Project Information 탭 우측 상단의 <img src="../../images/project/status_bar/status_drop_icon.png" width="50px" height="20px"> 버튼을 클릭합니다. Project Status가 <img src="../../images/project/status_bar/status_complete_icon.png" width="60px" height="20px"> 인 경우에는 Drop 기능이 동작하지 않습니다.  
  <img src="../../images/project/status_bar/status_drop.png" width="600px" height="100px" class="styled-image">  
  2. Drop 사유를 입력하고 OK 버튼을 클릭합니다.  
  <img src="../../images/project/status_bar/status_drop_reason.png" width="400px" height="300px" class="styled-image">  
 

### Reopen
{: .specific-title }  
- Project Status가 Drop인데, 다시 OSC Process를 진행해야 하는 경우 Project를 Open 할 수 있습니다.  
  1. Project Information 탭 우측 상단의 <img src="../../images/project/status_bar/status_reopen_icon2.png" width="50px" height="20px"> 버튼을 클릭합니다.  
  <img src="../../images/project/status_bar/status_reopen2.png" width="600px" height="100px" class="styled-image">
