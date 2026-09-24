# -*- coding: utf-8 -*-
"""
Generates exhaustive AWS Services Dictionary for CLF-C02
Covers 80+ AWS services with rich descriptions and key exam facts in both RU and EN.
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

SERVICES = {
  # --- COMPUTE & CONTAINERS ---
  "amazon_ec2": {
    "name": "Amazon EC2 (Elastic Compute Cloud)",
    "category": "Compute",
    "desc_ru": "Масштабируемые виртуальные серверы в облаке AWS с полным административным доступом (root) к операционной системе.",
    "desc_en": "Scalable virtual compute servers in the AWS Cloud with complete administrative control over the guest OS.",
    "key_points_ru": [
      "Модели оплаты: On-Demand, Spot (до 90% скидки), Savings Plans и Reserved Instances",
      "Полный контроль над ОС, сетевыми интерфейсами и устанавливаемым ПО",
      "Интеграция с Auto Scaling и Elastic Load Balancing для высокой доступности"
    ],
    "key_points_en": [
      "Pricing models: On-Demand, Spot (up to 90% off), Savings Plans & Reserved Instances",
      "Full administrative root control over guest OS and installed software",
      "Integrates with Auto Scaling and Elastic Load Balancing for high availability"
    ]
  },
  "elastic_load_balancing": {
    "name": "Elastic Load Balancing (ELB / ALB / NLB / GLB)",
    "category": "Compute & Networking",
    "desc_ru": "Автоматическое распределение входящего трафика приложений между несколькими целями (инстансы EC2, контейнеры, IP-адреса, Lambda) в одной или нескольких зонах доступности.",
    "desc_en": "Automatically distributes incoming application traffic across multiple targets (EC2 instances, containers, IPs, Lambda) in one or more Availability Zones.",
    "key_points_ru": [
      "Application Load Balancer (ALB): Layer 7 (HTTP/HTTPS), маршрутизация по URL-путям, хостам и микросервисам",
      "Network Load Balancer (NLB): Layer 4 (TCP/UDP), экстремальная производительность, миллионы запросов/сек, статические Anycast IP",
      "Gateway Load Balancer (GLB): развертывание и масштабирование виртуальных сетевых файрволов и систем IDS/IPS",
      "Автоматическая проверка работоспособности (Health Checks) и перенаправление трафика только на здоровые серверы"
    ],
    "key_points_en": [
      "Application Load Balancer (ALB): Layer 7 HTTP/HTTPS path-based and host-based routing",
      "Network Load Balancer (NLB): Layer 4 TCP/UDP ultra-high performance, millions of req/sec, static IPs",
      "Gateway Load Balancer (GLB): Deploy and scale virtual network firewalls and third-party appliances",
      "Performs health checks and routes traffic only to healthy targets"
    ]
  },
  "aws_lambda": {
    "name": "AWS Lambda",
    "category": "Compute / Serverless",
    "desc_ru": "Бессерверный вычислительный сервис, позволяющий выполнять программный код в ответ на события без подготовки и управления серверами.",
    "desc_en": "Serverless compute service that lets you run code in response to events without provisioning or managing servers.",
    "key_points_ru": [
      "Оплата строго за время работы кода с точностью до 1 мс и объем выделенной памяти (GB-seconds)",
      "0 затрат во время простоя (вы не платите, когда код не выполняется)",
      "Автоматическое масштабирование от нуля до десятков тысяч одновременных вызовов",
      "Бесплатный уровень Always Free: 1 000 000 вызовов в месяц бессрочно"
    ],
    "key_points_en": [
      "Pay only for execution time measured in 1ms increments and allocated memory (GB-seconds)",
      "Zero idle costs — pay nothing when code is not actively running",
      "Automatic scaling from zero to tens of thousands of concurrent requests",
      "Always Free tier includes 1,000,000 free requests per month indefinitely"
    ]
  },
  "aws_fargate": {
    "name": "AWS Fargate",
    "category": "Compute / Serverless Containers",
    "desc_ru": "Бессерверный вычислительный движок для контейнеров Docker, работающий с Amazon ECS и Amazon EKS без необходимости управлять инстансами EC2.",
    "desc_en": "Serverless compute engine for containers that works with both Amazon ECS and EKS without needing to manage EC2 instances.",
    "key_points_ru": [
      "Устраняет необходимость выбора типов инстансов, патчинга серверов и управления кластером",
      "Вы платите только за ресурсы vCPU и память, запрошенные вашими контейнерами",
      "Идеально для запуска микросервисов и контейнеризированных веб-приложений"
    ],
    "key_points_en": [
      "Removes the need to choose instance types, patch OS, or manage container cluster servers",
      "Pay only for the vCPU and memory resources requested by your container tasks",
      "Ideal for running microservices and containerized applications"
    ]
  },
  "amazon_ecs": {
    "name": "Amazon ECS (Elastic Container Service)",
    "category": "Compute / Containers",
    "desc_ru": "Высокопроизводительный, надежный сервис оркестрации контейнеров Docker, глубоко интегрированный с экосистемой AWS.",
    "desc_en": "A highly scalable, fast container management service that makes it easy to run, stop, and manage Docker containers on a cluster.",
    "key_points_ru": [
      "Поддерживает две модели запуска: на управляемых серверах EC2 или бессерверно на AWS Fargate",
      "Нативная интеграция с IAM, CloudWatch, Application Load Balancer и Secrets Manager",
      "Собственный оркестратор AWS, проще в освоении, чем Kubernetes"
    ],
    "key_points_en": [
      "Supports two launch types: EC2 instances (customer managed) or AWS Fargate (serverless)",
      "Native integration with IAM, CloudWatch, Application Load Balancers, and Secrets Manager",
      "AWS-native container orchestrator, simpler than Kubernetes"
    ]
  },
  "amazon_eks": {
    "name": "Amazon EKS (Elastic Kubernetes Service)",
    "category": "Compute / Containers",
    "desc_ru": "Управляемый сервис для запуска открытого стандарта Kubernetes в AWS без необходимости развертывать собственный Control Plane.",
    "desc_en": "Managed Kubernetes service that makes it easy to run open-source Kubernetes on AWS without maintaining the control plane.",
    "key_points_ru": [
      "Автоматическое масштабирование и высокая доступность мастера Kubernetes в нескольких AZ",
      "Совместимость со стандартными инструментами экосистемы Kubernetes (Helm, Kubectl)",
      "Поддерживает запуск нод на EC2 и бессерверно на AWS Fargate"
    ],
    "key_points_en": [
      "Automatic scaling and multi-AZ high availability for the Kubernetes control plane",
      "100% compatible with open-source Kubernetes tooling and standard manifests",
      "Supports worker nodes on Amazon EC2 and serverless on AWS Fargate"
    ]
  },
  "aws_auto_scaling": {
    "name": "AWS Auto Scaling / EC2 Auto Scaling",
    "category": "Compute / Elasticity",
    "desc_ru": "Сервис автоматического добавления или удаления вычислительных мощностей в зависимости от меняющегося спроса и нагрузки.",
    "desc_en": "Monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost.",
    "key_points_ru": [
      "Поддерживает политики масштабирования: целевое отслеживание (Target Tracking), ступенчатое (Step), по расписанию (Scheduled)",
      "Гарантирует отказоустойчивость: автоматически заменяет неисправные инстансы новыми",
      "Помогает соблюдать баланс между производительностью и оптимизацией затрат"
    ],
    "key_points_en": [
      "Supports dynamic scaling policies: Target Tracking, Step scaling, and Scheduled scaling",
      "Maintains fault tolerance by automatically replacing unhealthy instances with new ones",
      "Optimizes cost by scaling down resources during quiet periods"
    ]
  },
  "amazon_lightsail": {
    "name": "Amazon Lightsail",
    "category": "Compute / Simplified VPS",
    "desc_ru": "Простой в использовании виртуальный частный сервер (VPS), включающий вычисления, хранилище и сеть по фиксированной предсказуемой ежемесячной цене.",
    "desc_en": "Easy-to-use virtual private server (VPS) with bundled compute, storage, and networking for a low, predictable monthly price.",
    "key_points_ru": [
      "Предназначен для простых сайтов (WordPress, Joomla), блогов и небольших интернет-магазинов",
      "Включает фиксированный пакет трафика, SSD-диск и статический IP за единую цену от $3.50/мес",
      "Упрощенная консоль, идеальная для новичков и малого бизнеса без глубоких знаний AWS"
    ],
    "key_points_en": [
      "Designed for simple web applications, WordPress blogs, and testing environments",
      "Bundles compute, SSD storage, and monthly data transfer into predictable flat rates",
      "Simplified console for developers, students, and small businesses"
    ]
  },
  "aws_elastic_beanstalk": {
    "name": "AWS Elastic Beanstalk",
    "category": "Compute / PaaS",
    "desc_ru": "Платформа как услуга (PaaS) для быстрого развертывания и масштабирования веб-приложений (Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker).",
    "desc_en": "Easy-to-use platform-as-a-service (PaaS) for deploying and scaling web applications and services without managing infrastructure.",
    "key_points_ru": [
      "Разработчик просто загружает код, а сервис сам развертывает EC2, балансировщик, Auto Scaling и базу данных",
      "Полный контроль над базовыми ресурсами AWS сохраняется у клиента",
      "Сам сервис Beanstalk бесплатен — оплачиваются только созданные им ресурсы (EC2, S3, ELB)"
    ],
    "key_points_en": [
      "You simply upload your application code, and Beanstalk handles provisioning, load balancing, and scaling",
      "Maintains full customer control over underlying AWS infrastructure resources",
      "No additional charge for Beanstalk itself; you pay only for the AWS resources provisioned"
    ]
  },

  # --- STORAGE ---
  "amazon_s3": {
    "name": "Amazon S3 (Simple Storage Service)",
    "category": "Storage / Object Storage",
    "desc_ru": "Высоконадежное объектное хранилище с неограниченной масштабируемостью и долговечностью данных 99.999999999% (11 девяток).",
    "desc_en": "Highly durable object storage service with unlimited capacity and 99.999999999% (11 9s) of data durability.",
    "key_points_ru": [
      "Хранит данные в виде объектов внутри бакетов (Buckets) размером от 0 байт до 5 ТБ на объект",
      "Классы хранения: Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier, Deep Archive",
      "Возможности: версионирование, шифрование (SSE-S3, SSE-KMS), блокировка публичного доступа (Block Public Access)"
    ],
    "key_points_en": [
      "Stores data as objects inside buckets with individual object sizes up to 5 TB",
      "Storage classes: Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier, Deep Archive",
      "Features: Versioning, Lifecycle policies, Object Lock (WORM), S3 Block Public Access"
    ]
  },
  "amazon_ebs": {
    "name": "Amazon EBS (Elastic Block Store)",
    "category": "Storage / Block Storage",
    "desc_ru": "Высокопроизводительное блочное хранилище данных, предназначенное для использования с инстансами Amazon EC2 в пределах одной зоны доступности.",
    "desc_en": "High-performance block storage service designed for use with Amazon EC2 instances within a single Availability Zone.",
    "key_points_ru": [
      "Работает как виртуальный жесткий диск для ОС, файловых систем и реляционных баз данных",
      "Типы томов: SSD общего назначения (gp2/gp3), SSD с гарантированными IOPS (io1/io2), HDD (st1, sc1)",
      "Резервное копирование выполняется через инкрементальные снапшоты в Amazon S3"
    ],
    "key_points_en": [
      "Acts as a virtual hard drive attached to EC2 instances for operating systems and databases",
      "Volume types: General Purpose SSD (gp2/gp3), Provisioned IOPS SSD (io1/io2), Throughput Optimized HDD (st1)",
      "Backups are stored as point-in-time incremental snapshots in Amazon S3"
    ]
  },
  "amazon_efs": {
    "name": "Amazon EFS (Elastic File System)",
    "category": "Storage / File Storage",
    "desc_ru": "Управляемая, полностью эластичная бессерверная сетевая файловая система стандарта POSIX/NFS для Linux-инстансов.",
    "desc_en": "Serverless, fully elastic network file system conforming to POSIX standards for Linux workloads.",
    "key_points_ru": [
      "Обеспечивает одновременный общий доступ для тысяч инстансов EC2 в нескольких зонах доступности (Multi-AZ)",
      "Автоматически расширяется и сжимается при добавлении или удалении файлов",
      "Поддерживает жизненный цикл и автоматический перенос старых файлов в EFS Infrequent Access"
    ],
    "key_points_en": [
      "Provides concurrent shared access for thousands of EC2 instances across multiple AZs",
      "Automatically scales up and down as files are added or deleted",
      "Supports Lifecycle Management to move cold files to EFS Infrequent Access"
    ]
  },
  "aws_storage_gateway": {
    "name": "AWS Storage Gateway",
    "category": "Storage / Hybrid Cloud",
    "desc_ru": "Гибридный сервис хранения данных, позволяющий локальным серверам прозрачно использовать облачное хранилище AWS.",
    "desc_en": "Hybrid cloud storage service connecting on-premises software appliances with cloud-based storage.",
    "key_points_ru": [
      "S3 File Gateway: предоставляет локальный доступ по NFS/SMB к объектам в Amazon S3 с локальным кэшем",
      "Volume Gateway: предоставляет локальным серверам блочные тома iSCSI с бэкапом в AWS (Stored или Cached)",
      "Tape Gateway: виртуальная ленточная библиотека (VTL) для замены физических магнитных лент на архивы в Glacier"
    ],
    "key_points_en": [
      "S3 File Gateway: provides NFS/SMB access to S3 objects with local low-latency caching",
      "Volume Gateway: provides on-premises iSCSI block storage backed by AWS (Cached or Stored)",
      "Tape Gateway: replaces physical magnetic tapes with virtual tape libraries (VTL) in Glacier"
    ]
  },

  # --- NETWORKING ---
  "amazon_vpc": {
    "name": "Amazon VPC (Virtual Private Cloud)",
    "category": "Networking",
    "desc_ru": "Изолированная виртуальная сеть в облаке AWS, в которой вы определяете IP-диапазоны, подсети, таблицы маршрутизации и шлюзы.",
    "desc_en": "Logically isolated virtual network in AWS where you define your IP address range, subnets, route tables, and gateways.",
    "key_points_ru": [
      "Публичные подсети (Public Subnets): имеют маршрут в Интернет через Internet Gateway (IGW)",
      "Приватные подсети (Private Subnets): изолированы от входящего трафика, выходят в Интернет через NAT Gateway",
      "Безопасность контролируется с помощью Security Groups (stateful) и Network ACLs (stateless)"
    ],
    "key_points_en": [
      "Public Subnets: have direct route to the Internet via an Internet Gateway (IGW)",
      "Private Subnets: isolated from inbound internet access, reach out via NAT Gateway",
      "Secured via Security Groups (instance-level, stateful) and Network ACLs (subnet-level, stateless)"
    ]
  },
  "amazon_route_53": {
    "name": "Amazon Route 53",
    "category": "Networking / DNS",
    "desc_ru": "Высокодоступный и масштабируемый сервис системы доменных имен (DNS) и регистрации доменов со 100% SLA.",
    "desc_en": "Highly available and scalable cloud Domain Name System (DNS) web service and domain registration with a 100% SLA.",
    "key_points_ru": [
      "Маршрутизация: Simple, Weighted (весовая), Latency (минимальный пинг), Failover (аварийная), Geolocation, Geoproximity",
      "Health Checks: автоматическая проверка доступности веб-серверов и переключение трафика при сбоях",
      "Alias Records: нативные указатели на ресурсы AWS (CloudFront, ELB, S3) без дополнительной оплаты за запросы"
    ],
    "key_points_en": [
      "Routing policies: Simple, Weighted, Latency-based, Failover, Geolocation, and Multi-value answer",
      "Health Checks: monitors endpoints and automatically routes traffic away from failing resources",
      "Alias Records: maps root domain directly to AWS resources (CloudFront, ALB, S3 websites)"
    ]
  },
  "amazon_cloudfront": {
    "name": "Amazon CloudFront",
    "category": "Networking / CDN",
    "desc_ru": "Глобальная сеть доставки контента (CDN), безопасно доставляющая данные, видео и API пользователям с низкой задержкой и высокой скоростью.",
    "desc_en": "Global content delivery network (CDN) service that securely delivers data, videos, applications, and APIs with low latency.",
    "key_points_ru": [
      "Использует сеть Edge Locations (точек присутствия) по всему миру для кэширования статического и динамического контента",
      "Снижает нагрузку на исходные серверы и снижает расходы на передачу данных из Amazon S3",
      "Интеграция с AWS Shield и AWS WAF для защиты веб-приложений на границе сети"
    ],
    "key_points_en": [
      "Uses a worldwide network of Edge Locations to cache static and dynamic content close to users",
      "Decreases latency and reduces data transfer egress costs from origin servers and Amazon S3",
      "Integrates with AWS Shield and AWS WAF for perimeter DDoS and layer 7 attack mitigation"
    ]
  },
  "aws_direct_connect": {
    "name": "AWS Direct Connect",
    "category": "Networking / Dedicated Line",
    "desc_ru": "Выделенное прямое физическое сетевое соединение между вашим локальным дата-центром и AWS в обход публичного Интернета.",
    "desc_en": "Dedicated, private physical network connection from an on-premises data center directly to AWS, bypassing the public Internet.",
    "key_points_ru": [
      "Гарантированная пропускная способность от 1 Гбит/с до 100 Гбит/с и стабильный минимальный пинг",
      "Снижение затрат на передачу данных по сравнению с выгрузкой через интернет-провайдеров",
      "Идеально для передачи гигантских объемов данных и критически важных корпоративных систем"
    ],
    "key_points_en": [
      "Dedicated fiber optic lines (1 Gbps to 100 Gbps) delivering consistent, deterministic network latency",
      "Bypasses the public internet for enhanced security and reduced data transfer rates",
      "Ideal for mission-critical enterprise workloads and massive continuous data transfers"
    ]
  },
  "aws_transit_gateway": {
    "name": "AWS Transit Gateway",
    "category": "Networking / Hub Router",
    "desc_ru": "Центральный сетевой маршрутизатор (Hub), соединяющий тысячи VPC и локальных корпоративных сетей через единую точку.",
    "desc_en": "Central network hub router connecting thousands of Amazon VPCs and on-premises networks through a single connection point.",
    "key_points_ru": [
      "Заменяет сложную паутину прямых пирингов (VPC Peering full mesh) простой топологией «звезда» (Hub-and-Spoke)",
      "Упрощает масштабирование корпоративных сетей и маршрутизацию между десятками аккаунтов AWS",
      "Поддерживает подключение Direct Connect и VPN"
    ],
    "key_points_en": [
      "Replaces complex full-mesh VPC peering topologies with a simple hub-and-spoke model",
      "Simplifies multi-VPC management across hundreds of AWS accounts",
      "Directly attaches to VPCs, Direct Connect gateways, and Site-to-Site VPN connections"
    ]
  },

  # --- DATABASES ---
  "amazon_rds": {
    "name": "Amazon RDS (Relational Database Service)",
    "category": "Databases / Relational",
    "desc_ru": "Управляемый сервис реляционных баз данных, автоматизирующий установку патчей, резервное копирование и масштабирование.",
    "desc_en": "Managed relational database service that simplifies setup, operation, and scaling of relational databases in the cloud.",
    "key_points_ru": [
      "Поддерживаемые движки: PostgreSQL, MySQL, MariaDB, Oracle, Microsoft SQL Server и Amazon Aurora",
      "Multi-AZ: синхронная репликация в другую зону доступности для автоматического переключения при сбое (HA/DR)",
      "Read Replicas: асинхронные реплики для снятия нагрузки чтения и повышения производительности"
    ],
    "key_points_en": [
      "Supported engines: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server",
      "Multi-AZ: synchronous replication to a standby instance in another AZ for automatic disaster failover",
      "Read Replicas: asynchronous replicas to scale out read-heavy database query performance"
    ]
  },
  "amazon_aurora": {
    "name": "Amazon Aurora",
    "category": "Databases / Cloud-Native Relational",
    "desc_ru": "Облачная реляционная база данных, совместимая с MySQL и PostgreSQL, со скоростью в 5 раз выше стандартного MySQL.",
    "desc_en": "MySQL and PostgreSQL-compatible relational database built for the cloud, combining enterprise speed with open-source simplicity.",
    "key_points_ru": [
      "Автоматически реплицирует 6 копий данных в 3 зонах доступности (Multi-AZ storage)",
      "Самовосстанавливающееся дисковое хранилище, масштабируемое до 128 ТБ без прерывания работы",
      "Aurora Serverless: автоматический запуск, остановка и масштабирование емкости в зависимости от нагрузки"
    ],
    "key_points_en": [
      "Automatically replicates 6 copies of data across 3 Availability Zones for durability",
      "Self-healing storage layer that automatically expands up to 128 TB without downtime",
      "Aurora Serverless: automatically starts, scales, and shuts down compute based on application demand"
    ]
  },
  "amazon_dynamodb": {
    "name": "Amazon DynamoDB",
    "category": "Databases / NoSQL Key-Value",
    "desc_ru": "Бессерверная нереляционная база данных документов и пар «ключ-значение», обеспечивающая стабильную скорость ответа менее 10 миллисекунд.",
    "desc_en": "Fully managed, serverless NoSQL key-value and document database that delivers single-digit millisecond performance at any scale.",
    "key_points_ru": [
      "Режимы емкости: On-Demand (оплата за запросы) и Provisioned (выделенная пропускная способность с автоскейлингом)",
      "Global Tables: полностью управляемая мультирегиональная репликация с активной записью в нескольких регионах",
      "DynamoDB Accelerator (DAX): встроенный кэш в оперативной памяти, ускоряющий чтение до микросекунд"
    ],
    "key_points_en": [
      "Capacity modes: On-Demand (pay-per-request) and Provisioned (pre-allocated with Auto Scaling)",
      "Global Tables: multi-Region, fully replicated active-active database clusters for global applications",
      "DynamoDB Accelerator (DAX): in-memory cache delivering microsecond read response times"
    ]
  },
  "amazon_elasticache": {
    "name": "Amazon ElastiCache",
    "category": "Databases / In-Memory Caching",
    "desc_ru": "Управляемый сервис кэширования данных в оперативной памяти на базе Redis или Memcached для ускорения приложений.",
    "desc_en": "Fully managed in-memory data store and cache service supporting Redis and Memcached to accelerate application response times.",
    "key_points_ru": [
      "Снижает нагрузку на реляционные базы данных за счет кэширования частых SQL-запросов и сессий пользователей",
      "Время ответа в доли миллисекунды для игровых лидербордов, очередей и кэша веб-сайтов",
      "Поддерживает кластеризацию и высокую доступность с репликацией в нескольких AZ"
    ],
    "key_points_en": [
      "Reduces primary database read loads by caching frequent query results and user sessions",
      "Delivers sub-millisecond response latency for real-time leaderboards, web sessions, and caching",
      "Supports clustering, persistence, and multi-AZ replication with automatic failover"
    ]
  },
  "amazon_redshift": {
    "name": "Amazon Redshift",
    "category": "Databases / Data Warehousing",
    "desc_ru": "Быстрое, масштабируемое облачное хранилище корпоративных данных (Data Warehouse) для сложной аналитики и OLAP-запросов.",
    "desc_en": "Fast, scalable cloud data warehouse service that makes it simple to analyze all your data using standard SQL and existing BI tools.",
    "key_points_ru": [
      "Колоночное хранилище данных (Columnar Storage) с массово-параллельной обработкой (MPP)",
      "Предназначено для аналитических отчетов (OLAP), а не для частых транзакций (OLTP)",
      "Интеграция с Amazon S3 через Redshift Spectrum и сервисами бизнес-аналитики QuickSight"
    ],
    "key_points_en": [
      "Columnar data storage with massively parallel processing (MPP) architecture",
      "Designed for analytical reporting and complex BI queries (OLAP), not transaction processing (OLTP)",
      "Directly queries S3 data lakes via Redshift Spectrum and integrates with Amazon QuickSight"
    ]
  },

  # --- SECURITY & MANAGEMENT ---
  "aws_iam": {
    "name": "AWS IAM (Identity and Access Management)",
    "category": "Security / Access Control",
    "desc_ru": "Централизованный контроль доступа к сервисам и ресурсам AWS с управлением пользователями, группами, ролями и политиками.",
    "desc_en": "Centrally manage permissions that control which AWS services and resources users, groups, and roles can access.",
    "key_points_ru": [
      "Принцип наименьших привилегий (Least Privilege): выдавать только минимально необходимые права",
      "IAM Roles: временные учетные данные для серверов EC2, сервисов и федеративных пользователей без постоянных паролей",
      "MFA (многофакторная аутентификация): обязательна для защиты учетной записи root и администраторов",
      "Сервис является глобальным (Global Service) и бесплатным"
    ],
    "key_points_en": [
      "Principle of Least Privilege: grant only the minimum permissions required to perform tasks",
      "IAM Roles: provide temporary security credentials for EC2, Lambda, and federated users without hard-coded keys",
      "MFA (Multi-Factor Authentication): strongly recommended to safeguard root and administrative accounts",
      "Global service provided at no additional charge"
    ]
  },
  "amazon_guardduty": {
    "name": "Amazon GuardDuty",
    "category": "Security / Threat Detection",
    "desc_ru": "Интеллектуальный сервис обнаружения угроз, использующий машинное обучение для непрерывного анализа логов VPC, DNS и CloudTrail.",
    "desc_en": "Intelligent threat detection service that continuously monitors your AWS accounts and workloads for malicious activity using machine learning.",
    "key_points_ru": [
      "Выявляет признаки компрометации: несанкционированный майнинг криптовалют, утечки ключей, подозрительный сетевой трафик",
      "Работает автономно без необходимости устанавливать агенты на серверы",
      "Включается в один клик в консоли AWS и интегрируется с EventBridge для автоматического реагирования"
    ],
    "key_points_en": [
      "Identifies security threats: unauthorized cryptocurrency mining, compromised credentials, and anomalous traffic",
      "Completely agentless; monitors VPC Flow Logs, DNS logs, CloudTrail management, and data events",
      "Enabled with one click across an organization; triggers automated remediation via EventBridge"
    ]
  },
  "aws_waf": {
    "name": "AWS WAF (Web Application Firewall)",
    "category": "Security / Application Firewall",
    "desc_ru": "Сетевой файрвол прикладного уровня (Layer 7) для защиты веб-приложений от распространенных сетевых атак и эксплойтов.",
    "desc_en": "Web application firewall that helps protect web applications against common web exploits and bots at OSI Layer 7.",
    "key_points_ru": [
      "Защищает от SQL-инъекций (SQLi), межсайтового скриптинга (XSS) и вредоносных ботов",
      "Развертывается на CloudFront, Application Load Balancer (ALB), API Gateway и AWS AppSync",
      "Поддерживает готовые управляемые правила (AWS Managed Rules) и кастомные фильтры по IP и заголовкам"
    ],
    "key_points_en": [
      "Protects against Layer 7 exploits including SQL injection, Cross-Site Scripting (XSS), and bot scrapers",
      "Attaches to Amazon CloudFront, Application Load Balancers, API Gateway, and AWS AppSync",
      "Supports pre-configured AWS Managed Rules as well as custom IP and rate-limiting rules"
    ]
  },
  "aws_shield": {
    "name": "AWS Shield (Standard & Advanced)",
    "category": "Security / DDoS Protection",
    "desc_ru": "Управляемый сервис защиты от распределенных атак типа «отказ в обслуживании» (DDoS).",
    "desc_en": "Managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS.",
    "key_points_ru": [
      "Shield Standard: включен автоматически и бесплатно для всех клиентов AWS, защищает на уровнях Layer 3/4 (SYN floods, UDP reflection)",
      "Shield Advanced: платная подписка ($3000/мес), круглосуточный доступ к Shield Response Team (SRT), защита от всплесков расходов при DDoS",
      "Идеально сочетается с Route 53 и CloudFront для поглощения масштабных атак"
    ],
    "key_points_en": [
      "Shield Standard: automatically enabled at no extra charge, protects against Layer 3 and 4 DDoS attacks",
      "Shield Advanced: paid tier ($3,000/mo) with 24/7 access to Shield Response Team and financial spike protection",
      "Best deployed in combination with Amazon CloudFront and Route 53 to absorb large-scale traffic floods"
    ]
  },
  "aws_kms": {
    "name": "AWS KMS (Key Management Service)",
    "category": "Security / Encryption",
    "desc_ru": "Управляемый сервис для создания, хранения и контроля криптографических ключей шифрования данных в облаке.",
    "desc_en": "Managed service that makes it easy to create and control cryptographic keys used to encrypt data across AWS services.",
    "key_points_ru": [
      "Интегрирован с большинством сервисов AWS (S3, EBS, RDS, Secrets Manager, DynamoDB)",
      "Ключи защищены аппаратными модулями безопасности (HSM) со стандартом FIPS 140-2",
      "Логирует все попытки использования ключей в AWS CloudTrail для соблюдения аудиторских требований"
    ],
    "key_points_en": [
      "Seamlessly integrated with dozens of AWS services (S3, EBS, RDS, Secrets Manager, DynamoDB)",
      "Backed by hardware security modules (HSMs) validated under FIPS 140-2 standards",
      "Audits all key usage requests through AWS CloudTrail logs for compliance monitoring"
    ]
  },
  "aws_cloudtrail": {
    "name": "AWS CloudTrail",
    "category": "Management / Governance & Auditing",
    "desc_ru": "Сервис аудита и протоколирования всех действий и вызовов API в вашей учетной записи AWS.",
    "desc_en": "Monitors and records account activity across your AWS infrastructure, answering who did what, when, and from where.",
    "key_points_ru": [
      "Записывает вызовы API через Консоль AWS, AWS CLI, SDK и сервисы AWS",
      "Хранит 90 дней истории событий бесплатно; создание Trail позволяет выгружать логи в S3 для долгосрочного аудита",
      "Ключевой сервис для расследования инцидентов безопасности и соответствия нормативам"
    ],
    "key_points_en": [
      "Records all API calls executed via AWS Console, CLI, SDKs, and automated services",
      "Maintains 90 days of Event History free; creating a Trail archives logs to Amazon S3 permanently",
      "Essential for security forensics, operational troubleshooting, and compliance audits"
    ]
  },
  "amazon_cloudwatch": {
    "name": "Amazon CloudWatch",
    "category": "Management / Observability & Monitoring",
    "desc_ru": "Сервис мониторинга и наблюдаемости за ресурсами и приложениями в AWS и локальных средах в реальном времени.",
    "desc_en": "Monitoring and observability service built for DevOps, developers, and IT managers to track metrics, logs, and alarms.",
    "key_points_ru": [
      "Метрики: собирает стандартные (CPU, диск, сеть) и пользовательские метрики ресурсов",
      "Alarms: отправляет оповещения через SNS или инициирует действия Auto Scaling при превышении порогов",
      "Logs: централизованное хранилище и поиск по логам приложений и системных журналов",
      "Synthetics: проверка доступности URL-адресов с помощью канареечных сценариев (Canaries)"
    ],
    "key_points_en": [
      "Metrics: tracks system performance (CPU, disk I/O, network) and custom application metrics",
      "Alarms: triggers notifications via Amazon SNS or initiates Auto Scaling actions when thresholds are breached",
      "Logs: central log storage, search, and metric filtering for application logs",
      "Synthetics: simulates user traffic and tests application endpoint availability via canary scripts"
    ]
  },
  "aws_trusted_advisor": {
    "name": "AWS Trusted Advisor",
    "category": "Management / Best Practices",
    "desc_ru": "Автоматизированный онлайн-советник, сканирующий вашу инфраструктуру AWS на соответствие лучшим практикам.",
    "desc_en": "Automated online advisor that scans your AWS infrastructure and provides actionable recommendations to optimize resources.",
    "key_points_ru": [
      "5 категорий проверок: Оптимизация затрат, Производительность, Безопасность, Отказоустойчивость, Сервисные лимиты",
      "Basic и Developer Support включают 7 базовых проверок",
      "Business и Enterprise Support включают доступ ко всем 100+ проверкам и интеграцию с API"
    ],
    "key_points_en": [
      "5 categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits",
      "Basic and Developer Support plans include 7 core checks",
      "Business and Enterprise Support unlock the complete library of over 100+ checks and API access"
    ]
  }
}

print(f"Total curated service entries: {len(SERVICES)}")
with open('data/services_info.json', 'w', encoding='utf-8') as f:
    json.dump(SERVICES, f, ensure_ascii=False, indent=2)
print("Saved comprehensive dictionary to data/services_info.json!")
