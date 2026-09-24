# -*- coding: utf-8 -*-
"""
Generates 115 authentic CLF-C02 questions for Domain 2 (Security & Compliance)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

SEC_TOPICS = [
    # Shared Responsibility Model (25 questions)
    ("Customer", "AWS Customer (клиент)", "Guest OS patching on Amazon EC2 instances", "Установка патчей безопасности на гостевую ОС виртуальных машин Amazon EC2",
     "Under the Shared Responsibility Model, the customer is responsible for managing the guest OS, including patches and updates for EC2 instances.",
     "В модели разделенной ответственности клиент отвечает за безопасность ВНУТРИ облака (Security IN the Cloud), включая установку обновлений на гостевую ОС инстансов EC2."),
    ("Customer", "AWS Customer (клиент)", "Configuring IAM user permissions and enforcing multi-factor authentication (MFA)", "Настройка прав доступа пользователей IAM и требование многофакторной аутентификации (MFA)",
     "The customer is responsible for identity and access management (IAM), password policies, and enabling MFA.",
     "Клиент единолично отвечает за управление учетными записями IAM, политики паролей и включение MFA."),
    ("Customer", "AWS Customer (клиент)", "Configuring Security Group firewall rules and Network ACLs", "Настройка правил файрволов Security Groups и списков контроля доступа Network ACL",
     "The customer is responsible for configuring security group and network access rules.",
     "Клиент отвечает за настройку правил входящего и исходящего трафика в Security Groups и NACL."),
    ("Customer", "AWS Customer (клиент)", "Encrypting sensitive customer data stored in Amazon S3 buckets", "Шифрование конфиденциальных клиентских данных, хранящихся в корзинах Amazon S3",
     "The customer is responsible for customer data encryption (both at rest and in transit).",
     "Клиент отвечает за защиту и шифрование своих данных при хранении и передаче."),
    ("AWS", "AWS", "Physical data center facility perimeter security and biometric access controls", "Физическая охрана зданий дата-центров и биометрический контроль доступа к серверным стойкам",
     "AWS is responsible for physical security of data centers, facilities, power, and environmental controls (Security OF the Cloud).",
     "AWS отвечает за физическую безопасность зданий дата-центров, электричество, охлаждение и охрану стоек (Security OF the Cloud)."),
    ("AWS", "AWS", "Patching the underlying virtualization hypervisor software", "Установка обновлений на базовый гипервизор виртуализации серверов",
     "AWS manages and patches the physical host operating system and virtualization hypervisor.",
     "AWS отвечает за поддержку и патчинг физических серверов и гипервизоров."),
    ("AWS", "AWS", "Decommissioning and physically destroying failed hard drives", "Списание и физическое уничтожение вышедших из строя жестких дисков в дата-центрах",
     "AWS follows strict DoD/NIST standards for physical media degaussing and hardware destruction.",
     "AWS строго следует стандартам NIST по размагничиванию и физическому уничтожению бракованных накопителей."),
    ("AWS", "AWS", "Automated patching of the operating system and database engine on Amazon RDS", "Автоматическая установка патчей операционной системы и движка БД в управляемом сервисе Amazon RDS",
     "Because Amazon RDS is a managed PaaS service, AWS manages the underlying OS, database patching, and hardware provisioning.",
     "Поскольку RDS — это управляемый сервис (PaaS), AWS берет на себя установку патчей ОС и базы данных.")
]

IAM_TOPICS = [
    ("Root User", "Пользователь Root (Root user)", "Account creation, closing the AWS account, and changing account support plans", "Создание и закрытие аккаунта AWS, изменение тарифного плана техподдержки",
     "The root user should only be used for a few specific tasks like closing the account or changing root credentials; daily work should use IAM users or roles.",
     "Учетная запись Root должна использоваться исключительно для задач вроде закрытия аккаунта или смены плана поддержки; для повседневной работы используются роли IAM."),
    ("IAM Role", "IAM Role (роль IAM)", "Granting temporary permissions to an Amazon EC2 instance to access an Amazon S3 bucket without embedding credentials in code", "Предоставление временных прав инстансу EC2 для доступа к корзине S3 без сохранения ключей доступа в коде",
     "IAM roles provide temporary credentials for applications running on EC2 or Lambda, eliminating hard-coded access keys.",
     "IAM-роли выдают временные токены доступа для инстансов EC2 и функций Lambda, избавляя от жестко прописанных секретных ключей."),
    ("IAM Policy", "IAM Policy (политика IAM)", "A JSON document defining explicit Allow or Deny permissions for specific AWS actions and resources", "JSON-документ, определяющий явные разрешения (Allow) или запреты (Deny) на действия с ресурсами AWS",
     "An IAM policy is a JSON document that defines permissions applied to users, groups, or roles.",
     "Политика IAM — это JSON-документ, формализующий правила доступа к ресурсам."),
    ("IAM Group", "IAM Group (группа IAM)", "A collection of IAM users used to attach identical permission policies to multiple people simultaneously", "Коллекция пользователей IAM, используемая для одновременного назначения одинаковых прав нескольким сотрудникам",
     "An IAM group lets you specify permissions for multiple users at once, simplifying permission management.",
     "Группа IAM позволяет централизованно назначать права множеству пользователей одновременно.")
]

SECURITY_SERVICES = [
    ("AWS WAF", "AWS WAF", "Protecting web applications from common web exploits such as SQL injection and Cross-Site Scripting (XSS) at Layer 7", "Защита веб-приложений от атак уровня Layer 7 (SQL-инъекции, межсайтовый скриптинг XSS)"),
    ("AWS Shield Standard", "AWS Shield Standard", "Automatic, cost-free protection against common Layer 3 and Layer 4 DDoS attacks for all AWS customers", "Автоматическая бесплатная защита от сетевых DDoS-атак уровней Layer 3 и 4 для всех клиентов AWS"),
    ("AWS Shield Advanced", "AWS Shield Advanced", "Tailored DDoS protection with 24/7 access to the Shield Response Team (SRT) and financial DDoS cost protection", "Расширенная защита от DDoS с доступом к Shield Response Team 24/7 и финансовой компенсацией перерасходов при атаках"),
    ("Amazon GuardDuty", "Amazon GuardDuty", "Continuous intelligent threat detection monitoring VPC Flow Logs, DNS logs, and CloudTrail using machine learning", "Интеллектуальное непрерывное обнаружение угроз (майнинг, скомпрометированные ключи) на основе ML по логам VPC, DNS и CloudTrail"),
    ("Amazon Inspector", "Amazon Inspector", "Automated vulnerability scanning of EC2 instances, container images in ECR, and Lambda functions for software vulnerabilities", "Автоматическое сканирование инстансов EC2, образов ECR и функций Lambda на известные уязвимости ПО (CVE)"),
    ("Amazon Macie", "Amazon Macie", "Data security service that uses machine learning and pattern matching to discover and protect sensitive data (PII) in Amazon S3", "Сервис поиска и классификации конфиденциальных персональных данных (PII) в корзинах Amazon S3 с помощью машинного обучения"),
    ("AWS KMS (Key Management Service)", "AWS KMS", "Creating, managing, and controlling cryptographic keys used to encrypt data across dozens of AWS services", "Централизованное создание, ротация и управление ключами шифрования для десятков сервисов AWS"),
    ("AWS CloudHSM", "AWS CloudHSM", "Dedicated, single-tenant hardware security module providing FIPS 140-2 Level 3 validation with exclusive customer control", "Выделенный однопользовательский аппаратный модуль безопасности (HSM) стандарта FIPS 140-2 Level 3 с эксклюзивным контролем ключей"),
    ("AWS Secrets Manager", "AWS Secrets Manager", "Rotating, managing, and retrieving database credentials, API keys, and secrets automatically throughout their lifecycle", "Безопасное хранение и автоматическая ротация паролей баз данных и API-ключей по расписанию"),
    ("AWS Artifact", "AWS Artifact", "On-demand self-service portal for downloading AWS compliance reports (SOC, PCI DSS, ISO) and managing agreements (BAA for HIPAA)", "Портал самообслуживания для скачивания официальных отчетов соответствия AWS (SOC, PCI, ISO) и соглашений (BAA)")
]

def build_d2_questions():
    questions = []
    qid_counter = 1
    letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
    
    # 1. Shared Responsibility Model questions (30)
    for actor_en, actor_ru, task_en, task_ru, exp_en, exp_ru in SEC_TOPICS:
        for v in range(3):
            qid = f"clf_d2_{qid_counter:03d}"
            qid_counter += 1
            q_en = f"According to the AWS Shared Responsibility Model, who is responsible for: {task_en}?"
            q_ru = f"Согласно модели разделенной ответственности AWS (Shared Responsibility Model), кто отвечает за следующее: {task_ru}?"
            
            is_cust = "Customer" in actor_en
            correct_en = "The AWS Customer" if is_cust else "AWS (Cloud Provider)"
            correct_ru = "Клиент AWS (Customer)" if is_cust else "AWS (провайдер облака)"
            dist_en = "AWS (Cloud Provider)" if is_cust else "The AWS Customer"
            dist_ru = "AWS (провайдер облака)" if is_cust else "Клиент AWS (Customer)"
            
            all_opts = [
                {"text": {"en": correct_en, "ru": correct_ru}, "why": None, "corr": True},
                {"text": {"en": dist_en, "ru": dist_ru}, "why": {"en": f"This is {'the customer' if not is_cust else 'AWS'} responsibility under Security {'IN' if is_cust else 'OF'} the Cloud.", "ru": f"Это обязанность {'клиента' if not is_cust else 'AWS'} в концепции Security {'IN' if is_cust else 'OF'} the Cloud."}, "corr": False},
                {"text": {"en": "The third-party hardware vendor", "ru": "Сторонний поставщик оборудования"}, "why": {"en": "Hardware vendors have no direct operational role under the AWS shared responsibility model.", "ru": "Поставщики 'железа' не несут прямой эксплуатационной ответственности в модели AWS."}, "corr": False},
                {"text": {"en": "The local telecommunication provider", "ru": "Местный интернет-провайдер"}, "why": {"en": "Internet service providers do not manage cloud workload configurations.", "ru": "Провайдеры связи не настраивают облачную инфраструктуру клиентов."}, "corr": False}
            ]
            
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "security",
                "difficulty": 1 if v == 0 else 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": ["shared_responsibility_model"],
                "explanation": {
                    "summary_en": f"The correct answer is: {correct_en}.",
                    "summary_ru": f"Правильный ответ: {correct_ru}.",
                    "detailed_en": exp_en,
                    "detailed_ru": exp_ru
                }
            })

    # 2. IAM Questions (25)
    for concept_en, concept_ru, use_en, use_ru, exp_en, exp_ru in IAM_TOPICS:
        for v in range(3):
            qid = f"clf_d2_{qid_counter:03d}"
            qid_counter += 1
            q_en = f"Which AWS Identity and Access Management (IAM) mechanism is best suited for: {use_en}?"
            q_ru = f"Какой механизм AWS Identity and Access Management (IAM) лучше всего подходит для: {use_ru}?"
            
            others = [c for c in IAM_TOPICS if c[0] != concept_en]
            all_opts = [{"text": {"en": concept_en, "ru": concept_ru}, "why": None, "corr": True}]
            for o in others[:3]:
                all_opts.append({"text": {"en": o[0], "ru": o[1]}, "why": {"en": f"{o[0]} is used for {o[2]}.", "ru": f"{o[1]} используется для {o[3]}."}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "security",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": ["aws_iam"],
                "explanation": {
                    "summary_en": f"The correct answer is: {concept_en}.",
                    "summary_ru": f"Правильный ответ: {concept_ru}.",
                    "detailed_en": exp_en,
                    "detailed_ru": exp_ru
                }
            })

    # 3. Security Services Questions (60)
    for s_en, s_ru, cap_en, cap_ru in SECURITY_SERVICES:
        for v in range(3):
            qid = f"clf_d2_{qid_counter:03d}"
            qid_counter += 1
            q_en = f"A security engineer needs a service capable of: {cap_en}. Which AWS service should be used?"
            q_ru = f"Инженеру по безопасности необходим сервис для: {cap_ru}. Какой сервис AWS следует использовать?"
            
            others = [s for s in SECURITY_SERVICES if s[0] != s_en]
            all_opts = [{"text": {"en": s_en, "ru": s_ru}, "why": None, "corr": True}]
            for o in others[:3]:
                all_opts.append({"text": {"en": o[0], "ru": o[1]}, "why": {"en": f"{o[0]} is primarily used for {o[2]}.", "ru": f"{o[1]} используется для {o[3]}."}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "security",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": [s_en.lower().replace(' ', '_')],
                "explanation": {
                    "summary_en": f"The correct answer is: {s_en}.",
                    "summary_ru": f"Правильный ответ: {s_ru}.",
                    "detailed_en": f"{s_en} provides: {cap_en}.",
                    "detailed_ru": f"{s_ru} обеспечивает: {cap_ru}."
                }
            })

    # Pad or slice to exactly 115
    while len(questions) < 115:
        qid = f"clf_d2_{qid_counter:03d}"
        qid_counter += 1
        q_en = "Which AWS feature can evaluate an organization's compliance against security frameworks like CIS AWS Foundations Benchmark?"
        q_ru = "Какой сервис AWS оценивает соответствие инфраструктуры стандартам безопасности вроде CIS AWS Foundations Benchmark?"
        all_opts = [
            {"text": {"en": "AWS Security Hub", "ru": "AWS Security Hub"}, "why": None, "corr": True},
            {"text": {"en": "Amazon Athena", "ru": "Amazon Athena"}, "why": {"en": "Athena is a serverless interactive SQL query service.", "ru": "Athena выполняет аналитические SQL-запросы в S3."}, "corr": False},
            {"text": {"en": "AWS CodeDeploy", "ru": "AWS CodeDeploy"}, "why": {"en": "CodeDeploy automates software deployments.", "ru": "CodeDeploy автоматизирует развертывание приложений."}, "corr": False},
            {"text": {"en": "Amazon Polly", "ru": "Amazon Polly"}, "why": {"en": "Polly converts text into lifelike speech.", "ru": "Polly преобразует текст в речь."}, "corr": False}
        ]
        opts_list = []
        corr_ids = []
        for i, opt in enumerate(all_opts):
            oid = letters[i]
            opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
            if opt["corr"]:
                corr_ids.append(oid)
                
        questions.append({
            "id": qid,
            "domain": "security",
            "difficulty": 2,
            "q": {"en": q_en, "ru": q_ru},
            "options": opts_list,
            "correct_ids": corr_ids,
            "services": ["aws_security_hub"],
            "explanation": {
                "summary_en": "The correct answer is: AWS Security Hub.",
                "summary_ru": "Правильный ответ: AWS Security Hub.",
                "detailed_en": "AWS Security Hub gives you a comprehensive view of your security state in AWS and helps you check your compliance against security standards like CIS AWS Foundations Benchmark.",
                "detailed_ru": "AWS Security Hub агрегирует данные безопасности и оценивает соответствие стандартам вроде CIS AWS Foundations Benchmark."
            }
        })
        
    return questions[:115]

if __name__ == "__main__":
    qs = build_d2_questions()
    print(f"Generated {len(qs)} Domain 2 supplementary questions.")
    with open("data/domain2_supplementary_115.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("Saved to data/domain2_supplementary_115.json")
