
```text
Python
      ↓
MCU / Computer Architecture
      ↓
OS / Linux
      ↓
CAN / UDS / Automotive Ethernet
      ↓
Machine Learning
      ↓
LLM / RAG
      ↓
SBOM
      ↓
Vehicle Security Assistant
      ↓
AI Agent
      ↓
CAN / Ethernet 심화
      ↓
IDS Rule
      ↓
Firmware Reverse Engineering
      ↓
TARA / Secure Boot / HSM
      ↓
Vehicle Cybersecurity Copilot
```
# 2026년 7월

## 목표
Python 기초를 익히고 차량 소프트웨어 및 임베디드 시스템의 기본 구조를 이해한다.

---

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
- Python 변수
- 자료형
- 조건문
- 반복문
- 함수
- 파일 입출력
- MCU란?
- CPU와 MCU의 차이

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
- Flash Memory
- RAM
- EEPROM

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
- GPIO
- Interrupt
- CAN 기본 구조
- CAN Frame
- CAN ID
- DLC
- Arbitration

산출물
- CVE 조회 자동화
- SBOM 자동 분석기
- Python CLI Tool

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

Python 데이터 분석 능력을 익히고 컴퓨터 구조 및 차량 진단 프로토콜을 이해한다.

---

### 1주차

주제
- NumPy 기초
- ndarray
- 배열 연산
- CPU 동작 원리
- Cache Memory

산출물
- NumPy 실습 노트
- 배열 데이터 처리 예제

---

### 2주차

주제
- Pandas
- DataFrame
- CSV 처리
- Stack
- Heap
- Memory Layout

산출물
- 로그 CSV 분석
- 데이터 전처리

---

### 3주차

주제
- Matplotlib
- 그래프
- 통계 시각화
- UDS
- Diagnostic Session
- Security Access

산출물
- 이벤트 그래프
- 시간별 이벤트 그래프
- Severity 그래프

---

### 4주차

주제
- 로그 데이터 통합 분석
- ReadDataByIdentifier
- WriteDataByIdentifier
- DID 개념

산출물
- Dashboard
- 로그 분석 Notebook

---

### 프로젝트

Vehicle Log Dashboard

구현 기능

- CSV 읽기
- 시간별 이벤트 분석
- ECU별 이벤트 분석
- Severity 분석
- 그래프 출력

---

# 2026년 9월

## 목표

Machine Learning 기반 이상 탐지를 구현하고 Linux 및 차량 Ethernet의 기본 구조를 이해한다.

---

### 1주차

주제
- AI 개념
- Machine Learning
- 지도학습
- 비지도학습
- Process
- Thread

산출물
- AI 개념 정리
- Process와 Thread 비교 정리

---

### 2주차

주제
- scikit-learn
- 데이터 전처리
- Virtual Memory
- Linux Process

산출물
- 학습 데이터 생성
- Linux Process 실습

---

### 3주차

주제
- Anomaly Detection
- Isolation Forest
- One-Class SVM
- ps
- top
- /proc

산출물
- 이상 탐지 모델
- Linux Process 분석

---

### 4주차

주제
- 모델 평가
- 결과 분석
- Automotive Ethernet
- Ethernet Frame
- SOME/IP
- DoIP

산출물
- IDS 이상 탐지 프로그램
- Ethernet Packet 분석

---

### 프로젝트

Vehicle IDS Anomaly Detection

구현 기능

- 정상 로그 학습
- 이상 로그 탐지
- 결과 시각화
- Ethernet 로그 분석

# 2026년 10월

## 목표
LLM을 활용하여 차량 사이버보안 업무를 지원하는 AI 애플리케이션을 개발한다.

---

### 1주차

주제
- OpenAI API
- API Key 관리
- Prompt Engineering
- DLT(Log & Trace) 구조
- ECU Logging 구조

산출물
- OpenAI API 실습
- 로그 요약 AI

---

### 2주차

주제
- Embedding
- Vector Database
- Chunking
- TCP/IP
- UDP
- Socket 기초

산출물
- Vector Search
- 문서 검색 시스템

---

### 3주차

주제
- RAG(Retrieval-Augmented Generation)
- Context 구성
- Prompt 최적화
- OSI 7계층
- Routing 기초

산출물
- RAG Pipeline
- 차량 보안 문서 검색기

---

### 4주차

주제
- LangChain
- Tool Calling 기초
- AI Workflow
- 차량 로그 분석 자동화

산출물
- LLM Application
- 차량 보안 Q&A Assistant

---

### 프로젝트

CVE Search AI

구현 기능

- CVE 검색
- 영향 분석
- 패치 방법 추천
- 완화 방안 생성
- AI 질의응답

---

# 2026년 11월

## 목표
SBOM과 차량 IDS를 이해하고 AI 기반 보안 분석기를 구현한다.

---

### 1주차

주제
- SBOM 개요
- SPDX
- SBOM 생성 원리
- CAN IDS 개념

산출물
- SPDX Parser

---

### 2주차

주제
- CycloneDX
- Component 분석
- Dependency 구조
- Ethernet IDS 개념

산출물
- CycloneDX Parser

---

### 3주차

주제
- SBOM Parsing
- CVE 매핑
- 10BASE-T1S
- 100BASE-T1

산출물
- SBOM 분석기

---

### 4주차

주제
- AI 기반 SBOM 분석
- 위험도 계산
- PHY
- MAC
- TSN 개요

산출물
- AI SBOM Analyzer

---

### 프로젝트

SBOM Analysis AI

구현 기능

- SPDX 분석
- CycloneDX 분석
- CVE 조회
- 위험도 계산
- AI 분석 리포트 생성

---

# 2026년 12월

## 목표
차량 사이버보안 Assistant를 개발하여 로그 분석과 보안 대응을 자동화한다.

---

### 1주차

주제
- IDS 로그 분석
- CAN 로그 분석
- Bootloader 개념

산출물
- 로그 분석 모듈

---

### 2주차

주제
- AI 응답 생성
- 공격 추론
- Boot Process
- Firmware Update

산출물
- AI 응답 모듈

---

### 3주차

주제
- 보고서 자동 생성
- 대응 방안 추천
- Secure Boot 개념

산출물
- 보안 보고서 생성기

---

### 4주차

주제
- 프로젝트 통합
- 코드 리팩토링
- 테스트
- 문서화

산출물
- Vehicle Security Assistant

---

### 프로젝트

Vehicle Cybersecurity Assistant

구현 기능

- IDS 로그 분석
- CAN/Ethernet 로그 분석
- 공격 추론
- 영향 ECU 분석
- 대응 방안 추천
- 보안 보고서 생성
- AI 질의응답


# 2027년 1월

## 목표
AI Agent를 이해하고 차량 사이버보안 업무를 자동화할 수 있는 Agent를 개발한다.

---

### 1주차

주제
- Function Calling
- OpenAI Tools
- RTOS 개요
- Task와 Process의 차이

산출물
- Function Calling 실습
- RTOS 개념 정리

---

### 2주차

주제
- Tool Calling
- Tool 설계
- RTOS Scheduler
- Context Switching

산출물
- Tool Calling 예제
- AI Tool 개발

---

### 3주차

주제
- MCP(Model Context Protocol)
- AI Workflow
- Interrupt
- RTOS와 Interrupt

산출물
- MCP 실습
- AI Workflow 구현

---

### 4주차

주제
- Multi Agent
- Agent 협업 구조
- Memory 관리
- AI Agent 설계

산출물
- Security AI Agent

---

### 프로젝트

Security AI Agent

구현 기능

- Tool Calling
- CVE 검색
- SBOM 분석
- IDS 로그 분석
- 차량 보안 문서 검색
- AI Agent Workflow

---

# 2027년 2월

## 목표
차량 네트워크를 심층적으로 이해하고 패킷 분석기를 구현한다.

---

### 1주차

주제
- CAN Protocol
- CAN Frame 구조
- CAN Physical Layer

산출물
- CAN Frame 분석

---

### 2주차

주제
- CAN FD
- CAN Controller
- CAN Transceiver

산출물
- CAN FD Parser

---

### 3주차

주제
- Automotive Ethernet
- Ethernet PHY
- Ethernet Switch

산출물
- Ethernet Packet 분석

---

### 4주차

주제
- DoIP
- SOME/IP
- 차량 네트워크 통신 흐름

산출물
- DoIP Packet 분석

---

### 프로젝트

CAN Packet Analyzer

구현 기능

- CAN Frame Parser
- CAN FD Parser
- Packet 분석
- CSV Export
- Packet 시각화

---

# 2027년 3월

## 목표
IDS Rule을 이해하고 차량 환경에 적용 가능한 탐지 규칙을 생성한다.

---

### 1주차

주제
- IDS 개념
- Signature 기반 탐지
- Anomaly 기반 탐지
- Socket Programming 기초

산출물
- IDS 개념 정리

---

### 2주차

주제
- Suricata
- Rule 구조
- Packet Capture
- libpcap 개요

산출물
- Suricata Rule 작성

---

### 3주차

주제
- Zeek
- Event 기반 분석
- Wireshark
- Packet 분석

산출물
- Zeek Script 실습

---

### 4주차

주제
- Sigma Rule
- Rule 변환
- tcpdump
- Packet Filtering

산출물
- IDS Rule Generator

---

### 프로젝트

Vehicle IDS Rule Generator

구현 기능

- Rule 생성
- Rule 검증
- 로그 테스트
- Packet 분석
- Rule 자동 생성

# 2027년 4월

## 목표
Firmware Reverse Engineering 기초를 익히고 ECU Firmware의 구조를 이해한다.

---

### 1주차

주제
- ELF 파일 구조
- 실행 파일 포맷
- Memory Map
- Flash Memory Layout

산출물
- ELF 구조 분석
- Memory Map 정리

---

### 2주차

주제
- PE 파일 구조
- Section
- Vector Table
- Interrupt Vector

산출물
- PE 구조 분석
- Vector Table 분석

---

### 3주차

주제
- Ghidra 사용법
- Static Analysis
- Linker Script 개념

산출물
- Ghidra 분석 실습
- Linker Script 정리

---

### 4주차

주제
- Firmware 분석
- 함수 분석
- Startup Code
- Boot Sequence

산출물
- Firmware 분석 보고서

---

### 프로젝트

Firmware Analyzer

구현 기능

- Binary 분석
- 문자열 추출
- 함수 분석
- Memory Map 분석
- Firmware 정보 추출

---

# 2027년 5월

## 목표
차량 보안 설계를 이해하고 Threat Modeling을 수행할 수 있다.

---

### 1주차

주제
- TARA
- Asset 식별
- Damage Scenario
- Root of Trust

산출물
- TARA 실습

---

### 2주차

주제
- Attack Tree
- Attack Path
- Risk Assessment
- Secure Flash

산출물
- Attack Tree 작성

---

### 3주차

주제
- Secure Boot
- Secure Update
- Chain of Trust
- Secure Debug

산출물
- Secure Boot 구조 정리

---

### 4주차

주제
- HSM
- Key Management
- Secure Storage
- ECU Security Architecture

산출물
- Threat Modeling 문서

---

### 프로젝트

Threat Modeling AI

구현 기능

- Threat 생성
- Attack Tree 작성
- Risk 분석
- 대응 방안 생성
- AI 기반 Threat Modeling

---

# 2027년 6월

## 목표
1년 동안 개발한 프로젝트를 하나의 AI 기반 차량 사이버보안 플랫폼으로 통합한다.

---

### 1주차

주제
- 프로젝트 구조 설계
- 시스템 아키텍처
- 모듈 설계

산출물
- 시스템 아키텍처 문서

---

### 2주차

주제
- 기능 통합
- API 연동
- 데이터 흐름 설계

산출물
- 통합 플랫폼 Prototype

---

### 3주차

주제
- UI 개선
- 사용성 개선
- 테스트
- 성능 최적화

산출물
- Beta Version

---

### 4주차

주제
- 문서화
- GitHub 정리
- README 작성
- 프로젝트 배포

산출물
- Vehicle Cybersecurity Copilot v1.0

---

### 프로젝트

Vehicle Cybersecurity Copilot

구현 기능

- AI 질의응답
- IDS 로그 분석
- CAN/Ethernet 로그 분석
- SBOM 분석
- CVE 분석
- Threat Modeling
- 보안 보고서 생성
- Firmware 분석
- AI Agent Workflow