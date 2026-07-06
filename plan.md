# PLAN
# AI + 차량 사이버보안 학습 로드맵
기간 : 2026.07 ~ 2027.06

---

# 2026년 7월
## 목표
Python 기초를 익히고 보안 자동화 프로그램을 작성할 수 있다.

### 1주차 (완료)
주제
- Git
- GitHub
- SSH
- Markdown
- VS Code 개발환경 구축

산출물
- Git Repository 구축
- SSH Key 연동
- Markdown 문서 작성
- AI-Learning 개발환경 구축

---

### 2주차
주제
- 변수
- 자료형
- 조건문
- 반복문
- 함수
- 파일 입출력

산출물
- Python 기초 예제
- 로그 파일 읽기 프로그램
- 문자열 검색 프로그램
- CLI 로그 검색기

---

### 3주차
주제
- 클래스(OOP)
- 예외처리
- JSON
- CSV
- Module

산출물
- JSON Parser
- CSV Reader
- 차량 로그(JSON) 분석기
- SBOM(JSON) Reader

---

### 4주차
주제
- requests
- pathlib
- subprocess
- argparse

산출물
- CVE 조회 자동화
- SBOM 자동 분석기
- Python CLI Tool

---

### 차량보안 병행학습
- CAN 기본 구조
- CAN Frame
- CAN ID
- DLC
- Arbitration
- CAN 통신 흐름

---

### 프로젝트
Python Security Toolkit

구현 기능

- 로그 검색
- JSON 분석
- SBOM Reader
- CVE 자동 조회
- CLI 프로그램

---

# 2026년 8월
## 목표
Python 데이터 분석 능력을 익히고 로그를 시각화한다.

### 1주차
주제
- NumPy 기초
- ndarray
- 배열 연산

산출물
- NumPy 실습 노트
- 배열 데이터 처리 예제

---

### 2주차
주제
- Pandas
- DataFrame
- CSV 처리

산출물
- 로그 CSV 분석
- 데이터 전처리

---

### 3주차
주제
- Matplotlib
- 그래프
- 통계 시각화

산출물
- 이벤트 그래프
- 시간별 이벤트 그래프
- Severity 그래프

---

### 4주차
주제
- 로그 데이터 통합 분석

산출물
- Dashboard
- 로그 분석 Notebook

---

### 차량보안 병행학습
- UDS
- Diagnostic Session
- Security Access
- ReadDataByIdentifier
- WriteDataByIdentifier

---

### 프로젝트
Vehicle Log Dashboard

구현 기능

- CSV 읽기
- 시간별 이벤트
- ECU별 이벤트
- Severity 분석
- 그래프 출력

---

# 2026년 9월
## 목표
Machine Learning을 이용한 이상 탐지를 구현한다.

### 1주차
주제
- AI 개념
- Machine Learning
- 지도학습
- 비지도학습

산출물
- AI 개념 정리

---

### 2주차
주제
- scikit-learn
- 데이터 전처리

산출물
- 학습 데이터 생성

---

### 3주차
주제
- Anomaly Detection
- Isolation Forest
- One-Class SVM

산출물
- 이상 탐지 모델

---

### 4주차
주제
- 모델 평가
- 결과 분석

산출물
- IDS 이상 탐지 프로그램

---

### 차량보안 병행학습
- Automotive Ethernet
- SOME/IP
- DoIP
- Ethernet Packet 구조

---

### 프로젝트
Vehicle IDS Anomaly Detection

구현 기능

- 정상 로그 학습
- 이상 로그 탐지
- 결과 시각화

---

# 2026년 10월
## 목표
LLM 기반 보안 도우미를 만든다.

### 1주차
- OpenAI API
- Prompt Engineering

산출물
- API 실습

---

### 2주차
- Embedding
- Vector Database

산출물
- Vector Search

---

### 3주차
- RAG

산출물
- RAG Pipeline

---

### 4주차
- LangChain

산출물
- LLM Application

---

### 차량보안 병행학습
- DLT 로그
- Logging 구조
- ECU 로그

---

### 프로젝트
CVE Search AI

구현 기능

- CVE 검색
- 영향 분석
- 패치 방법
- 완화조치 생성

---

# 2026년 11월
## 목표
SBOM 기반 AI 분석기를 만든다.

### 1주차
- SPDX

### 2주차
- CycloneDX

### 3주차
- SBOM Parsing

### 4주차
- AI 연동

산출물
- SBOM 분석기

---

### 차량보안 병행학습
- CAN IDS
- Ethernet IDS
- 공격 패턴
- 탐지 원리

---

### 프로젝트
SBOM Analysis AI

구현 기능

- SPDX 분석
- CycloneDX 분석
- CVE 조회
- 위험도 계산

---

# 2026년 12월
## 목표
차량 사이버보안 Assistant를 개발한다.

### 1주차
- 로그 분석

### 2주차
- AI 응답 생성

### 3주차
- 보고서 생성

### 4주차
- 프로젝트 통합

산출물
- Vehicle Security Assistant

---

### 차량보안 병행학습
- 실제 IDS 로그 분석
- 공격 사례 분석
- AI 적용 아이디어 정리

---

### 프로젝트
Vehicle Cybersecurity Assistant

구현 기능

- IDS 로그 분석
- 공격 추론
- 영향 ECU 분석
- 대응 방안 추천
- 보고서 생성

---

# 2027년 1월
## 목표
AI Agent를 이해하고 Tool Calling을 구현한다.

### 1주차
- Function Calling

### 2주차
- Tool Calling

### 3주차
- MCP 개념

### 4주차
- Multi Agent

산출물
- Security Agent

---

### 프로젝트
Security AI Agent

구현 기능

- Tool Calling
- CVE 검색
- SBOM 분석
- 로그 분석

---

# 2027년 2월
## 목표
차량 네트워크를 깊이 이해한다.

### 1주차
- CAN

### 2주차
- CAN FD

### 3주차
- Ethernet

### 4주차
- DoIP

산출물
- CAN Packet Parser

---

### 프로젝트
CAN Packet Analyzer

구현 기능

- CAN Frame Parser
- Packet 분석
- CSV Export

---

# 2027년 3월
## 목표
IDS Rule을 이해하고 생성한다.

### 1주차
- IDS 개념

### 2주차
- Suricata

### 3주차
- Zeek

### 4주차
- Sigma Rule

산출물
- IDS Rule Generator

---

### 프로젝트
Vehicle IDS Rule Generator

구현 기능

- Rule 생성
- Rule 검증
- 로그 테스트

---

# 2027년 4월
## 목표
Firmware Reverse Engineering 기초를 익힌다.

### 1주차
- ELF

### 2주차
- PE

### 3주차
- Ghidra

### 4주차
- Firmware 분석

산출물
- Firmware 분석 보고서

---

### 프로젝트
Firmware Analyzer

구현 기능

- Binary 분석
- 문자열 추출
- 함수 분석

---

# 2027년 5월
## 목표
차량 보안 설계를 이해한다.

### 1주차
- TARA

### 2주차
- Attack Tree

### 3주차
- Secure Boot

### 4주차
- HSM

산출물
- Threat Modeling 문서

---

### 프로젝트
Threat Modeling AI

구현 기능

- Threat 생성
- Attack Tree 작성
- 대응방안 생성

---

# 2027년 6월
## 목표
1년간 만든 프로젝트를 하나의 AI 플랫폼으로 통합한다.

### 1주차
- 프로젝트 통합 설계

### 2주차
- 기능 통합

### 3주차
- UI 개선

### 4주차
- 문서화 및 배포

산출물
- Vehicle Cybersecurity Copilot

---

### 프로젝트
Vehicle Cybersecurity Copilot

구현 기능

- 로그 분석
- SBOM 분석
- CVE 분석
- IDS 분석
- AI 질의응답
- 보안 보고서 생성