# 로컬 미리보기: PowerShell에서 .\preview.ps1 실행 후 http://localhost:1313/ 접속 (종료: Ctrl+C)
#
# - 이미 실행 중인 hugo 가 있으면 먼저 종료한다.
#   (멈춘 예전 서버가 오래된 화면을 계속 보여 주거나, 빌드 잠금 파일 .hugo_build.lock 을 잡고 있어
#    `python .github/pages_build.py --build` 가 멈추는 문제를 실제로 겪었기 때문)
# - 결과물은 메모리에만 만들어 site/public 폴더를 남기지 않는다.

$hugoDir = Join-Path $env:LOCALAPPDATA 'Programs\hugo'
if (-not (Get-Command hugo -ErrorAction SilentlyContinue)) { $env:Path += ";$hugoDir" }
if (-not (Get-Command hugo -ErrorAction SilentlyContinue)) {
    Write-Host "hugo 를 찾을 수 없습니다. README.md 의 '2. 설치'를 먼저 진행하세요." -ForegroundColor Red
    exit 1
}

$running = Get-Process hugo -ErrorAction SilentlyContinue
if ($running) {
    Write-Host "실행 중인 hugo 프로세스 $($running.Count)개를 종료합니다." -ForegroundColor Yellow
    $running | Stop-Process -Force
    Start-Sleep -Milliseconds 500
}

Write-Host "미리보기 주소: http://localhost:1313/  (영어: http://localhost:1313/en/)  종료: Ctrl+C" -ForegroundColor Green
Set-Location (Join-Path $PSScriptRoot 'site')
hugo server --baseURL http://localhost:1313/ --appendPort=false --buildDrafts --disableFastRender --renderToMemory
