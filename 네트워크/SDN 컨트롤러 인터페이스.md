### **SDN 아키텍처 핵심 인터페이스: Northbound API vs Southbound API**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 SDN 컨트롤러가 네트워크의 "운영체제"인가)
Ⅱ. Northbound·Southbound API 핵심 구조
Ⅲ. 비교 및 적용 체계
Ⅳ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 VXLAN·VTEP이 '데이터센터 오버레이 네트워크의 데이터 평면'을 다룬다면, SDN(Software Defined Networking)의 Northbound·Southbound API는 '그 데이터 평면을 소프트웨어로 제어하는 제어 평면의 상하 인터페이스'다 — SDN 컨트롤러를 네트워크의 운영체제(OS)에 비유하면, Southbound API는 '운영체제가 하드웨어(스위치·라우터)를 제어하는 드라이버 인터페이스'이고, Northbound API는 '애플리케이션이 운영체제에 요청하는 시스템 콜'에 해당하며, 앞서 다룬 SRv6·VXLAN이 실제 패킷을 나르는 데이터 평면이라면 이 두 API가 그 데이터 평면을 프로그래밍 가능하게 만드는 SDN의 핵심 아키텍처 경계"\*\*라는 한 줄로 시작하면 전체 맥락이 드러납니다.

***

#### Ⅱ. Northbound·Southbound API 핵심 구조

**가. SDN 3계층 아키텍처와 API 위치**

```
[SDN 아키텍처 3계층]

애플리케이션 계층 (Application Layer)
  네트워크 앱: 로드밸런서·방화벽 앱·오케스트레이터
       ↕ Northbound API (North↔Controller)
제어 계층 (Control Layer)
  SDN 컨트롤러: OpenDaylight·ONOS·Ryu
       ↕ Southbound API (Controller↔South)
데이터 계층 (Data Plane / Infrastructure Layer)
  물리·가상 스위치·라우터: OpenFlow 스위치·화이트박스 스위치
```

***

**나. Northbound API 핵심 체계**

| 항목         | 내용                                          |
| :--------- | :------------------------------------------ |
| **정의**     | SDN 컨트롤러 ↔ 상위 애플리케이션 간 인터페이스                |
| **역할**     | 애플리케이션이 네트워크 상태 조회·정책 요청                    |
| **표준화 수준** | 표준 없음 / 컨트롤러마다 상이 (사실상 벤더 종속)               |
| **주요 형태**  | REST API (가장 보편적) / Python/Java SDK         |
| **대표 사례**  | ONOS REST API·OpenDaylight RESTCONF         |
| **연계 응용**  | 앞서 다룬 **SRv6 SR-TE Policy** 배포 / 오케스트레이터 연동 |

***

**다. Southbound API 핵심 체계**

| 항목          | 내용                                           |
| :---------- | :------------------------------------------- |
| **정의**      | SDN 컨트롤러 ↔ 물리·가상 네트워크 장비 간 인터페이스             |
| **역할**      | 컨트롤러가 스위치·라우터의 포워딩 규칙을 실시간 프로그래밍             |
| **표준화 수준**  | **OpenFlow가 사실상 표준** / 다수 프로토콜 병존            |
| **주요 프로토콜** | OpenFlow·NETCONF/YANG·P4·OVSDB·BGP-LS        |
| **대표 사례**   | OpenFlow 플로우 테이블 삽입·삭제                       |
| **연계 응용**   | 앞서 다룬 **LPM 알고리즘** 기반 플로우 매칭 / VXLAN VTEP 제어 |

***

#### Ⅲ. 비교 및 적용 체계

**가. Northbound vs Southbound API 전면 비교**

| 비교 항목       | Northbound API  | Southbound API            |
| :---------- | :-------------- | :------------------------ |
| **연결 대상**   | 컨트롤러 ↔ 애플리케이션   | 컨트롤러 ↔ 네트워크 장비            |
| **방향**      | 위쪽(애플리케이션)      | 아래쪽(하드웨어)                 |
| **표준화**     | 없음 (사실상 벤더 종속)  | **OpenFlow 사실상 표준**       |
| **주요 프로토콜** | REST·gRPC·SDK   | OpenFlow·NETCONF·P4·OVSDB |
| **실시간성 요구** | 상대적으로 낮음        | **매우 높음** (패킷 단위 제어)      |
| **주요 용도**   | 정책 정의·앱 통합·모니터링 | 플로우 테이블 프로그래밍·상태 수집       |
| **변경 빈도**   | 상대적으로 낮음        | 높음(트래픽 변화 실시간 반영)         |

***

**나. Southbound 프로토콜별 비교**

| 프로토콜             | 특징                          | 적용                  |
| :--------------- | :-------------------------- | :------------------ |
| **OpenFlow**     | 플로우 테이블 직접 제어 / L2\~L4 매칭   | 사실상 SDN 표준          |
| **NETCONF/YANG** | 장비 설정 전체(Configuration) 관리  | 전통 장비의 SDN 편입       |
| **P4**           | 데이터 평면 파이프라인 자체를 프로그래밍      | 차세대 프로그래머블 스위치      |
| **OVSDB**        | Open vSwitch 데이터베이스 관리 프로토콜 | 가상 스위치 제어(VXLAN 연계) |
| **BGP-LS**       | 기존 라우팅 프로토콜 상태 정보 수집        | 하이브리드 SDN 환경        |

***

**다. 앞서 다룬 개념과의 연결**

| 연계 개념               | 연결 내용                                                   |
| :------------------ | :------------------------------------------------------ |
| **SRv6**            | Northbound로 SR-TE Policy 수신 → Southbound로 SID 플로우 규칙 배포 |
| **VXLAN·VTEP**      | Southbound(OVSDB)로 VTEP·VNI 매핑 테이블 제어                   |
| **LPM 알고리즘**        | OpenFlow 플로우 테이블 매칭이 LPM 원리의 확장 형태                      |
| **IBN(의도 기반 네트워킹)** | Northbound API로 상위 의도(Intent) 입력 → 컨트롤러가 Southbound로 구현 |
| **NGFW·CASB**       | Northbound API로 보안 정책 앱과 SDN 컨트롤러 연동                    |

***

**라. 실무 적용 시나리오**

| 시나리오          | Northbound 활용           | Southbound 활용             |
| :------------ | :---------------------- | :------------------------ |
| **데이터센터 자동화** | 오케스트레이터가 REST로 네트워크 요청  | OpenFlow로 스위치 플로우 실시간 반영  |
| **트래픽 엔지니어링** | 앱이 SR-TE Policy 정의 요청   | P4/OpenFlow로 경로 프로그래밍     |
| **멀티벤더 통합**   | 단일 Northbound로 앱 개발 단순화 | NETCONF로 이기종 장비 통합 관리     |
| **보안 정책 자동화** | 보안 앱이 차단 정책 API 호출      | OpenFlow로 즉시 트래픽 차단 규칙 삽입 |

***

**(제언)** "Northbound·Southbound API는 SDN 컨트롤러를 중심으로 '위로는 유연한 혁신(표준 없는 REST 기반 확장성), 아래로는 엄격한 표준(OpenFlow 기반 상호운용성)'이라는 비대칭 설계 철학을 보여줍니다. **앞서 다룬 SRv6의 SR-TE Policy가 Northbound로 애플리케이션 의도를 받아 Southbound OpenFlow·P4로 실제 플로우 규칙을 하드웨어에 반영하는 흐름이 IBN(의도 기반 네트워킹)의 실제 구현이며, VXLAN 환경에서는 Southbound OVSDB로 VTEP를 제어하는 것처럼, 네트워크 자동화 설계 시 Northbound는 표준화 부재를 감안해 벤더 종속을 최소화하는 추상화 계층을 별도로 두고 Southbound는 OpenFlow를 기본으로 P4·NETCONF를 혼용하는 하이브리드 전략이 현대 SDN 아키텍처 설계의 핵심입니다.**"
