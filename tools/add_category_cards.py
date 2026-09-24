import json

category_cards = {
  "compute": {
    "name": "Compute Services in AWS",
    "category": "Domain 3: Technology",
    "desc_ru": "Вычислительные сервисы AWS обеспечивают запуск кода, контейнеров и виртуальных серверов с различными уровнями контроля и масштабируемости.",
    "desc_en": "AWS Compute services provide scalable compute capacity in the cloud, ranging from virtual servers to serverless code execution.",
    "key_points_ru": [
      "Amazon EC2: виртуальные серверы с полным контролем над ОС и конфигурацией",
      "AWS Lambda: бессерверные вычисления, оплата за миллисекунды работы кода, zero idle cost",
      "AWS Fargate: бессерверный запуск контейнеров Docker без управления серверами EC2",
      "Amazon ECS и EKS: оркестрация контейнеров (собственный движок AWS и управляемый Kubernetes)",
      "AWS Batch: пакетная обработка сотен тысяч вычислительных задач"
    ],
    "key_points_en": [
      "Amazon EC2: Scalable virtual compute instances with complete OS control",
      "AWS Lambda: Serverless event-driven compute with millisecond billing and zero idle cost",
      "AWS Fargate: Serverless container compute engine without managing EC2 servers",
      "Amazon ECS & EKS: Container orchestration (AWS native and managed Kubernetes)",
      "AWS Batch: Automated batch computing at any scale using Spot and On-Demand"
    ]
  },
  "net": {
    "name": "Networking & Content Delivery",
    "category": "Domain 3: Technology",
    "desc_ru": "Сетевые сервисы AWS формируют изолированные виртуальные сети, распределяют нагрузку и ускоряют доставку контента пользователям по всему миру.",
    "desc_en": "AWS Networking and Content Delivery services establish isolated virtual networks, distribute application load, and accelerate global data delivery.",
    "key_points_ru": [
      "Amazon VPC: логически изолированная виртуальная сеть в облаке AWS с подсетями и таблицами маршрутизации",
      "Elastic Load Balancing (ELB): автоматическое распределение трафика (ALB - Layer 7, NLB - Layer 4)",
      "Amazon Route 53: высокодоступный DNS-сервис с проверкой работоспособности (Health Checks)",
      "Amazon CloudFront: глобальная сеть доставки контента (CDN) с низкой задержкой",
      "AWS Direct Connect: выделенное оптоволоконное соединение в обход публичного интернета"
    ],
    "key_points_en": [
      "Amazon VPC: Logically isolated virtual network with subnets and route tables",
      "Elastic Load Balancing: Traffic distribution across healthy targets (ALB Layer 7, NLB Layer 4)",
      "Amazon Route 53: Scalable DNS web service with built-in health check routing",
      "Amazon CloudFront: Global Content Delivery Network (CDN) caching content at Edge Locations",
      "AWS Direct Connect: Dedicated private physical connection bypassing the public Internet"
    ]
  },
  "sec": {
    "name": "Security, Identity & Compliance",
    "category": "Domain 2: Security and Compliance",
    "desc_ru": "Комплекс сервисов AWS для защиты данных, учетных записей, сетевого периметра и соответствия мировым регуляторным стандартам.",
    "desc_en": "Suite of security, access management, governance, and compliance services protecting cloud workloads.",
    "key_points_ru": [
      "AWS IAM: управление пользователями, группами, ролями и политиками доступа (принцип наименьших привилегий)",
      "AWS KMS: управление криптографическими ключами шифрования (at-rest и in-transit)",
      "AWS Shield: автоматическая защита от DDoS-атак (Standard бесплатный, Advanced с защитой от списаний)",
      "AWS WAF: веб-файрвол для фильтрации вредоносных HTTP/HTTPS запросов и ботов (Layer 7)",
      "Amazon GuardDuty: интеллектуальное обнаружение угроз на основе машинного обучения и логов"
    ],
    "key_points_en": [
      "AWS IAM: Identity and Access Management with granular least-privilege permissions",
      "AWS KMS: Key Management Service for hardware-secured data encryption at rest and in transit",
      "AWS Shield: DDoS protection (Standard free for all, Advanced with financial cost protection)",
      "AWS WAF: Web Application Firewall blocking SQL injection, XSS, and bots at Layer 7",
      "Amazon GuardDuty: Intelligent threat detection using machine learning and event analysis"
    ]
  },
  "storage": {
    "name": "Storage Services in AWS",
    "category": "Domain 3: Technology",
    "desc_ru": "Хранилища данных в AWS: объектное (S3), блочное (EBS), общее файловое (EFS/FSx) и гибридное (Storage Gateway).",
    "desc_en": "Scalable storage services in AWS: object storage (S3), block storage (EBS), shared file systems (EFS/FSx), and hybrid storage (Storage Gateway).",
    "key_points_ru": [
      "Amazon S3: объектное хранилище с долговечностью 99.999999999% (11 девяток)",
      "Amazon EBS: блочные сетевые накопители для томов ОС и баз данных на инстансах EC2 (в пределах одной AZ)",
      "Amazon EFS: общее сетевое файловое хранилище NFS для Linux с одновременным доступом из сотен серверов",
      "Amazon FSx: файловые серверы для Windows (SMB) и высокопроизводительных кластеров Lustre",
      "AWS Storage Gateway: интеграция локальной инфраструктуры с облачным хранилищем AWS"
    ],
    "key_points_en": [
      "Amazon S3: Highly durable 99.999999999% (11 9s) object storage with lifecycle tiering",
      "Amazon EBS: Persistent block storage volumes for EC2 instances locked to a single AZ",
      "Amazon EFS: Elastic NFS file system supporting concurrent access from hundreds of Linux instances",
      "Amazon FSx: Native Windows SMB file shares and ultra-high-speed Lustre storage",
      "AWS Storage Gateway: Hybrid cloud storage bridging on-premises and AWS cloud"
    ]
  },
  "db": {
    "name": "Database Services in AWS",
    "category": "Domain 3: Technology",
    "desc_ru": "Управляемые реляционные (SQL), документоориентированные (NoSQL), in-memory кэши и специализированные хранилища данных.",
    "desc_en": "Fully managed relational SQL databases, high-speed NoSQL databases, in-memory caches, and specialized engines.",
    "key_points_ru": [
      "Amazon RDS: управляемые реляционные БД (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server) с Multi-AZ и Read Replicas",
      "Amazon Aurora: облачная СУБД с 3-5-кратным ускорением MySQL/PostgreSQL и хранением 6 копий данных в 3 AZ",
      "Amazon DynamoDB: бессерверная NoSQL база данных с задержкой ответа менее 10 миллисекунд при любом масштабе",
      "Amazon ElastiCache: сверхбыстрое кэширование в оперативной памяти (Redis / Memcached)",
      "Amazon Redshift: колоночное петабайтное аналитическое хранилище данных (Data Warehouse)"
    ],
    "key_points_en": [
      "Amazon RDS: Managed relational engines (PostgreSQL, MySQL, Oracle, SQL Server) with automated backups and Multi-AZ",
      "Amazon Aurora: Cloud-native database engine delivering up to 5x MySQL performance with 6-way replication",
      "Amazon DynamoDB: Serverless fast NoSQL key-value database delivering single-digit millisecond latency",
      "Amazon ElastiCache: Ultra-fast in-memory caching engine (Redis and Memcached)",
      "Amazon Redshift: Petabyte-scale columnar cloud data warehouse for OLAP analytics"
    ]
  },
  "mgmt": {
    "name": "Management & Governance",
    "category": "Domain 3: Technology",
    "desc_ru": "Инструменты для мониторинга, аудита, автоматизации и соответствия политикам во всей облачной инфраструктуре AWS.",
    "desc_en": "Services designed to track, monitor, audit, automate, and govern resources across the entire AWS cloud footprint.",
    "key_points_ru": [
      "Amazon CloudWatch: сбор метрик, логов и настройка алертов при превышении порогов использования ресурсов",
      "AWS CloudTrail: непрерывный аудит и запись всех вызовов API и действий пользователей (кто, что, когда сделал)",
      "AWS Config: отслеживание конфигураций ресурсов и проверка их на соответствие правилам безопасности",
      "AWS Organizations: централизованное управление множеством аккаунтов и политики Service Control Policies (SCP)",
      "AWS Trusted Advisor: персональный советник по оптимизации затрат, безопасности, производительности и надежности"
    ],
    "key_points_en": [
      "Amazon CloudWatch: Monitors operational metrics, application logs, and sets alarms",
      "AWS CloudTrail: Records and audits every API call across AWS accounts (who did what, where, and when)",
      "AWS Config: Continually evaluates and audits resource configuration compliance against rules",
      "AWS Organizations: Multi-account governance with Service Control Policies (SCPs) and consolidated billing",
      "AWS Trusted Advisor: Automated recommendations for cost reduction, performance, fault tolerance, and security"
    ]
  },
  "cloud": {
    "name": "Cloud Concepts & Value Proposition",
    "category": "Domain 1: Cloud Concepts",
    "desc_ru": "Фундаментальные концепции облачных вычислений: преимущества облака, модели развертывания и архитектурные принципы.",
    "desc_en": "Foundational cloud computing principles: key value propositions, deployment models, and cloud design patterns.",
    "key_points_ru": [
      "6 преимуществ облака: Trade capital expense for variable expense (OpEx vs CapEx), Benefit from massive economies of scale, Stop guessing capacity, Increase speed and agility, Stop spending money running data centers, Go global in minutes",
      "Модели развертывания: Public Cloud (публичное облако), Hybrid Cloud (гибридное), Private Cloud / On-Premises (частное)",
      "Высокая доступность (High Availability), отказоустойчивость (Fault Tolerance) и эластичность (Elasticity)"
    ],
    "key_points_en": [
      "6 Cloud Advantages: Trade CapEx for variable OpEx, Economies of scale, Stop guessing capacity, Agility, Eliminate data center maintenance, Go global in minutes",
      "Deployment Models: Public Cloud, Hybrid Cloud, On-Premises / Private Cloud",
      "Core Concepts: High Availability, Fault Tolerance, Scalability, and Elasticity"
    ]
  },
  "cloud_economics": {
    "name": "Cloud Economics & TCO",
    "category": "Domain 4: Billing and Pricing",
    "desc_ru": "Финансовые аспекты облака: совокупная стоимость владения (TCO), переход от капитальных затрат (CapEx) к операционным (OpEx) и оптимизация расходов.",
    "desc_en": "Financial aspects of the cloud: Total Cost of Ownership (TCO), capital expenditure (CapEx) vs operational expenditure (OpEx), and cost efficiency.",
    "key_points_ru": [
      "CapEx (капитальные затраты): покупка серверов, аренда стоек, электропитание вперед на 3-5 лет",
      "OpEx (операционные затраты): оплата только за фактически потребленные ресурсы по факту (Pay-as-you-go)",
      "AWS Pricing Calculator: оценка ориентировочной стоимости архитектуры в AWS перед запуском"
    ],
    "key_points_en": [
      "CapEx: Upfront capital investments in physical hardware, cooling, and data center leases",
      "OpEx: Operational expenses paying only for actual resource consumption on a variable basis",
      "AWS Pricing Calculator: Web tool to estimate upfront monthly spend prior to deployment"
    ]
  },
  "cloud_migration": {
    "name": "Cloud Migration Strategies (6 Rs)",
    "category": "Domain 1: Cloud Concepts",
    "desc_ru": "Стратегии миграции корпоративных приложений и баз данных в облако AWS (6 Rs) и инструменты миграции.",
    "desc_en": "Enterprise cloud migration frameworks (the 6 Rs of migration) and migration acceleration tools.",
    "key_points_ru": [
      "Rehost (Lift-and-shift): перенос без изменений с помощью AWS Application Migration Service (MGN)",
      "Replatform (Lift-tinker-and-shift): небольшая оптимизация под облако (например, переход на Amazon RDS)",
      "Repurchase (Drop-and-shop): переход на готовое SaaS решение",
      "Refactor / Re-architect: полная переработка под облачно-нативную или serverless архитектуру",
      "Retire: вывод из эксплуатации устаревших систем",
      "Retain: сохранение критических систем на локальной инфраструктуре (on-premise)"
    ],
    "key_points_en": [
      "Rehost (Lift-and-shift): Move servers without code changes via AWS MGN",
      "Replatform: Make minor cloud optimizations like switching to managed Amazon RDS",
      "Repurchase: Move to a different product, typically a SaaS solution",
      "Refactor: Redesign code to cloud-native or serverless architecture",
      "Retire: Decommission applications no longer needed",
      "Retain: Keep legacy applications on-premises for compliance or dependency reasons"
    ]
  },
  "disaster_recovery": {
    "name": "Disaster Recovery (DR) Strategies",
    "category": "Domain 3: Technology",
    "desc_ru": "Стратегии восстановления после катастроф в облаке AWS, балансирующие показатели RPO, RTO и стоимость реализации.",
    "desc_en": "Disaster recovery architectures in AWS balancing RPO (Recovery Point Objective), RTO (Recovery Time Objective), and implementation cost.",
    "key_points_ru": [
      "RPO (Recovery Point Objective): допустимый объем потери данных, измеряемый во времени",
      "RTO (Recovery Time Objective): допустимое время простоя до полного восстановления сервиса",
      "Backup & Restore: самая дешевая стратегия, но максимальный RTO/RPO",
      "Pilot Light: минимальное ядро системы работает в резервном регионе, данные реплицируются",
      "Warm Standby: уменьшенная полнофункциональная копия системы всегда работает в резервном регионе",
      "Multi-Site Active/Active: трафик распределяется между регионами, мгновенный RTO/RPO близкий к 0 (самая дорогая)"
    ],
    "key_points_en": [
      "RPO (Recovery Point Objective): Acceptable maximum data loss duration",
      "RTO (Recovery Time Objective): Acceptable maximum downtime until restored",
      "Backup & Restore: Lowest cost, longest RPO/RTO",
      "Pilot Light: Core components run in standby region with continuous data replication",
      "Warm Standby: Scaled-down version of full environment running 24/7 in secondary region",
      "Multi-Site Active/Active: Near-zero downtime failover with live multi-region traffic (highest cost)"
    ]
  },
  "aws_billing": {
    "name": "AWS Billing & Cost Management",
    "category": "Domain 4: Billing and Pricing",
    "desc_ru": "Комплекс инструментов для мониторинга, оповещения и прогнозирования затрат на сервисы AWS.",
    "desc_en": "Tools and services for viewing, alerting, and forecasting your AWS cloud expenditures.",
    "key_points_ru": [
      "AWS Budgets: установка персональных бюджетов затрат и использования с алертами по email/SNS при превышении порога",
      "AWS Cost Explorer: визуализация, фильтрация и прогнозирование расходов на срок до 12 месяцев",
      "AWS Cost and Usage Report (CUR): максимально детализированные отчеты с сохранением в S3",
      "Consolidated Billing: объединение счетов всех аккаунтов в организации с получением оптовых скидок"
    ],
    "key_points_en": [
      "AWS Budgets: Set custom cost and usage limits with email/SNS notifications",
      "AWS Cost Explorer: Interactive charts to visualize, filter, and forecast costs for up to 12 months",
      "AWS Cost & Usage Report (CUR): Detailed granular usage delivered to Amazon S3",
      "Consolidated Billing: Combines multiple account invoices to qualify for tier-based volume discounts"
    ]
  },
  "aws_pricing": {
    "name": "AWS Pricing Models & Fundamentals",
    "category": "Domain 4: Billing and Pricing",
    "desc_ru": "Фундаментальные принципы ценообразования в AWS: Pay-as-you-go, скидки за резервирование и оптовые объемы.",
    "desc_en": "Fundamental AWS pricing pillars: pay-as-you-go, commitment discounts, and volume-based pricing.",
    "key_points_ru": [
      "Pay-as-you-go: оплата только за фактически потребленные ресурсы без долгосрочных контрактов",
      "Save when you commit: скидки до 72% при обязательстве на 1 или 3 года (Savings Plans, Reserved Instances)",
      "Pay less by using more: скидки за объем (Tiered pricing) на хранилище S3 и исходящий трафик",
      "Входящий трафик (Inbound data transfer) во всех регионах AWS всегда бесплатный; исходящий (Outbound data transfer) тарифицируется"
    ],
    "key_points_en": [
      "Pay-as-you-go: Pay strictly for active resources without upfront commitments or lock-ins",
      "Save when you commit: Up to 72% discount for 1- or 3-year term commitments (Savings Plans, RIs)",
      "Pay less by using more: Tiered volume pricing where per-unit cost decreases as consumption scales",
      "Inbound data transfer is always free; Outbound data transfer across the Internet incurs bandwidth fees"
    ]
  },
  "cicd": {
    "name": "CI/CD & Developer Tools",
    "category": "Domain 3: Technology",
    "desc_ru": "Инструменты автоматизации сборки, тестирования и развертывания приложений в облаке AWS.",
    "desc_en": "Services enabling continuous integration, continuous delivery, and deployment automation on AWS.",
    "key_points_ru": [
      "AWS CodeCommit: безопасный управляемый сервис хостинга Git-репозиториев",
      "AWS CodeBuild: полностью управляемый сервис непрерывной интеграции для сборки и запуска тестов",
      "AWS CodeDeploy: автоматизация развертывания кода на EC2, Fargate, Lambda или локальные серверы",
      "AWS CodePipeline: оркестрация этапов CI/CD пайплайна (Source -> Build -> Test -> Deploy)",
      "AWS Cloud9: облачная IDE в браузере для совместного написания кода"
    ],
    "key_points_en": [
      "AWS CodeCommit: Managed Git-based private repository hosting",
      "AWS CodeBuild: Fully managed build and automated testing service",
      "AWS CodeDeploy: Automated code deployment across EC2, Lambda, and on-premises",
      "AWS CodePipeline: Orchestrates multi-stage CI/CD workflows from commit to production",
      "AWS Cloud9: Cloud-native browser-based IDE with collaborative real-time pairing"
    ]
  },
  "ai": {
    "name": "Artificial Intelligence & Machine Learning (AI/ML)",
    "category": "Domain 3: Technology",
    "desc_ru": "Стек сервисов искусственного интеллекта AWS: от готовых предобученных API до платформы полного цикла Amazon SageMaker и генеративного ИИ Amazon Bedrock.",
    "desc_en": "AWS AI/ML services spanning pre-trained cognitive APIs to the comprehensive Amazon SageMaker platform and foundation models via Amazon Bedrock.",
    "key_points_ru": [
      "Amazon SageMaker: платформа для построения, обучения и развертывания моделей машинного обучения любого масштаба",
      "Amazon Bedrock: бессерверный доступ к ведущим базовым моделям (Foundation Models) генеративного ИИ через единый API",
      "Amazon Rekognition (компьютерное зрение), Polly (синтез речи), Transcribe (распознавание речи), Translate (машинный перевод), Comprehend (анализ текста NLP)",
      "Amazon Lex: создание чат-ботов с пониманием естественной речи (технология голосового помощника Alexa)"
    ],
    "key_points_en": [
      "Amazon SageMaker: End-to-end platform to build, train, tune, and deploy machine learning models",
      "Amazon Bedrock: Serverless unified API to access leading generative AI foundation models",
      "Pre-trained APIs: Rekognition (vision), Polly (text-to-speech), Transcribe (speech-to-text), Translate, Comprehend (NLP)",
      "Amazon Lex: Conversational AI and chatbot engine powering Amazon Alexa"
    ]
  },
  "mig": {
    "name": "Migration & Data Transfer",
    "category": "Domain 3: Technology",
    "desc_ru": "Сервисы для безопасного переноса баз данных, серверов и больших объемов данных в облако AWS.",
    "desc_en": "Services designed to securely migrate databases, server workloads, and high-volume datasets into AWS.",
    "key_points_ru": [
      "AWS Database Migration Service (AWS DMS): миграция баз данных практически без простоя (однородная и разнородная миграция)",
      "AWS Schema Conversion Tool (SCT): конвертация схем между различными движками баз данных (например, Oracle в PostgreSQL)",
      "AWS Application Migration Service (MGN): блочная репликация физических и виртуальных серверов",
      "AWS Snow Family: физические устройства для офлайн-переноса петабайтов данных (Snowcone, Snowball, Snowmobile)"
    ],
    "key_points_en": [
      "AWS Database Migration Service (DMS): Continuous near-zero downtime database migrations",
      "AWS Schema Conversion Tool (SCT): Converts database schemas between different engines (e.g., Oracle to PostgreSQL)",
      "AWS Application Migration Service (MGN): Block-level server lift-and-shift migration",
      "AWS Snow Family: Physical storage devices for offline petabyte-scale data ingestion"
    ]
  },
  "aws_core": {
    "name": "AWS Core Services & Global Architecture",
    "category": "Domain 1: Cloud Concepts",
    "desc_ru": "Фундаментальные компоненты AWS: глобальная инфраструктура (Регионы, Зоны доступности, Edge Locations) и базовые сервисы вычислений, сети и хранения.",
    "desc_en": "Core AWS architecture foundational services spanning global compute, networking, security, and storage building blocks.",
    "key_points_ru": [
      "Регионы AWS изолированы друг от друга и содержат несколько Зон Доступности (AZ)",
      "Выбор региона основывается на 4 факторах: Compliance/Legal requirements, Proximity (минимальная задержка до клиентов), Available services, Pricing (разная стоимость в регионах)",
      "Модель совместной ответственности и отказоустойчивость при проектировании с резервированием между AZ"
    ],
    "key_points_en": [
      "AWS Regions are globally isolated and contain multiple discrete Availability Zones",
      "4 key factors for Region selection: Compliance & data residency, Proximity to end users, Available services, Cost variations",
      "Shared Responsibility Model and designing for Multi-AZ fault tolerance"
    ]
  }
}

with open("data/services_info.json", "r", encoding="utf-8") as f:
    db = json.load(f)

for k, v in category_cards.items():
    db[k] = v

with open("data/services_info.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Updated with category cards! Total keys in services_info.json:", len(db))
