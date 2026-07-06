git basics
2026-07-03

# Git 개념

                GitHub (원격 저장소)
                       ▲
                  git push
                       │
               Local Repository
                  (git commit)
                       ▲
                  git commit
                       │
                 Staging Area
                   (git add)
                       ▲
                   git add
                       │
               Working Directory
             (내가 실제로 작업하는 공간)

## Git이란?

Git은 프로그램의 **소스코드 변경 이력을 기록**하고 여러 사람과 **협업하여 개발**할 수 있게 해주는 **분산 버전 관리 시스템(DVCS)** 이다.

Git을 사용하면 파일을 수정할 때마다 새로운 파일을 계속 만드는 것이 아니라, **변경된 내용과 변경시점을 기록**하여 언제든지 이전 버전으로 되돌아가거나 변경 내역을 비교할 수 있다.



---
## 버전 관리 (Version Control)란?

버전 관리란 파일의 변경 이력을 체계적으로 관리하는 것을 의미한다.

예를 들어 보고서를 수정할 때 다음과 같이 파일을 계속 복사해서 저장한 경험이 있을 것이다.

report.docx
report_v1.docx
report_final.docx
report_final_final.docx

이러한 방식은 어떤 파일이 최신인지 알기 어렵고, 이전 변경 내용을 추적하기도 힘들다.

Git을 사용하면 하나의  파일만 유지하면서도 모든 변경 이력을 기록하고 관리할 수 있다.

--- 

## 분산 버전 관리 시스템(DVCS)이란?

Git은 중앙 서버에만 코드가 저장되는 방식이 아니라, 각 개발자의 컴퓨터에도 프로젝트 전체와 변경 이력이 모두 저장되는 구조이다.

즉, Github 서버가 없어도
- commit
- branch 생성
- 이전 변경 복원
- 변경 이력 조회
등 대부분의 작업을 내 컴퓨터에서 수행할 수 있다.

인터넷이 연결되면 Github와 동기화 (Push/Pull) 하면 된다.
---
##  왜 GIT이 만들어졌는가?

소프트웨어 개발이 점점 커지면서 다음과 같은 문제가 발생한다.
- 여러 개발자가 동시에 같은 파일을 수정
- 이전 버전으로 복원해야 하는 상황 발생
- 누가 어떤 코드를 수정했는지 확인이 어려움
- 협업 과정에서 코드가 덮어쓰여지는 문제 발생

이러한 문제를 해결하기 위해 Git이 만들어졌다.

Git은 모든 변경 사항을 기록하고, 여러 사람이 동시에 작업하더라도 변경 내용을 안전하게 병합(Merge)할 수 있도록 설계되었다.
---
## 왜 개발자는 GIT을 사용하는가?
1. 변경 이력을 모두 기록할 수 있다.
2. 이전 버전으로 언제든지 복구할 수 있다.
3. 여러 개발자가 동시에 협업할 수 있다.
4. 실험적인 기능을 Branch로 안전하게 개발할 수 있다.
5. GitHub와 연동하여 프로젝트를 백업하고 관리할 수 있다.

즉, Git은 단순히 코드를 저장하는 도구가 아니라 개발 협업 핵심 도구이다.
---

## Git 과 GitHub의 차이
- Git : 소스 코드 버전을 관리하는 프로그램(도구) 자체. 내 컴퓨터 내에서 버전을 관리함
- GitHub : Git으로 관리하는 프로젝트를 인터넷상에 올려두고, 전 세계 개발자들과 공유하거나 협업할 수 있도록 돕는 원격 저장소 웹 호스팅 서비스

<구조>
Git -> 내 컴퓨터 -> GitHub -> 클라우드

### Git/GitHub 관계
(1) 내 컴퓨터에서 코드 작업

    내 MacBook
    AI-Learning/
    │
    ├── README.md
    ├── notes/
    │   └── 2026-07-02-git-basics.md
    └── python-practice/

(2) Git 이 변경사항 기록

 $ git add .
 $ git commit -m "Add Git notes"

    실행 시, 

    내 MacBook
    AI-Learning/
    │
    ├── README.md
    ├── notes/
    │   └── 2026-07-02-git-basics.md
    │
    └── .git  ← Git이 변경 이력을 저장하는 공간

    * Git은 내 컴퓨터 안에서만 동작함
    * 즉, 이 시점에는 GitHub에 아무것도 올라가지 않음

(3) GitHub는 인터넷에 있는 저장소

 $ git push 
 를 하면

                    git push
    내 컴퓨터  --------------------->  GitHub

    AI-Learning                    AI-Learning
    README.md                      README.md
    notes/                         notes/
    python-practice/               python-practice/

즉, 내 컴퓨터의 Git 저장소를 GitHub에 복사

        인터넷

    ┌───────────────┐
    │    GitHub     │
    │ (원격 저장소)    │
    └──────▲────────┘
            │
    git push / pull
            │
            ▼
┌──────────────────┐
│   내 컴퓨터        │
│                  │
│ AI-Learning      │
│                  │
│  Git(.git)       │
│  변경 이력 관리     │ 
└──────────────────┘
--- 
## Repository 란
### Repository(저장소)란
Repository는 프로젝트의 모든 파일과 Git의 변경 이력(Commit)을 저장하는 공간이다.

Repository 안에는 현재 프로젝트의 파일뿐만 아니라, 누가 언제 무엇을 수정했는지에 대한 모든 기록도 함께 저장된다.

예를 들어, 현재 아래 프로젝트는 하나의 Repository 이다.
AI-Learning (Repository)
│
├── README.md
├── notes/
├── python-practice/
└── .git/

여기서 .git 폴더가 Git의 모든 기록을 저장하는 공간이다.

### 왜 프로젝트 하나당 하나의 Repository를 만들까?
프로젝트마다 목적과 변경 이력이 다르기 때문이다.
그래서 프로젝트별로 Repository를 분리한다.

## Git의 작업 흐름
Working Directory
        │
   git add
        ▼
Staging Area
        │
 git commit
        ▼
Local Repository
        │
  git push
        ▼
GitHub(Remote Repository)

### Working Directory
내가 실제로 작업하는 공간

### Staging Area
이번 Commit에 포함할 파일을 선택하는 공간
 $ git add 파일명
해당 파일이 Commit에 들어간다.

### Commit (Local Repository)
현재 Staging Area의 내용을 하나의 버전으로 저장하는 것
저장된 위치는 Local Repository 이다.
 $ git commit -m "Update File"

** git commit은 로컬 저장소(Local Repository)에 저장됨

### Push
Local Repository의 Commit을 GitHub(Remote Repository)로 업로드하는 작업
 $ git push
Local Repository 가 GitHub로 복사된다.


### Pull
Push의 반대 개념으로, GitHub에 있는 최신 내용을 내 컴퓨터로 가져오는 작업이다.

### Git 사용 작업 요약
 개발자 A
 1. 코드 수정 (Working Directory)
 2. $ git add -> Staging Area
 3. $ git commit -> Local Repository
 4. $ git push -> GitHub Repository

 다른 개발자 B
 1. git pull -> Local Repository로 최신 코드 다운로드

# Git 사용법
1. 프로젝트 생성 
   - mkdir AI-Study
   - cd AI-Study
2. Git 시작
   - git init
3. 파일 생성
   - echo "# AI Study" > README.md
4. 추가
   - git add .
5. 커밋
   - git commit -m "Initial Commit"
6. GitHub 저장소 연결
   - git remote add origin git@github.com:username/AI-Study.git
7. 최초 업로드
   - git push -u origin main
8. 이후 파일 수정 시,
   - git add.
   - git comit -m "설명"
   - git push