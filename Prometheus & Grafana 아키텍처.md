### **클라우드 네이티브 관측성의 표준: Prometheus & Grafana**

***

#### 답안 전체 스토리 흐름 (목차)

```
Ⅰ. 개요 (왜 로그만으로는 시스템 상태를 파악할 수 없는가)
Ⅱ. Prometheus 핵심 아키텍처
Ⅲ. Grafana 핵심 구조 및 연계
Ⅳ. 비교 및 적용 체계
Ⅴ. 결론
```

포인트: 개요에서 \*\*"앞서 다룬 DORA 지표·심리적 안전감이 '개발팀 성과를 무엇으로 측정할 것인가'를 다뤘다면, Prometheus·Grafana는 '그 지표를 실제로 어떻게 수집·저장·시각화할 것인가'를 구현하는 클라우드 네이티브 모니터링의 사실상 표준 아키텍처다 — 2012년 SoundCloud가 개발해 CNCF(Cloud Native Computing Foundation) 2번째 졸업 프로젝트가 된 Prometheus는 '에이전트가 중앙으로 데이터를 밀어넣는(Push)' 전통 모니터링과 반대로 '서버가 각 대상에서 직접 데이터를 끌어오는(Pull)' 방식을 채택했으며, Grafana는 그렇게 수집된 시계열 데이터를 대시보드로 시각화하는 계층으로, 앞서 다룬 플랫폼 엔지니어링의 Golden Path에서 관측성(Observability) 계층의 핵심 구성요소로 자리잡은 것"\*\*이라는 한 줄로 시작하면 전체 맥락이 드러납니다.

***

#### Ⅱ. Prometheus 핵심 아키텍처

**가. Pull 기반 수집 구조**

```
[Prometheus Pull 모델]

기존 Push 모델(Graphite 등):
  애플리케이션 → 능동적으로 메트릭 전송
  → 서버 부하 시 메트릭 전송 자체가 실패 가능 🚨

Prometheus Pull 모델:
  Prometheus Server가 주기적으로(15~30초)
  각 Target의 /metrics 엔드포인트를 스크래핑(Scrape)

  Target A(/metrics) ←──scrape──┐
  Target B(/metrics) ←──scrape──┤ Prometheus Server
  Target C(/metrics) ←──scrape──┘

장점:
  Target 생존 여부를 스크래핑 성공/실패로 직접 확인(Up 메트릭)
  중앙에서 수집 주기·대상을 통제 → 장애 전파 최소화
```

**나. Prometheus 핵심 구성요소**

| 구성요소                  | 역할                                                            |
| :-------------------- | :------------------------------------------------------------ |
| **Prometheus Server** | 스크래핑·저장·질의(PromQL) 처리 핵심 엔진                                   |
| **Exporter**          | 대상 시스템의 메트릭을 /metrics 형식으로 노출(Node Exporter·MySQL Exporter 등) |
| **Pushgateway**       | 짧은 배치 작업 등 Pull이 어려운 경우 임시 Push 수신 후 대기                       |
| **Service Discovery** | Kubernetes·Consul 연동으로 동적 Target 자동 탐지                        |
| **Alertmanager**      | 알림 규칙 평가·중복 제거·라우팅·Slack/PagerDuty 연동                         |
| **TSDB**              | 자체 시계열 데이터베이스(로컬 디스크·시간 기반 압축 저장)                             |

**다. 데이터 모델 및 PromQL**

| 항목            | 내용                                                              |
| :------------ | :-------------------------------------------------------------- |
| **데이터 모델**    | 메트릭명 + 레이블(Key-Value) 조합의 다차원 시계열                               |
| **4대 메트릭 타입** | Counter(누적 증가) / Gauge(증감 값) / Histogram(분포·버킷) / Summary(분위수)  |
| **PromQL**    | 함수형 질의 언어 / `rate()`·`sum by()`·`histogram_quantile()` 등 시계열 연산 |
| **저장 방식**     | 로컬 TSDB 기본(2주 기본 보존) / 장기 저장은 Thanos·Cortex·Mimir 연동            |

***

#### Ⅲ. Grafana 핵심 구조 및 연계

**가. Grafana 역할 및 데이터소스 연계**

```
[Grafana 다중 데이터소스 통합 시각화]

Prometheus (메트릭) ──┐
Loki (로그)          ──┼──→ Grafana ──→ 통합 대시보드
Tempo (트레이스)      ──┘         │
                                  └──→ Alerting(알림 규칙)

→ 앞서 다룬 관측성 3대 축(메트릭·로그·트레이스)을
  단일 대시보드에서 상관 분석 가능
```

**나. Grafana 핵심 구성요소**

| 구성요소                | 역할                                          |
| :------------------ | :------------------------------------------ |
| **Data Source**     | Prometheus·Loki·Tempo·InfluxDB 등 플러그인 방식 연동 |
| **Dashboard/Panel** | 시계열 그래프·게이지·히트맵 등 시각화 패널 구성                 |
| **Alerting**        | 임계값 기반 알림 규칙·다채널 통지(Slack·Email·PagerDuty)  |
| **Variables**       | 대시보드 템플릿화(서비스·인스턴스별 동적 필터링)                 |
| **RBAC**            | 팀·조직별 대시보드 접근 권한 관리                         |

***

#### Ⅳ. 비교 및 적용 체계

**가. Prometheus vs 전통 모니터링 비교**

| 비교 항목         | 전통 모니터링(Nagios·Zabbix) | Prometheus                  |
| :------------ | :--------------------- | :-------------------------- |
| **수집 방식**     | Push 또는 Agent 폴링       | **Pull(Scrape)** ✅          |
| **데이터 모델**    | 단순 트리 구조               | **다차원 레이블 기반** ✅            |
| **동적 환경 적합성** | 낮음(정적 설정) 🚨           | **높음(Service Discovery)** ✅ |
| **쿼리 언어**     | 제한적                    | **PromQL(함수형)** ✅           |
| **장기 저장**     | 기본 지원                  | 별도 연동 필요(Thanos 등)          |
| **CNCF 생태계**  | 해당 없음                  | **CNCF 졸업 프로젝트** ✅          |

**나. 시나리오별 조합 전략**

| 시나리오                | 구성                                  | 비고                 |
| :------------------ | :---------------------------------- | :----------------- |
| **단일 클러스터 모니터링**    | Prometheus + Grafana                | 표준 최소 구성           |
| **멀티 클러스터·장기 보관**   | Prometheus + Thanos/Mimir + Grafana | 글로벌 뷰·장기 저장 확보     |
| **로그까지 통합 관측**      | Prometheus + Loki + Grafana         | 앞서 다룬 관측성 3대 축 통합  |
| **짧은 배치 작업 모니터링**   | Prometheus + Pushgateway            | Pull 어려운 워크로드 대응   |
| **Kubernetes 네이티브** | kube-prometheus-stack               | Operator 기반 자동화 배포 |

***

**(제언)** "Prometheus·Grafana 조합은 '수집은 단순하고 견고하게(Pull), 저장은 효율적으로(TSDB), 질의는 유연하게(PromQL), 시각화는 통합적으로(Grafana)'라는 관측성 설계 철학을 구현한 클라우드 네이티브 표준입니다. 단일 Prometheus 서버는 로컬 디스크 용량과 단일 장애점이라는 한계를 가지므로 대규모 환경에서는 Thanos나 Mimir로 장기 저장과 글로벌 질의를 확장하는 아키텍처를 반드시 함께 설계해야 하며, 알림 규칙 설계 시 단순 임계값 초과가 아닌 앞서 다룬 SLO(Service Level Objective) 기반 에러 예산(Error Budget) 소진율로 알림을 구성하는 것이 알림 피로(Alert Fatigue)를 줄이는 실무의 핵심입니다.

***

**앞서 다룬 개념과의 연결**

| 연계 개념               | 연결 내용                                     |
| :------------------ | :---------------------------------------- |
| **DORA 지표**         | Prometheus 메트릭으로 배포 빈도·MTTR 등을 실시간 대시보드화  |
| **플랫폼 엔지니어링**       | Golden Path의 관측성 계층 기본 제공 구성요소            |
| **AI-SOC**          | 보안 이벤트 메트릭도 Prometheus·Grafana로 통합 시각화 가능 |
| **Shift-Right 테스팅** | 카나리 배포 시 Prometheus 메트릭으로 실시간 이상 탐지       |
| **AIDLC**           | AI 에이전트가 Grafana 대시보드 이상 패턴을 자동 분석·알림     |
