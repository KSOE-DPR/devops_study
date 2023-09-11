# DevOps 실습 

## 준비

### Using Docker

- `devops_study` 경로에서 빌드 및 실행
    ```bash
    docker build -t devops:devops -f docker/Dockerfile .
    docker run -itd --name devops_study devops:devops /bin/bash
    ```
- 빌드된 컨테이너 접속
    ```bash
    docker exec -it devops_study /bin/bash
    ```

## ROS2 Project 관리

1. [X] Github Repository 
    - Clone "KSOE-DPR/devops_study" 

2. [X] [STUDY] Git branch 전략/관리
    - 고정: main(master), develop
    - Master(main) 브랜치: Pont.OS 통합 릴리즈 버전 관리용
    - Develope 브랜치: Pont.OS 의 feature 개발 내용 통합 관리용
    - Hotfix 브랜치: Release된 버전에 대한 긴급 문제 해결용
    - Feature 브랜치: Issue 생길때 마다 branch 생성

3. [ ] [실습] Git clone 
    - develop 브랜치에서 `feature/{function}_dev` 브랜치 fork
    - `{function}` 리스트:
        -  아래 참고
        -  e.g. `feature/rectangle_dev`
    
4. [ ] [실습] ROS2 설치 및 test 프로젝트 생성
    - 실습주제: Math
    - 기능:
        1. Fibonacci → 기본
        2. Rectangle
        3. Circle
        4. Calculator
        5. List math Operations

6. [ ] [Study] Code(Program) analysis 방식 STUDY
    - Static Code Analysis(정적 분석) 이란?
        - 실제 실행 없이 소프트웨어(코드)를 분석하는 것
        - 분석 가능한 것: 잠재적인 버그, 성능 문제, 오타, 사용되지 않는 코드, 잠재적인 취약점, 코드 스타일(컨벤션)
        - Formal Method(정형 기법), Lint 등 여러 툴/기법 존재
        - 직접적인 프로그램 실행이 필요없으므로 IDE 또는 CI/CD 파이프라인의 첫 단계에 수행
    - Dynamic Code Analysis(동적 분석)이란?
        - 프로그램(코드) 실행을 통해 코드를 분석하여 오류 검출하는 것 (런타임에 분석)
        - 일반적으로 디버깅, 유닛 테스팅, 코드 coverage 분석 등이 동적 분석에 포함

7. [ ] [실습] ROS2 에서 Static Code Analysis 활성
    - Python 프로젝트에서는 기본적으로 Linter 적용되어 있음 
9. [ ] [실습] ROS2 에서 Dynamic Code Analysis 수행
    1. Unit Test 프레임워크 Study
    2. Test Driven Developement 소개
    3. PyTest를 통한 Unit Test 수행하기
    4. `Fibonacci` 추가 테스트 작성하기
    5. `Fibonacci` 기능 수정하기
    6. 담당 Function 에 대한 테스트 케이스
    7. 담당 Function 작성하기
    8. Test 실행해보기
      
10. [ ] Github update
    - Pull Request/ Code Reviewer/Assignee 설정
    - Code Reviewer: 이상현, Assignee: 김사론

## CI(Continuous Integration) 

8. [ ] Jenkins 개요 스터디
    - **Jenkins 소개**
        - 프로젝트의 빌드, 테스트 실행, 배포 등의 통합을 자동화
        - Maven, Ant, Gradle, Junit, Nexus와 잘 작동하며, Git, Svn과 같은 형상 관리 툴을 지원
        - CI를 위한 다양한 기능을 제공해주는 Java 기반의 오픈소스 툴
        - 방대한 오픈소스 커뮤니티가 존재하며 형상 관리 툴과 쉽게 통합

10. [ ] ROS-Jenkins 를 통한 자동 테스트 및 통합
    - Jenkins 설치
      
11. [ ] Jenkins test

* CI/CD -> 에서 CD 제외
