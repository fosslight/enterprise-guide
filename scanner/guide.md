---
title: Guide
sort: 2
published: true
---

# FOSSLight Scanner Database
[`fosslight_scanner`](https://pypi.org/project/fosslight-scanner/) 또는 [`fosslight_source`](https://pypi.org/project/fosslight-source/) 실행 시 FOSSLight Scanner Database의 OSS Information (OSS Name, OSS Version, Download location)을 추가로 조회할 수 있습니다.

## FOSSLight Scanner Database Token 발행 요청 방법
FOSSLight Scanner Database 접속에 필요한 Token은 아래 정보를 포함하여 [`support`](../support/)에 이슈를 생성해 발행을 요청합니다.

- 접속할 IP 또는 IP 대역
- Token을 수신할 이메일 주소

### 토큰 발행 후 접속 가능 여부 확인 방법
접속 허용 여부는 아래 방법 중 하나를 선택하여 확인합니다.
1. 실행할 서버에서 [https://kb.fosslight.org/health](https://kb.fosslight.org/health)에 접속하여 아래와 같은 응답이 표시되는지 확인합니다.
	`{"status":"healthy","redis":"ok"}`
2. FOSSLight Scanner 실행 시 생성된 로그 파일을 확인합니다.
	호출에 실패한 경우 로그에 아래와 같이 실패 사유가 남습니다.
	`KB(https://kb.fosslight.org/) Invalid token.`

## FOSSLight Scanner Database 연동 방법
`fosslight` 또는 `fosslight_source` 명령어 실행 시 `--kb_url`, `--kb_token` 옵션을 지정합니다.

예시 (fosslight, 현재 디렉터리를 분석하는 경우):
````
fosslight --kb_url "https://kb.fosslight.org/" --kb_token "example-token-1234567890abcdef" -p .
````

예시 (fosslight_source, 현재 디렉터리를 분석하는 경우):
````
fosslight_source --kb_url "https://kb.fosslight.org/" --kb_token "example-token-1234567890abcdef" -p .
````

## Tip: Scanner Database 접속 정보 저장
아래와 같이 FOSSLight Database 접속 정보를 저장하면, 명령어 실행 시 `--kb_url`, `--kb_token`을 매번 입력하지 않아도 저장된 값이 자동으로 적용됩니다.

### Linux / macOS
현재 터미널 세션에만 적용:
````
export KB_URL="https://kb.fosslight.org/"
export KB_TOKEN="example-token-1234567890abcdef"
````

쉘 시작 파일에 추가하여 계속 사용:
````
echo 'export KB_URL="https://kb.fosslight.org/"' >> ~/.bashrc
echo 'export KB_TOKEN="example-token-1234567890abcdef"' >> ~/.bashrc
source ~/.bashrc
````

zsh 사용자는 `~/.zshrc`에 추가합니다.

### Windows Command Prompt
현재 세션에만 적용:
````
set KB_URL=https://kb.fosslight.org/
set KB_TOKEN=example-token-1234567890abcdef
````

사용자 환경변수로 저장:
````
setx KB_URL "https://kb.fosslight.org/"
setx KB_TOKEN "example-token-1234567890abcdef"
````

### Windows PowerShell
현재 세션에만 적용:
````
$env:KB_URL = "https://kb.fosslight.org/"
$env:KB_TOKEN = "example-token-1234567890abcdef"
````

사용자 환경변수로 저장:
````
[System.Environment]::SetEnvironmentVariable("KB_URL", "https://kb.fosslight.org/", "User")
[System.Environment]::SetEnvironmentVariable("KB_TOKEN", "example-token-1234567890abcdef", "User")
````
