# -*- coding: utf-8 -*-
"""
Generator for Domain 4: Billing, Pricing, and Support (72 authentic questions)
CLF-C02 Syllabus compliant, Jon Bonso style with detailed why_incorrect explanations.
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_domain4():
    items = []

    # 1. AWS Support Plans (Developer, Business, Enterprise On-Ramp, Enterprise) - 15 questions
    support_scenarios = [
        {
            "id": "clf_bill_001",
            "q_en": "A company is planning to migrate mission-critical production workloads to AWS and requires 24/7 access to Senior Cloud Support Engineers by phone, chat, and email, along with a guaranteed response time of under 15 minutes for business-critical system down events. A designated Technical Account Manager (TAM) is also required. Which AWS Support plan meets these requirements?",
            "q_ru": "Компания планирует миграцию критически важных рабочих нагрузок в AWS и требует круглосуточного доступа (24/7) к старшим инженерам поддержки по телефону, в чате и по email с гарантированным временем ответа менее 15 минут при сбое критически важных систем. Также требуется выделенный Technical Account Manager (TAM). Какой план поддержки AWS необходим?",
            "correct": "Enterprise Support",
            "correct_why_en": "AWS Enterprise Support includes 24/7 technical support by phone, email, and chat, <15 minute response time for business-critical system down events, a designated Technical Account Manager (TAM), and consultative architectural reviews.",
            "correct_why_ru": "AWS Enterprise Support включает круглосуточную поддержку 24/7 по телефону, почте и чату, время ответа менее 15 минут при отказе критических систем, персонального Technical Account Manager (TAM) и архитектурные обзоры.",
            "distractors": [
                ("Business Support",
                 "Business Support provides 24/7 access to Cloud Support Engineers and a 1-hour response time for production down, but does not provide a designated TAM or <15 min response time.",
                 "Business Support обеспечивает доступ 24/7 и ответ до 1 часа при сбое продакшена, но не включает персонального TAM и ответ менее 15 минут."),
                ("Enterprise On-Ramp Support",
                 "Enterprise On-Ramp includes a pool of TAMs (not a designated dedicated TAM) and a 30-minute response time for business-critical events.",
                 "Enterprise On-Ramp предоставляет пул TAM (а не персонального выделенного TAM) и гарантирует ответ до 30 минут, а не 15."),
                ("Developer Support",
                 "Developer Support only provides business-hours email access to Cloud Support Associates with response times of 12 to 24 hours.",
                 "Developer Support предоставляет доступ только по email в рабочие часы и время ответа от 12 до 24 часов.")
            ],
            "services": ["aws_support", "aws_enterprise_support", "aws_business_support"]
        },
        {
            "id": "clf_bill_002",
            "q_en": "A startup with limited budget needs AWS technical support during local business hours via email, with general architectural guidance on building on AWS. Which is the lowest-cost paid AWS Support plan that meets these needs?",
            "q_ru": "Стартап с ограниченным бюджетом нуждается в технической поддержке AWS в рабочие часы по электронной почте и базовых архитектурных рекомендациях. Какой самый недорогой платный план поддержки AWS удовлетворяет этим требованиям?",
            "correct": "Developer Support",
            "correct_why_en": "Developer Support is the most cost-effective paid plan ($29/month or 3% of monthly AWS usage). It provides business-hours access to Cloud Support Associates via email and general architectural guidance.",
            "correct_why_ru": "Developer Support — минимальный платный тариф ($29/мес или 3% от счета). Дает доступ к Cloud Support Associates по email в рабочие часы и общие архитектурные рекомендации.",
            "distractors": [
                ("Basic Support",
                 "Basic Support is free for all customers, but does not provide access to technical support engineers or 1-on-1 architectural guidance.",
                 "Basic Support бесплатен, но не дает доступа к инженерам техподдержки и индивидуальным консультациям."),
                ("Business Support",
                 "Business Support costs at least $100/month and provides 24/7 phone/chat access, which exceeds the startup's minimal requirement.",
                 "Business Support стоит от $100/мес и ориентирован на круглосуточную эксплуатацию рабочих нагрузок."),
                ("Enterprise On-Ramp Support",
                 "Enterprise On-Ramp starts at $5,500/month and is designed for enterprise-scale workloads.",
                 "Enterprise On-Ramp начинается от $5,500/мес и предназначен для крупных корпоративных систем.")
            ],
            "services": ["aws_support", "aws_developer_support"]
        },
        {
            "id": "clf_bill_003",
            "q_en": "Which feature is available to customers on the AWS Basic Support plan at no extra charge? (Select TWO)",
            "q_ru": "Какие возможности доступны клиентам на бесплатном плане AWS Basic Support без дополнительной оплаты? (Выберите ДВА)",
            "correct": ["AWS Health Dashboard and AWS Health API", "7 Core AWS Trusted Advisor checks"],
            "correct_why_en": "All AWS customers with Basic Support get access to the AWS Health Dashboard (personalized health alerts), documentation, whitepapers, re:Post community, billing/account support, and 7 core Trusted Advisor checks.",
            "correct_why_ru": "Все клиенты AWS с Basic Support бесплатно получают доступ к AWS Health Dashboard, 7 базовым проверкам Trusted Advisor, документации, форуму re:Post и поддержке по вопросам биллинга.",
            "distractors": [
                ("24/7 phone access to Cloud Support Engineers",
                 "Phone and chat access to Cloud Support Engineers requires at least the Business Support plan.",
                 "Круглосуточный доступ к инженерам по телефону и чату требует как минимум плана Business Support."),
                ("Infrastructure Event Management (IEM)",
                 "Infrastructure Event Management is included in Enterprise Support and available for purchase in Business Support, but not in Basic.",
                 "Infrastructure Event Management входит в Enterprise и приобретается отдельно в Business, но недоступен в Basic."),
                ("A designated Technical Account Manager (TAM)",
                 "A designated TAM is exclusive to the Enterprise Support plan.",
                 "Персональный выделенный TAM предоставляется исключительно на плане Enterprise Support.")
            ],
            "services": ["aws_support", "aws_trusted_advisor", "aws_health_dashboard"]
        },
        {
            "id": "clf_bill_004",
            "q_en": "A company is preparing for an upcoming Black Friday flash sale and wants AWS experts to review their architecture, prepare operational runbooks, and provide real-time monitoring support during the event. Which AWS Support offering provides this?",
            "q_ru": "Компания готовится к распродаже Black Friday и хочет, чтобы эксперты AWS провели аудит архитектуры, подготовили регламенты реагирования и обеспечили онлайн-мониторинг во время распродажи. Какая опция поддержки AWS предоставляет это?",
            "correct": "AWS Infrastructure Event Management (IEM)",
            "correct_why_en": "AWS Infrastructure Event Management (IEM) is a structured program that provides architectural guidance, operational readiness reviews, and real-time support during critical business launches or flash sales. It is included in Enterprise Support and available as an add-on for Business Support.",
            "correct_why_ru": "AWS Infrastructure Event Management (IEM) — программа поддержки масштабных мероприятий (запуск продуктов, распродажи). Включает аудит архитектуры и мониторинг в реальном времени. Входит в Enterprise Support и доступна для заказа в Business Support.",
            "distractors": [
                ("AWS Concierge Support",
                 "Concierge Support assists only with billing and account administration inquiries, not operational infrastructure readiness.",
                 "Concierge Support помогает исключительно с вопросами счетов, договоров и биллинга, а не с архитектурой и пиковыми нагрузками."),
                ("AWS Systems Manager",
                 "AWS Systems Manager is an operational automation and management service, not a team of AWS support experts.",
                 "AWS Systems Manager — это сервис автоматизации и управления конфигурациями, а не команда экспертов поддержки."),
                ("AWS Trusted Advisor",
                 "Trusted Advisor provides automated best practice recommendations, but cannot provide active human event monitoring or custom operational runbooks.",
                 "Trusted Advisor предоставляет автоматические рекомендации, но не может осуществлять ручной мониторинг и планирование событий в реальном времени.")
            ],
            "services": ["aws_support", "aws_infrastructure_event_management"]
        },
        {
            "id": "clf_bill_005",
            "q_en": "A financial company needs assistance with billing and account management questions, such as invoice analysis and consolidated billing optimization across 50 accounts. Which AWS team is dedicated to assisting with billing and account administration for Enterprise Support customers?",
            "q_ru": "Финансовой компании требуется помощь с вопросами биллинга и управления аккаунтами (анализ счетов, оптимизация консолидированного биллинга по 50 аккаунтам). Какая команда AWS специализируется на вопросах биллинга и администрирования аккаунтов для клиентов плана Enterprise Support?",
            "correct": "AWS Concierge Support Team",
            "correct_why_en": "The AWS Concierge Support team consists of senior billing and account management experts dedicated to addressing billing, account, and invoicing inquiries for Enterprise and Enterprise On-Ramp customers.",
            "correct_why_ru": "Команда AWS Concierge Support состоит из экспертов по биллингу и аккаунтам, которые помогают корпоративным клиентам с вопросами выставления счетов, консолидации и анализа затрат.",
            "distractors": [
                ("Technical Account Manager (TAM)",
                 "A TAM focuses on technical architecture, proactive operational health, and strategic guidance, while Concierge handles billing administrative matters.",
                 "TAM фокусируется на технической архитектуре, стабильности и лучших практиках, в то время как биллинговые вопросы решает Concierge."),
                ("AWS Trust & Safety",
                 "The AWS Trust & Safety team handles abusive activities such as phishing, spam, and denial-of-service originating from AWS resources.",
                 "AWS Trust & Safety занимается расследованием нарушений (спам, сканирование портов, DoS-атаки, фишинг)."),
                ("AWS Managed Services (AMS)",
                 "AWS Managed Services provides ongoing operational management of AWS infrastructure for enterprise customers, not billing support.",
                 "AWS Managed Services (AMS) осуществляет круглосуточную эксплуатацию облачной инфраструктуры заказчика.")
            ],
            "services": ["aws_support", "aws_concierge_support"]
        }
    ]

    # Let's generate a total of 72 rich billing questions
    # We will build out 72 questions covering:
    # - Support Plans & Teams (clf_bill_001 .. 018)
    # - Budgets & Cost Explorer (clf_bill_019 .. 036)
    # - CUR, Pricing Calculator, Marketplace & TCO (clf_bill_037 .. 054)
    # - Organizations, Consolidated Billing & Discounts (clf_bill_055 .. 072)
    return support_scenarios

print("Domain 4 builder script template ready.")
