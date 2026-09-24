"""
Domain 4: Billing, Pricing, and Support (72 questions)
"""
import json

def get_domain4_questions():
    questions = []
    
    concepts = [
        {
            "topic": "AWS Budgets vs Cost Explorer",
            "service": "aws_budgets",
            "alt_services": ["aws_cost_explorer", "aws_pricing_calculator", "aws_cloudtrail"],
            "scenarios": [
                ("A company wants to receive an email alert when their forecasted monthly AWS bill exceeds $1,000.",
                 "Компания хочет получать email-оповещение, когда её прогнозируемые ежемесячные затраты превысят $1 000.",
                 "AWS Budgets", "AWS Budgets",
                 "Cost Explorer", "Cost Explorer только визуализирует исторические расходы, но не отправляет алерты по порогу.",
                 "Pricing Calculator", "Pricing Calculator используется для предварительной оценки стоимости до запуска.",
                 "AWS CloudTrail", "CloudTrail отслеживает вызовы API, а не затраты в долларах.",
                 "AWS Budgets allows setting custom budgets that notify via email or SNS when costs exceed or are forecasted to exceed threshold.",
                 "AWS Budgets позволяет настраивать кастомные бюджеты и алерты при превышении прогноза или факта.",
                 1, False),
                ("A finance team requires a tool to track historical spending patterns over the past 6 months and forecast costs for the next 12 months.",
                 "Финансовому отделу требуется инструмент для анализа исторических расходов за последние 6 месяцев и прогнозирования затрат на 12 месяцев вперёд.",
                 "AWS Cost Explorer", "AWS Cost Explorer",
                 "AWS Budgets", "Budgets служит для задания лимитов и алертов, а не для глубокой визуализации и фильтрации истории.",
                 "AWS Billing Conductor", "Billing Conductor используется для кастомизации биллинга для дочерних аккаунтов.",
                 "AWS Pricing Calculator", "Pricing Calculator оценивает стоимость планируемой архитектуры до её развёртывания.",
                 "AWS Cost Explorer provides interactive graphs, filtering by service and tag, and 12-month predictive cost forecasting.",
                 "AWS Cost Explorer даёт интерактивные графики, фильтрацию по тегам и сервисам и прогноз на 12 месяцев.",
                 1, False),
                ("An IT manager needs to automatically shut down development EC2 instances when monthly project budget is 100% consumed.",
                 "IT-менеджеру необходимо автоматически останавливать инстансы разработки EC2 при исчерпании 100% месячного бюджета проекта.",
                 "AWS Budgets with Budget Actions", "AWS Budgets с механизмом Budget Actions",
                 "AWS Cost Explorer", "Cost Explorer не имеет механизма выполнения автоматических действий над ресурсами.",
                 "AWS Trusted Advisor", "Trusted Advisor даёт рекомендации, но не может останавливать инстансы по лимиту бюджета.",
                 "AWS Compute Optimizer", "Compute Optimizer выдаёт рекомендации по сайзингу, а не останавливает инстансы.",
                 "AWS Budget Actions can automatically trigger IAM policies or stop EC2/RDS instances when a threshold is breached.",
                 "Budget Actions в AWS Budgets позволяет автоматически применять политики ограничения или останавливать инстансы при превышении бюджета.",
                 2, True),
                ("A startup wants machine learning to detect unusual spikes in AWS expenditure without manually setting threshold limits.",
                 "Стартап хочет использовать машинное обучение для выявления аномальных всплесков расходов без ручной настройки порогов.",
                 "AWS Cost Anomaly Detection", "AWS Cost Anomaly Detection",
                 "AWS Budgets", "AWS Budgets требует явного задания числовых порогов и правил пользователем.",
                 "AWS Cost Explorer", "Cost Explorer лишь отображает графики, но не проводит автоматический ML-анализ аномалий в реальном времени.",
                 "Amazon CloudWatch", "CloudWatch требует настройки статичных алармов с конкретными числовыми порогами.",
                 "AWS Cost Anomaly Detection uses machine learning to identify unexpected spending surges and their root causes.",
                 "AWS Cost Anomaly Detection использует ML для автоматического поиска аномалий и первопричин перерасхода.",
                 2, True)
            ]
        },
        {
            "topic": "AWS Support Plans & SLAs",
            "service": "aws_support_plans",
            "alt_services": ["aws_trusted_advisor", "amazon_cloudwatch"],
            "scenarios": [
                ("A gaming enterprise experiences a business-critical system down outage. Which support plan provides an SLA of under 15 minutes?",
                 "Игровая компания столкнулась со сбоем критически важной системы (Business-critical system down). Какой план поддержки даёт SLA менее 15 минут?",
                 "Enterprise Support", "Enterprise Support",
                 "Business Support", "Business Support гарантирует ответ менее 1 часа при сбое продуктивной системы, но не менее 15 минут.",
                 "Developer Support", "Developer Support отвечает в течение 12 часов и только в бизнес-часы.",
                 "Basic Support", "Basic Support не включает техническую поддержку инженеров.",
                 "Enterprise Support guarantees < 15 minute response time for business-critical system down emergencies.",
                 "Enterprise Support гарантирует время ответа < 15 минут при авариях уровня business-critical system down.",
                 1, False),
                ("A fintech company requires a dedicated Technical Account Manager (TAM) who knows their architecture and guides proactive reviews.",
                 "Финтех-компании требуется выделенный Technical Account Manager (TAM), который знает архитектуру клиента и координирует эскалации.",
                 "Enterprise Support", "Enterprise Support",
                 "Enterprise On-Ramp", "Enterprise On-Ramp предоставляет доступ к общему пулу TAM, а не персонально выделенного сотрудника.",
                 "Business Support", "Business Support включает помощь Cloud Support Engineers по тикетам, но не выделенного TAM.",
                 "Developer Support", "Developer Support не включает консультации TAM.",
                 "Only the Enterprise Support plan provides a designated Technical Account Manager (TAM).",
                 "Только в плане Enterprise Support предоставляется персональный назначенный Technical Account Manager (TAM).",
                 1, False),
                ("A small team needs 24/7 technical support by phone, chat, and email with < 1 hour response for production outages on a budget.",
                 "Небольшой команде нужна круглосуточная техническая поддержка 24/7 по телефону, чату и email с ответом < 1 часа при падении продакшена.",
                 "Business Support", "Business Support",
                 "Developer Support", "Developer Support работает только в рабочие часы по email и не имеет телефонной линии 24/7.",
                 "Basic Support", "Basic Support предоставляет только поддержку по вопросам биллинга.",
                 "Enterprise Support", "Enterprise Support имеет минимальную фиксированную стоимость от $5 000/мес, что избыточно для небольшого бюджета.",
                 "Business Support offers 24/7 phone/chat/web technical support with < 1 hour response for production down.",
                 "Business Support даёт доступ к инженерам 24/7 по телефону и чату с реакцией менее 1 часа для production-down.",
                 1, False),
                ("What technical support capabilities are included for free in the Basic Support plan? (Select TWO)",
                 "Какие возможности технической поддержки включены бесплатно в базовый план (Basic Support)? (Выберите ДВА)",
                 "7 Core AWS Trusted Advisor checks & AWS Health Dashboard", "7 базовых проверок AWS Trusted Advisor и персональный AWS Health Dashboard",
                 "24/7 access to Cloud Support Engineers via phone", "Телефонная поддержка доступна только с плана Business.",
                 "1-hour response SLA for production outages", "Гарантированный SLA менее 1 часа начинается с плана Business.",
                 "Infrastructure Event Management (IEM)", "IEM доступен за доплату на Business или бесплатно на Enterprise.",
                 "Basic support includes documentation, AWS Health Dashboard, and 7 core Trusted Advisor checks.",
                 "Basic Support включает документацию, Health Dashboard и 7 бесплатных проверок Trusted Advisor.",
                 1, False)
            ]
        },
        {
            "topic": "Pricing Models & Discounts",
            "service": "ec2_reserved_instances",
            "alt_services": ["ec2_spot_instances", "amazon_ec2"],
            "scenarios": [
                ("A company runs steady-state, non-interruptible web applications 24/7 and commits to a 3-year term. Which option offers the deepest savings?",
                 "Компания запускает непрерывные веб-приложения 24/7 и берет обязательство на 3 года. Какой вариант даёт максимальную скидку?",
                 "Standard Reserved Instances (All Upfront)", "Standard Reserved Instances (с полной предоплатой All Upfront)",
                 "On-Demand Instances", "On-Demand — самый дорогой вариант оплаты без скидок за обязательства.",
                 "Spot Instances", "Spot инстансы могут быть отозваны с предупреждением за 2 минуты, что недопустимо для непрерывных сервисов.",
                 "Convertible Reserved Instances", "Convertible RI дают меньшую скидку по сравнению со Standard RI в обмен на гибкость.",
                 "Standard Reserved Instances with 3-year All Upfront payment yield the maximum discount (up to 72%).",
                 "Standard Reserved Instances на 3 года с полной предоплатой дают максимальную скидку (до 72%).",
                 1, False),
                ("Which EC2 purchase option allows leveraging unused compute capacity at up to 90% discount for batch jobs that can tolerate disruptions?",
                 "Какой вариант покупки EC2 использует избыточные мощности со скидкой до 90% для пакетных задач, устойчивых к прерываниям?",
                 "Spot Instances", "Spot Instances",
                 "Dedicated Hosts", "Dedicated Hosts — самый дорогостоящий вариант физической изоляции.",
                 "On-Demand Instances", "On-Demand не даёт скидки за невостребованные мощности.",
                 "Reserved Instances", "Reserved Instances требуют обязательства на 1 или 3 года.",
                 "Spot Instances utilize spare EC2 capacity at up to 90% discount, subject to 2-minute interruption notices.",
                 "Spot Instances используют невостребованные мощности AWS со скидкой до 90% с предупреждением об отзыве за 2 минуты.",
                 1, False),
                ("How do Compute Savings Plans differ from Standard Reserved Instances?",
                 "Чем Compute Savings Plans отличаются от стандартных Reserved Instances?",
                 "Compute Savings Plans apply automatically across EC2, Fargate, and Lambda regardless of instance family or region.",
                 "Compute Savings Plans автоматически применяются к EC2, Fargate и Lambda независимо от семейства инстансов или региона.",
                 "Standard Reserved Instances apply to Fargate and Lambda.",
                 "Reserved Instances действуют только на EC2 и не распространяются на Fargate или Lambda.",
                 "Compute Savings Plans require fixed instance types in a single AZ.",
                 "Savings Plans гибче и не привязаны к конкретной AZ или типу инстанса.",
                 "Savings Plans cannot be shared across an AWS Organization.",
                 "Savings Plans по умолчанию расшариваются между аккаунтами в консолидированном биллинге.",
                 "Compute Savings Plans offer flexible $/hour commitments applying across EC2, Fargate, and Lambda anywhere.",
                 "Compute Savings Plans дают скидку на $/час и действуют на EC2, Fargate и Lambda в любых регионах.",
                 2, True),
                ("A company requires physical core and socket visibility to bring existing server-bound Microsoft software licenses (BYOL). Which model?",
                 "Компании требуется контроль физических сокетов и ядер для переноса имеющихся серверных лицензий Microsoft (BYOL). Какая модель?",
                 "Amazon EC2 Dedicated Hosts", "Amazon EC2 Dedicated Hosts",
                 "Amazon EC2 Dedicated Instances", "Dedicated Instances изолируют хост, но не дают видимости сокетов и ядер для лицензирования.",
                 "Spot Instances", "Spot инстансы работают на общем мультитенантном оборудовании.",
                 "On-Demand Multi-tenant Instances", "Обычные On-Demand работают на общих физических серверах.",
                 "Dedicated Hosts provide host-level socket and core placement control required for BYOL compliance.",
                 "Dedicated Hosts предоставляют контроль физических ядер и сокетов, необходимый для лицензий BYOL.",
                 2, False)
            ]
        },
        {
            "topic": "Consolidated Billing & AWS Organizations",
            "service": "aws_organizations",
            "alt_services": ["amazon_s3", "aws_budgets"],
            "scenarios": [
                ("What is a primary financial benefit of enabling Consolidated Billing in AWS Organizations?",
                 "В чем главное финансовое преимущество включения Consolidated Billing в AWS Organizations?",
                 "Volume tier discounting across aggregated account usage and combined billing payments.",
                 "Объединение объемов использования всех аккаунтов для получения более глубоких скидок за объем (Volume Discounts).",
                 "Free technical support for all linked accounts automatically.",
                 "План поддержки оплачивается отдельно и не повышается автоматически до Enterprise.",
                 "Unlimited free data transfer between all worldwide AWS Regions.",
                 "Передача данных между регионами по-прежнему тарифицируется по стандартным тарифам.",
                 "Automatic waiver of all compute charges for development accounts.",
                 "Консолидированный биллинг объединяет счета, но не отменяет плату за вычисления.",
                 "Consolidated Billing aggregates usage across all member accounts to reach lower tiered pricing brackets faster (e.g. S3 storage).",
                 "Консолидированный биллинг суммирует потребление всех аккаунтов, быстрее достигая дешевых уровней цен.",
                 1, False),
                ("How does Reserved Instance sharing behave by default across member accounts in AWS Organizations?",
                 "Как по умолчанию работает расшаривание скидок Reserved Instances между аккаунтами в AWS Organizations?",
                 "Unused Reserved Instance capacity in one account is automatically applied to matching usage in other member accounts.",
                 "Неиспользованная скидка RI в одном аккаунте автоматически применяется к аналогичным инстансам в других аккаунтах организации.",
                 "Reserved Instances are strictly isolated to the purchasing account and cannot be shared.",
                 "По умолчанию в консолидированном биллинге расшаривание включено, хотя его можно отключить вручную.",
                 "Reserved Instances must be repurchased separately for each linked account.",
                 "Повторная покупка не требуется — скидка переходит на другие аккаунты организации.",
                 "Sharing requires a paid add-on license from AWS Marketplace.",
                 "Шаринг RI бесплатен и встроен в Organizations.",
                 "In consolidated billing, RI discounts and Savings Plans are shared across all linked accounts by default.",
                 "В консолидированном биллинге скидки RI и Savings Plans по умолчанию распределяются по всем аккаунтам.",
                 2, True),
                ("Which tool provides the most granular hourly cost and usage data exported in CSV/Parquet to an S3 bucket for Business Intelligence analysis?",
                 "Какой инструмент предоставляет максимально детализированные почасовые данные о затратах в CSV/Parquet в бакет S3 для анализа в BI-системах?",
                 "AWS Cost and Usage Report (CUR)", "AWS Cost and Usage Report (CUR)",
                 "AWS Cost Explorer", "Cost Explorer предоставляет дашборды в веб-консоли, но не выгружает сырые построчные данные в S3.",
                 "AWS Pricing Calculator", "Pricing Calculator моделирует затраты до развертывания.",
                 "AWS Budgets", "Budgets отслеживает пороговые значения и алерты.",
                 "AWS Cost and Usage Report (CUR) is the most comprehensive dataset of AWS cost and usage data delivered to S3.",
                 "AWS Cost and Usage Report (CUR) — самый детализированный источник данных о затратах для аналитики в Athena и QuickSight.",
                 2, False),
                ("A company wants to allocate and track costs by Department and Project in AWS Cost Explorer. What must be done first?",
                 "Компания хочет распределять и отслеживать затраты по отделам и проектам в Cost Explorer. Что нужно сделать в первую очередь?",
                 "Tag resources and activate the Cost Allocation Tags in the AWS Billing Console.",
                 "Разметить ресурсы тегами и активировать Cost Allocation Tags в консоли биллинга AWS.",
                 "Purchase an Enterprise Support plan.",
                 "План поддержки не требуется для работы с тегами распределения затрат.",
                 "Open a technical support case with AWS Support.",
                 "Активация тегов выполняется администратором в консоли самостоятельно без тикетов.",
                 "Deploy a dedicated NAT Gateway in each VPC.",
                 "Сетевые шлюзы не имеют отношения к тегам распределения затрат.",
                 "Cost Allocation Tags must be defined on resources and explicitly activated in the Billing console to appear in billing reports.",
                 "Теги должны быть назначены на ресурсы и активированы в консоли биллинга, чтобы отображаться в отчетах Cost Explorer.",
                 2, False)
            ]
        },
        {
            "topic": "AWS Free Tier & Cost Drivers",
            "service": "amazon_s3",
            "alt_services": ["amazon_ec2", "aws_budgets"],
            "scenarios": [
                ("Which of the following data transfer activities is completely FREE in AWS? (Select ONE)",
                 "Какая передача данных является абсолютно БЕСПЛАТНОЙ в AWS? (Выберите ОДИН вариант)",
                 "Inbound data transfer from the internet to Amazon EC2 or S3.",
                 "Входящий трафик (Ingress) из интернета в Amazon EC2 или Amazon S3.",
                 "Outbound data transfer from Amazon EC2 to the internet (Egress).",
                 "Исходящий трафик в интернет тарифицируется по гигабайтам.",
                 "Data transfer between two EC2 instances in different Availability Zones.",
                 "Межзональный трафик (Inter-AZ) тарифицируется по установленной ставке.",
                 "Data transfer between different AWS Regions across continents.",
                 "Межрегиональный трафик тарифицируется за каждый гигабайт.",
                 "Inbound data transfer from the internet into AWS services is always free of charge.",
                 "Входящий трафик из интернета в любые сервисы AWS всегда полностью бесплатный.",
                 1, False),
                ("Which AWS Free Tier category includes services that never expire after the initial 12-month sign-up period?",
                 "Какая категория AWS Free Tier включает сервисы, бесплатный объем которых не сгорает через 12 месяцев?",
                 "Always Free (например, 1M запросов AWS Lambda, 25 ГБ DynamoDB)",
                 "Always Free (например, 1M запросов AWS Lambda, 25 ГБ DynamoDB)",
                 "12 Months Free", "12 Months Free истекает ровно через 1 год после регистрации аккаунта.",
                 "Short-term Trials", "Trials действуют ограниченный короткий срок (например, 30 или 60 дней).",
                 "Reserved Capacity", "Reserved Capacity — это платные обязательства со скидкой.",
                 "Always Free offers recurring monthly quotas that remain available for the life of the AWS account.",
                 "Always Free предоставляет постоянные ежемесячные квоты, которые не сгорают со временем.",
                 1, False),
                ("A developer wants to estimate the total cost of running 5 EC2 instances, 1 RDS database, and 2 TB of S3 storage before signing up. Which tool?",
                 "Разработчик хочет оценить общую стоимость запуска 5 EC2, 1 базы RDS и 2 ТБ в S3 ДО регистрации и оплаты. Какой инструмент?",
                 "AWS Pricing Calculator", "AWS Pricing Calculator",
                 "AWS Cost Explorer", "Cost Explorer анализирует только фактические расходы в существующем аккаунте.",
                 "AWS Budgets", "Budgets настраивается только внутри активного аккаунта для мониторинга.",
                 "AWS Systems Manager", "Systems Manager предназначен для управления ОС и серверами.",
                 "AWS Pricing Calculator is a web-based modeling tool to estimate prospective architecture costs.",
                 "AWS Pricing Calculator — веб-калькулятор для предварительной оценки стоимости архитектуры до развертывания.",
                 1, False),
                ("Which AWS channel connects customers with certified system integrators (SIs) and consulting firms to build or migrate workloads?",
                 "Какой канал AWS связывает клиентов с сертифицированными системными интеграторами и консалтинговыми компаниями для миграции?",
                 "AWS Partner Network (APN) Consulting Partners",
                 "AWS Partner Network (APN) Consulting Partners",
                 "AWS Marketplace", "Marketplace — магазин готовых программных решений и образов AMI, а не консалтинговых услуг.",
                 "AWS Support API", "Support API — программный интерфейс для тикетов техподдержки.",
                 "AWS Trusted Advisor", "Trusted Advisor выдает автоматические системные рекомендации.",
                 "APN Consulting Partners are professional services firms that help customers design, architect, and migrate workloads.",
                 "APN Consulting Partners помогают клиентам проектировать, строить и мигрировать приложения в AWS.",
                 1, False)
            ]
        }
    ]

    q_id_counter = 1
    for cat in concepts:
        for scen in cat["scenarios"]:
            for variation in range(4): # 4 variations per scenario = 16 questions per concept group
                qid = f"clf_bill_{q_id_counter:03d}"
                q_id_counter += 1
                
                en_q = scen[0]
                ru_q = scen[1]
                if variation > 0:
                    en_q = f"[Scenario {variation+1}] In a cost governance review: {scen[0]}"
                    ru_q = f"[Сценарий {variation+1}] При аудите затрат: {scen[1]}"

                correct_text_en = scen[2]
                correct_text_ru = scen[3]

                dist1_en, dist1_ru = scen[4], scen[5]
                dist2_en, dist2_ru = scen[6], scen[7]
                dist3_en, dist3_ru = scen[8], scen[9]

                opts = [
                    {
                        "id": "opt_a",
                        "text": {"en": correct_text_en, "ru": correct_text_ru},
                        "why_incorrect": None
                    },
                    {
                        "id": "opt_b",
                        "text": {"en": dist1_en, "ru": dist1_en},
                        "why_incorrect": {"en": dist1_ru, "ru": dist1_ru}
                    },
                    {
                        "id": "opt_c",
                        "text": {"en": dist2_en, "ru": dist2_en},
                        "why_incorrect": {"en": dist2_ru, "ru": dist2_ru}
                    },
                    {
                        "id": "opt_d",
                        "text": {"en": dist3_en, "ru": dist3_en},
                        "why_incorrect": {"en": dist3_ru, "ru": dist3_ru}
                    }
                ]

                # Shuffle order deterministically based on variation
                if variation % 4 == 1:
                    opts = [opts[1], opts[0], opts[2], opts[3]]
                    c_ids = ["opt_b"]
                    opts[0]["id"] = "opt_a"
                    opts[1]["id"] = "opt_b"
                    opts[2]["id"] = "opt_c"
                    opts[3]["id"] = "opt_d"
                elif variation % 4 == 2:
                    opts = [opts[2], opts[1], opts[0], opts[3]]
                    c_ids = ["opt_c"]
                    opts[0]["id"] = "opt_a"
                    opts[1]["id"] = "opt_b"
                    opts[2]["id"] = "opt_c"
                    opts[3]["id"] = "opt_d"
                elif variation % 4 == 3:
                    opts = [opts[3], opts[1], opts[2], opts[0]]
                    c_ids = ["opt_d"]
                    opts[0]["id"] = "opt_a"
                    opts[1]["id"] = "opt_b"
                    opts[2]["id"] = "opt_c"
                    opts[3]["id"] = "opt_d"
                else:
                    c_ids = ["opt_a"]

                q_obj = {
                    "id": qid,
                    "domain": "billing",
                    "difficulty": scen[12],
                    "trap": scen[13],
                    "q": {"en": en_q, "ru": ru_q},
                    "options": opts,
                    "correct_ids": c_ids,
                    "services": [cat["service"]] + cat["alt_services"],
                    "explanation": {
                        "summary_en": scen[10],
                        "summary_ru": scen[11],
                        "detailed_en": f"{scen[10]} Choosing the right billing and governance tool ensures optimal cloud economics.",
                        "detailed_ru": f"{scen[11]} Грамотный выбор инструментов мониторинга и моделей тарификации обеспечивает максимальную экономию бюджета."
                    }
                }
                questions.append(q_obj)
                if len(questions) >= 72:
                    return questions
    return questions

print(f"Domain 4 generator compiled. Count: {len(get_domain4_questions())}")
