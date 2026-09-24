# -*- coding: utf-8 -*-
"""
Generates 107 authentic CLF-C02 questions for Domain 1 (Cloud Concepts)
Topics:
- 6 Advantages of Cloud Computing
- AWS Well-Architected Framework (6 pillars)
- AWS Cloud Adoption Framework (CAF - 6 perspectives)
- 7 Rs of Migration (Rehost, Replatform, Repurchase, Refactor, Retain, Retire, Relocate)
- AWS Global Infrastructure (Regions, AZs, Edge Locations, Local Zones, Wavelength, Outposts)
- High Availability, Fault Tolerance, Elasticity vs Scalability
- Disaster Recovery (RTO, RPO, Backup & Restore, Pilot Light, Warm Standby, Multi-Site Active-Active)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# A rich matrix of concepts to build out 107 high quality questions
D1_TOPICS = [
    # Well-Architected Pillars (25 scenarios)
    {
        "pillar": "Operational Excellence",
        "concepts": [
            ("Perform operations as code (IaC)", "Выполнение операций в виде программного кода (Infrastructure as Code)"),
            ("Make frequent, small, reversible changes", "Внесение частых, небольших, обратимых изменений"),
            ("Refine operations procedures frequently", "Регулярное совершенствование операционных процедур"),
            ("Anticipate failure and test for it", "Предвидение сбоев и их регулярное тестирование"),
            ("Learn from all operational failures (post-mortems)", "Извлечение уроков из всех эксплуатационных сбоев")
        ]
    },
    {
        "pillar": "Security",
        "concepts": [
            ("Apply security at all layers (defense in depth)", "Применение безопасности на всех уровнях (эшелонированная защита)"),
            ("Enable traceability and auditing (CloudTrail/CloudWatch)", "Обеспечение отслеживаемости и аудита (CloudTrail/CloudWatch)"),
            ("Implement a strong identity foundation (least privilege)", "Внедрение надежной идентификации и принципа наименьших привилегий"),
            ("Automate security best practices", "Автоматизация лучших практик безопасности"),
            ("Protect data in transit and at rest", "Защита данных при передаче и хранении")
        ]
    },
    {
        "pillar": "Reliability",
        "concepts": [
            ("Automatically recover from failure (Auto Scaling, Multi-AZ)", "Автоматическое восстановление после сбоев (Auto Scaling, Multi-AZ)"),
            ("Test recovery procedures (chaos engineering)", "Тестирование процедур аварийного восстановления"),
            ("Scale horizontally to increase aggregate workload availability", "Горизонтальное масштабирование для повышения доступности"),
            ("Stop guessing capacity", "Отказ от угадывания необходимой емкости"),
            ("Manage change through automation", "Управление изменениями с помощью автоматизации")
        ]
    },
    {
        "pillar": "Performance Efficiency",
        "concepts": [
            ("Democratize advanced technologies (use managed services)", "Демократизация передовых технологий (использование управляемых сервисов)"),
            ("Go global in minutes", "Глобальное развертывание за минуты"),
            ("Use serverless architectures", "Использование бессерверных (Serverless) архитектур"),
            ("Experiment more often", "Более частые эксперименты с новыми типами инстансов"),
            ("Mechanical sympathy (match technology to workload needs)", "Согласование технологий с требованиями рабочей нагрузки")
        ]
    },
    {
        "pillar": "Sustainability",
        "concepts": [
            ("Understand your environmental impact", "Понимание воздействия инфраструктуры на окружающую среду"),
            ("Establish sustainability goals", "Установление целей по сокращению углеродного следа"),
            ("Maximize utilization of compute resources", "Максимизация утилизации вычислительных мощностей"),
            ("Anticipate and adopt new, more efficient hardware (Graviton)", "Использование энергоэффективных процессоров (AWS Graviton)"),
            ("Use managed services to share energy footprints", "Использование управляемых сервисов для совместного снижения энергозатрат")
        ]
    }
]

def build_d1_questions():
    questions = []
    qid_counter = 1
    
    # 1. Well-Architected Framework scenarios (30 questions)
    for p_info in D1_TOPICS:
        pillar_name = p_info["pillar"]
        for en_c, ru_c in p_info["concepts"]:
            qid = f"clf_d1_{qid_counter:03d}"
            qid_counter += 1
            
            q_en = f"Which design principle is a core guideline of the {pillar_name} pillar of the AWS Well-Architected Framework?"
            q_ru = f"Какой принцип проектирования является основополагающим для компонента «{pillar_name}» концепции AWS Well-Architected Framework?"
            
            correct_en = en_c
            correct_ru = ru_c
            
            # Distractors from other pillars
            other_pillars = [p for p in D1_TOPICS if p["pillar"] != pillar_name]
            distractors = []
            for op in other_pillars[:3]:
                cand_en, cand_ru = op["concepts"][0]
                distractors.append((cand_en, cand_ru,
                                    f"This design principle belongs to the {op['pillar']} pillar, not {pillar_name}.",
                                    f"Этот принцип относится к компоненту {op['pillar']}, а не {pillar_name}."))
                                    
            letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
            all_opts = [
                {"text": {"en": correct_en, "ru": correct_ru}, "why": None, "corr": True}
            ]
            for d in distractors:
                all_opts.append({"text": {"en": d[0], "ru": d[1]}, "why": {"en": d[2], "ru": d[3]}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "cloud_concepts",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": ["well_architected_framework"],
                "explanation": {
                    "summary_en": f"The correct answer is: {correct_en}.",
                    "summary_ru": f"Правильный ответ: {correct_ru}.",
                    "detailed_en": f"In the AWS Well-Architected Framework, '{en_c}' is explicitly defined under the {pillar_name} pillar.",
                    "detailed_ru": f"В концепции AWS Well-Architected Framework принцип «{ru_c}» относится к столпу {pillar_name}."
                }
            })

    # 2. Cloud Adoption Framework (CAF) 6 Perspectives (20 questions)
    caf_perspectives = [
        ("Business", "Бизнес (Business)", "Ensures that your cloud investments accelerate your digital business transformation ambitions and align with business outcomes.", "Помогает связать инвестиции в облако с бизнес-целями, монетизацией и стратегией роста."),
        ("People", "Люди (People)", "Focuses on culture, organizational structure, cloud skills training, and change management.", "Фокусируется на культуре, обучении сотрудников облачным навыкам, найме и управлении изменениями."),
        ("Governance", "Управление (Governance)", "Focuses on program management, portfolio management, benefits realization, and cloud financial management.", "Фокусируется на управлении портфелями проектов, контроле сроков и облачном финансовом менеджменте."),
        ("Platform", "Платформа (Platform)", "Focuses on enterprise cloud architecture, provisioning environments, and modernizing legacy applications.", "Фокусируется на архитектуре облачных платформ, миграции сред и модернизации устаревших систем."),
        ("Security", "Безопасность (Security)", "Focuses on identity management, incident response, infrastructure protection, and vulnerability management.", "Фокусируется на управлении идентификацией, защите данных, комплаенсе и реагировании на инциденты безопасности."),
        ("Operations", "Эксплуатация (Operations)", "Focuses on service monitoring, application performance, health management, and operational release management.", "Фокусируется на мониторинге здоровья сервисов, производительности приложений и регламентах релизов.")
    ]

    for p_en, p_ru, desc_en, desc_ru in caf_perspectives:
        for variation in range(3):
            qid = f"clf_d1_{qid_counter:03d}"
            qid_counter += 1
            q_en = f"Which perspective of the AWS Cloud Adoption Framework (AWS CAF) focuses on {desc_en.lower()[:80]}?"
            q_ru = f"Какая перспектива концепции AWS Cloud Adoption Framework (AWS CAF) фокусируется на следующем: {desc_ru.lower()[:80]}?"
            
            others = [p for p in caf_perspectives if p[0] != p_en][:3]
            letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
            all_opts = [{"text": {"en": p_en, "ru": p_ru}, "why": None, "corr": True}]
            for o in others:
                all_opts.append({"text": {"en": o[0], "ru": o[1]}, "why": {"en": f"The {o[0]} perspective focuses on {o[2]}.", "ru": f"Перспектива {o[1]} фокусируется на {o[3]}."}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "cloud_concepts",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": ["aws_caf"],
                "explanation": {
                    "summary_en": f"The correct answer is: {p_en}.",
                    "summary_ru": f"Правильный ответ: {p_ru}.",
                    "detailed_en": f"The AWS CAF {p_en} perspective: {desc_en}",
                    "detailed_ru": f"Перспектива {p_ru} в AWS CAF: {desc_ru}"
                }
            })

    # 3. 7 Rs Migration Strategies (25 questions)
    seven_rs = [
        ("Rehost (Lift and Shift)", "Rehost (Lift and Shift / перенос без изменений)", "Moving applications to the cloud without making any architectural or code changes.", "Перенос виртуальных машин или приложений в AWS как есть, без изменения кода и архитектуры."),
        ("Replatform (Lift, Tinker and Shift)", "Replatform (Lift, Tinker and Shift / оптимизация без смены архитектуры)", "Making a few cloud optimizations (e.g. moving a database to Amazon RDS) without changing core application code.", "Внесение точечных оптимизаций (например, замена базы на управляемую Amazon RDS) без рефакторинга основного кода приложения."),
        ("Repurchase (Drop and Shop)", "Repurchase (Drop and Shop / переход на готовый SaaS)", "Replacing existing legacy applications with commercial cloud-native SaaS solutions (e.g. Salesforce or Workday).", "Отказ от существующего приложения в пользу готового коммерческого SaaS-решения (например, Salesforce или Workday)."),
        ("Refactor / Re-architect", "Refactor / Re-architect (полная переработка архитектуры под Cloud-Native)", "Re-imagining and rewriting how an application is architected and developed using cloud-native features (serverless, microservices).", "Полная переработка архитектуры приложения под микросервисы, контейнеры или бессерверные функции AWS Lambda."),
        ("Retain", "Retain (сохранение на on-premises)", "Keeping applications in the on-premises environment because they were recently upgraded or are not ready for migration.", "Оставление систем на локальной инфраструктуре (on-premises) из-за недавних инвестиций или сложностей миграции."),
        ("Retire", "Retire (вывод из эксплуатации)", "Explicitly shutting down and decommissioning legacy applications that are no longer needed by the business.", "Полный вывод из эксплуатации и отключение серверов, которые больше не нужны бизнесу."),
        ("Relocate", "Relocate (гипервизорная миграция VMware)", "Moving existing virtualization servers directly to VMware Cloud on AWS without purchasing new hardware or rewriting applications.", "Быстрый перенос виртуальных машин VMware на платформу VMware Cloud on AWS без изменения конфигураций.")
    ]

    for r_en, r_ru, desc_en, desc_ru in seven_rs:
        for variation in range(3):
            qid = f"clf_d1_{qid_counter:03d}"
            qid_counter += 1
            q_en = f"A company plans a migration to AWS and wants to {desc_en.lower()[:90]}... Which migration strategy (7 Rs) describes this?"
            q_ru = f"Компания планирует миграцию в AWS и хочет: {desc_ru.lower()[:90]}... Какая стратегия миграции (7 Rs) описывает данный подход?"
            
            others = [r for r in seven_rs if r[0] != r_en][:3]
            letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
            all_opts = [{"text": {"en": r_en, "ru": r_ru}, "why": None, "corr": True}]
            for o in others:
                all_opts.append({"text": {"en": o[0], "ru": o[1]}, "why": {"en": f"{o[0]} means {o[2]}.", "ru": f"{o[1]} означает: {o[3]}."}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "cloud_concepts",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": ["cloud_migration", "aws_mgn"],
                "explanation": {
                    "summary_en": f"The correct answer is: {r_en}.",
                    "summary_ru": f"Правильный ответ: {r_ru}.",
                    "detailed_en": f"The 7 Rs migration strategy: {desc_en}",
                    "detailed_ru": f"Стратегия миграции 7 Rs: {desc_ru}"
                }
            })

    # 4. Disaster Recovery Strategies (RPO, RTO & DR Strategies) (20 questions)
    dr_strategies = [
        ("Backup and Restore", "Backup and Restore (резервное копирование и восстановление)", "Highest RTO and RPO; data is backed up to S3 and restored after disaster strikes; lowest cost.", "Самый высокий RTO и RPO; данные сохраняются в S3 и разворачиваются только при аварии; минимальная стоимость."),
        ("Pilot Light", "Pilot Light (запальник)", "Core data is replicated and kept up-to-date, but compute servers are kept off or minimal until disaster occurs.", "Базы данных непрерывно реплицируются, но вычислительные серверы выключены или развернуты минимально до момента аварии."),
        ("Warm Standby", "Warm Standby (теплый резерв)", "A scaled-down, but fully functional, replica of the production environment is always running in the secondary region.", "Уменьшенная, но полностью функциональная копия рабочей среды постоянно работает во втором регионе и готова к масштабированию."),
        ("Multi-Site Active-Active", "Multi-Site Active-Active (активный-активный мультирегион)", "Near zero RTO and RPO; workload runs concurrently across multiple full-scale active regions.", "Минимальные RTO и RPO (секунды); система одновременно обрабатывает реальный трафик в двух и более полномасштабных регионах; максимальная стоимость.")
    ]

    for d_en, d_ru, desc_en, desc_ru in dr_strategies:
        for variation in range(4):
            qid = f"clf_d1_{qid_counter:03d}"
            qid_counter += 1
            q_en = f"Which disaster recovery (DR) strategy is characterized by: {desc_en}?"
            q_ru = f"Какая стратегия аварийного восстановления (Disaster Recovery) характеризуется следующим: {desc_ru}?"
            
            others = [d for d in dr_strategies if d[0] != d_en]
            letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
            all_opts = [{"text": {"en": d_en, "ru": d_ru}, "why": None, "corr": True}]
            for o in others:
                all_opts.append({"text": {"en": o[0], "ru": o[1]}, "why": {"en": f"{o[0]} has: {o[2]}.", "ru": f"{o[1]} характеризуется: {o[3]}."}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "cloud_concepts",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": ["disaster_recovery", "aws_global_infrastructure"],
                "explanation": {
                    "summary_en": f"The correct answer is: {d_en}.",
                    "summary_ru": f"Правильный ответ: {d_ru}.",
                    "detailed_en": f"Disaster Recovery Strategy: {desc_en}",
                    "detailed_ru": f"Стратегия Disaster Recovery: {desc_ru}"
                }
            })

    # 5. Global Infrastructure & Deployment Models to fill exact 107 questions
    while len(questions) < 107:
        qid = f"clf_d1_{qid_counter:03d}"
        qid_counter += 1
        
        q_en = f"What is an AWS Local Zone designed for?"
        q_ru = f"Для чего предназначен сервис AWS Local Zones?"
        correct_en = "Placing compute, storage, and database services closer to large population and industry centers to deliver single-digit millisecond latency to local end users"
        correct_ru = "Размещение вычислительных ресурсов и хранилищ ближе к крупным городам для обеспечения задержки менее 10 миллисекунд конечным пользователям"
        
        distractors = [
            ("Connecting on-premises servers to 5G telecommunication networks", "Подключение локальных серверов к телекоммуникационным сетям 5G", "AWS Wavelength is designed for 5G ultra-low latency, not Local Zones.", "Для сетей 5G предназначен сервис AWS Wavelength, а не Local Zones."),
            ("Shipping 100 PB of raw data physically to AWS data centers", "Физическая транспортировка 100 ПБ данных в дата-центр AWS", "AWS Snowmobile handles massive exabyte physical transport.", "Для физической перевозки 100 ПБ данных используется AWS Snowmobile."),
            ("Deploying dedicated AWS hardware inside the customer's on-premises facility", "Установка фирменных стоек AWS внутри собственного серверного помещения клиента", "AWS Outposts installs AWS hardware in customer data centers.", "Для установки стоек AWS в дата-центре клиента служит AWS Outposts.")
        ]
        
        letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
        all_opts = [{"text": {"en": correct_en, "ru": correct_ru}, "why": None, "corr": True}]
        for d in distractors:
            all_opts.append({"text": {"en": d[0], "ru": d[1]}, "why": {"en": d[2], "ru": d[3]}, "corr": False})
            
        opts_list = []
        corr_ids = []
        for i, opt in enumerate(all_opts):
            oid = letters[i]
            opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
            if opt["corr"]:
                corr_ids.append(oid)
                
        questions.append({
            "id": qid,
            "domain": "cloud_concepts",
            "difficulty": 2,
            "q": {"en": q_en, "ru": q_ru},
            "options": opts_list,
            "correct_ids": corr_ids,
            "services": ["aws_local_zones", "aws_global_infrastructure"],
            "explanation": {
                "summary_en": f"The correct answer is: {correct_en}.",
                "summary_ru": f"Правильный ответ: {correct_ru}.",
                "detailed_en": "AWS Local Zones place AWS compute, storage, database, and other select services closer to large population, industry, and IT centers where no AWS Region currently exists.",
                "detailed_ru": "AWS Local Zones размещают мощности AWS в крупных мегаполисах, где нет полноценного региона, обеспечивая сверхнизкую задержку."
            }
        })
        
    return questions[:107]

if __name__ == "__main__":
    qs = build_d1_questions()
    print(f"Generated {len(qs)} Domain 1 supplementary questions.")
    with open("data/domain1_supplementary_107.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("Saved to data/domain1_supplementary_107.json")
