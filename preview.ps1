# 로컬 미리보기: PowerShell에서 .\preview.ps1 실행 후 http://localhost:1313/ 접속 (종료: Ctrl+C)
$hugoDir = Join-Path $env:LOCALAPPDATA 'Programs\hugo'
if (-not (Get-Command hugo -ErrorAction SilentlyContinue)) { $env:Path += ";$hugoDir" }
Set-Location (Join-Path $PSScriptRoot 'site')
hugo server --baseURL http://localhost:1313/ --appendPort=false --buildDrafts --disableFastRender
