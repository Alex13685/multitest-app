# -*- coding: utf-8 -*-
"""
Builder for CLF-C02 Domain 4: Billing, Pricing, and Support (72 questions)
100% compliant with question_schema.json, bilingual EN/RU, Jon Bonso style with why_incorrect.
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 72 Core CLF-C02 Scenarios for Domain 4
BILLING_DATA = [
    # Support Plans (1-18)
    ("clf_bill_001", 2,
     "A company needs 24/7 phone access to Cloud Support Engineers and a response time under 15 minutes for business-critical system down events. Which AWS Support plan is required?",
     "Компании требуется круглосуточный телефонный доступ к инженерам техподдержки и время ответа менее 15 минут при отказе критических систем. Какой план поддержки AWS необходим?",
     "Enterprise Support", "Enterprise Support",
     "Enterprise Support provides 24/7 phone, chat, and email support with a <15 min response time for business-critical system down events, plus a designated TAM.",
     "Enterprise Support предоставляет доступ 24/7 по телефону, чату и почте с временем ответа <15 мин при отказе критических систем и выделенного TAM.",
     [
         ("Business Support", "Business Support", "Business Support has a 1-hour response time for production down and does not include <15 min response time or a designated TAM.", "Business Support гарантирует ответ в течение 1 часа при сбое продакшена и не дает персонального TAM."),
         ("Enterprise On-Ramp", "Enterprise On-Ramp", "Enterprise On-Ramp provides a 30-minute response time and a pool of TAMs, not a designated TAM or 15-minute response.", "Enterprise On-Ramp дает ответ до 30 минут и пул консультантов TAM вместо персонального выделенного TAM."),
         ("Developer Support", "Developer Support", "Developer Support only offers email support during business hours with 12-24 hour response times.", "Developer Support предоставляет поддержку только по email в рабочие часы с временем ответа 12-24 ч.")
     ],
     ["aws_support", "aws_enterprise_support"]),

    ("clf_bill_002", 1,
     "A startup wants technical support via email during business hours with general architecture guidance. What is the lowest-cost paid AWS Support plan available?",
     "Стартапу требуется техподдержка по email в рабочие часы и общие архитектурные консультации. Какой самый недорогой платный план поддержки AWS доступен?",
     "Developer Support", "Developer Support",
     "Developer Support starts at $29/month and provides business-hours email access to Cloud Support Associates along with architectural building blocks guidance.",
     "Developer Support стоит от $29/мес и дает доступ к инженерам поддержки по email в рабочие часы и базовые архитектурные консультации.",
     [
         ("Basic Support", "Basic Support", "Basic Support is free and does not include access to technical support engineers or 1-on-1 architecture advice.", "Basic Support бесплатен, но не включает доступ к инженерам техподдержки и консультациям."),
         ("Business Support", "Business Support", "Business Support starts at $100/month and offers 24/7 phone/chat access, which exceeds the startup's requirements.", "Business Support стоит от $100/мес и ориентирован на круглосуточные продакшен-нагрузки."),
         ("Enterprise Support", "Enterprise Support", "Enterprise Support starts at $15,000/month and is intended for large-scale enterprise deployments.", "Enterprise Support стоит от $15 000/мес и предназначен для крупных корпоративных сред.")
     ],
     ["aws_support", "aws_developer_support"]),

    ("clf_bill_003", 2,
     "Which architectural advisory and launch preparation program is included with Enterprise Support and available for purchase with Business Support?",
     "Какая программа архитектурного планирования и подготовки к масштабным событиям включена в Enterprise Support и доступна для платного заказа в Business Support?",
     "AWS Infrastructure Event Management (IEM)", "AWS Infrastructure Event Management (IEM)",
     "AWS Infrastructure Event Management (IEM) offers guidance and real-time support during product launches, marketing campaigns, or migrations.",
     "AWS Infrastructure Event Management (IEM) обеспечивает сопровождение и аудит архитектуры при запуске продуктов, распродажах и масштабных миграциях.",
     [
         ("AWS Trusted Advisor", "AWS Trusted Advisor", "AWS Trusted Advisor is an automated tool that provides best-practice recommendations, not personalized event management.", "Trusted Advisor — это автоматизированный сервис рекомендаций, а не программа ручного сопровождения запуска."),
         ("AWS Concierge Support", "AWS Concierge Support", "Concierge Support assists only with billing and account administration inquiries.", "Concierge Support помогает исключительно с вопросами счетов и биллинга."),
         ("AWS Well-Architected Tool", "AWS Well-Architected Tool", "The Well-Architected Tool is a self-service assessment framework, not an operational event support team.", "Well-Architected Tool — это инструмент самостоятельной оценки архитектуры по опросникам.")
     ],
     ["aws_support", "aws_infrastructure_event_management"]),

    ("clf_bill_004", 1,
     "Which AWS team is dedicated to assisting Enterprise Support customers with billing, invoices, and payment inquiries?",
     "Какая специализированная команда AWS помогает клиентам Enterprise Support с вопросами биллинга, счетов и оплаты?",
     "AWS Concierge Support Team", "AWS Concierge Support Team",
     "The AWS Concierge Support team consists of billing and account experts dedicated to answering invoicing, billing, and account management queries.",
     "AWS Concierge Support Team — это команда экспертов по биллингу, которая решает вопросы счетов, оплаты и консолидации затрат для корпоративных клиентов.",
     [
         ("Technical Account Manager (TAM)", "Technical Account Manager (TAM)", "A TAM provides technical architecture and proactive operational guidance, not billing invoice support.", "TAM отвечает за техническую архитектуру и стабильность систем, а не за бухгалтерские счета."),
         ("AWS Trust & Safety", "AWS Trust & Safety", "AWS Trust & Safety deals with abusive activities such as phishing, spam, and DoS attacks originating from AWS.", "AWS Trust & Safety расследует инциденты безопасности и сетевые злоупотребления (спам, фишинг)."),
         ("AWS Partner Solutions Architects", "AWS Partner Solutions Architects", "Partner SAs help APN partners build architectures, not end-user billing disputes.", "Partner Solutions Architects работают с компаниями-партнерами APN, а не со счетами клиентов.")
     ],
     ["aws_support", "aws_concierge_support"]),

    ("clf_bill_005", 2,
     "Which checks are included with the free AWS Basic Support plan within AWS Trusted Advisor?",
     "Какие проверки AWS Trusted Advisor доступны клиентам на бесплатном плане AWS Basic Support?",
     "7 Core checks (Security and Service Limits)", "7 базовых проверок (Security и Service Limits)",
     "Basic Support customers receive 7 core Trusted Advisor checks (including S3 open bucket permissions, MFA on root, IAM password policy, and common service limits).",
     "Клиенты Basic Support получают 7 базовых проверок Trusted Advisor (открытые S3 бакеты, MFA на root, политика паролей IAM и базовые лимиты сервисов).",
     [
         ("All 5 categories with 100+ checks", "Все 5 категорий и 100+ проверок", "Full checks across all 5 categories require Business, Enterprise On-Ramp, or Enterprise Support.", "Полный набор проверок по всем 5 категориям требует плана Business, Enterprise On-Ramp или Enterprise."),
         ("Only Cost Optimization checks", "Только проверки оптимизации затрат", "Cost Optimization checks are only available on Business and Enterprise Support tiers.", "Проверки оптимизации затрат доступны только на платных тарифах Business и выше."),
         ("Performance and Fault Tolerance checks only", "Только проверки производительности и отказоустойчивости", "Performance and Fault Tolerance checks require Business Support or higher.", "Проверки производительности и отказоустойчивости требуют плана Business Support или выше.")
     ],
     ["aws_trusted_advisor", "aws_support"]),

    ("clf_bill_006", 1,
     "A company needs a primary technical point of contact who provides proactive architectural advice, organizes Well-Architected reviews, and coordinates support escalations. Which role fulfills this in Enterprise Support?",
     "Компании требуется главный технический консультант, предоставляющий проактивные архитектурные рекомендации, организующий обзоры Well-Architected и координирующий запросы в поддержку. Какая роль выполняет это в Enterprise Support?",
     "Technical Account Manager (TAM)", "Technical Account Manager (TAM)",
     "A Technical Account Manager (TAM) is a designated technical advisor assigned to Enterprise Support customers to deliver proactive guidance and operational health reviews.",
     "Technical Account Manager (TAM) — это персональный технический консультант в рамках Enterprise Support, помогающий планировать архитектуру и координировать поддержку.",
     [
         ("Cloud Support Associate", "Cloud Support Associate", "Cloud Support Associates handle initial ticket triage and reactive support, not dedicated strategic advisory.", "Cloud Support Associates обрабатывают тикеты реактивно и не ведут персональную стратегическую работу."),
         ("AWS Concierge", "AWS Concierge", "AWS Concierge handles billing and billing account management, not technical architecture.", "AWS Concierge решает вопросы биллинга и счетов, а не архитектуры."),
         ("Solutions Architect from AWS Training", "Solutions Architect from AWS Training", "Training instructors deliver educational courses, not ongoing designated enterprise support.", "Инструкторы проводят курсы обучения, но не ведут поддержку учетных записей.")
     ],
     ["aws_support", "aws_tam"]),

    ("clf_bill_007", 2,
     "What is the guaranteed response time for a production system outage (production down) under the AWS Business Support plan?",
     "Каково гарантированное время первого ответа при сбое производственной системы (production down) на плане AWS Business Support?",
     "< 1 hour", "< 1 часа",
     "Under AWS Business Support, production system down incidents have a guaranteed response time of less than 1 hour.",
     "В тарифе AWS Business Support время реакции на сбой производственной системы (production down) составляет менее 1 часа.",
     [
         ("< 15 minutes", "< 15 минут", "< 15 minute response time for business-critical system down is exclusive to Enterprise Support.", "Время реакции менее 15 минут при отказе критических систем предоставляется только в Enterprise Support."),
         ("< 4 hours", "< 4 часов", "< 4 hours is the response time for production system impaired (not system down).", "< 4 часов — это время реакции на ухудшение работы (impaired), а не полный отказ системы."),
         ("< 12 hours", "< 12 часов", "< 12 hours is the SLA for general system guidance.", "< 12 часов — это время ответа на общие вопросы по системе (general guidance).")
     ],
     ["aws_support", "aws_business_support"]),

    ("clf_bill_008", 2,
     "What is the guaranteed response time for a business-critical system failure under the AWS Enterprise On-Ramp Support plan?",
     "Каково гарантированное время ответа при критическом отказе бизнес-системы (business-critical down) в плане AWS Enterprise On-Ramp Support?",
     "< 30 minutes", "< 30 минут",
     "AWS Enterprise On-Ramp offers a response time of < 30 minutes for business-critical system down events, handled by senior engineers.",
     "В плане AWS Enterprise On-Ramp время реакции на критический сбой системы (business-critical down) составляет менее 30 минут.",
     [
         ("< 15 minutes", "< 15 минут", "< 15 minutes is available only on the Enterprise Support plan.", "< 15 минут доступно только на максимальном плане Enterprise Support."),
         ("< 1 hour", "< 1 часа", "< 1 hour is the production system down response time for Business Support.", "< 1 час — это время ответа при отказе продакшена в плане Business Support."),
         ("< 2 hours", "< 2 часов", "There is no standard AWS Support SLA of 2 hours for critical incidents.", "В SLA поддержки AWS нет 2-часового норматива для критических инцидентов.")
     ],
     ["aws_support", "aws_enterprise_on_ramp"]),

    ("clf_bill_009", 1,
     "Which communication channels are available to contact technical support on the AWS Business Support plan?",
     "Какие каналы связи доступны для обращения в техническую поддержку на плане AWS Business Support?",
     "24/7 Phone, Chat, and Web ticketing system", "Телефон, чат и веб-тикеты 24/7",
     "Business Support customers have 24/7 access to Cloud Support Engineers via phone, live chat, and web-based case management.",
     "Клиенты Business Support имеют круглосуточный доступ 24/7 к инженерам техподдержки по телефону, в онлайн-чате и через тикет-систему.",
     [
         ("Email only during business hours", "Только email в рабочие часы", "Email-only support during business hours is a limitation of Developer Support.", "Поддержка только по email в рабочие часы — это ограничение тарифа Developer Support."),
         ("Web ticketing only", "Только веб-тикеты", "Business Support includes real-time phone and chat in addition to web tickets.", "План Business включает онлайн-чат и телефон помимо создания веб-тикетов."),
         ("Physical on-site engineer visits", "Выезд инженера в офис компании", "AWS does not provide on-site technical engineer visits as part of standard support plans.", "AWS не предоставляет физических выездов инженеров на площадку заказчика в рамках стандартных планов поддержки.")
     ],
     ["aws_support", "aws_business_support"]),

    ("clf_bill_010", 2,
     "Which AWS tool alerts customers when systems are impacted by AWS-wide outages or scheduled maintenance for services they actively use?",
     "Какой сервис AWS уведомляет клиентов о глобальных сбоях инфраструктуры AWS или плановом техобслуживании именно тех сервисов, которые они используют?",
     "AWS Health Dashboard", "AWS Health Dashboard",
     "The AWS Health Dashboard provides personalized alerts and remediation guidance when AWS is experiencing issues that affect specific customer resources.",
     "AWS Health Dashboard предоставляет персонализированные оповещения и рекомендации, если возникают проблемы или работы, затрагивающие ресурсы конкретного аккаунта.",
     [
         ("AWS Service Catalog", "AWS Service Catalog", "AWS Service Catalog allows organizations to manage catalogs of approved IT services, not operational health.", "AWS Service Catalog управляет каталогом разрешенных IT-шаблонов, а не мониторингом сбоев инфраструктуры."),
         ("Amazon CloudWatch", "Amazon CloudWatch", "CloudWatch monitors user-deployed metrics and logs, but does not provide AWS infrastructure health advisories.", "CloudWatch отслеживает метрики ваших приложений, но не формирует официальные бюллетени статуса дата-центров AWS."),
         ("AWS Cost Explorer", "AWS Cost Explorer", "Cost Explorer analyzes historical and forecasted billing expenditures.", "Cost Explorer анализирует исторические и прогнозируемые финансовые расходы.")
     ],
     ["aws_health_dashboard", "aws_support"]),

    # Cost Management & Forecasting (11-30)
    ("clf_bill_011", 1,
     "A company needs to visualize, understand, and manage its AWS costs and usage over time, and forecast future spend for the next 12 months. Which service should they use?",
     "Компании необходимо визуализировать, анализировать и прогнозировать расходы и использование AWS на следующие 12 месяцев. Какой сервис следует использовать?",
     "AWS Cost Explorer", "AWS Cost Explorer",
     "AWS Cost Explorer allows you to view historical data (up to the last 14 months), analyze spending trends, and forecast spending for the next 12 months.",
     "AWS Cost Explorer позволяет просматривать исторические данные (до 14 месяцев назад), анализировать тренды и прогнозировать затраты на 12 месяцев вперед.",
     [
         ("AWS Budgets", "AWS Budgets", "AWS Budgets sets custom spending alerts when costs exceed thresholds, but Cost Explorer is the primary visual analytical tool.", "AWS Budgets настраивает оповещения при превышении порогов, но инструментом графического анализа и прогноза является Cost Explorer."),
         ("AWS Pricing Calculator", "AWS Pricing Calculator", "The Pricing Calculator estimates costs before deploying resources, but cannot analyze actual historical spend.", "Pricing Calculator оценивает затраты до развертывания ресурсов, но не анализирует реальные счета."),
         ("AWS Cost and Usage Report (CUR)", "AWS Cost and Usage Report (CUR)", "CUR produces raw, granular CSV/Parquet files in S3, not an out-of-the-box visual interactive chart with forecasting.", "CUR выгружает сырые детализированные файлы CSV/Parquet в S3, а не интерактивные графики с прогнозом из коробки.")
     ],
     ["aws_cost_explorer", "aws_budgets"]),

    ("clf_bill_012", 2,
     "A DevOps lead wants to receive an automated notification via Amazon SNS and email whenever the forecasted monthly AWS bill exceeds $2,500. Which tool should be configured?",
     "DevOps-инженер хочет получать автоматические уведомления через SNS и email, когда прогнозируемый ежемесячный счет за AWS превысит $2 500. Какой инструмент следует настроить?",
     "AWS Budgets", "AWS Budgets",
     "AWS Budgets allows you to set custom budgets that track actual or forecasted costs and usage, and trigger notifications via SNS or email when thresholds are breached.",
     "AWS Budgets позволяет задавать лимиты затрат или использования (фактические и прогнозные) и отправлять уведомления через email/SNS при риске превышения бюджета.",
     [
         ("AWS Billing Conductor", "AWS Billing Conductor", "AWS Billing Conductor customizes billing rates and showback for end-customers or internal business units.", "Billing Conductor настраивает кастомные тарифные сетки и взаиморасчеты с субклиентами."),
         ("AWS Cost Anomaly Detection", "AWS Cost Anomaly Detection", "Cost Anomaly Detection uses machine learning to identify unexpected spikes, but does not track threshold budgets against a dollar limit.", "Cost Anomaly Detection ищет аномальные скачки с помощью ML, но не служит инструментом задания фиксированного месячного лимита."),
         ("AWS Trusted Advisor", "AWS Trusted Advisor", "Trusted Advisor provides general recommendations, but does not provide custom forecasted threshold budgeting alerts.", "Trusted Advisor выдает рекомендации, но не предоставляет гибкого механизма оповещений по плановому лимиту бюджета.")
     ],
     ["aws_budgets", "aws_cost_explorer"]),

    ("clf_bill_013", 1,
     "A company needs to estimate the cost of moving a planned architecture to AWS before launching any actual resources. Which web-based tool should they use?",
     "Компании необходимо оценить стоимость переноса планируемой архитектуры в AWS до фактического запуска каких-либо ресурсов. Какой веб-инструмент следует использовать?",
     "AWS Pricing Calculator", "AWS Pricing Calculator",
     "AWS Pricing Calculator is a free web-based planning tool that allows you to model proposed architectures and estimate AWS monthly costs prior to deployment.",
     "AWS Pricing Calculator — это бесплатный веб-калькулятор, позволяющий смоделировать проектируемую архитектуру и рассчитать ежемесячные расходы до развертывания ресурсов.",
     [
         ("AWS Cost Explorer", "AWS Cost Explorer", "Cost Explorer analyzes existing, deployed infrastructure costs, not hypothetical pre-deployment architectures.", "Cost Explorer анализирует уже существующие затраты по факту использования, а не гипотетические планы."),
         ("AWS Budgets", "AWS Budgets", "AWS Budgets tracks active account spending against defined limits.", "AWS Budgets отслеживает фактический биллинг активного аккаунта."),
         ("AWS Application Discovery Service", "AWS Application Discovery Service", "Application Discovery Service inventories on-premises servers, but does not provide an interactive AWS service pricing calculation.", "Application Discovery Service собирает данные о серверах в on-premise дата-центре, но не рассчитывает онлайн-смету AWS сервисов.")
     ],
     ["aws_pricing_calculator", "aws_cost_explorer"]),

    ("clf_bill_014", 2,
     "Which AWS billing deliverable provides the most granular, detailed raw metadata about hourly resource usage, cost allocation tags, and pricing rates?",
     "Какой инструмент AWS формирует наиболее детализированные сырые данные с почасовым учетом использования каждого ресурса, тегов и тарифных ставок?",
     "AWS Cost and Usage Report (CUR)", "AWS Cost and Usage Report (CUR)",
     "The AWS Cost and Usage Report (CUR) provides the most detailed billing data available, delivering hourly line items to an Amazon S3 bucket for analysis with Amazon Athena or Amazon QuickSight.",
     "AWS Cost and Usage Report (CUR) — самый подробный отчет о расходах, выгружающий почасовую детализацию в S3 для анализа с помощью Athena или QuickSight.",
     [
         ("AWS Monthly Bill PDF", "AWS Monthly Bill PDF", "The monthly PDF bill is a high-level summary invoice without hourly granular line items.", "Ежемесячный PDF-счет содержит сводные данные и не дает почасовой детализации."),
         ("AWS Budgets Report", "AWS Budgets Report", "Budgets reports summarize budget status, not exhaustive per-resource hourly usage logs.", "Отчеты Budgets суммируют выполнение бюджетов, а не сырые лог-записи биллинга."),
         ("AWS Billing Dashboard", "AWS Billing Dashboard", "The Billing Dashboard provides summary widgets, but cannot match the raw per-attribute granularity of CUR.", "Billing Dashboard отображает графические виджеты, но не предоставляет сырых данных с точностью до вызова.")
     ],
     ["aws_cur", "aws_cost_explorer"]),

    ("clf_bill_015", 1,
     "How can a company organize and allocate AWS costs across different departments, cost centers, or development environments (e.g., Dev, Staging, Prod)?",
     "Как компания может организовать и распределить затраты на AWS между различными отделами, центрами затрат или средами разработки (Dev, Staging, Prod)?",
     "Activate Cost Allocation Tags", "Активировать Cost Allocation Tags (теги распределения затрат)",
     "Cost Allocation Tags (user-defined or AWS-generated) can be attached to resources and activated in the Billing console to track and categorize costs by department, environment, or project.",
     "Cost Allocation Tags позволяют размечать ресурсы пользовательскими или системными тегами и активировать их в консоли биллинга для группировки расходов по проектам и отделам.",
     [
         ("Use AWS Secrets Manager", "Использовать AWS Secrets Manager", "Secrets Manager manages database passwords and API tokens, not billing cost classification.", "Secrets Manager управляет секретами и паролями приложений, а не учетом финансов."),
         ("Configure Security Group rules", "Настроить правила Security Group", "Security Groups are virtual firewalls that filter network traffic, having no effect on billing categorization.", "Security Group — это сетевой файрвол для инстансов, не связанный с финансовой аналитикой."),
         ("Create multiple IAM Roles", "Создать несколько ролей IAM", "IAM Roles grant temporary security permissions, not cost categorization metadata.", "IAM-роли выдают права доступа, а не группируют расходы.")
     ],
     ["aws_cost_allocation_tags", "aws_cost_explorer"]),

    ("clf_bill_016", 2,
     "A company uses machine learning to identify unexpected cost spikes, unusual resource provisioning, and root causes of billing abnormalities. Which service provides this automatically?",
     "Компания хочет автоматически выявлять непредвиденные скачки расходов, аномалии в использовании ресурсов и причины перерасхода с помощью машинного обучения. Какой сервис решает эту задачу?",
     "AWS Cost Anomaly Detection", "AWS Cost Anomaly Detection",
     "AWS Cost Anomaly Detection uses advanced machine learning models to continuously monitor your cost and usage patterns, detect anomalous spend, and identify the root cause.",
     "AWS Cost Anomaly Detection использует машинное обучение для непрерывного анализа расходов, раннего выявления аномалий и определения первопричин скачков затрат.",
     [
         ("AWS Pricing Calculator", "AWS Pricing Calculator", "The Pricing Calculator models future spend, not real-time cost anomaly analysis.", "Pricing Calculator рассчитывает предварительную смету, а не анализирует реальные аномалии."),
         ("AWS Systems Manager", "AWS Systems Manager", "Systems Manager manages server configurations and patching, not financial anomaly analytics.", "Systems Manager управляет серверами и патчингом, а не поиском финансовых отклонений."),
         ("AWS Shield Advanced", "AWS Shield Advanced", "Shield Advanced protects against DDoS attacks, not billing anomalies.", "Shield Advanced защищает от сетевых DDoS-атак, а не от непредвиденных трат.")
     ],
     ["aws_cost_anomaly_detection", "aws_cost_explorer"]),

    # Organizations & Consolidated Billing (31-50)
    ("clf_bill_017", 1,
     "What is a primary financial benefit of using Consolidated Billing in AWS Organizations?",
     "В чем заключается основное финансовое преимущество использования Consolidated Billing (консолидированного биллинга) в AWS Organizations?",
     "Aggregated usage across all linked accounts to qualify for tiered volume discounts", "Объединение объемов использования всех связанных аккаунтов для получения оптовых скидок за объем (volume discounts)",
     "Consolidated Billing aggregates the usage of all member accounts in the organization, allowing the company to reach higher volume discount tiers for services like Amazon S3 and data transfer.",
     "Consolidated Billing суммирует потребление всех связанных аккаунтов организации, позволяя быстрее достигать более дешевых ступеней тарификации (volume discounts) для S3 и трафика.",
     [
         ("Free unlimited compute capacity for member accounts", "Бесплатные неограниченные вычислительные ресурсы для дочерних аккаунтов", "Consolidated Billing does not provide free compute resources; it only aggregates billing calculations.", "Консолидированный биллинг объединяет счета, но не делает вычислительные ресурсы бесплатными."),
         ("Automatic elimination of all outbound data transfer charges", "Автоматическое обнуление платы за весь исходящий интернет-трафик", "Outbound data transfer is still billed, though aggregated volume tiers may reduce the per-GB rate.", "Исходящий трафик остается платным, снижается лишь ставка за гигабайт при достижении оптовых объемов."),
         ("Replacement of IAM permissions with credit lines", "Замена прав доступа IAM на кредитные линии", "Consolidated billing affects only financial invoicing and payment, not IAM security authorization.", "Консолидированный биллинг относится к бухгалтерии, а не к управлению правами пользователей.")
     ],
     ["aws_organizations", "aws_consolidated_billing"]),

    ("clf_bill_018", 2,
     "In an AWS Organization with Consolidated Billing enabled, which account is responsible for paying all charges incurred by all member accounts?",
     "В AWS Organization с включенным Consolidated Billing какой аккаунт несет ответственность за оплату всех счетов, выставленных по дочерним аккаунтам?",
     "The Management (Payer) Account", "Management (Payer) Account (управляющий аккаунт)",
     "In AWS Organizations, the Management (Payer) account pays the single consolidated monthly invoice for all member (linked) accounts.",
     "В AWS Organizations управляющий аккаунт (Management Account) получает и оплачивает единый консолидированный счет за все дочерние аккаунты.",
     [
         ("Each Member Account independently", "Каждый Member Account независимо", "Member accounts do not pay AWS directly when Consolidated Billing is active; all charges roll up to the Management account.", "При включенном Consolidated Billing дочерние аккаунты не платят напрямую — все расходы консолидируются на основном счете."),
         ("The AWS Support Account", "Аккаунт техподдержки AWS Support Account", "There is no special 'Support Account' responsible for customer payments.", "Не существует отдельного аккаунта службы поддержки, оплачивающего клиентские счета."),
         ("The IAM Identity Center Master Account", "Мастер-аккаунт IAM Identity Center", "IAM Identity Center manages single sign-on authentication, not billing settlement.", "IAM Identity Center управляет входом пользователей (SSO), а не выставлением и оплатой счетов.")
     ],
     ["aws_organizations", "aws_consolidated_billing"]),

    ("clf_bill_019", 2,
     "Can Reserved Instance (RI) and Savings Plans discounts be shared across member accounts in an AWS Organization by default?",
     "Могут ли скидки Reserved Instances (RI) и Savings Plans по умолчанию распределяться между дочерними аккаунтами в AWS Organization?",
     "Yes, discount sharing is enabled by default across all accounts in the Organization", "Да, распределение скидок по умолчанию включено для всех аккаунтов организации",
     "By default, AWS Organizations enables discount sharing for Reserved Instances and Savings Plans across all member accounts in the organization, though it can be opted out in billing preferences.",
     "По умолчанию в AWS Organizations включен общий доступ к скидкам RI и Savings Plans: неиспользованные часы одного аккаунта автоматически покрывают инстансы другого.",
     [
         ("No, RIs can only be applied to the specific account that purchased them", "Нет, RI применяются только к тому аккаунту, в котором были куплены", "RI discounts can be shared across member accounts within the same consolidated billing family unless explicitly disabled.", "Скидки могут распределяться по всей семье аккаунтов, если это явно не отключено в настройках биллинга."),
         ("Only if all accounts are in the same AWS Region", "Только если все аккаунты находятся в одном регионе AWS", "RIs apply to matching instance usage in their target region regardless of which account owns them.", "Скидка применяется к подходящему инстансу в целевом регионе независимо от аккаунта."),
         ("Only for Enterprise Support customers", "Только для клиентов с тарифом Enterprise Support", "Discount sharing is a standard feature of Consolidated Billing available to all AWS Organizations tiers.", "Общий доступ к скидкам доступен всем организациям независимо от тарифного плана техподдержки.")
     ],
     ["aws_organizations", "aws_reserved_instances", "aws_savings_plans"]),

    ("clf_bill_020", 2,
     "A company needs to define custom pricing rules and allocate billing statements to internal cost centers or business units with custom billing rates. Which service provides this?",
     "Компании необходимо настроить индивидуальные тарифные сетки и формировать внутренние счета для подразделений с учетом кастомных наценок или скидок. Какой сервис решает эту задачу?",
     "AWS Billing Conductor", "AWS Billing Conductor",
     "AWS Billing Conductor is a customizable billing service that allows you to configure billing groups, create custom pricing rules, and generate customized showback/chargeback statements.",
     "AWS Billing Conductor позволяет настраивать правила тарификации, группировать аккаунты и формировать индивидуальные отчеты о расходах (showback/chargeback) для внутренних клиентов.",
     [
         ("AWS Cost Explorer", "AWS Cost Explorer", "Cost Explorer shows standard AWS billing rates and does not support custom rate modeling or markups.", "Cost Explorer показывает стандартные цены AWS и не поддерживает кастомные надбавки и тарифы."),
         ("AWS Budgets", "AWS Budgets", "AWS Budgets tracks threshold alerts, not customized billing rate tables.", "AWS Budgets отслеживает пороговые лимиты, но не пересчитывает тарифы."),
         ("AWS Control Tower", "AWS Control Tower", "Control Tower automates multi-account governance and landing zones, not custom billing billing rate transformation.", "Control Tower развертывает многоаккаунтную среду (Landing Zone), а не кастомные финансовые тарифные сетки.")
     ],
     ["aws_billing_conductor", "aws_cost_explorer"]),

    # Purchasing Options & Savings Plans (51-72)
    ("clf_bill_021", 1,
     "Which Amazon EC2 purchasing option provides the highest cost discount (up to 90%) in exchange for capacity that can be reclaimed by AWS with a 2-minute interruption notice?",
     "Какой вариант приобретения Amazon EC2 обеспечивает наибольшую скидку (до 90%) в обмен на готовность к прерыванию работы инстанса с предупреждением за 2 минуты?",
     "Spot Instances", "Spot Instances",
     "Amazon EC2 Spot Instances offer up to 90% savings compared to On-Demand by utilizing unused EC2 capacity, suitable for fault-tolerant and stateless workloads.",
     "Spot Instances предоставляют скидку до 90% от цены On-Demand за счет использования свободных мощностей дата-центров AWS, если приложение устойчиво к прерываниям.",
     [
         ("Reserved Instances", "Reserved Instances", "Reserved Instances offer up to 72% discount for a 1- or 3-year steady-state commitment, without capacity interruptions.", "Reserved Instances дают до 72% скидки за обязательство на 1-3 года и не прерываются."),
         ("On-Demand Instances", "On-Demand Instances", "On-Demand instances have no long-term commitment and are billed at full list price per second/hour.", "On-Demand оплачивается по полному тарифу без долгосрочных обязательств."),
         ("Dedicated Hosts", "Dedicated Hosts", "Dedicated Hosts provide dedicated physical servers for licensing compliance, typically at higher cost.", "Dedicated Hosts выделяют физический сервер целиком под лицензии заказчика и стоят дороже.")
     ],
     ["amazon_ec2", "ec2_spot_instances"]),

    ("clf_bill_022", 2,
     "Which pricing commitment model offers flexible discounts of up to 66% across Amazon EC2, AWS Lambda, and AWS Fargate usage regardless of instance family, size, OS, or Region?",
     "Какая модель ценовых обязательств дает скидку до 66% на Amazon EC2, AWS Lambda и AWS Fargate независимо от семейства инстансов, размера, ОС или региона?",
     "Compute Savings Plans", "Compute Savings Plans",
     "Compute Savings Plans provide the greatest flexibility, automatically applying discounts to EC2 instances (any family, OS, Region), AWS Fargate, and AWS Lambda.",
     "Compute Savings Plans дают максимальную гибкость: скидка до 66% автоматически покрывает любые инстансы EC2 (любое семейство, ОС, регион), а также контейнеры Fargate и функции Lambda.",
     [
         ("EC2 Instance Savings Plans", "EC2 Instance Savings Plans", "EC2 Instance Savings Plans provide up to 72% savings but require committing to a specific instance family in a specific Region.", "EC2 Instance Savings Plans привязаны к конкретному семейству инстансов в выбранном регионе."),
         ("Standard Reserved Instances", "Standard Reserved Instances", "Standard RIs apply only to EC2 instances in a specific region, not to Lambda or Fargate.", "Standard RI не распространяются на бессерверные вычисления Lambda и Fargate."),
         ("On-Demand Capacity Reservations", "On-Demand Capacity Reservations", "Capacity Reservations reserve compute capacity without providing any pricing discount.", "Capacity Reservations резервируют вычислительные мощности, но не предоставляют ценовой скидки.")
     ],
     ["aws_savings_plans", "amazon_ec2", "aws_lambda", "aws_fargate"]),

    ("clf_bill_023", 2,
     "What payment option for 1-year or 3-year Reserved Instances (RIs) or Savings Plans delivers the greatest overall discount percentage?",
     "Какой вариант первоначального платежа при покупке Reserved Instances (RI) или Savings Plans на 1 или 3 года обеспечивает максимальный процент скидки?",
     "All Upfront", "All Upfront (полная предоплата)",
     "The All Upfront payment option requires paying for the entire commitment duration in a single lump sum, delivering the highest overall discount compared to Partial Upfront or No Upfront.",
     "Вариант All Upfront предполагает единовременную 100% оплату всего срока (1 или 3 года), что гарантирует максимальный размер скидки по сравнению с Partial Upfront и No Upfront.",
     [
         ("No Upfront", "No Upfront", "No Upfront requires no immediate payment but provides the lowest discount tier among commitment options.", "No Upfront не требует аванса, но дает наименьший размер скидки."),
         ("Partial Upfront", "Partial Upfront", "Partial Upfront offers a middle ground between discount size and initial cash outlay.", "Partial Upfront представляет собой компромисс между скидкой и суммой предоплаты."),
         ("Monthly Invoicing with no commitment", "Ежемесячный счет без обязательств", "Monthly invoicing without commitment is On-Demand pricing with no discount.", "Оплата помесячно без обязательств — это стандартный тариф On-Demand без скидки.")
     ],
     ["aws_reserved_instances", "aws_savings_plans"]),

    ("clf_bill_024", 1,
     "Which digital catalog makes it easy for customers to find, test, buy, and deploy third-party software products and SaaS solutions that run on AWS, with unified billing on their AWS invoice?",
     "Какой онлайн-каталог позволяет находить, тестировать, приобретать и развертывать стороннее ПО и SaaS-решения, работающие на AWS, с оплатой через единый счет AWS?",
     "AWS Marketplace", "AWS Marketplace",
     "AWS Marketplace is a curated digital catalog of thousands of third-party software listings (AMI, SaaS, CloudFormation, Containers) billed directly to your AWS account.",
     "AWS Marketplace — это каталог проверенного стороннего программного обеспечения (AMI, SaaS, контейнеры), стоимость которого автоматически включается в единый ежемесячный счет AWS.",
     [
         ("AWS Service Catalog", "AWS Service Catalog", "AWS Service Catalog organizes internal approved IT service templates for internal enterprise users.", "Service Catalog упорядочивает внутренние корпоративные IT-шаблоны для сотрудников компании."),
         ("AWS CodeArtifact", "AWS CodeArtifact", "CodeArtifact is a secure artifact repository for software packages (npm, maven, pypi), not commercial licenses.", "CodeArtifact — это репозиторий пакетов зависимостей (npm, maven, pip), а не магазин готового ПО."),
         ("Amazon QuickSight", "Amazon QuickSight", "QuickSight is a cloud-native business intelligence data visualization tool.", "QuickSight — это сервис бизнес-аналитики и визуализации дашбордов.")
     ],
     ["aws_marketplace", "aws_billing"])
]

# We need 72 distinct questions for Domain 4.
# Let's expand BILLING_DATA systematically to 72 complete scenarios.
# Let's add remaining billing topics:
# - Free tier types (Always Free, 12 months, Trials)
# - Inbound vs Outbound data transfer
# - Intra-AZ vs Inter-AZ vs Inter-Region data transfer costs
# - S3 API call costs (PUT vs GET)
# - S3 Glacier retrieval costs
# - RDS Multi-AZ pricing (standby cost)
# - NAT Gateway hourly + per-GB data processing charge
# - Elastic IP idle fees
# - Route 53 hosted zone and query pricing
# - CloudFront free tier (1 TB free transfer per month)
# - DynamoDB on-demand vs provisioned capacity pricing
# - Lambda requests + duration (GB-seconds) pricing
# - EBS gp3 vs gp2 cost advantage
# - EBS snapshots incremental pricing
# - AWS Budgets Actions (IAM policy rollback, stop EC2)
# - Cost allocation tags limit and activation in Billing Console
# - AWS Price List API
# - AWS TCO calculation concepts
# - APN Consulting Partners vs APN Technology Partners

MORE_BILLING_TOPICS = [
    # Free Tier (25-30)
    ("clf_bill_025", 1,
     "Which AWS Free Tier category includes services that never expire and remain free indefinitely within specified usage limits (such as 1,000,000 AWS Lambda requests per month)?",
     "К какой категории AWS Free Tier относятся сервисы, бесплатный объем использования которых не имеет срока давности (например, 1 000 000 вызовов AWS Lambda в месяц)?",
     "Always Free", "Always Free (всегда бесплатно)",
     "The 'Always Free' tier includes offerings like 1M free Lambda requests, 25 GB of DynamoDB storage, and 10 CloudWatch metrics that never expire after 12 months.",
     "Категория 'Always Free' включает сервисы (1 млн вызовов Lambda, 25 ГБ в DynamoDB, 10 метрик CloudWatch), бесплатный лимит которых действует бессрочно.",
     [
         ("12 Months Free", "12 Months Free", "12 Months Free services (such as 750 hours of t2.micro/t3.micro EC2) expire exactly one year after initial account registration.", "12 Months Free действует только первые 12 месяцев после создания аккаунта."),
         ("Short-term Trials", "Short-term Trials", "Trials activate upon first service usage and expire after a short period (e.g., 30 or 60 days).", "Trials — это краткосрочные пробные периоды (напр. 30 дней) с момента активации сервиса."),
         ("Enterprise Credit Tier", "Enterprise Credit Tier", "There is no official 'Enterprise Credit Tier' in the AWS Free Tier program.", "В программе AWS Free Tier нет официальной категории 'Enterprise Credit Tier'.")
     ],
     ["aws_free_tier", "aws_lambda", "amazon_dynamodb"]),

    ("clf_bill_026", 1,
     "Which offering is available for 12 months free following new AWS account creation?",
     "Какое предложение входит в категорию '12 Months Free' после регистрации нового аккаунта AWS?",
     "750 hours per month of Linux or Windows t2.micro/t3.micro EC2 instance usage", "750 часов в месяц инстанса EC2 t2.micro/t3.micro (Linux или Windows)",
     "New AWS accounts receive 750 hours of t2.micro (or t3.micro in regions without t2) per month for the first 12 months.",
     "Новые аккаунты получают 750 часов инстанса t2.micro/t3.micro в месяц на протяжении первых 12 месяцев.",
     [
         ("Unlimited S3 Standard storage capacity", "Неограниченное хранилище S3 Standard", "S3 Free Tier provides 5 GB of standard storage for 12 months, not unlimited.", "В Free Tier включено 5 ГБ хранилища S3 Standard, а не неограниченный объем."),
         ("Free 24/7 Enterprise Support for 1 year", "Бесплатная поддержка Enterprise Support на 1 год", "Enterprise Support is a paid service and is never included in the AWS Free Tier.", "Enterprise Support — дорогой корпоративный тариф и не входит в Free Tier."),
         ("Free unlimited outbound Internet data transfer", "Бесплатный исходящий интернет-трафик без ограничений", "Only 100 GB of free internet egress is included across AWS services.", "Бесплатный исходящий интернет-трафик ограничен (до 100 ГБ/мес), а не безлимитен.")
     ],
     ["aws_free_tier", "amazon_ec2"]),

    # Data Transfer Economics (27-36)
    ("clf_bill_027", 1,
     "In AWS data transfer pricing, which data flow is generally free of charge?",
     "В правилах тарификации передачи данных AWS какой поток трафика, как правило, является бесплатным?",
     "Inbound data transfer from the Internet to AWS resources", "Входящий трафик из Интернета в сервисы AWS (Inbound Data Transfer)",
     "Inbound data transfer into AWS from the internet across virtually all services is completely free of charge.",
     "Входящий трафик из Интернета в сервисы AWS (ingress) абсолютно бесплатен для подавляющего большинства сервисов.",
     [
         ("Outbound data transfer from AWS to the Internet", "Исходящий трафик из AWS в Интернет", "Outbound data transfer from AWS to the Internet is billable per GB above the free tier.", "Исходящий трафик в Интернет тарифицируется за каждый гигабайт сверх бесплатного лимита."),
         ("Data transfer between different AWS Regions", "Передача данных между различными регионами AWS", "Inter-region data transfer incurs charges on both egress and ingress ends.", "Межрегиональная передача данных тарифицируется по стандартным расценкам между регионами."),
         ("Data transfer between Availability Zones across VPC peering", "Передача данных между зонами доступности (AZ) через VPC Peering", "Cross-AZ traffic within the same region incurs a nominal per-GB charge for each direction.", "Трафик между разными AZ внутри одного региона оплачивается за каждый гигабайт.")
     ],
     ["aws_pricing", "amazon_vpc"]),

    ("clf_bill_028", 2,
     "How does data transfer pricing behave between two EC2 instances located in the same AWS Region and in the same Availability Zone using private IP addresses?",
     "Как тарифицируется передача данных между двумя инстансами EC2, расположенными в одном регионе и в одной зоне доступности (AZ) при общении по приватным IP-адресам?",
     "Data transfer is completely free", "Передача данных полностью бесплатна",
     "Data transfer between AWS resources located in the same Availability Zone communicating via private IP addresses is free of charge.",
     "Передача данных между ресурсами в одной и той же Availability Zone по приватным IP-адресам бесплатна.",
     [
         ("Billed at $0.09 per GB", "Тарифицируется по $0.09 за ГБ", "Standard egress pricing applies to internet egress, not intra-AZ private communications.", "Тариф $0.09/ГБ применяется к исходящему трафику в Интернет, а не внутри одной зоны доступности."),
         ("Billed at standard cross-AZ rates", "Тарифицируется по стандартной ставке между зонами доступности", "Cross-AZ rates apply only when traffic crosses different Availability Zones.", "Межзональный тариф действует только если инстансы находятся в разных AZ."),
         ("Requires an active Direct Connect connection", "Требует наличия выделенного канала Direct Connect", "Direct Connect is a dedicated network connection from on-premises to AWS, not intra-AZ traffic.", "Direct Connect соединяет дата-центр клиента с AWS, а не инстансы внутри AZ.")
     ],
     ["amazon_ec2", "amazon_vpc", "aws_pricing"]),

    ("clf_bill_029", 2,
     "A company hosts media files in Amazon S3 and delivers them worldwide. Which service should they use to lower data transfer costs to end users while improving latency?",
     "Компания хранит медиафайлы в S3 и раздает их пользователям по всему миру. Какой сервис следует подключить, чтобы снизить расходы на исходящий трафик и уменьшить задержку?",
     "Amazon CloudFront", "Amazon CloudFront",
     "Data transfer out from Amazon S3 to Amazon CloudFront edge locations is free of charge, and CloudFront offers lower outbound rates to the internet compared to direct S3 egress, along with 1 TB free egress per month.",
     "Передача данных из S3 в CloudFront бесплатна, а исходящий трафик из CloudFront в Интернет стоит дешевле прямого выгруза из S3 (плюс 1 ТБ в месяц бесплатно).",
     [
         ("AWS Direct Connect", "AWS Direct Connect", "Direct Connect provides private leased lines from on-premises offices to AWS, not CDN delivery to global web users.", "Direct Connect соединяет корпоративный офис с AWS, а не кэширует контент для интернет-пользователей."),
         ("AWS Snowball Edge", "AWS Snowball Edge", "Snowball Edge is a physical data transport appliance, not an edge caching CDN.", "Snowball Edge — это физическое устройство для перевозки данных, а не CDN."),
         ("Amazon Route 53", "Amazon Route 53", "Route 53 is a DNS service and does not cache media assets or eliminate S3 data transfer egress costs.", "Route 53 — это DNS-сервис, он маршрутизирует домены, но не хранит кэш медиафайлов.")
     ],
     ["amazon_cloudfront", "amazon_s3", "aws_pricing"]),

    ("clf_bill_030", 2,
     "What causes an unexpected cost for an Amazon Elastic IP address?",
     "Что приводит к начислению платы за Elastic IP-адрес в аккаунте AWS?",
     "The Elastic IP address is allocated to the account but not associated with a running EC2 instance", "Elastic IP выделен аккаунту, но не привязан к работающему инстансу EC2 (простаивает)",
     "AWS imposes a small hourly charge for allocated Elastic IP addresses that are not associated with a running instance to prevent IP address hoarding.",
     "AWS начисляет небольшую почасовую плату за каждый выделенный Elastic IP, который не ассоциирован с запущенным инстансом, чтобы стимулировать освобождение неиспользуемых публичных IPv4-адресов.",
     [
         ("The Elastic IP is associated with an active running EC2 instance", "Elastic IP привязан к запущенному инстансу EC2", "One Elastic IP associated with a running EC2 instance historically incurs no idle fee.", "Один Elastic IP, привязанный к работающему инстансу, не облагается штрафом за простой."),
         ("The Elastic IP is located inside a private subnet", "Elastic IP размещен в приватной подсети", "Elastic IPs can only map to resources with internet gateway route tables.", "Elastic IP предназначен для публичного доступа через Internet Gateway."),
         ("The Elastic IP is used by AWS Shield Standard", "Elastic IP используется сервисом AWS Shield Standard", "Shield Standard provides automatic protection without altering IP billing rules.", "Shield Standard защищает ресурсы бесплатно и не влияет на правила Elastic IP.")
     ],
     ["amazon_vpc", "amazon_ec2", "aws_pricing"]),

    # Storage & Compute Pricing Models (31-45)
    ("clf_bill_031", 2,
     "Which Amazon S3 storage class automatically optimizes storage costs by moving objects between frequent and infrequent access tiers based on changing access patterns without operational overhead or retrieval fees?",
     "Какой класс хранилища Amazon S3 автоматически оптимизирует расходы, перемещая объекты между уровнями частого и редкого доступа без платы за извлечение и без ручного вмешательства?",
     "Amazon S3 Intelligent-Tiering", "Amazon S3 Intelligent-Tiering",
     "S3 Intelligent-Tiering monitors access patterns and automatically moves data between access tiers (Frequent, Infrequent, Archive Instant, Archive, Deep Archive) to minimize costs without retrieval fees.",
     "S3 Intelligent-Tiering отслеживает паттерны обращений и автоматически перемещает объекты между тирами (Frequent, Infrequent, Archive) без штрафов за выборку данных.",
     [
         ("Amazon S3 Standard-IA", "Amazon S3 Standard-IA", "Standard-IA is for data accessed less frequently but requires manual lifecycle rules and charges per-GB retrieval fees.", "Standard-IA требует настройки правил жизненного цикла и взимает плату за каждый извлеченный гигабайт."),
         ("Amazon S3 Glacier Flexible Archive", "Amazon S3 Glacier Flexible Archive", "Glacier is for long-term archiving with multi-hour retrieval times, not automatic tiering.", "Glacier — архивный класс с задержкой выборки от минут до часов, а не автоматический оптимизатор."),
         ("Amazon S3 One Zone-IA", "Amazon S3 One Zone-IA", "One Zone-IA stores data in a single AZ and does not provide automatic access pattern tiering.", "One Zone-IA хранит данные в одной зоне доступности и не оптимизирует тиры автоматически.")
     ],
     ["amazon_s3", "aws_pricing"]),

    ("clf_bill_032", 2,
     "What billing components make up the total monthly cost of using Amazon EBS gp3 volumes? (Select TWO)",
     "Из каких компонентов складывается ежемесячная стоимость использования томов Amazon EBS типа gp3? (Выберите ДВА)",
     ["Storage capacity provisioned (GB per month)", "Baseline and provisioned IOPS and throughput above free baseline thresholds"],
     ["Выделенный объем дискового пространства (ГБ в месяц)", "Выделенные IOPS и пропускная способность сверх базового лимита"],
     "EBS gp3 volumes bill for provisioned GB per month, with 3,000 IOPS and 125 MB/s throughput included free; additional provisioned IOPS and throughput are billed independently.",
     "Тома EBS gp3 тарифицируются за выделенный объем (ГБ в месяц), при этом 3000 IOPS и 125 МБ/с включены бесплатно, а дополнительные IOPS и пропускная способность оплачиваются отдельно.",
     [
         ("Number of files stored inside the filesystem", "Количество файлов, хранящихся в файловой системе", "EBS bills based on raw block capacity provisioned, regardless of how many files exist.", "EBS тарифицируется по выделенной блочной емкости, независимо от числа файлов."),
         ("Data transfer within the same Availability Zone", "Передача данных между EBS и EC2 внутри одной AZ", "Data transfer between an EC2 instance and its attached EBS volume in the same AZ is free.", "Обмен данными между инстансом EC2 и подключенным томом EBS внутри одной AZ бесплатен."),
         ("Operating system license fees for every attached volume", "Лицензионные сборы за операционную систему на каждом томе", "OS licenses are attached to the EC2 compute instance, not individual data EBS storage volumes.", "Лицензия на ОС привязана к инстансу EC2, а не к блочному диску EBS.")
     ],
     ["amazon_ebs", "amazon_ec2", "aws_pricing"]),

    ("clf_bill_033", 1,
     "How are AWS Lambda serverless execution costs calculated?",
     "Как рассчитывается стоимость выполнения серверлесс-функций в AWS Lambda?",
     "Number of requests and compute duration (measured in milliseconds allocated memory-time in GB-seconds)", "Количество вызовов (запросов) и время выполнения (в миллисекундах и ГБ-секундах выделенной памяти)",
     "AWS Lambda charges based on total requests ($0.20 per 1M requests) and compute duration measured in millisecond increments scaled by allocated RAM (GB-seconds).",
     "Lambda тарифицируется по количеству запросов ($0.20 за миллион) и времени работы функции (в миллисекундах), помноженному на объем выделенной оперативной памяти (GB-seconds).",
     [
         ("Fixed 24/7 server reservation fee", "Фиксированная абонентская плата за резервирование сервера 24/7", "Lambda is serverless; you pay nothing when your code is not running.", "Lambda — бессерверный сервис, вы платите 0, когда код не исполняется."),
         ("Storage capacity of the uploaded ZIP code file only", "Только размер загруженного ZIP-архива с кодом", "Lambda does not charge for code storage within normal limits; charges stem from invocations and execution time.", "Размер архива с кодом не является основной статьей расходов."),
         ("Number of lines of code executed", "Количество выполненных строк программного кода", "AWS Lambda does not count lines of code; it bills on duration and RAM.", "Lambda тарифицирует время и память, а не строки кода.")
     ],
     ["aws_lambda", "aws_pricing"]),

    ("clf_bill_034", 2,
     "A company needs to decide between Provisioned and On-Demand capacity modes for a new Amazon DynamoDB table. Which mode is most cost-effective for workloads with unpredictable or unknown traffic?",
     "Компании нужно выбрать режим емкости (Capacity Mode) для таблицы DynamoDB с непредсказуемым трафиком. Какой режим наиболее экономичен при внезапных всплесках нагрузки?",
     "On-Demand Capacity Mode", "On-Demand Capacity Mode (по требованию)",
     "DynamoDB On-Demand capacity mode charges strictly for read/write requests performed, making it ideal for unpredictable workloads where capacity planning is difficult.",
     "Режим On-Demand в DynamoDB тарифицирует исключительно выполненные операции чтения/записи, исключая переплату за неиспользуемые мощности при непредсказуемом трафике.",
     [
         ("Provisioned Capacity Mode without Auto Scaling", "Provisioned Capacity Mode без авто масштабирования", "Provisioned mode without auto-scaling requires paying for peak capacity 24/7 even during idle periods.", "Provisioned режим требует оплаты фиксированного пикового значения 24/7."),
         ("Dedicated DynamoDB Host Mode", "Dedicated DynamoDB Host Mode", "DynamoDB is a fully managed multi-tenant NoSQL service; dedicated hosts do not exist for DynamoDB.", "DynamoDB — бессерверная управляемая база данных, для нее не существует выделенных серверов (Dedicated Hosts)."),
         ("Spot Table Capacity", "Spot Table Capacity", "There is no 'Spot' capacity mode for Amazon DynamoDB.", "В DynamoDB нет понятия 'Spot'.")
     ],
     ["amazon_dynamodb", "aws_pricing"]),

    ("clf_bill_035", 2,
     "Which architectural factor increases the hourly cost of an Amazon RDS database deployment by approximately 100% to ensure high availability and automatic failover across data centers?",
     "Какая опция развертывания Amazon RDS увеличивает почасовую стоимость базы данных примерно вдвое ради обеспечения высокой доступности и автоматического переключения при сбое дата-центра?",
     "Enabling Multi-AZ deployment", "Включение Multi-AZ развертывания (Multi-AZ Deployment)",
     "Amazon RDS Multi-AZ synchronously replicates data to a standby replica in a second Availability Zone, which doubles instance and storage resource usage and cost.",
     "Опция Multi-AZ в Amazon RDS синхронно реплицирует данные на резервный инстанс в другой зоне доступности, удваивая стоимость ресурсов ради защиты от катастроф.",
     [
         ("Creating automated daily snapshots", "Создание ежедневных автоматических снапшотов", "Automated snapshots within the backup retention period up to 100% of database size are included at no extra cost.", "Снапшоты в пределах объема базы данных включены в стоимость без доплат."),
         ("Enabling Enhanced Monitoring", "Включение Enhanced Monitoring", "Enhanced Monitoring has minimal CloudWatch metrics cost, not a 100% database cost increase.", "Enhanced Monitoring генерирует небольшой трафик метрик CloudWatch, а не удваивает цену базы."),
         ("Using AWS Secrets Manager for credentials", "Использование Secrets Manager для паролей", "Secrets Manager costs $0.40/month per secret, not doubling the RDS instance cost.", "Secrets Manager стоит фиксированные $0.40 в месяц за секрет.")
     ],
     ["amazon_rds", "aws_pricing"]),

    # TCO, CAF, Migration & Well-Architected Cost (46-60)
    ("clf_bill_036", 1,
     "Which financial concept describes transitioning from large upfront infrastructure investments (CAPEX) in physical data centers to ongoing pay-as-you-go operational expenses (OPEX)?",
     "Какая финансовая концепция описывает переход от крупных единовременных капитальных вложений в дата-центры (CAPEX) к гибким переменным операционным расходам (OPEX)?",
     "Trading Capital Expense (CAPEX) for Variable Operating Expense (OPEX)", "Замена капитальных затрат (CAPEX) переменными операционными расходами (OPEX)",
     "One of the 6 core advantages of cloud computing is trading capital expense (heavy upfront physical data center purchases) for low, pay-as-you-go variable operating expenses.",
     "Одно из главных преимуществ облака — замена фиксированных капитальных затрат (CAPEX) на переменные операционные расходы (OPEX) по модели pay-as-you-go.",
     [
         ("Maximizing Capital Depreciation", "Максимизация амортизации капитала", "Cloud computing eliminates hardware ownership and associated multi-year asset depreciation schedules.", "В облаке нет физического оборудования на балансе и многолетней амортизации серверов."),
         ("Fixed Capacity Over-provisioning", "Избыточное резервирование фиксированных мощностей", "Over-provisioning is an on-premises antipattern that cloud elasticity is designed to eliminate.", "Избыточная закупка мощностей впрок — это недостаток традиционных дата-центров, устраняемый облачной эластичностью."),
         ("Static Infrastructure Amortization", "Статическая амортизация инфраструктуры", "Static amortization is an on-premises accounting concept not applicable to on-demand cloud services.", "Статическая амортизация относится к покупке физического 'железа'.")
     ],
     ["cloud_economics", "aws_pricing"]),

    ("clf_bill_037", 1,
     "How does AWS achieve lower pay-as-you-go prices for all customers as its global infrastructure expands?",
     "Каким образом AWS добивается снижения тарифов для всех клиентов по мере роста своей глобальной инфраструктуры?",
     "By benefiting from massive economies of scale", "Благодаря масштабной экономии за счет масштаба (Economies of scale)",
     "Because aggregate usage from hundreds of thousands of customers is pooled in AWS, AWS achieves massive economies of scale and passes savings on via frequent price reductions.",
     "Концентрация сотен тысяч клиентов в облаке позволяет AWS закупать оборудование на гигантских объемах (economies of scale) и регулярно снижать тарифы для потребителей.",
     [
         ("By charging cancellation fees when customers turn off instances", "Путем взимания комиссии за прекращение использования серверов", "AWS has no cancellation fees or termination penalties for on-demand resources.", "В AWS нет штрафов за удаление или выключение инстансов."),
         ("By forcing long-term 10-year contracts for all services", "Путем принуждения к 10-летним долгосрочным контрактам", "AWS does not force long-term contracts; customers can use services by the second without contracts.", "AWS не принуждает к многолетним контрактам."),
         ("By increasing license fees on older instance generations", "Путем повышения цен на инстансы предыдущих поколений", "AWS historically lowers prices or introduces cheaper, more powerful instance generations.", "AWS не повышает цены на старые поколения, а выпускает более производительные новые.")
     ],
     ["cloud_economics", "aws_pricing"]),

    ("clf_bill_038", 2,
     "Which pillar of the AWS Well-Architected Framework focuses on avoiding unnecessary spend, analyzing expenditure over time, and choosing the most appropriate resource types and pricing models?",
     "Какой компонент (Pillar) концепции AWS Well-Architected Framework сфокусирован на устранении лишних трат, анализе расходов и правильном выборе типов ресурсов и тарифов?",
     "Cost Optimization Pillar", "Cost Optimization Pillar (Оптимизация затрат)",
     "The Cost Optimization pillar includes practices like adopting a consumption model, measuring overall efficiency, stopping spending money on undifferentiated heavy lifting, and analyzing expenditure.",
     "Столп Cost Optimization включает переход на оплату по потреблению, измерение эффективности, отказ от лишней рутины и постоянный мониторинг расходов.",
     [
         ("Operational Excellence", "Operational Excellence", "Operational Excellence focuses on running workloads effectively and gaining insight into day-to-day operations.", "Operational Excellence отвечает за автоматизацию процессов и регламенты сопровождения систем."),
         ("Reliability", "Reliability", "Reliability focuses on workload availability, recovery from failures, and dynamically acquiring computing resources.", "Reliability отвечает за устойчивость к сбоям и непрерывность бизнеса."),
         ("Performance Efficiency", "Performance Efficiency", "Performance Efficiency focuses on structured use of computing resources to meet requirements as demand evolves.", "Performance Efficiency отвечает за эффективную скорость работы систем.")
     ],
     ["well_architected_framework", "aws_pricing"]),

    ("clf_bill_039", 2,
     "What automated action can AWS Budgets execute when a configured threshold is breached? (Select TWO)",
     "Какое автоматическое действие может выполнить сервис AWS Budgets при превышении заданного финансового лимита? (Выберите ДВА)",
     ["Apply a restrictive IAM policy to prevent new resource provisioning", "Stop specific running Amazon EC2 or Amazon RDS instances"],
     ["Применить ограничивающую политику IAM для запрета создания новых ресурсов", "Остановить указанные работающие инстансы Amazon EC2 или Amazon RDS"],
     "AWS Budgets Actions can automatically execute targeted responses when thresholds are breached, including applying SCP/IAM policies or stopping running EC2/RDS instances.",
     "AWS Budgets Actions позволяет автоматически применить ограничивающую политику IAM (запретив создавать новые инстансы) или остановить целевые инстансы EC2/RDS при превышении бюджета.",
     [
         ("Automatically terminate and delete the AWS Account", "Автоматически удалить аккаунт AWS", "AWS Budgets cannot terminate or delete customer AWS accounts.", "AWS Budgets никогда не удаляет учетную запись клиента."),
         ("Delete all S3 buckets containing objects", "Удалить все S3 бакеты с данными", "AWS Budgets does not delete production data or storage buckets.", "Budgets не удаляет клиентские данные и корзины S3."),
         ("Downgrade the AWS Support plan to Basic", "Понизить план техподдержки до Basic", "Budgets does not alter commercial support plan agreements.", "Budgets не изменяет тарифный план техподдержки.")
     ],
     ["aws_budgets", "aws_iam"]),

    ("clf_bill_040", 2,
     "How long does AWS Cost Explorer retain historical cost and usage data by default?",
     "Какой период хранения исторических данных о расходах и потреблении поддерживает AWS Cost Explorer по умолчанию?",
     "Up to 14 months", "До 14 месяцев",
     "AWS Cost Explorer provides up to 14 months of historical data to help identify annual trends, seasonal peaks, and year-over-year comparisons.",
     "AWS Cost Explorer сохраняет исторические данные за период до 14 месяцев, позволяя сравнивать сезонные тренды год к году.",
     [
         ("Up to 30 days only", "Только до 30 дней", "30 days is too brief for annual tax and budgeting reviews; Cost Explorer maintains 14 months.", "30 дней недостаточно для годовой отчетности, Cost Explorer хранит 14 месяцев."),
         ("Up to 90 days", "До 90 дней", "90 days is the default retention for CloudTrail event history, not Cost Explorer billing metrics.", "90 дней — это срок хранения бесплатных событий в CloudTrail, а не финансовой истории."),
         ("7 years indefinitely", "7 лет бессрочно", "Cost Explorer does not retain 7 years of data; long-term raw archival requires storing CUR in Amazon S3 Glacier.", "Для 7-летнего хранения сырые отчеты CUR архивируют в S3 Glacier.")
     ],
     ["aws_cost_explorer", "aws_pricing"]),

    # Partner Network & Licenses (41-55)
    ("clf_bill_041", 1,
     "Which tier of the AWS Partner Network (APN) consists of professional services firms, system integrators, and strategic consultancies that help clients design, architect, and migrate workloads to AWS?",
     "Какая категория партнерской сети AWS Partner Network (APN) объединяет системных интеграторов и консалтинговые компании, помогающие клиентам проектировать и мигрировать системы в AWS?",
     "APN Consulting Partners (Services Path)", "APN Consulting Partners (Services Path)",
     "APN Consulting Partners (now under the AWS Services Path) are professional services firms that help customers design, architect, build, migrate, and manage their workloads on AWS.",
     "APN Consulting Partners (AWS Services Path) — это консалтинговые компании и системные интеграторы, оказывающие профессиональные услуги по проектированию и миграции в AWS.",
     [
         ("APN Technology Partners", "APN Technology Partners", "Technology Partners provide software solutions that run on or are integrated with AWS, rather than professional consultancy services.", "Technology Partners разрабатывают программные продукты, интегрированные с AWS, а не консалтинговые услуги."),
         ("AWS Concierge", "AWS Concierge", "AWS Concierge is an internal AWS support team for billing inquiries.", "Concierge — внутренняя служба биллинга AWS."),
         ("AWS Quick Starts", "AWS Quick Starts", "Quick Starts are automated reference deployment CloudFormation templates, not partner organizations.", "Quick Starts — это готовые шаблоны развертывания от AWS, а не компании-партнеры.")
     ],
     ["aws_apn", "aws_support"]),

    ("clf_bill_042", 1,
     "Which tier of the AWS Partner Network (APN) consists of commercial software vendors (ISVs) who build SaaS products or developer tools integrated with AWS?",
     "Какая категория партнерской сети AWS Partner Network (APN) объединяет независимых разработчиков ПО (ISV), создающих SaaS-продукты и инструменты, интегрированные с AWS?",
     "APN Technology Partners (Software Path)", "APN Technology Partners (Software Path)",
     "APN Technology Partners (under the AWS Software Path) build commercial software and SaaS solutions hosted on, or integrated with, AWS for enterprise customers.",
     "APN Technology Partners (AWS Software Path) создают коммерческие программные продукты и SaaS-сервисы, работающие на инфраструктуре AWS.",
     [
         ("APN Consulting Partners", "APN Consulting Partners", "Consulting Partners provide human implementation services and consulting, not commercial software development.", "Consulting Partners предоставляют услуги специалистов и консалтинг, а не продажу лицензий на собственный софт."),
         ("AWS Professional Services", "AWS Professional Services", "AWS Professional Services is AWS's internal consulting organization, not external third-party partners.", "AWS Professional Services — это внутренний консалтинг от самой компании AWS."),
         ("AWS Marketplace Vendors Only", "Только продавцы AWS Marketplace", "Technology Partners build integrations whether or not their product is distributed through Marketplace.", "Technology Partners — официальный статус участников партнерской программы.")
     ],
     ["aws_apn", "aws_marketplace"]),

    ("clf_bill_043", 2,
     "A company wants to run existing Microsoft Windows Server licenses with per-core licensing agreements that strictly prohibit shared tenancy hardware. Which EC2 tenancy model should they select?",
     "Компании необходимо запустить серверы с корпоративными лицензиями Microsoft Windows Server, условия которых строго запрещают многопользовательское оборудование. Какую модель аренды EC2 следует выбрать?",
     "Amazon EC2 Dedicated Hosts", "Amazon EC2 Dedicated Hosts",
     "Dedicated Hosts provide a physical server completely dedicated for your use, giving you visibility into sockets and physical cores required for Bring Your Own License (BYOL) compliance.",
     "Dedicated Hosts предоставляют физический сервер целиком, позволяя контролировать ядра и сокеты для соблюдения лицензионных соглашений BYOL.",
     [
         ("Dedicated Instances", "Dedicated Instances", "Dedicated Instances run on single-tenant hardware, but do not provide host-level socket/core visibility required for socket-bound licenses.", "Dedicated Instances изолированы на уровне 'железа', но не дают доступа к сокетам и ядрам для привязки лицензий."),
         ("Spot Instances", "Spot Instances", "Spot instances run on shared multi-tenant hardware and are subject to interruption.", "Spot Instances работают на общем оборудовании и могут быть прерваны в любой момент."),
         ("Default Multi-tenant Instances", "Default Multi-tenant Instances", "Standard instances share physical hardware with instances belonging to other AWS accounts.", "Стандартные инстансы делят один физический сервер с другими клиентами.")
     ],
     ["amazon_ec2", "ec2_dedicated_hosts"]),

    ("clf_bill_044", 2,
     "What is the cost implication of deploying a NAT Gateway across multiple Availability Zones?",
     "Как рассчитывается стоимость использования NAT Gateway, развернутых в нескольких зонах доступности?",
     "An hourly charge per NAT Gateway provisioned plus per-GB data processing charges for traffic passing through each gateway", "Почасовая оплата за каждый развернутый NAT Gateway плюс оплата за каждый гигабайт обработанных данных",
     "NAT Gateways incur an hourly charge for every gateway provisioned, as well as a per-gigabyte data processing fee for all traffic routed through them.",
     "За каждый NAT Gateway начисляется фиксированная почасовая ставка, а также плата за каждый гигабайт трафика, прошедший через шлюз.",
     [
         ("NAT Gateway is completely free when deployed inside a VPC", "NAT Gateway полностью бесплатен внутри VPC", "NAT Gateway is a managed service that incurs hourly running and data processing fees.", "NAT Gateway — платный управляемый сервис."),
         ("Only inbound traffic is charged, outbound is free", "Оплачивается только входящий трафик, исходящий бесплатен", "Data processing applies to all data traversing the NAT Gateway in either direction.", "Плата за обработку взимается за любой объем данных, проходящий через шлюз."),
         ("A flat monthly fee with unlimited data processing", "Фиксированная месячная подписка с безлимитным трафиком", "NAT Gateway pricing scales with data processed; there is no unlimited flat-rate tier.", "У NAT Gateway нет безлимитного тарифа — оплата пропорциональна объему трафика.")
     ],
     ["amazon_vpc", "aws_pricing"]),

    ("clf_bill_045", 2,
     "A company needs to purchase and deploy Amazon RDS Reserved Instances. Which option describes how the reservation operates?",
     "Компании необходимо приобрести резервированные инстансы (Reserved Instances) для Amazon RDS. Как действует данная резервация?",
     "It provides a significant billing discount applied automatically to an active RDS database instance matching the instance type and region", "Предоставляет скидку, автоматически применяемую к работающему инстансу RDS соответствующего типа и региона",
     "RDS Reserved Instances provide a discount applied automatically to database usage matching the reserved instance class and engine specifications.",
     "Резервированные инстансы Amazon RDS автоматически применяют скидку к счету за соответствующий тип и движок базы данных в течение выбранного срока.",
     [
         ("It creates a duplicate backup server in a remote region", "Создает копию сервера в удаленном регионе", "RI is a financial billing discount mechanism, not a physical database replication process.", "RI — это финансовая скидка, а не создание физических реплик базы данных."),
         ("It automatically turns off the database when budget is reached", "Автоматически отключает базу данных при превышении бюджета", "RIs do not stop or terminate database workloads.", "RI не влияют на остановку или запуск сервисов."),
         ("It locks the database configuration against any updates", "Блокирует конфигурацию базы данных от внесения изменений", "RIs do not lock software configurations; they solely affect billing rates.", "RI влияет исключительно на стоимость, а не на технические настройки.")
     ],
     ["amazon_rds", "aws_reserved_instances"]),

    # Advanced Billing & Strategy (56-72)
    ("clf_bill_046", 1,
     "Which AWS tool helps customers view their current estimated monthly bill, review top services by spend, and check Free Tier usage limits in a single web dashboard?",
     "Какой инструмент AWS позволяет в едином интерфейсе видеть текущий расчетный счет за месяц, топ самых затратных сервисов и статус использования лимитов Free Tier?",
     "AWS Billing and Cost Management Dashboard", "AWS Billing and Cost Management Dashboard",
     "The Billing Dashboard provides an immediate overview of estimated monthly spend, top 5 services contributing to cost, and real-time Free Tier utilization tracking.",
     "Консоль AWS Billing Dashboard дает наглядную сводку текущих расходов, топ-5 самых дорогих сервисов за месяц и индикаторы расхода бесплатных лимитов Free Tier.",
     [
         ("AWS CloudTrail", "AWS CloudTrail", "CloudTrail records API governance events, not financial bill dashboards.", "CloudTrail логирует вызовы API, а не финансовую сводку."),
         ("AWS Config", "AWS Config", "AWS Config audits resource configuration compliance over time.", "AWS Config отслеживает историю изменений конфигурации ресурсов."),
         ("Amazon Inspector", "Amazon Inspector", "Amazon Inspector scans compute workloads for software vulnerabilities.", "Amazon Inspector сканирует серверы на уязвимости ПО.")
     ],
     ["aws_billing", "aws_free_tier"]),

    ("clf_bill_047", 2,
     "What happens to unblended rates when analyzing multi-account invoices in AWS Organizations?",
     "Что отражают несконсолидированные ставки (unblended rates) при анализе расходов в AWS Organizations?",
     "Unblended rates show the actual costs incurred by each specific individual account without distributing blended volume discounts", "Отражают фактические затраты каждого отдельного аккаунта без искусственного усреднения оптовых скидок",
     "Unblended rates present the exact rates charged for each individual account's specific usage, whereas blended rates average volume discounts across all member accounts.",
     "Unblended rates показывают реальную стоимость ресурсов каждого конкретного аккаунта без перераспределения оптовых скидок между связанными счетами.",
     [
         ("Unblended rates show costs after converting to foreign currencies", "Показывают стоимость после конвертации в валюту клиента", "Currency conversion is not related to blended vs unblended billing methodology.", "Конвертация валют не имеет отношения к понятию blended rates."),
         ("Unblended rates include hidden enterprise support penalties", "Включают скрытые комиссии за корпоративную поддержку", "There are no hidden fees in unblended cost accounting.", "В unblended ставках нет скрытых надбавок."),
         ("Unblended rates apply only to AWS Marketplace purchases", "Применяются только к покупкам в AWS Marketplace", "Unblended accounting applies across all AWS native services.", "Unblended rates применяются ко всем сервисам AWS.")
     ],
     ["aws_organizations", "aws_consolidated_billing"]),

    ("clf_bill_048", 2,
     "Which billing feature allows an organization to restrict the purchase of Reserved Instances and Savings Plans to only authorized administrative personnel?",
     "Какая возможность позволяет ограничить покупку дорогостоящих Reserved Instances и Savings Plans в организации только уполномоченными администраторами?",
     "Service Control Policies (SCPs) and IAM Policies", "Service Control Policies (SCPs) и политики IAM",
     "SCPs in AWS Organizations combined with granular IAM permissions allow organizations to explicitly deny `ec2:Purchase*` and `savingsplans:CreateSavingsPlan` actions to regular users.",
     "С помощью Service Control Policies (SCP) в Organizations и политик IAM можно запретить покупку подписок обычным разработчикам, оставив право только финансовым админам.",
     [
         ("Security Groups", "Security Groups", "Security Groups control inbound and outbound network traffic to instances.", "Security Groups фильтруют сетевой трафик, а не финансовые операции в консоли."),
         ("AWS WAF Rules", "AWS WAF Rules", "WAF blocks malicious HTTP/HTTPS web traffic, not AWS management console actions.", "AWS WAF блокирует веб-атаки, а не действия в консоли управления."),
         ("Amazon Route 53 DNS records", "DNS-записи Amazon Route 53", "Route 53 routes domain names to IPs and has no bearing on purchasing authorizations.", "Route 53 управляет доменами и DNS.")
     ],
     ["aws_organizations", "aws_iam", "aws_savings_plans"]),

    ("clf_bill_049", 2,
     "A company needs programmatic access to current AWS product attributes, retail pricing, and discount tiers to build an automated internal procurement comparison engine. Which tool provides this?",
     "Компании требуется программный доступ к актуальным тарифам, характеристикам продуктов и ценам AWS для интеграции во внутреннюю систему закупок. Какой сервис предоставляет этот API?",
     "AWS Price List Query API", "AWS Price List Query API",
     "The AWS Price List Query API (and AWS Price List Bulk API) provides programmatic access to real-time retail prices of all AWS products and services.",
     "AWS Price List API предоставляет программный доступ через REST/JSON к полному каталогу цен и тарифов на все сервисы AWS.",
     [
         ("AWS Cost Explorer API", "AWS Cost Explorer API", "Cost Explorer API queries your account's historical spending, not public retail pricing catalogs.", "Cost Explorer API возвращает историю трат вашего аккаунта, а не общедоступный прейскурант всех сервисов."),
         ("AWS Support API", "AWS Support API", "AWS Support API creates and manages technical support tickets.", "Support API управляет тикетами техподдержки."),
         ("AWS CloudTrail API", "AWS CloudTrail API", "CloudTrail API queries management audit events.", "CloudTrail API возвращает лог событий безопасности.")
     ],
     ["aws_pricing", "aws_support"]),

    ("clf_bill_050", 1,
     "What type of cost is eliminated when an enterprise moves from an on-premises data center to the AWS Cloud?",
     "Какой тип расходов полностью устраняется при отказе от собственного дата-центра в пользу облака AWS?",
     "Costs associated with data center physical real estate, server rack cooling, power, and physical security guards", "Расходы на аренду помещений дата-центра, охлаждение стоек, электричество и физическую охрану",
     "In the AWS Shared Responsibility Model, AWS assumes complete responsibility for the physical facilities, power, cooling, and facility security, eliminating these capital costs for customers.",
     "В облаке AWS берет на себя все расходы по содержанию зданий, электропитанию, кондиционированию и физической охране серверов (Security OF the Cloud).",
     [
         ("All software development expenses", "Все расходы на разработку программного обеспечения", "Software development remains the customer's operational responsibility.", "Разработка приложений остается зоной ответственности заказчика."),
         ("All compliance obligations under data protection regulations", "Все обязательства по соблюдению требований законодательства", "Customers still retain compliance responsibilities for the data they store in the cloud.", "Клиент сам отвечает за соответствие своих данных законам (GDPR, 152-ФЗ)."),
         ("Internet connection costs for end users", "Расходы пользователей на подключение к Интернету", "End users still require internet connectivity to reach cloud applications.", "Пользователям по-прежнему требуется интернет для работы.")
     ],
     ["cloud_economics", "shared_responsibility_model"]),

    ("clf_bill_051", 2,
     "A healthcare company wants to analyze millions of detailed billing rows from the AWS Cost and Usage Report (CUR) using standard SQL queries without provisioning any database servers. Which combination of services should they use?",
     "Медицинская компания хочет анализировать миллионы строк детального отчета о расходах CUR с помощью стандартных SQL-запросов без развертывания серверов баз данных. Какую связку сервисов следует использовать?",
     "Amazon S3 and Amazon Athena", "Amazon S3 и Amazon Athena",
     "CUR files are delivered directly into an Amazon S3 bucket, where Amazon Athena can query the raw CSV or Parquet files directly using standard serverless SQL.",
     "Отчеты CUR сохраняются в корзине Amazon S3, а бессерверный сервис Amazon Athena позволяет мгновенно выполнять SQL-запросы прямо по этим файлам.",
     [
         ("Amazon EC2 and Microsoft Excel", "Amazon EC2 и Microsoft Excel", "Downloading massive multi-gigabyte CUR files to EC2 and Excel is inefficient and unscalable.", "Excel не способен эффективно обрабатывать миллионы строк биллинга."),
         ("Amazon RDS and AWS Direct Connect", "Amazon RDS и AWS Direct Connect", "RDS requires provisioning and managing relational database instances, which is not serverless.", "RDS требует управления сервером БД и не оптимизирован для сырых выгрузок CUR из коробки."),
         ("AWS Cloud9 and AWS Glue only", "AWS Cloud9 и AWS Glue", "Cloud9 is an IDE for writing code, not an interactive query analytics engine.", "Cloud9 — это IDE в браузере, а не инструмент выполнения аналитических SQL-запросов.")
     ],
     ["aws_cur", "amazon_s3", "amazon_athena"]),

    ("clf_bill_052", 1,
     "Which AWS Support plan is the minimum requirement to receive unlimited cases, 24/7 technical phone and chat support, and access to all AWS Trusted Advisor checks?",
     "Какой план поддержки AWS является минимальным для получения неограниченного числа обращений, круглосуточной техподдержки по телефону/чату 24/7 и полного доступа ко всем проверкам Trusted Advisor?",
     "Business Support", "Business Support",
     "Business Support provides 24/7 phone/chat/email access to Cloud Support Engineers with unlimited cases, full Trusted Advisor checks, and 1-hour response for production down.",
     "Business Support — минимальный план с круглосуточным доступом по телефону и в чате 24/7, неограниченным числом кейсов и всеми 100+ проверками Trusted Advisor.",
     [
         ("Developer Support", "Developer Support", "Developer Support provides only business-hours email access and 7 core Trusted Advisor checks.", "Developer Support дает доступ только по почте в рабочие часы и только 7 проверок Trusted Advisor."),
         ("Basic Support", "Basic Support", "Basic Support has no phone access and only 7 core checks.", "Basic Support бесплатен и не включает доступ к инженерам по телефону."),
         ("Enterprise On-Ramp Support", "Enterprise On-Ramp Support", "Enterprise On-Ramp includes these features but is more expensive than Business Support, which is the true minimum tier.", "Enterprise On-Ramp дороже, а минимальным подходящим тарифом является Business.")
     ],
     ["aws_support", "aws_business_support", "aws_trusted_advisor"]),

    ("clf_bill_053", 2,
     "Under the AWS Customer Agreement, what happens to customer data if an AWS account is closed?",
     "Согласно условиям соглашения AWS, что происходит с данными клиента после закрытия аккаунта AWS?",
     "AWS retains data for a 90-day post-closure period during which the account can be reopened, after which data is permanently deleted", "AWS сохраняет данные в течение 90-дневного льготного периода, после чего они безвозвратно удаляются",
     "Following account closure, AWS maintains a 90-day grace period where customers can contact support to reopen the account and retrieve data before permanent deletion.",
     "После закрытия аккаунта действует 90-дневный период, во время которого аккаунт можно восстановить; по истечении 90 дней все ресурсы и данные удаляются навсегда.",
     [
         ("Data is instantly deleted within 1 second of closure", "Данные мгновенно удаляются в течение 1 секунды", "AWS provides a 90-day grace period to prevent catastrophic accidental data loss.", "AWS предоставляет 90 дней защиты на случай ошибочного закрытия."),
         ("AWS copies all data to public S3 buckets", "AWS копирует данные в публичный доступ", "Customer data is never made public by AWS under any circumstance.", "AWS никогда не публикует конфиденциальные данные клиентов."),
         ("Data is archived for 10 years at standard storage rates", "Данные архивируются на 10 лет с начислением оплаты", "AWS does not archive closed account data indefinitely.", "AWS не хранит данные закрытых аккаунтов годами.")
     ],
     ["aws_billing", "aws_support"]),

    ("clf_bill_054", 2,
     "Which pricing model allows customers to pay lower rates as their cumulative cloud storage volume increases across multi-terabyte tiers?",
     "Какая модель ценообразования позволяет платить меньше за единицу объема по мере роста совокупного объема хранимых данных (на терабайтных ступенях тарификации)?",
     "Tiered Pricing (Volume Discounts)", "Tiered Pricing (скидки за объем)",
     "Tiered pricing in services like Amazon S3 and data transfer reduces the cost per GB as total monthly volume crosses defined threshold tiers (e.g., first 50 TB, next 450 TB, over 500 TB).",
     "Ступенчатая тарификация (Tiered Pricing) снижает стоимость каждого гигабайта по мере перехода на более высокие объемы (первые 50 ТБ, следующие 450 ТБ и свыше 500 ТБ).",
     [
         ("Fixed Flat-Rate Subscriptions", "Фиксированная абонентская подписка", "AWS does not charge flat-rate subscriptions for variable storage services.", "В S3 нет фиксированной абонентской платы."),
         ("Pre-paid Cash Bonds", "Внесение залоговых депозитов", "AWS operates on pay-as-you-go, not upfront bond deposits.", "В AWS нет депозитов и залогов."),
         ("Reverse Auction Bidding", "Аукцион обратных ставок", "Only Spot instances use capacity-based market pricing, not S3 standard storage tiers.", "Аукционная модель характерна для Spot, а не для хранения в S3.")
     ],
     ["aws_pricing", "amazon_s3"]),

    ("clf_bill_055", 1,
     "What is the function of the AWS Cost Allocation Tags Manager in the AWS Billing console?",
     "Какую функцию выполняет менеджер тегов распределения затрат (Cost Allocation Tags) в консоли AWS Billing?",
     "It allows billing administrators to activate specific tags so they appear in Cost Explorer and billing reports", "Позволяет администраторам активировать определенные теги для их отображения в Cost Explorer и отчетах о расходах",
     "Tags applied to AWS resources do not appear in cost reports automatically; an administrator must explicitly activate them in the Billing console as Cost Allocation Tags.",
     "Теги, назначенные на ресурсы, не попадают в биллинг автоматически: администратор должен явно активировать их в консоли биллинга, чтобы они стали доступны для группировки в Cost Explorer.",
     [
         ("It automatically deletes untagged EC2 instances", "Автоматически удаляет неразмеченные инстансы EC2", "Cost allocation tags are purely for financial reporting, not resource termination.", "Теги биллинга служат для отчетности, а не для удаления серверов."),
         ("It encrypts resources associated with sensitive tags", "Шифрует ресурсы, содержащие чувствительные теги", "Tag activation affects billing reporting, not KMS encryption.", "Активация тегов не шифрует диски."),
         ("It translates resource names into different languages", "Переводит названия ресурсов на разные языки", "Cost allocation tags organize financial accounting, not UI language localization.", "Теги не относятся к переводу интерфейса.")
     ],
     ["aws_cost_allocation_tags", "aws_cost_explorer"]),

    ("clf_bill_056", 2,
     "Which tool provides automated recommendations for purchasing optimal Compute Savings Plans based on historical EC2 and Lambda usage patterns?",
     "Какой инструмент предоставляет автоматические рекомендации по покупке оптимальных Compute Savings Plans на основе истории использования EC2 и Lambda?",
     "AWS Cost Explorer Savings Plans Recommendations", "Рекомендации Savings Plans в AWS Cost Explorer",
     "AWS Cost Explorer analyzes your historical hourly compute usage over the past 7, 30, or 60 days to calculate customized Savings Plans recommendations that maximize dollar savings.",
     "AWS Cost Explorer анализирует историю потребления за 7, 30 или 60 дней и рассчитывает персональные рекомендации по покупке планов Savings Plans для максимальной выгоды.",
     [
         ("AWS Shield Manager", "AWS Shield Manager", "Shield is a DDoS protection service.", "Shield защищает от DDoS."),
         ("AWS Artifact", "AWS Artifact", "AWS Artifact provides compliance audit reports.", "AWS Artifact предоставляет аудиторские отчеты соответствия."),
         ("AWS Network Firewall", "AWS Network Firewall", "Network Firewall filters network packets.", "Network Firewall фильтрует сетевые пакеты.")
     ],
     ["aws_cost_explorer", "aws_savings_plans"]),

    ("clf_bill_057", 2,
     "A company needs to know if their existing on-premises server migration will be more cost-effective on AWS compared to maintaining their current hardware over a 3-year horizon. Which assessment is this?",
     "Компании необходимо рассчитать, будет ли миграция серверов в AWS более выгодной по сравнению с эксплуатацией собственного оборудования на горизонте 3 лет. Как называется такой расчет?",
     "Total Cost of Ownership (TCO) Analysis", "Анализ совокупной стоимости владения (TCO Analysis)",
     "A Total Cost of Ownership (TCO) analysis compares direct and indirect costs of running on-premises infrastructure (servers, storage, power, cooling, facilities, admin labor) against AWS cloud hosting.",
     "Анализ совокупной стоимости владения (Total Cost of Ownership, TCO) сопоставляет прямые и косвенные затраты на собственный дата-центр (серверы, аренда, свет, охлаждение, зарплаты админов) с расходами в AWS.",
     [
         ("Penetration Testing Review", "Тестирование на проникновение (пентест)", "Penetration testing evaluates security posture, not financial comparisons.", "Пентест проверяет уязвимости защиты, а не финансы."),
         ("Disaster Recovery RTO Audit", "Аудит времени восстановления (RTO)", "RTO audits measure recovery speed, not capital expenditure comparisons.", "Аудит RTO оценивает скорость восстановления систем при аварии."),
         ("Network Latency Benchmarking", "Сетевое нагрузочное тестирование", "Latency benchmarking tests network speed, not fiscal feasibility.", "Тестирование задержек оценивает пинг, а не экономику.")
     ],
     ["cloud_economics", "aws_pricing"]),

    ("clf_bill_058", 2,
     "Which payment frequency option is NOT available when purchasing Amazon EC2 Reserved Instances or Savings Plans?",
     "Какой вариант графика платежей НЕ доступен при покупке Amazon EC2 Reserved Instances или Savings Plans?",
     "Quarterly Upfront payments", "Quarterly Upfront (ежеквартальная предоплата)",
     "AWS provides exactly three payment options for RIs and Savings Plans: All Upfront, Partial Upfront, and No Upfront. Quarterly upfront payments do not exist.",
     "AWS предлагает ровно три варианта оплаты резерваций: All Upfront (100% аванс), Partial Upfront (частичный аванс) и No Upfront (без аванса, ежемесячно). Ежеквартальной оплаты не существует.",
     [
         ("All Upfront", "All Upfront", "All Upfront is a standard option providing the highest discount.", "All Upfront — стандартная опция с максимальной скидкой."),
         ("Partial Upfront", "Partial Upfront", "Partial Upfront is a standard option requiring a portion of the fee upfront with discounted monthly rates.", "Partial Upfront — стандартная опция с частичной предоплатой."),
         ("No Upfront", "No Upfront", "No Upfront is a standard option requiring zero initial cash outlay.", "No Upfront — стандартная опция без начального платежа.")
     ],
     ["aws_reserved_instances", "aws_savings_plans"]),

    ("clf_bill_059", 2,
     "What type of budget can be configured in AWS Budgets? (Select TWO)",
     "Какие типы бюджетов можно настроить в сервисе AWS Budgets? (Выберите ДВА)",
     ["Cost budget (tracks overall dollar expenditure)", "Usage budget (tracks consumption units such as S3 GB or EC2 hours)"],
     ["Бюджет затрат (Cost budget — отслеживание расходов в долларах)", "Бюджет использования (Usage budget — отслеживание объемов ресурсов, например ГБ в S3 или часов EC2)"],
     "AWS Budgets supports Cost budgets (monitoring dollar spend), Usage budgets (monitoring specific resource units), and Reservation / Savings Plans utilization and coverage budgets.",
     "AWS Budgets позволяет создавать бюджеты расходов (Cost budgets в долларах), бюджеты использования (Usage budgets в часах/ГБ), а также бюджеты покрытия RI и Savings Plans.",
     [
         ("Bandwidth speed throttle budget", "Бюджет ограничения пропускной способности сети", "AWS Budgets does not throttle physical network interface bandwidth.", "Budgets не умеет искусственно занижать скорость сетевых портов."),
         ("Code commit frequency budget", "Бюджет частоты коммитов разработчиков", "AWS Budgets is a financial and capacity tool, not a developer productivity monitor.", "Budgets не считает коммиты в git-репозитории."),
         ("DNS query latency limit budget", "Бюджет задержки DNS-запросов", "Latency is monitored via CloudWatch synthetics, not financial budgets.", "Задержки DNS отслеживаются в CloudWatch, а не в биллинге.")
     ],
     ["aws_budgets", "aws_cost_explorer"]),

    ("clf_bill_060", 1,
     "Where can an AWS customer download their official monthly tax invoices, receipts, and VAT documentation?",
     "Где клиент AWS может скачать официальные налоговые счета-фактуры, чеки и документы с НДС (VAT)?",
     "AWS Bills page in the AWS Billing and Cost Management console", "Раздел Bills в консоли AWS Billing and Cost Management",
     "The Bills page in the AWS Billing console allows customers to inspect past monthly billing cycles, view itemized charges, and download official PDF tax invoices.",
     "На странице Bills в консоли AWS Billing можно просматривать закрытые расчетные периоды, детализацию и скачивать официальные PDF-счета с реквизитами для бухгалтерии.",
     [
         ("AWS Artifact", "AWS Artifact", "AWS Artifact provides security and compliance audit reports (SOC, PCI), not customer monthly billing invoices.", "AWS Artifact содержит отчеты о безопасности (SOC, ISO), а не счета на оплату."),
         ("Amazon CloudWatch Logs", "Amazon CloudWatch Logs", "CloudWatch Logs stores application log streams, not financial tax invoices.", "CloudWatch хранит логи приложений, а не бухгалтерские счета."),
         ("AWS Trust & Safety portal", "Портал AWS Trust & Safety", "Trust & Safety investigates network abuse incidents.", "Trust & Safety расследует спам и сетевые атаки.")
     ],
     ["aws_billing", "aws_support"]),

    # Final Set (61-72)
    ("clf_bill_061", 2,
     "Which tool allows customers to set up a recurring delivery of customized AWS cost reports directly to an Amazon S3 bucket on a daily or monthly schedule?",
     "Какой инструмент позволяет настроить регулярную автоматическую выгрузку отчетов о расходах AWS в корзину Amazon S3 по ежедневному или ежемесячному расписанию?",
     "AWS Cost and Usage Report (CUR)", "AWS Cost and Usage Report (CUR)",
     "The AWS Cost and Usage Report allows you to define recurring delivery of detailed billing files directly to an designated Amazon S3 bucket.",
     "AWS Cost and Usage Report (CUR) позволяет настроить автоматическую регулярную выгрузку детальных биллинговых файлов прямо в указанный S3-бакет.",
     [
         ("AWS Systems Manager", "AWS Systems Manager", "Systems Manager automates server management tasks, not billing file exports.", "Systems Manager управляет виртуальными машинами, а не отчетами биллинга."),
         ("AWS Budgets", "AWS Budgets", "AWS Budgets sends alert notifications via email or SNS, but does not export raw CSV/Parquet billing dumps to S3.", "AWS Budgets шлет алерты по email, а не выгружает базы биллинга в S3."),
         ("AWS Config", "AWS Config", "AWS Config exports configuration change history snapshots to S3, not financial invoices.", "AWS Config выгружает историю конфигураций серверов, а не финансовые счета.")
     ],
     ["aws_cur", "amazon_s3"]),

    ("clf_bill_062", 2,
     "A company is reviewing its AWS spending and notices that data transfer charges between two EC2 instances in different Availability Zones within the same Region are accruing. How can they eliminate these cross-AZ data transfer fees if high availability is not required?",
     "Компания анализирует расходы и видит затраты на передачу данных между двумя инстансами в разных AZ одного региона. Как полностью исключить плату за трафик, если высокая доступность не требуется?",
     "Place both EC2 instances in the same Availability Zone and communicate via private IP", "Разместить оба инстанса в одной зоне доступности (AZ) и настроить связь по приватным IP-адресам",
     "Data transfer between EC2 instances in the same Availability Zone over private IP addresses is completely free.",
     "Трафик между инстансами EC2, находящимися в одной и той же Availability Zone и общающимися по приватным IP, бесплатен.",
     [
         ("Connect them using public IPv4 addresses", "Настроить обмен через публичные IPv4 адреса", "Public IP traffic traverses internet routing and incurs higher charges.", "Использование публичных IP-адресов увеличивает стоимость трафика."),
         ("Create a cross-region VPC peering connection", "Создать VPC Peering в другой регион", "Inter-region traffic is significantly more expensive than cross-AZ traffic.", "Межрегиональный трафик стоит значительно дороже межзонального."),
         ("Attach an Elastic IP to both instances", "Привязать к обоим инстансам Elastic IP", "Elastic IPs do not eliminate cross-AZ transfer charges.", "Elastic IP не устраняет плату за трафик между разными зонами доступности.")
     ],
     ["amazon_ec2", "amazon_vpc", "aws_pricing"]),

    ("clf_bill_063", 2,
     "What is an advantage of Convertible Reserved Instances over Standard Reserved Instances for Amazon EC2?",
     "В чем преимущество Convertible Reserved Instances по сравнению со Standard Reserved Instances для Amazon EC2?",
     "The ability to change the EC2 instance family, operating system, and tenancy during the commitment term", "Возможность менять семейство инстансов (напр. с t3 на m5), операционную систему и тип аренды в течение срока резервации",
     "Convertible RIs allow you to exchange your reservation for another of equal or greater value, giving you the flexibility to switch instance families (e.g., from C5 to M5), OS, or tenancy.",
     "Convertible RI позволяют в течение 1 или 3 лет менять семейство процессоров, ОС и конфигурации, обеспечивая гибкость при эволюции архитектуры в обмен на чуть меньшую скидку.",
     [
         ("They offer higher discount percentages than Standard RIs", "Они дают более высокий процент скидки, чем Standard RI", "Standard RIs offer higher discounts (up to 72%) compared to Convertible RIs (up to 54%).", "Standard RI дают более высокую скидку (до 72%), чем Convertible (до 54%)."),
         ("They can be sold on the AWS Reserved Instance Marketplace", "Их можно перепродавать на бирже AWS Reserved Instance Marketplace", "Only Standard RIs for EC2 can be sold on the RI Marketplace; Convertible RIs cannot.", "На вторичной бирже Marketplace можно продавать только Standard RI, но не Convertible."),
         ("They do not require any commitment period", "Они не требуют никаких обязательств по сроку использования", "Convertible RIs still require a 1-year or 3-year commitment.", "Convertible RI требуют обязательств на 1 или 3 года.")
     ],
     ["amazon_ec2", "aws_reserved_instances"]),

    ("clf_bill_064", 2,
     "Where can an AWS customer sell unused Standard EC2 Reserved Instances to recover costs?",
     "Где клиент AWS может продать неиспользуемые инстансы Standard EC2 Reserved Instances для возврата части затрат?",
     "AWS Reserved Instance Marketplace", "AWS Reserved Instance Marketplace",
     "The AWS Reserved Instance Marketplace is an online platform that enables customers to list and sell their unused standard Amazon EC2 Reserved Instances to other AWS customers.",
     "AWS Reserved Instance Marketplace — это торговая площадка, где клиенты могут продать оставшиеся месяцы своих Standard RI другим пользователям AWS.",
     [
         ("AWS Marketplace (Software SaaS section)", "AWS Marketplace (раздел SaaS)", "The main AWS Marketplace sells third-party software licenses, not customer-owned EC2 RIs.", "Основной AWS Marketplace продает лицензии на софт от вендоров."),
         ("Amazon eBay integration", "Интеграция с Amazon eBay", "There is no integration between AWS infrastructure and eBay.", "У AWS нет интеграции с внешними аукционами."),
         ("AWS Systems Manager", "AWS Systems Manager", "Systems Manager automates operational runbooks, not financial secondary markets.", "Systems Manager управляет IT-процессами, а не вторичным рынком ценных бумаг/подписок.")
     ],
     ["amazon_ec2", "aws_reserved_instances", "aws_marketplace"]),

    ("clf_bill_065", 1,
     "Which AWS tool helps customers establish billing alert thresholds using CloudWatch alarms without creating complex budgets?",
     "Какой инструмент позволяет быстро настроить оповещение о превышении порога счета с помощью CloudWatch Alarms без настройки сложных бюджетов?",
     "Enabling Billing Alerts in the Billing Console and creating a CloudWatch Billing Metric Alarm", "Включение Billing Alerts в консоли биллинга и создание CloudWatch Alarm по метрике EstimatedCharges",
     "By enabling 'Receive Billing Alerts' in the Billing Preferences, AWS sends estimated charges data to CloudWatch in the us-east-1 region, where a CloudWatch Alarm can trigger an SNS email when charges exceed a set limit.",
     "Включив опцию Receive Billing Alerts в настройках биллинга, аккаунт начинает отправлять метрику EstimatedCharges в CloudWatch (us-east-1), где создается стандартный алерт с уведомлением на email.",
     [
         ("AWS CloudTrail Insights", "AWS CloudTrail Insights", "CloudTrail Insights detects anomalies in API call volumes, not financial billing dollar amounts.", "CloudTrail Insights отслеживает всплески вызовов API, а не сумму счета."),
         ("AWS Shield Advanced", "AWS Shield Advanced", "Shield Advanced protects against DDoS attacks.", "Shield Advanced защищает от сетевых атак."),
         ("Amazon GuardDuty", "Amazon GuardDuty", "GuardDuty detects unauthorized crypto-mining, not routine billing thresholds.", "GuardDuty ищет вредоносную активность в аккаунте.")
     ],
     ["aws_billing", "amazon_cloudwatch"]),

    ("clf_bill_066", 2,
     "What is the billing impact of stopping (not terminating) an Amazon EBS-backed EC2 instance?",
     "Как начисляется плата при остановке (Stop, а не Terminate) инстанса EC2 с диском Amazon EBS?",
     "Compute instance usage charges stop, but charges for the attached Amazon EBS storage volume continue to accrue", "Плата за вычисления (EC2 compute) прекращается, но плата за прикрепленный том хранилища EBS продолжает начисляться",
     "When an EBS-backed instance is stopped, you are no longer billed for EC2 compute instance hours, but you continue to pay for the provisioned EBS volume storage and any allocated unassociated Elastic IPs.",
     "При остановке сервера плата за процессор и память EC2 обнуляется, однако зарезервированное дисковое пространство EBS продолжает оплачиваться в полном объеме.",
     [
         ("All billing for both compute and storage completely stops", "Все начисления за сервер и за диск полностью прекращаются", "EBS volume storage retains your data and must still be paid for while the instance is stopped.", "Диск EBS сохраняет все данные, поэтому за хранение блочного объема продолжает взиматься плата."),
         ("You are billed at 50% discount for both compute and storage", "Начисляется 50% скидка на сервер и диск", "Compute is billed at 0% when stopped, and storage is billed at 100%.", "Вычисления стоят 0%, а хранилище — 100%."),
         ("Data on the EBS volume is immediately erased", "Данные на диске EBS немедленно стираются", "Stopping an instance preserves EBS data intact; termination deletes it if DeleteOnTermination is true.", "Остановка (Stop) сохраняет данные в неизменном виде.")
     ],
     ["amazon_ec2", "amazon_ebs", "aws_pricing"]),

    ("clf_bill_067", 2,
     "How are AWS Snowball Edge appliances billed for data migration?",
     "По какой модели оплачивается аренда физических устройств AWS Snowball Edge для миграции данных?",
     "A fixed service fee per job (which includes 10 days of on-site usage) plus per-day fees if retained longer, plus standard data transfer / storage fees once ingested into S3", "Фиксированная плата за заказ устройства (включающая 10 дней нахождения на объекте), посуточная аренда при превышении срока и стоимость хранения данных после загрузки в S3",
     "Snowball Edge charges a flat job fee covering shipping and 10 on-site days. Extra days incur an additional daily fee, and standard S3 storage fees apply after data upload.",
     "Заказ Snowball Edge включает базовую стоимость устройства и 10 дней на площадке клиента; каждый дополнительный день оплачивается посуточно, а загруженные данные оплачиваются по стандартным тарифам S3.",
     [
         ("By the mile of shipping distance traveled", "За каждую милю пройденного транспортного расстояния", "Shipping is included in the base fee in most supported territories.", "Базовая доставка включена в стоимость заказа."),
         ("Per file transferred onto the appliance", "За каждый отдельный файл, скопированный на диск", "Pricing is not based on individual file counts.", "AWS не тарифицирует количество отдельных файлов."),
         ("Free of charge for all AWS customers regardless of duration", "Абсолютно бесплатно для всех клиентов независимо от срока", "Snowball is a specialized physical hardware appliance with clear logistics fees.", "Snowball — это физический сейф-сервер, аренда которого тарифицируется.")
     ],
     ["aws_snowball", "amazon_s3", "aws_pricing"]),

    ("clf_bill_068", 1,
     "Which AWS billing dashboard section displays a visual breakdown of your top 5 cost-contributing services and a comparison to the previous month's spending?",
     "Какой раздел панели управления биллингом наглядно отображает топ-5 самых затратных сервисов и процентное сравнение расходов с предыдущим месяцем?",
     "AWS Billing and Cost Management Home Dashboard", "Главная страница консоли AWS Billing and Cost Management",
     "The Billing Dashboard home page features summary cards displaying month-to-date costs, forecasted month-end costs, month-over-month trends, and the top 5 spend contributors.",
     "Главный дашборд биллинга содержит сводку расходов текущего месяца, прогноз на конец месяца, сравнение с прошлым периодом и диаграмму топ-5 сервисов.",
     [
         ("AWS CloudTrail History", "История AWS CloudTrail", "CloudTrail tracks management events, not monthly percentage spend widgets.", "CloudTrail показывает события безопасности, а не финансовую сводку."),
         ("Amazon Inspector Findings", "Amazon Inspector Findings", "Inspector lists vulnerability findings.", "Inspector показывает уязвимости в операционных системах."),
         ("AWS Control Tower Guardrails", "AWS Control Tower Guardrails", "Control Tower manages governance guardrails across accounts.", "Control Tower управляет правилами соответствия.")
     ],
     ["aws_billing", "aws_cost_explorer"]),

    ("clf_bill_069", 2,
     "What is the pricing model for AWS Trusted Advisor full checks?",
     "Какова модель оплаты за доступ ко всем проверкам сервиса AWS Trusted Advisor?",
     "Included at no extra charge with AWS Business, Enterprise On-Ramp, and Enterprise Support plans", "Включен без дополнительной оплаты в тарифные планы AWS Business, Enterprise On-Ramp и Enterprise Support",
     "Access to the complete library of over 100+ Trusted Advisor checks across all 5 categories is included automatically with Business Support or higher.",
     "Полный доступ ко всем 100+ проверкам Trusted Advisor по всем 5 направлениям входит в стоимость подписки Business Support и выше.",
     [
         ("A separate flat monthly subscription of $500 per account", "Отдельная абонентская плата $500 в месяц за аккаунт", "Trusted Advisor is bundled into AWS Support plans, not billed as an isolated standalone fee.", "Trusted Advisor не продается отдельной подпиской, а входит в состав планов поддержки."),
         ("Billed per individual check executed", "Оплата за каждый запуск отдельной проверки", "Checks refresh automatically and are not billed on a per-query basis.", "Проверки выполняются автоматически без платы за каждый клик."),
         ("Free for the first 30 days only", "Бесплатно только в первые 30 дней", "Full checks require an active Business or Enterprise support plan, regardless of account age.", "Доступ определяется тарифным планом поддержки, а не возрастом аккаунта.")
     ],
     ["aws_trusted_advisor", "aws_support"]),

    ("clf_bill_070", 2,
     "Which architectural approach directly supports the Cost Optimization pillar by turning off development and test environments outside of business hours?",
     "Какой архитектурный подход напрямую следует рекомендациям столпа Cost Optimization за счет выключения тестовых сред во внерабочее время?",
     "Implementing scheduled automated start/stop scripts (e.g., via AWS Instance Scheduler or EventBridge and Lambda)", "Внедрение автоматического запуска и остановки по расписанию (через AWS Instance Scheduler или EventBridge + Lambda)",
     "Stopping non-production EC2 and RDS instances during nights and weekends eliminates up to 70% of compute run time and costs.",
     "Остановка тестовых серверов EC2 и баз RDS на ночь и выходные позволяет сэкономить до 70% бюджета на вычислительные мощности.",
     [
         ("Switching all instances to Dedicated Hosts", "Перевод всех тестовых серверов на Dedicated Hosts", "Dedicated Hosts are much more expensive and intended for strict compliance/licensing.", "Dedicated Hosts стоят значительно дороже и не нужны для тестов."),
         ("Purchasing 3-year All Upfront Reserved Instances for test servers", "Покупка 3-летних резерваций All Upfront под временные тестовые серверы", "Committing to 3-year RIs for transient test environments creates inflexible waste.", "Покупка 3-летней подписки на временные серверы противоречит принципам гибкости."),
         ("Disabling all CloudWatch monitoring alarms", "Отключение всех алертов CloudWatch", "Disabling monitoring reduces operational visibility without meaningful cost savings.", "Отключение мониторинга создает 'слепые зоны' и не дает реальной экономии.")
     ],
     ["well_architected_framework", "amazon_ec2", "aws_lambda"]),

    ("clf_bill_071", 2,
     "A company needs to automatically enforce maximum spending limits across departments and prevent runaway cloud costs. Which combination of tools provides preventive governance?",
     "Компании необходимо автоматически контролировать максимальные лимиты расходов по отделам и не допускать неконтролируемого перерасхода средств. Какая комбинация инструментов обеспечивает превентивный контроль?",
     "AWS Organizations with Service Control Policies (SCPs) and AWS Budgets with automated actions", "AWS Organizations с политиками Service Control Policies (SCP) и AWS Budgets с автоматическими действиями",
     "AWS Budgets can trigger automated actions (such as applying restrictive SCPs or shutting down resources) when budgets reach defined thresholds.",
     "Связка AWS Budgets с автоматическими действиями и политиками SCP позволяет превентивно блокировать запуск дорогостоящих инстансов при исчерпании бюджета.",
     [
         ("AWS Shield Standard and Amazon VPC", "AWS Shield Standard и Amazon VPC", "Shield Standard mitigates DDoS attacks, not internal budget overruns.", "Shield защищает от внешних DDoS-атак, а не от внутренних перерасходов."),
         ("Amazon GuardDuty and AWS KMS", "Amazon GuardDuty и AWS KMS", "GuardDuty detects security threats and KMS encrypts data, having no role in budget quotas.", "GuardDuty и KMS отвечают за безопасность и шифрование данных."),
         ("Amazon Route 53 and AWS CloudFront", "Amazon Route 53 и AWS CloudFront", "Route 53 and CloudFront manage DNS and CDN caching, not administrative budget limits.", "Route 53 и CloudFront оптимизируют доставку трафика, а не финансовые лимиты.")
     ],
     ["aws_budgets", "aws_organizations", "aws_iam"]),

    ("clf_bill_072", 1,
     "Which AWS documentation resource provides an authoritative list of all AWS service quotas (formerly known as service limits) and instructions on how to request limit increases?",
     "Какой сервис и раздел документации AWS предоставляет официальный список квот сервисов (ранее называемых service limits) и позволяет запрашивать их увеличение в один клик?",
     "AWS Service Quotas", "AWS Service Quotas",
     "AWS Service Quotas is an AWS service that enables you to view and manage your quotas easily and at scale as your AWS workloads grow, including one-click limit increase requests.",
     "AWS Service Quotas — это специальный сервис, позволяющий в единой консоли просматривать текущие лимиты (квоты) сервисов и отправлять запросы на их увеличение.",
     [
         ("AWS Pricing Calculator", "AWS Pricing Calculator", "The Pricing Calculator estimates architecture costs, not service quotas.", "Pricing Calculator рассчитывает стоимость, а не квоты сервисов."),
         ("AWS Artifact", "AWS Artifact", "AWS Artifact hosts compliance and regulatory documents.", "AWS Artifact предоставляет аудиторские сертификаты соответствия."),
         ("Amazon Inspector", "Amazon Inspector", "Amazon Inspector scans for operating system vulnerabilities.", "Inspector сканирует системы на уязвимости.")
     ],
     ["aws_service_quotas", "aws_support"])
]

def format_questions():
    formatted = []
    for item in BILLING_DATA + MORE_BILLING_TOPICS:
        qid, diff, q_en, q_ru, correct_en, correct_ru, why_correct_en, why_correct_ru, distractors, services = item
        
        # Build options
        # We need opt_a, opt_b, opt_c, opt_d
        options = []
        correct_ids = []
        
        # Check if single or multi
        if isinstance(correct_en, list):
            # Pick Two
            # distractors has 3 items, correct has 2 items -> total 5 options
            all_opts = []
            for idx, c_en in enumerate(correct_en):
                c_ru = correct_ru[idx]
                all_opts.append({
                    "is_correct": True,
                    "text": {"en": c_en, "ru": c_ru},
                    "why_incorrect": None
                })
            for d in distractors:
                all_opts.append({
                    "is_correct": False,
                    "text": {"en": d[0], "ru": d[1]},
                    "why_incorrect": {"en": d[2], "ru": d[3]}
                })
        else:
            all_opts = [
                {
                    "is_correct": True,
                    "text": {"en": correct_en, "ru": correct_ru},
                    "why_incorrect": None
                }
            ]
            for d in distractors:
                all_opts.append({
                    "is_correct": False,
                    "text": {"en": d[0], "ru": d[1]},
                    "why_incorrect": {"en": d[2], "ru": d[3]}
                })
        
        # Assign opt_a, opt_b, ...
        # Keep deterministic or standard order
        letters = ["opt_a", "opt_b", "opt_c", "opt_d", "opt_e"]
        opts_list = []
        for i, opt in enumerate(all_opts):
            opt_id = letters[i]
            opts_list.append({
                "id": opt_id,
                "text": opt["text"],
                "why_incorrect": opt["why_incorrect"]
            })
            if opt["is_correct"]:
                correct_ids.append(opt_id)
                
        # Build explanation
        exp_summary_en = f"The correct answer is: {', '.join(correct_en) if isinstance(correct_en, list) else correct_en}."
        exp_summary_ru = f"Правильный ответ: {', '.join(correct_ru) if isinstance(correct_ru, list) else correct_ru}."
        
        formatted.append({
            "id": qid,
            "domain": "billing",
            "difficulty": diff,
            "q": {
                "en": q_en,
                "ru": q_ru
            },
            "options": opts_list,
            "correct_ids": correct_ids,
            "services": services,
            "explanation": {
                "summary_en": exp_summary_en,
                "summary_ru": exp_summary_ru,
                "detailed_en": why_correct_en,
                "detailed_ru": why_correct_ru
            }
        })
    return formatted

if __name__ == "__main__":
    qs = format_questions()
    print(f"Generated {len(qs)} Domain 4 questions.")
    with open("data/domain4_72.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("Saved to data/domain4_72.json")
