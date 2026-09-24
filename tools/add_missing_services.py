import json

new_services = {
  "aws_security_hub": {
    "name": "AWS Security Hub",
    "category": "Security, Identity & Compliance",
    "desc_ru": "Централизованный сервис управления состоянием безопасности и соответствия стандартам (CSPM), объединяющий оповещения от GuardDuty, Inspector, Macie, IAM Access Analyzer и систем партнеров.",
    "desc_en": "Centralized security posture management service (CSPM) that aggregates, organizes, and prioritizes security alerts and compliance checks from multiple AWS services and partner tools.",
    "key_points_ru": [
      "Автоматическая проверка соответствия отраслевым стандартам: CIS AWS Foundations Benchmark, PCI-DSS, AWS Best Practices",
      "Единый консолидированный дашборд безопасности для всех аккаунтов в AWS Organizations",
      "Автоматический расчет единого индекса безопасности (Security Score) организации"
    ],
    "key_points_en": [
      "Performs automated compliance checks against CIS AWS Foundations Benchmark, PCI-DSS, and AWS Foundational Security Best Practices",
      "Unified single-pane-of-glass dashboard across multi-account AWS Organizations",
      "Computes an overall organizational Security Score"
    ]
  },
  "aws_global_infrastructure": {
    "name": "AWS Global Infrastructure (Regions, AZs, Edge Locations)",
    "category": "Cloud Infrastructure",
    "desc_ru": "Глобальная физическая инфраструктура AWS: Регионы (изолированные географические зоны), Зоны Доступности (AZ, дата-центры на расстоянии < 100 км с независимым питанием) и Краевые Точки (Edge Locations для CloudFront).",
    "desc_en": "Physical global infrastructure of AWS comprising Regions (isolated geographic locations), Availability Zones (AZs, discrete data centers with redundant power and low latency networking), and Edge Locations (CloudFront CDN PoPs).",
    "key_points_ru": [
      "Регион AWS состоит минимум из трех независимых Зон Доступности (AZ)",
      "Каждая AZ состоит из одного или нескольких изолированных дата-центров",
      "Edge Locations (PoP) используются для кэширования контента CloudFront и ускорения Route 53 ближе к пользователям",
      "AWS Local Zones и Wavelength приближают вычислительные мощности к крупным мегаполисам и вышкам 5G для сверхнизких задержек (< 10 мс)"
    ],
    "key_points_en": [
      "An AWS Region consists of a minimum of 3 isolated Availability Zones",
      "Each AZ consists of one or more physical data centers with redundant power and cooling",
      "Edge Locations cache CloudFront content and speed up Route 53 queries closest to end users",
      "Local Zones and Wavelength extend compute closer to metro centers and 5G networks for single-digit millisecond latency"
    ]
  },
  "well_architected_framework": {
    "name": "AWS Well-Architected Framework",
    "category": "Architecture & Best Practices",
    "desc_ru": "Набор архитектурных рекомендаций и принципов AWS, помогающий проектировать безопасные, высокопроизводительные, отказоустойчивые и эффективные облачные приложения.",
    "desc_en": "Guidance and architectural best practices helping cloud architects build secure, high-performing, resilient, and cost-optimized cloud applications.",
    "key_points_ru": [
      "6 столпов (Pillars): Operational Excellence (Эксплуатационная надежность), Security (Безопасность), Reliability (Надежность), Performance Efficiency (Производительность), Cost Optimization (Оптимизация затрат), Sustainability (Устойчивое развитие/экология)",
      "AWS Well-Architected Tool: бесплатный инструмент в консоли для оценки архитектуры по контрольным вопросам"
    ],
    "key_points_en": [
      "6 Pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability",
      "AWS Well-Architected Tool: Free console service providing question-based reviews against AWS architectural guidelines"
    ]
  },
  "shared_responsibility_model": {
    "name": "AWS Shared Responsibility Model",
    "category": "Security & Compliance",
    "desc_ru": "Модель разделения ответственности за безопасность между AWS и клиентом: безопасность «САМОГО облака» (Security OF the Cloud) лежит на AWS, а безопасность «ВНУТРИ облака» (Security IN the Cloud) — на клиенте.",
    "desc_en": "Security model dividing security duties: AWS is responsible for Security OF the Cloud (hardware, physical data centers, host virtualization), while the customer is responsible for Security IN the Cloud (data, IAM, OS patching on EC2, network config).",
    "key_points_ru": [
      "AWS отвечает за: физическую безопасность ДЦ, серверное оборудование, сетевые кабели, гипервизор, утилизацию накопителей",
      "Клиент отвечает за: шифрование данных (at-rest и in-transit), права IAM, настройку Security Groups, установку обновлений ОС на EC2",
      "В управляемых сервисах (S3, DynamoDB, RDS, Lambda) AWS берет на себя ОС и патчинг движка, клиент управляет доступом и данными"
    ],
    "key_points_en": [
      "AWS manages: Physical facility security, host hardware, virtualization hypervisor, hardware disk decommissioning",
      "Customer manages: Customer data encryption, IAM policies and credentials, Security Groups firewall rules, OS patching for EC2",
      "For managed services (S3, DynamoDB, Lambda, RDS): AWS manages the OS and runtime; customer manages access controls and data"
    ]
  },
  "aws_local_zones": {
    "name": "AWS Local Zones",
    "category": "Cloud Infrastructure",
    "desc_ru": "Тип инфраструктуры AWS, размещающий вычислительные ресурсы (EC2, EBS, VPC) в непосредственной близости от крупных промышленных центров для обеспечения задержки менее 10 миллисекунд.",
    "desc_en": "Infrastructure deployment placing AWS compute, storage, and database services closer to large population, industry, and IT centers for single-digit millisecond latency.",
    "key_points_ru": [
      "Идеально подходит для видеостриминга в реальном времени, медиапродакшна, онлайн-гейминга и телемедицины",
      "Логически расширяет существующий родительский регион AWS через подсети VPC"
    ],
    "key_points_en": [
      "Ideal for real-time video streaming, live media production, competitive gaming, and healthcare workloads",
      "Logically extends an existing parent AWS Region into local subnets within your VPC"
    ]
  },
  "aws_caf": {
    "name": "AWS Cloud Adoption Framework (AWS CAF)",
    "category": "Cloud Strategy & Migration",
    "desc_ru": "Методология AWS, помогающая организациям разрабатывать эффективные планы перехода в облако с охватом бизнес- и технологических аспектов.",
    "desc_en": "Framework providing guidance and best practices to help organizations digitally transform and accelerate their cloud adoption journey.",
    "key_points_ru": [
      "6 перспектив CAF: Бизнес (Business), Люди (People), Управление (Governance), Платформа (Platform), Безопасность (Security), Эксплуатация (Operations)",
      "Бизнес-перспективы: Business, People, Governance; Технические перспективы: Platform, Security, Operations"
    ],
    "key_points_en": [
      "6 Perspectives: Business, People, Governance, Platform, Security, Operations",
      "Business-focused: Business, People, Governance; Technical-focused: Platform, Security, Operations"
    ]
  },
  "aws_mgn": {
    "name": "AWS Application Migration Service (AWS MGN)",
    "category": "Migration & Transfer",
    "desc_ru": "Основной рекомендуемый сервис AWS для переноса серверов и приложений в облако с минимальным временем простоя путем блочной репликации на уровне дисков.",
    "desc_en": "Primary recommended migration service for lift-and-shift physical, virtual, or cloud-based servers to AWS with minimal downtime using continuous block-level replication.",
    "key_points_ru": [
      "Автоматическая непрерывная репликация дисков в фоновом режиме без остановки исходного сервера",
      "Поддерживает широкий спектр ОС Windows и Linux",
      "Пришел на замену CloudEndure Migration"
    ],
    "key_points_en": [
      "Continuous block-level data replication without disrupting source production servers",
      "Supports wide variety of Windows and Linux operating systems",
      "Official AWS successor to CloudEndure Migration"
    ]
  },
  "aws_support": {
    "name": "AWS Support Plans",
    "category": "Cloud Support & Operations",
    "desc_ru": "Планы технической поддержки AWS: Basic (бесплатный), Developer (для тестирования), Business (для продакшна с 24/7 доступом к инженерам) и Enterprise (с выделенным TAM).",
    "desc_en": "Tiered support plans provided by AWS: Basic (free), Developer (experimentation), Business (production 24/7 support), and Enterprise (mission-critical with dedicated TAM).",
    "key_points_ru": [
      "Basic: доступ к документации, форумам и базовому Trusted Advisor (7 проверок). $0",
      "Developer: доступ к инженерам поддержки по email в рабочие часы, время ответа < 12 ч при сбоях. От $29/мес",
      "Business: круглосуточный 24/7 доступ по телефону, чату и email, ответ < 1 ч на production down, полный Trusted Advisor. От $100/мес",
      "Enterprise On-Ramp: 24/7 доступ, ответ < 30 мин на критические инциденты, пул технических аккаунт-менеджеров (TAM)",
      "Enterprise: время ответа < 15 мин на business-critical сбои, персональный выделенный TAM, консультации Well-Architected и координация IEM"
    ],
    "key_points_en": [
      "Basic: Customer service, documentation, whitepapers, 7 core Trusted Advisor checks. Free",
      "Developer: Business hours email access to Cloud Support Associates, < 12h response for impaired system. From $29/mo",
      "Business: 24/7 phone, email, chat access to Cloud Support Engineers, < 1h for production down, full Trusted Advisor. From $100/mo",
      "Enterprise On-Ramp: 24/7 access, < 30 min critical response, pooled Technical Account Managers (TAM)",
      "Enterprise: < 15 min response for business-critical system down, dedicated TAM, Well-Architected reviews, and IEM support"
    ]
  },
  "aws_tam": {
    "name": "Technical Account Manager (AWS TAM)",
    "category": "Cloud Support & Operations",
    "desc_ru": "Персональный технический консультант AWS, закрепляемый за клиентом на планах Enterprise Support для стратегического планирования, оптимизации архитектуры и решения эскалаций.",
    "desc_en": "Designated technical advisor and single point of contact at AWS for Enterprise Support customers, providing architectural guidance and operational reviews.",
    "key_points_ru": [
      "Доступен эксклюзивно на планах поддержки Enterprise Support (выделенный) и Enterprise On-Ramp (пул)",
      "Помогает планировать масштабные запуски через Infrastructure Event Management (IEM)",
      "Проводит регулярные ревью затрат и архитектуры Well-Architected Reviews"
    ],
    "key_points_en": [
      "Exclusive to Enterprise Support (dedicated TAM) and Enterprise On-Ramp (pooled TAM)",
      "Coordinates Infrastructure Event Management (IEM) for high-traffic events and product launches",
      "Conducts proactive architectural reviews and cost optimization sessions"
    ]
  },
  "aws_concierge_support": {
    "name": "AWS Concierge Support Team",
    "category": "Billing & Cost Management",
    "desc_ru": "Выделенная команда экспертов AWS по биллингу и управлению аккаунтами, доступная клиентам Enterprise Support.",
    "desc_en": "Senior customer service experts dedicated to addressing billing, invoicing, and account management inquiries for Enterprise Support customers.",
    "key_points_ru": [
      "Помогает разбираться со счетами, консолидированным биллингом, распределением скидок и объединением аккаунтов",
      "Входит в состав планов Enterprise Support и Enterprise On-Ramp"
    ],
    "key_points_en": [
      "Specialized in billing breakdowns, invoice inquiries, consolidated billing structures, and cost allocation questions",
      "Included with Enterprise and Enterprise On-Ramp Support plans"
    ]
  },
  "aws_infrastructure_event_management": {
    "name": "AWS Infrastructure Event Management (IEM)",
    "category": "Cloud Support & Operations",
    "desc_ru": "Программа подготовки и сопровождения критических бизнес-событий (Черная пятница, запуск продукта, миграция) инженерами AWS.",
    "desc_en": "Short-term engagement offering architectural guidance, capacity planning, and real-time operational support during critical business milestones and high-traffic launches.",
    "key_points_ru": [
      "Включена бесплатно в план Enterprise Support; доступна для покупки как дополнительная опция на плане Business Support",
      "Оценка масштабируемости, проверка квот и резервирование мощностей с архитекторами AWS перед днем запуска"
    ],
    "key_points_en": [
      "Included with Enterprise Support; available as an add-on purchase for Business Support customers",
      "Includes architecture guidance, operational readiness reviews, and real-time standby support during events"
    ]
  },
  "aws_health_dashboard": {
    "name": "AWS Health Dashboard",
    "category": "Management & Governance",
    "desc_ru": "Сервис, отображающий персонализированное состояние сервисов AWS, которые непосредственно используются вашими ресурсами (ранее Personal Health Dashboard).",
    "desc_en": "Provides personalized notifications and guidance when AWS is experiencing events that may impact your specific AWS accounts and cloud resources.",
    "key_points_ru": [
      "Показывает статус только тех сервисов и регионов, где у вас запущены инстансы, базы данных или ресурсы",
      "Предупреждает о плановом техническом обслуживании оборудования, выходе из строя дисков или устаревании версий ПО"
    ],
    "key_points_en": [
      "Displays targeted alerts affecting the specific AWS resources and regions you actively use",
      "Notifies of scheduled hardware maintenance, retired instance warnings, and upcoming software deprecations"
    ]
  },
  "aws_marketplace": {
    "name": "AWS Marketplace",
    "category": "Procurement & Governance",
    "desc_ru": "Онлайн-каталог тысяч программных продуктов сторонних разработчиков (ISV), готовых к мгновенному развертыванию на AWS с единым счетом через AWS Billing.",
    "desc_en": "Digital software catalog that helps customers discover, test, buy, and instantly deploy third-party software, AMI appliances, and SaaS solutions billed directly on AWS.",
    "key_points_ru": [
      "Тысячи готовых образов ОС, файрволов (Cisco, Fortinet, Palo Alto), баз данных и средств аналитики",
      "Оплата включается в общий ежемесячный счет AWS (Consolidated Billing)",
      "Поддерживает гибкие модели: Pay-as-you-go (почасовая), месячная подписка, BYOL (Bring Your Own License)"
    ],
    "key_points_en": [
      "Catalog containing thousands of third-party software listings across security, networking, analytics, and databases",
      "Simplified procurement with software charges consolidated directly into your standard AWS invoice",
      "Flexible pricing models: Hourly Pay-as-you-go, annual contracts, and Bring Your Own License (BYOL)"
    ]
  },
  "aws_service_quotas": {
    "name": "AWS Service Quotas",
    "category": "Management & Governance",
    "desc_ru": "Сервис централизованного просмотра и запроса на увеличение лимитов (квот) ресурсов AWS для предотвращения непреднамеренного перерасхода или сбоев.",
    "desc_en": "Central service to view, manage, and request increases for resource limits and quotas across all AWS services from a single console.",
    "key_points_ru": [
      "Позволяет просматривать стандартные и повышенные лимиты (например, количество Elastic IP или vCPU для EC2)",
      "Автоматическая подача заявок на повышение квот в пару кликов без ручного создания тикетов"
    ],
    "key_points_en": [
      "View default and applied quota limits across services (e.g., maximum Elastic IPs, VPCs, or EC2 vCPUs)",
      "Automates requesting quota increases directly without having to compose manual support tickets"
    ]
  },
  "aws_free_tier": {
    "name": "AWS Free Tier",
    "category": "Billing & Cost Management",
    "desc_ru": "Программа бесплатного использования сервисов AWS для ознакомления и обучения, разделенная на три четких типа предложений.",
    "desc_en": "Program offering hands-on free usage of AWS services across three distinct categories to learn and test cloud workloads.",
    "key_points_ru": [
      "12 Months Free: доступно в течение первых 12 месяцев после регистрации (например, 750 ч/мес EC2 t2.micro/t3.micro, 5 ГБ S3 Standard, 750 ч/мес RDS db.t2/t3/t4g.micro)",
      "Always Free: бессрочно бесплатно для всех аккаунтов (например, 1 000 000 вызовов AWS Lambda, 25 ГБ Amazon DynamoDB, 10 метрик CloudWatch)",
      "Trials: краткосрочные бесплатные пробные периоды (от 30 до 90 дней) для определенных сервисов (GuardDuty, Inspector, Macie)"
    ],
    "key_points_en": [
      "12 Months Free: Available for first year after signup (750 hours/mo EC2 t2/t3.micro, 5 GB S3 Standard, 750 hours/mo RDS db.micro)",
      "Always Free: Free forever for all accounts (1,000,000 Lambda invocations/mo, 25 GB DynamoDB storage, 10 CloudWatch metrics)",
      "Trials: Short-term free trial periods (30 to 90 days) for specific services like GuardDuty, Inspector, and Macie"
    ]
  },
  "aws_cur": {
    "name": "AWS Cost and Usage Report (AWS CUR)",
    "category": "Billing & Cost Management",
    "desc_ru": "Самый подробный и детализированный источник информации о затратах и использовании AWS, сохраняющий CSV/Parquet отчеты в бакет Amazon S3 с разбивкой до уровня часов и ресурсов.",
    "desc_en": "The most granular and comprehensive billing data source in AWS, delivering hourly or daily usage records and metadata directly to an Amazon S3 bucket.",
    "key_points_ru": [
      "Содержит метаданные по каждому ресурсу, тегам распределения затрат (Cost Allocation Tags) и скидкам",
      "Идеально подходит для углубленного анализа через Amazon Athena, Amazon QuickSight или интеграции с внешними BI-платформами"
    ],
    "key_points_en": [
      "Contains detailed line-item records per resource, cost allocation tags, discounts, and tiered usage",
      "Optimized for deep SQL queries using Amazon Athena and dashboarding with Amazon QuickSight"
    ]
  },
  "aws_cost_anomaly_detection": {
    "name": "AWS Cost Anomaly Detection",
    "category": "Billing & Cost Management",
    "desc_ru": "Сервис на базе машинного обучения, непрерывно анализирующий паттерны ваших расходов на AWS и немедленно выявляющий аномальные всплески затрат.",
    "desc_en": "Machine learning-powered service that continuously monitors your AWS spending patterns to detect anomalies and identify root causes of cost spikes.",
    "key_points_ru": [
      "Бесплатный инструмент для всех клиентов AWS",
      "Отправляет мгновенные оповещения через Amazon SNS или email при обнаружении неожиданных скачков расходов",
      "Точно указывает конкретный сервис, аккаунт и регион, вызвавший аномалию"
    ],
    "key_points_en": [
      "100% free tool available to all AWS customers",
      "Sends immediate alerts via Amazon SNS notifications or email when anomalous spending is detected",
      "Pinpoints the root cause, identifying the exact service, region, and account responsible for the spike"
    ]
  },
  "aws_consolidated_billing": {
    "name": "Consolidated Billing (AWS Organizations)",
    "category": "Billing & Cost Management",
    "desc_ru": "Функция AWS Organizations, объединяющая счета всех связанных аккаунтов компании в один единый счет, оплачиваемый головным управляющим аккаунтом (Management Account).",
    "desc_en": "Feature of AWS Organizations that aggregates the charges of all member accounts into a single master monthly invoice paid by the Management Account.",
    "key_points_ru": [
      "Один общий ежемесячный счет для всех дочерних аккаунтов компании",
      "Суммирование объемов потребления (Volume Discounts): трафик S3 и передача данных суммируются между всеми аккаунтами для получения максимальных оптовых скидок",
      "Совместное использование скидок Reserved Instances и Savings Plans между аккаунтами в организации"
    ],
    "key_points_en": [
      "One consolidated monthly bill for all linked member accounts in the organization",
      "Aggregates usage across accounts to qualify for tier-based volume discounts on S3, data transfer, etc.",
      "Enables sharing of Savings Plans and Reserved Instance pricing benefits across member accounts"
    ]
  },
  "aws_cost_allocation_tags": {
    "name": "AWS Cost Allocation Tags",
    "category": "Billing & Cost Management",
    "desc_ru": "Метки (пары ключ-значение), присваиваемые ресурсам AWS для детального отслеживания расходов по проектам, отделам, центрам затрат или средам (dev/stage/prod).",
    "desc_en": "Key-value labels assigned to AWS resources used to organize and track cloud spending by department, project, cost center, or environment.",
    "key_points_ru": [
      "AWS-generated tags (начинаются с aws:) и User-defined tags (создаются пользователем, например Environment: Production, CostCenter: 1042)",
      "Метки необходимо активировать в консоли Billing, после чего они появляются в Cost Explorer и Cost and Usage Report (CUR)"
    ],
    "key_points_en": [
      "Two types: AWS-generated tags (prefix aws:) and User-defined tags (e.g., Project: Alpha, Env: Prod)",
      "Must be activated in the Billing console to appear in Cost Explorer and Cost & Usage Reports"
    ]
  },
  "aws_savings_plans": {
    "name": "AWS Savings Plans",
    "category": "Billing & Cost Management",
    "desc_ru": "Гибкая модель ценообразования, предоставляющая скидки до 72% в обмен на обязательство поддерживать постоянный объем потребления вычислений ($/час) на срок 1 или 3 года.",
    "desc_en": "Flexible pricing model providing up to 72% discounts compared to On-Demand in exchange for a commitment to a consistent amount of compute usage ($/hour) for a 1- or 3-year term.",
    "key_points_ru": [
      "Compute Savings Plans: максимальная гибкость, автоматически покрывает EC2, AWS Fargate и AWS Lambda независимо от региона, семейства инстансов или ОС (до 66% скидки)",
      "EC2 Instance Savings Plans: привязаны к семейству инстансов в конкретном регионе (например, m5 в us-east-1), обеспечивают максимальную скидку (до 72%)",
      "SageMaker Savings Plans: распространяются на инстансы машинного обучения Amazon SageMaker"
    ],
    "key_points_en": [
      "Compute Savings Plans: Highest flexibility, automatically applies to EC2, Fargate, and Lambda regardless of family, OS, or region (up to 66% off)",
      "EC2 Instance Savings Plans: Locked to a specific instance family in a region (e.g., c5 in eu-west-1), offering higher savings (up to 72% off)",
      "SageMaker Savings Plans: Applies to machine learning compute instances in Amazon SageMaker"
    ]
  },
  "aws_reserved_instances": {
    "name": "Amazon EC2 Reserved Instances (RI)",
    "category": "Compute & Billing",
    "desc_ru": "Скидка на вычислительные мощности (до 72%) при резервировании мощности на срок 1 или 3 года с возможностью резервирования емкости (Capacity Reservation).",
    "desc_en": "Billing discount (up to 72%) applied to On-Demand compute capacity in exchange for a 1- or 3-year commitment, with optional Capacity Reservation in specific AZs.",
    "key_points_ru": [
      "Стандартные (Standard RI) дают наибольшую скидку, но не позволяют менять семейство инстансов; Конвертируемые (Convertible RI) позволяют менять тип инстанса и ОС (скидка до 54%)",
      "Варианты оплаты: All Upfront (вся сумма сразу — макс. скидка), Partial Upfront (частичная предоплата) и No Upfront (ежемесячно)",
      "Неиспользуемые стандартные RI можно продавать на торговой площадке Reserved Instance Marketplace"
    ],
    "key_points_en": [
      "Standard RIs provide highest discount but cannot change instance family; Convertible RIs allow altering instance attributes (up to 54% off)",
      "Payment options: All Upfront (greatest discount), Partial Upfront, and No Upfront",
      "Unused Standard EC2 RIs can be resold on the AWS Reserved Instance Marketplace"
    ]
  },
  "amazon_quicksight": {
    "name": "Amazon QuickSight",
    "category": "Analytics & BI",
    "desc_ru": "Масштабируемый бессерверный сервис бизнес-аналитики (BI) с поддержкой машинного обучения для создания интерактивных дашбордов и визуализации данных.",
    "desc_en": "Scalable, serverless business intelligence (BI) service powered by machine learning for creating interactive dashboards and visualizing corporate data.",
    "key_points_ru": [
      "Супербыстрый встроенный движок вычислений в оперативной памяти SPICE (Super-fast, Parallel, In-memory Calculation Engine)",
      "Интегрируется с S3, Athena, RDS, Redshift и внешними источниками данных (Salesforce, SQL Server, Snowflake)",
      "Поддерживает запросы на естественном языке с помощью QuickSight Q (Generative BI)"
    ],
    "key_points_en": [
      "In-memory calculation engine SPICE (Super-fast, Parallel, In-memory Calculation Engine) for rapid dashboard rendering",
      "Seamlessly connects to S3, Athena, RDS, Redshift, and external sources (Snowflake, Salesforce, BigQuery)",
      "Supports natural language querying via QuickSight Q"
    ]
  },
  "amazon_fsx_for_windows_file_server": {
    "name": "Amazon FSx for Windows File Server",
    "category": "Storage",
    "desc_ru": "Полностью управляемое файловое хранилище на базе Windows Server с поддержкой стандартного протокола SMB (Server Message Block) и интеграцией с Microsoft Active Directory.",
    "desc_en": "Fully managed shared file storage built on Windows Server, delivering native SMB protocol support and full Microsoft Active Directory integration.",
    "key_points_ru": [
      "Разработано специально для корпоративных нагрузок Windows: файловые шары, IIS, SQL Server, домашние каталоги пользователей",
      "Поддерживает DFS Namespaces, теневые копии VSS, списки контроля доступа NTFS и шифрование данных"
    ],
    "key_points_en": [
      "Engineered specifically for enterprise Windows workloads: shared files, IIS web serving, SQL Server Failover Clusters",
      "Native SMB support with Microsoft Active Directory authentication, DFS Namespaces, and NTFS permissions"
    ]
  },
  "aws_cloudhsm": {
    "name": "AWS CloudHSM",
    "category": "Security, Identity & Compliance",
    "desc_ru": "Выделенный аппаратный модуль безопасности (Hardware Security Module, HSM) стандарта FIPS 140-2 Level 3, находящийся под единоличным контролем клиента внутри его VPC.",
    "desc_en": "Cloud-based dedicated Hardware Security Module (HSM) that enables you to easily generate and use your own cryptographic keys on FIPS 140-2 Level 3 validated hardware under customer-exclusive control.",
    "key_points_ru": [
      "В отличие от AWS KMS (который является общим мультитенантным сервисом), CloudHSM предоставляет физически изолированное аппаратное устройство",
      "AWS не имеет доступа к вашим криптографическим ключам шифрования (Single-tenant dedicated HSM)",
      "Применяется в финансовых учреждениях и при строгих регуляторных требованиях (FIPS 140-2 Level 3)"
    ],
    "key_points_en": [
      "Dedicated single-tenant hardware appliance inside your VPC, unlike multi-tenant AWS KMS",
      "Customer maintains exclusive control over keys; AWS personnel cannot access or view customer keys",
      "Complies with strict regulatory standards requiring FIPS 140-2 Level 3 certification"
    ]
  },
  "aws_global_accelerator": {
    "name": "AWS Global Accelerator",
    "category": "Networking & Content Delivery",
    "desc_ru": "Сетевой сервис, направляющий трафик пользователей через глобальную частную оптоволоконную сеть AWS с помощью двух статических Anycast IP-адресов, снижая задержки и джиттер.",
    "desc_en": "Networking service that routes traffic through the global private AWS fiber backbone using two static Anycast IP addresses, lowering latency, packet loss, and jitter.",
    "key_points_ru": [
      "Предоставляет 2 статических Anycast IP адреса, которые не меняются при изменении бэкенда",
      "Мгновенное автоматическое переключение при сбое (Failover < 30 сек) на здоровые регионы AWS",
      "В отличие от CloudFront (кэширующего HTTP-контент), Global Accelerator ускоряет как TCP/UDP трафик, так и некэшируемые API и VoIP"
    ],
    "key_points_en": [
      "Provides 2 static Anycast IP addresses acting as a fixed entry point to your applications",
      "Instant failover (< 30 seconds) across healthy multi-region endpoints",
      "Accelerates both TCP/UDP traffic, gaming, and non-cacheable APIs, unlike CloudFront which focuses on caching"
    ]
  },
  "aws_snowball": {
    "name": "AWS Snow Family (Snowcone, Snowball, Snowmobile)",
    "category": "Migration & Edge Computing",
    "desc_ru": "Семейство физических защищенных устройств для безопасной транспортировки петабайтных объемов данных в AWS и запуска вычислений на периферии без интернета.",
    "desc_en": "Family of rugged physical edge devices for secure terabyte- to petabyte-scale offline data migration and edge computing in disconnected environments.",
    "key_points_ru": [
      "AWS Snowcone: сверхкомпактное устройство (8 ТБ или 14 ТБ SSD), вес 2 кг, работает от аккумулятора",
      "AWS Snowball Edge: защищенный чемодан (до 80 ТБ storage-optimized или compute-optimized с GPU)",
      "AWS Snowmobile: грузовик с контейнером для перемещения до 100 Петабайт данных за одну поездку",
      "Шифрование данных ключами AWS KMS (256-bit) перед записью на устройство"
    ],
    "key_points_en": [
      "AWS Snowcone: Ultra-portable, lightweight (8 TB HDD or 14 TB SSD, 4.5 lbs) edge device",
      "AWS Snowball Edge: Ruggedized shipping container device up to 80 TB with on-board compute and GPU options",
      "AWS Snowmobile: 45-foot shipping container pulled by a semi-truck carrying up to 100 PB for exabyte migrations",
      "All data automatically encrypted with 256-bit keys before leaving customer premises"
    ]
  },
  "aws_batch": {
    "name": "AWS Batch",
    "category": "Compute",
    "desc_ru": "Сервис пакетной обработки данных, автоматически распределяющий и выполняющий сотни тысяч вычислительных заданий на контейнерах с использованием EC2, Spot и Fargate.",
    "desc_en": "Batch computing service that dynamically provisions the optimal quantity and type of compute resources (EC2, Spot, Fargate) to execute batch jobs at any scale.",
    "key_points_ru": [
      "Автоматически запускает и гасит инстансы по мере выполнения очереди задач без оплаты за сам сервис Batch (платите только за EC2/Fargate)",
      "Оптимизирован для использования Spot Instances для 90% экономии на вычислительных задачах"
    ],
    "key_points_en": [
      "Dynamically scales compute resources based on volume and requirements of submitted jobs",
      "No extra charge for AWS Batch itself; you only pay for underlying compute (EC2 or Fargate)",
      "Heavily utilizes Spot Instances to reduce compute costs by up to 90%"
    ]
  },
  "aws_billing_conductor": {
    "name": "AWS Billing Conductor",
    "category": "Billing & Cost Management",
    "desc_ru": "Сервис кастомизации биллинга, позволяющий настраивать индивидуальные тарифы, наценки и скидки для дочерних аккаунтов или внутренних клиентов организации.",
    "desc_en": "Customizable billing service that enables configuring custom pricing rules, markup, and discount parameters for internal financial chargebacks or customer invoicing.",
    "key_points_ru": [
      "Помогает MSP-партнерам и корпоративным центрам выставлять индивидуальные счета подразделениям",
      "Не меняет реальные расчеты с AWS, а формирует виртуальный отчет о начислениях"
    ],
    "key_points_en": [
      "Simplifies billing workflows for Managed Service Providers (MSPs) and internal financial chargeback models",
      "Does not modify actual AWS charges; generates customized chargeback views and billing groups"
    ]
  },
  "aws_apn": {
    "name": "AWS Partner Network (APN)",
    "category": "Business & Partner Programs",
    "desc_ru": "Глобальное сообщество авторизованных партнеров AWS (системных интеграторов, консалтинговых компаний и независимых разработчиков ПО ISV), помогающих строить решения на AWS.",
    "desc_en": "Global community of certified AWS Partners leveraging AWS technologies and programs to build, market, and sell customer solutions and professional consulting services.",
    "key_points_ru": [
      "Services Partners: консалтинговые компании и агентства, помогающие внедрять и мигрировать приложения в AWS",
      "Software Partners: компании-разработчики SaaS и программного обеспечения, работающего на платформе AWS"
    ],
    "key_points_en": [
      "Services Partners: Consulting firms and systems integrators guiding cloud architecture and cloud migrations",
      "Software Partners: ISVs providing SaaS, security, and developer tools built on or integrated with AWS"
    ]
  }
}

# Aliases to map shorthand keys directly to canonical entries
aliases = {
  "elb": "elastic_load_balancing",
  "alb": "elastic_load_balancing",
  "nlb": "elastic_load_balancing",
  "glb": "elastic_load_balancing",
  "elastic_load_balancing_(application_load_balancer)": "elastic_load_balancing",
  "elastic_load_balancing_(network_load_balancer)": "elastic_load_balancing",
  "ec2": "amazon_ec2",
  "ec2_spot_instances": "amazon_ec2",
  "ec2_dedicated_hosts": "amazon_ec2",
  "s3": "amazon_s3",
  "amazon_s3_object_lock": "amazon_s3",
  "rds": "amazon_rds",
  "aurora": "amazon_aurora",
  "dynamodb": "amazon_dynamodb",
  "vpc": "amazon_vpc",
  "vpc_interface_endpoint_(aws_privatelink)": "amazon_vpc",
  "iam": "aws_iam",
  "kms": "aws_kms",
  "aws_kms_(key_management_service)": "aws_kms",
  "cloudwatch": "amazon_cloudwatch",
  "cloudtrail": "aws_cloudtrail",
  "cloudfront": "amazon_cloudfront",
  "route_53": "amazon_route_53",
  "route53": "amazon_route_53",
  "amazon_route_53_latency-based_routing": "amazon_route_53",
  "efs": "amazon_efs",
  "amazon_elastic_file_system_(amazon_efs)": "amazon_efs",
  "eks": "amazon_eks",
  "amazon_elastic_kubernetes_service_(amazon_eks)": "amazon_eks",
  "ecs": "amazon_ecs",
  "sqs": "amazon_sqs",
  "sns": "amazon_sns",
  "eventbridge": "amazon_eventbridge",
  "step_functions": "aws_step_functions",
  "shield": "aws_shield",
  "aws_shield_standard": "aws_shield",
  "aws_shield_advanced": "aws_shield",
  "waf": "aws_waf",
  "guardduty": "amazon_guardduty",
  "inspector": "amazon_inspector",
  "macie": "amazon_macie",
  "security_hub": "aws_security_hub",
  "storage_gateway": "aws_storage_gateway",
  "aws_storage_gateway_(volume_gateway)": "aws_storage_gateway",
  "aws_storage_gateway_(tape_gateway)": "aws_storage_gateway",
  "cloudformation": "aws_cloudformation",
  "elastic_beanstalk": "aws_elastic_beanstalk",
  "direct_connect": "aws_direct_connect",
  "transit_gateway": "aws_transit_gateway",
  "trusted_advisor": "aws_trusted_advisor",
  "cost_explorer": "aws_cost_explorer",
  "budgets": "aws_budgets",
  "organizations": "aws_organizations",
  "control_tower": "aws_control_tower",
  "artifact": "aws_artifact",
  "secrets_manager": "aws_secrets_manager",
  "parameter_store": "systems_manager_parameter_store",
  "systems_manager": "aws_systems_manager",
  "config": "aws_config",
  "pricing_calculator": "aws_pricing_calculator",
  "aws_developer_support": "aws_support",
  "aws_business_support": "aws_support",
  "aws_enterprise_support": "aws_support",
  "aws_enterprise_on_ramp": "aws_support"
}

with open("data/services_info.json", "r", encoding="utf-8") as f:
    db = json.load(f)

for k, v in new_services.items():
    db[k] = v

for alias, target in aliases.items():
    if target in db and alias not in db:
        db[alias] = db[target]

with open("data/services_info.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Success! Total keys in services_info.json:", len(db))
