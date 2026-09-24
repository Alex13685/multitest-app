# -*- coding: utf-8 -*-
"""
Expands data/services_info.json with complete details for all remaining CLF-C02 services.
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/services_info.json', 'r', encoding='utf-8') as f:
    services = json.load(f)

MORE_SERVICES = {
  "aws_secrets_manager": {
    "name": "AWS Secrets Manager",
    "category": "Security / Secrets Management",
    "desc_ru": "Сервис для безопасного хранения, ротации и извлечения учетных данных баз данных, API-ключей и паролей по расписанию.",
    "desc_en": "Helps you manage, retrieve, and automatically rotate database credentials, API keys, and other secrets throughout their lifecycle.",
    "key_points_ru": [
      "Автоматическая встроенная ротация паролей для Amazon RDS, Aurora и DocumentDB с помощью функций Lambda",
      "Шифрование секретов в состоянии покоя с помощью ключей AWS KMS",
      "Программный доступ через SDK с кэшированием токенов для исключения жестко зашитых паролей в коде"
    ],
    "key_points_en": [
      "Automated scheduled rotation of database credentials for Amazon RDS, Aurora, and DocumentDB",
      "Encrypts secret values at rest using AWS KMS encryption keys",
      "Eliminates hard-coded secrets in source code by providing programmatic API retrieval"
    ]
  },
  "systems_manager_parameter_store": {
    "name": "AWS Systems Manager Parameter Store",
    "category": "Management / Configuration Store",
    "desc_ru": "Безопасное иерархическое хранилище конфигурационных данных и секретов (строки подключения, пароли, AMI ID).",
    "desc_en": "Provides secure, hierarchical storage for configuration data management and secrets management.",
    "key_points_ru": [
      "Хранит обычный текст (String) и зашифрованные секреты (SecureString через AWS KMS)",
      "Стандартный уровень (Standard parameters) бесплатен (до 10 000 параметров)",
      "В отличие от Secrets Manager, не имеет встроенной автоматической ротации паролей по расписанию"
    ],
    "key_points_en": [
      "Stores plain text configuration strings and encrypted SecureString values via AWS KMS",
      "Standard tier is free of charge for up to 10,000 parameters per Region",
      "Does not provide built-in automatic scheduled rotation like AWS Secrets Manager"
    ]
  },
  "aws_systems_manager": {
    "name": "AWS Systems Manager (SSM)",
    "category": "Management / Operations Automation",
    "desc_ru": "Центр управления серверами и гибридной инфраструктурой, позволяющий просматривать и контролировать ресурсы в масштабе.",
    "desc_en": "Provides a unified interface to view operational data from multiple AWS services and automate operational tasks across resources.",
    "key_points_ru": [
      "Session Manager: безопасное подключение по SSH/RDP через браузер в один клик без открытых портов 22/3389 и без Bastion host",
      "Patch Manager: автоматическая установка обновлений безопасности на ОС Windows и Linux по расписанию",
      "Run Command: удаленное безопасное выполнение скриптов и команд на тысячах инстансов одновременно"
    ],
    "key_points_en": [
      "Session Manager: one-click browser SSH/RDP terminal access without opening port 22 or bastion hosts",
      "Patch Manager: automated operating system security patch deployment on Windows and Linux",
      "Run Command: remotely and securely execute management commands at fleet scale across instances"
    ]
  },
  "aws_config": {
    "name": "AWS Config",
    "category": "Management / Compliance & Configuration Audit",
    "desc_ru": "Сервис для непрерывного отслеживания, записи и оценки конфигураций ресурсов AWS на соответствие корпоративным политикам.",
    "desc_en": "Continually assesses, audits, and evaluates the configurations and relationships of your AWS resources.",
    "key_points_ru": [
      "Ведет подробную историю изменений конфигурации каждого ресурса во времени (Timeline)",
      "Config Rules: проверяет правила соответствия (например, «все S3 бакеты должны быть зашифрованы»)",
      "Remediation: автоматическое исправление несоответствующих настроек через AWS Systems Manager Automation"
    ],
    "key_points_en": [
      "Records resource configuration change timelines and historical relationships over time",
      "Config Rules: validates compliance against best practices (e.g. S3 buckets must be encrypted)",
      "Remediation: triggers automated remediation actions for non-compliant resources via Systems Manager"
    ]
  },
  "aws_artifact": {
    "name": "AWS Artifact",
    "category": "Security / Compliance Reports",
    "desc_ru": "Центральный портал самообслуживания для бесплатного скачивания официальных аудиторских отчетов соответствия AWS (SOC, PCI DSS, ISO).",
    "desc_en": "Your go-to, central resource for compliance-related information, providing on-demand downloads of AWS security reports.",
    "key_points_ru": [
      "AWS Artifact Reports: официальные отчеты независимых аудиторов (SOC 1/2/3, PCI DSS, FedRAMP, ISO 27001)",
      "AWS Artifact Agreements: заключение юридических соглашений с AWS (например, Business Associate Addendum — BAA для HIPAA)",
      "Бесплатен и доступен всем клиентам через Консоль управления AWS"
    ],
    "key_points_en": [
      "AWS Artifact Reports: download third-party compliance audit reports (SOC 1/2/3, PCI, ISO, FedRAMP)",
      "AWS Artifact Agreements: review, accept, and manage agreements such as the BAA for HIPAA compliance",
      "Free self-service portal accessible directly within the AWS Management Console"
    ]
  },
  "amazon_inspector": {
    "name": "Amazon Inspector",
    "category": "Security / Vulnerability Management",
    "desc_ru": "Сервис автоматизированного управления уязвимостями, непрерывно сканирующий инстансы EC2, образы ECR и функции Lambda на наличие известных CVE.",
    "desc_en": "Automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure.",
    "key_points_ru": [
      "Автоматически обнаруживает известные уязвимости программного обеспечения (CVE) и непреднамеренную открытость портов в сеть",
      "Сканирует инстансы EC2 (через Systems Manager агент), образы контейнеров в ECR и код функций AWS Lambda",
      "Присваивает контекстный балл риска (Inspector Risk Score) для приоритизации исправлений"
    ],
    "key_points_en": [
      "Automatically discovers common vulnerabilities and exposures (CVEs) and unintended network paths",
      "Scans Amazon EC2 instances (via SSM Agent), container images in Amazon ECR, and Lambda functions",
      "Provides contextualized Inspector risk scores to prioritize critical remediation patches"
    ]
  },
  "amazon_macie": {
    "name": "Amazon Macie",
    "category": "Security / Data Privacy & ML",
    "desc_ru": "Сервис безопасности данных, использующий машинное обучение и сопоставление с шаблонами для поиска и защиты персональных данных (PII) в Amazon S3.",
    "desc_en": "Data security and data privacy service that uses machine learning and pattern matching to discover and protect sensitive data in Amazon S3.",
    "key_points_ru": [
      "Автоматически находит конфиденциальные данные: номера кредитных карт, паспорта, персональные идентификаторы (PII)",
      "Оценивает открытость бакетов S3 (публичный доступ, отсутствие шифрования)",
      "Генерирует оповещения безопасности и интегрируется с EventBridge для блокировки утечек"
    ],
    "key_points_en": [
      "Discovers sensitive data in Amazon S3 such as personally identifiable information (PII) and credentials",
      "Evaluates bucket security posture (public access, lack of encryption, shared accounts)",
      "Generates actionable findings and triggers automated alerting via Amazon EventBridge"
    ]
  },
  "aws_organizations": {
    "name": "AWS Organizations",
    "category": "Management / Governance & Billing",
    "desc_ru": "Сервис централизованного управления и консолидации нескольких учетных записей AWS в единую иерархическую структуру.",
    "desc_en": "Helps you centrally manage and govern your environment as you grow and scale your AWS resources across multiple accounts.",
    "key_points_ru": [
      "Consolidated Billing: единый счет на оплату для всех аккаунтов и автоматическое получение оптовых скидок за объем (Volume discounts)",
      "Organizational Units (OUs): группировка связанных аккаунтов (например, Dev, Prod, Security)",
      "Service Control Policies (SCPs): централизованные правила, задающие максимальные разрешенные права для учетных записей"
    ],
    "key_points_en": [
      "Consolidated Billing: single combined invoice for all linked accounts with aggregated volume discount tiers",
      "Organizational Units (OUs): hierarchical grouping of related accounts (e.g., Development, Production)",
      "Service Control Policies (SCPs): central guardrails that define the maximum permissions boundary for accounts"
    ]
  },
  "aws_control_tower": {
    "name": "AWS Control Tower",
    "category": "Management / Multi-Account Governance",
    "desc_ru": "Сервис автоматизированного развертывания безопасной многоаккаунтной среды AWS на основе лучших практик (AWS Landing Zone).",
    "desc_en": "Simplifies multi-account setup and governance by automatically provisioning a secure, well-architected multi-account AWS Landing Zone.",
    "key_points_ru": [
      "Автоматически настраивает AWS Organizations, IAM Identity Center, централизованные логи в CloudTrail и правила AWS Config",
      "Guardrails (защитные барьеры): обязательные и рекомендуемые правила управления безопасностью",
      "Account Factory: шаблон для автоматизированного создания новых стандартизированных учетных записей"
    ],
    "key_points_en": [
      "Automates creation of a multi-account Landing Zone using AWS best practices",
      "Enforces pre-packaged preventive and detective guardrails via SCPs and AWS Config rules",
      "Account Factory: provides automated, standardized provisioning of newly requested AWS accounts"
    ]
  },
  "aws_budgets": {
    "name": "AWS Budgets",
    "category": "Billing / Cost Management & Alerts",
    "desc_ru": "Инструмент для установки индивидуальных лимитов затрат и использования с отправкой оповещений при риске перерасхода бюджета.",
    "desc_en": "Allows you to set custom budgets to track your cost and usage from the simplest to the most complex use cases.",
    "key_points_ru": [
      "Типы бюджетов: бюджеты расходов (Cost), использования ресурсов (Usage) и покрытия Savings Plans / RI",
      "Оповещения: автоматическая отправка уведомлений по email или в SNS при достижении фактического или прогнозного лимита",
      "Budgets Actions: автоматическая остановка серверов или применение ограничивающих политик IAM при превышении бюджета"
    ],
    "key_points_en": [
      "Budget types: Cost budgets, Usage budgets, and Reservation / Savings Plans utilization and coverage",
      "Alerts: notifies teams via email or Amazon SNS when actual or forecasted spend crosses defined percentage thresholds",
      "Budgets Actions: automatically shuts down instances or applies restrictive IAM policies upon budget breach"
    ]
  },
  "aws_cost_explorer": {
    "name": "AWS Cost Explorer",
    "category": "Billing / Cost Analytics & Forecasting",
    "desc_ru": "Интерактивный графический инструмент для визуализации, анализа расходов и прогнозирования затрат на 12 месяцев вперед.",
    "desc_en": "Interactive tool that lets you visualize, understand, and manage your AWS costs and usage over time.",
    "key_points_ru": [
      "Хранит до 14 месяцев исторических данных с фильтрацией по сервисам, тегам, аккаунтам и регионам",
      "Прогнозирует расходы на следующие 12 месяцев на основе машинного обучения",
      "Предоставляет персонализированные рекомендации по покупке Savings Plans и Reserved Instances"
    ],
    "key_points_en": [
      "Provides up to 14 months of historical billing data with filtering by service, tag, linked account, and region",
      "Forecasts future spending patterns up to 12 months ahead using machine learning",
      "Delivers automated recommendations for purchasing optimal Compute Savings Plans and Reserved Instances"
    ]
  },
  "aws_pricing_calculator": {
    "name": "AWS Pricing Calculator",
    "category": "Billing / Cost Estimation",
    "desc_ru": "Бесплатный веб-калькулятор для моделирования архитектуры и предварительного расчета ежемесячных расходов до запуска ресурсов.",
    "desc_en": "Web-based planning tool that allows you to model proposed architectures and estimate AWS monthly costs prior to deployment.",
    "key_points_ru": [
      "Позволяет оценить затраты на планируемую инфраструктуру без регистрации и без создания реальных ресурсов",
      "Формирует подробную смету с разбивкой по сервисам и регионам",
      "Позволяет экспортировать расчет в PDF или поделиться ссылкой с коллегами"
    ],
    "key_points_en": [
      "Estimate proposed architecture costs without deploying live resources or requiring an AWS account",
      "Breaks down projected monthly expenses by service, usage metrics, and chosen AWS Regions",
      "Enables exporting transparent price estimates to PDF or sharing via unique URLs"
    ]
  },
  "amazon_sqs": {
    "name": "Amazon SQS (Simple Queue Service)",
    "category": "Application Integration / Message Queues",
    "desc_ru": "Полностью управляемый сервис очередей сообщений, позволяющий разделить компоненты приложения (декаплинг) для повышения надежности.",
    "desc_en": "Fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless apps.",
    "key_points_ru": [
      "Standard Queues: неограниченная пропускная способность, доставка сообщений как минимум один раз (at-least-once), порядок best-effort",
      "FIFO Queues: строгий порядок первого прихода (First-In-First-Out) и строго однократная обработка (exactly-once)",
      "Обеспечивает асинхронное взаимодействие и сглаживает пики нагрузки между сервисами"
    ],
    "key_points_en": [
      "Standard Queues: unlimited throughput, at-least-once message delivery, best-effort message ordering",
      "FIFO Queues: strict First-In-First-Out ordering and exactly-once processing with high throughput",
      "Decouples microservice components and buffers bursts in high-traffic architectures"
    ]
  },
  "amazon_sns": {
    "name": "Amazon SNS (Simple Notification Service)",
    "category": "Application Integration / Pub-Sub",
    "desc_ru": "Высокодоступный сервис обмена сообщениями по модели «издатель-подписчик» (Publish/Subscribe) и отправки push-уведомлений.",
    "desc_en": "Fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.",
    "key_points_ru": [
      "Модель Pub/Sub: издатель отправляет сообщение в Topic, а сервис мгновенно доставляет его всем подписчикам",
      "A2A подписчики: Amazon SQS, AWS Lambda, HTTP/S эндпоинты, EventBridge",
      "A2P уведомления: отправка SMS, Email и мобильных Push-уведомлений конечным пользователям"
    ],
    "key_points_en": [
      "Pub/Sub pattern: publishers publish messages to Topics, which immediately fan out to multiple subscribers",
      "A2A subscribers: Amazon SQS queues, AWS Lambda functions, EventBridge, and HTTP/S webhooks",
      "A2P notifications: push messages to people via SMS text messages, email, and mobile push notifications"
    ]
  },
  "amazon_eventbridge": {
    "name": "Amazon EventBridge",
    "category": "Application Integration / Event Bus",
    "desc_ru": "Бессерверная шина событий (Event Bus), упрощающая создание управляемых событиями архитектур (Event-Driven Architecture).",
    "desc_en": "Serverless event bus that makes it easy to build event-driven applications at scale using events generated from applications and AWS.",
    "key_points_ru": [
      "Перехватывает системные события сервисов AWS (например, «EC2 остановлен», «S3 файл загружен») и направляет их на обработку",
      "Поддерживает интеграцию с популярными сторонними SaaS-платформами (Datadog, PagerDuty, Zendesk, Salesforce)",
      "Включает планировщик EventBridge Scheduler для запуска регулярных задач по расписанию (cron)"
    ],
    "key_points_en": [
      "Ingests AWS service state changes (e.g. EC2 instance state transitions, S3 uploads) and triggers target actions",
      "Native out-of-the-box integration with third-party SaaS partners (Datadog, PagerDuty, Shopify, Zendesk)",
      "Includes EventBridge Scheduler for triggering scheduled cron tasks with millisecond precision"
    ]
  },
  "aws_step_functions": {
    "name": "AWS Step Functions",
    "category": "Application Integration / Workflows",
    "desc_ru": "Сервис визуальной оркестрации рабочих процессов и построения распределенных конечных автоматов для бессерверных приложений.",
    "desc_en": "Visual workflow orchestration service that lets you coordinate multiple AWS services into serverless state machines.",
    "key_points_ru": [
      "Оркестрирует цепочки вызовов AWS Lambda, ECS, Batch и SNS с обработкой ошибок и повторными попытками (retries)",
      "Standard Workflows: для длительных процессов (до 1 года) с гарантией строго однократного выполнения",
      "Express Workflows: для высоконагруженных транзакций длительностью до 5 минут с обработкой сотен тысяч событий/сек"
    ],
    "key_points_en": [
      "Coordinates multiple AWS services into visual multi-step workflows with built-in retries and error handling",
      "Standard Workflows: for long-running processes (up to 1 year) with exactly-once execution guarantees",
      "Express Workflows: for high-volume, event-driven processing workloads running up to 5 minutes"
    ]
  },
  "aws_cloudformation": {
    "name": "AWS CloudFormation",
    "category": "Management / Infrastructure as Code",
    "desc_ru": "Сервис «Инфраструктура как код» (IaC), позволяющий моделировать и развертывать все ресурсы AWS с помощью декларативных шаблонов JSON или YAML.",
    "desc_en": "Infrastructure as Code (IaC) service that lets you model, provision, and manage AWS and third-party resources declaratively.",
    "key_points_ru": [
      "Позволяет описывать полную архитектуру в текстовых файлах шаблонов и сохранять их в системах контроля версий (Git)",
      "CloudFormation Stacks: создание, обновление и удаление связанных ресурсов как единого целого",
      "Сам сервис CloudFormation бесплатен — оплачиваются только созданные им ресурсы"
    ],
    "key_points_en": [
      "Allows entire architectures to be declared in YAML or JSON templates and managed under Git version control",
      "CloudFormation Stacks: manage collections of related AWS resources as a single atomic unit",
      "Free service provided by AWS; customers pay only for the resources provisioned by the template"
    ]
  },
  "amazon_athena": {
    "name": "Amazon Athena",
    "category": "Analytics / Serverless SQL",
    "desc_ru": "Бессерверный интерактивный сервис запросов, позволяющий анализировать данные напрямую в Amazon S3 с помощью стандартного SQL.",
    "desc_en": "Serverless, interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL.",
    "key_points_ru": [
      "Не требует настройки серверов или загрузки данных в базу данных; запросы выполняются прямо по файлам CSV, JSON, Parquet в S3",
      "Оплата строго за объем просканированных данных ($5 за 1 ТБ)",
      "Часто используется для анализа детальных отчетов биллинга AWS CUR, логов CloudTrail и логов VPC Flow Logs"
    ],
    "key_points_en": [
      "Serverless; queries unstructured and semi-structured data directly in Amazon S3 without loading into a database",
      "Pay only for the queries run, billed based on the amount of data scanned ($5 per TB scanned)",
      "Standard tool for querying AWS Cost and Usage Reports (CUR), CloudTrail logs, and VPC Flow Logs"
    ]
  },
  "aws_glue": {
    "name": "AWS Glue",
    "category": "Analytics / Serverless ETL",
    "desc_ru": "Бессерверный сервис интеграции данных и ETL (Extract, Transform, Load), упрощающий подготовку данных для аналитики.",
    "desc_en": "Serverless data integration service that makes it easy to discover, prepare, and combine data for analytics and machine learning.",
    "key_points_ru": [
      "AWS Glue Data Catalog: центральный метарепозиторий для хранения схем таблиц озер данных (Data Lake)",
      "Glue Crawlers: автоматическое сканирование файлов в S3 для определения схемы и типов данных",
      "Генерирует код трансформации данных на Python и Scala на базе Apache Spark"
    ],
    "key_points_en": [
      "AWS Glue Data Catalog: centralized metadata repository storing table schemas across Amazon S3 data lakes",
      "Glue Crawlers: automatically scan datasets in Amazon S3 to infer schemas and populate catalog tables",
      "Generates and runs serverless data extraction, transformation, and loading (ETL) pipelines using Apache Spark"
    ]
  },
  "amazon_workspaces": {
    "name": "Amazon WorkSpaces",
    "category": "End User Computing / DaaS",
    "desc_ru": "Управляемый сервис виртуальных рабочих столов в облаке (Desktop as a Service — DaaS), предоставляющий сотрудникам удаленные десктопы Windows или Linux.",
    "desc_en": "Fully managed virtual desktop-as-a-service (DaaS) solution enabling users to access Windows and Linux desktops from anywhere.",
    "key_points_ru": [
      "Полноценный виртуальный рабочий стол с доступом с ПК, Mac, iPad, Android и веб-браузеров",
      "Корпоративная безопасность: данные не сохраняются на локальных устройствах пользователей",
      "Интеграция с корпоративным каталогом Active Directory и поддержка шифрования дисков и MFA"
    ],
    "key_points_en": [
      "Complete cloud desktop experience accessible from Windows, Mac, iPad, Android, and web browsers",
      "Enhanced security: corporate data is stored in the AWS Cloud, not on local physical user devices",
      "Seamless integration with Microsoft Active Directory, disk volume encryption, and MFA"
    ]
  }
}

for k, v in MORE_SERVICES.items():
    services[k] = v

print(f"Updated dictionary total services: {len(services)}")
with open('data/services_info.json', 'w', encoding='utf-8') as f:
    json.dump(services, f, ensure_ascii=False, indent=2)
print("Successfully written exhaustive services dictionary!")
