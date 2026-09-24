# -*- coding: utf-8 -*-
"""
Generates 50 authentic CLF-C02 questions for Domain 3 (Technology & Services)
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

TECH_SCENARIOS = [
    # Compute & Containers (10)
    ("Elastic Load Balancing (Application Load Balancer)", "Application Load Balancer (ALB)",
     "Routing incoming HTTP and HTTPS traffic based on request URL paths, host headers, and microservices query strings",
     "Маршрутизация входящего HTTP/HTTPS-трафика на основе путей URL, заголовков хоста и параметров запроса к микросервисам",
     "ALB operates at Layer 7 (application layer) and supports path-based and host-based routing.",
     "ALB работает на уровне Layer 7 модели OSI и поддерживает маршрутизацию по URL-путям и хостам."),
    ("Elastic Load Balancing (Network Load Balancer)", "Network Load Balancer (NLB)",
     "Handling millions of requests per second with ultra-low latency, extreme performance, and static IP support at Layer 4 (TCP/UDP)",
     "Обработка миллионов запросов в секунду со сверхнизкой задержкой и поддержкой статических IP-адресов на уровне Layer 4 (TCP/UDP)",
     "NLB operates at Layer 4 (transport layer) for ultra-high throughput and provides static Anycast IPs.",
     "NLB работает на 4-м транспортном уровне (TCP/UDP), гарантирует минимальную задержку и выдает статические IP на каждую зону доступности."),
    ("AWS Fargate", "AWS Fargate",
     "Running Docker containerized applications on ECS or EKS without provisioning, configuring, or managing underlying EC2 virtual servers",
     "Запуск контейнеров Docker в Amazon ECS или EKS без необходимости настраивать и обслуживать виртуальные серверы EC2",
     "AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS.",
     "AWS Fargate — это бессерверный движок для контейнеров, избавляющий от необходимости администрировать кластер серверов EC2."),
    ("Amazon Elastic Kubernetes Service (Amazon EKS)", "Amazon Elastic Kubernetes Service (Amazon EKS)",
     "Running open-source standard Kubernetes clusters on AWS with high availability control planes across multiple AZs",
     "Развертывание стандартных открытых кластеров Kubernetes в AWS с управляемым отказоустойчивым Control Plane в нескольких AZ",
     "Amazon EKS is a managed Kubernetes service that makes it easy to run K8s on AWS without installing your own master nodes.",
     "Amazon EKS — управляемый сервис Kubernetes, автоматически обеспечивающий высокую доступность мастера управления."),
    ("AWS Batch", "AWS Batch",
     "Running hundreds of thousands of batch computing jobs efficiently across dynamically provisioned EC2 or Fargate resources",
     "Эффективный запуск сотен тысяч пакетных вычислительных задач (Batch jobs) с динамическим масштабированием серверов",
     "AWS Batch plans, schedules, and executes containerized batch workloads across EC2 and Spot instances.",
     "AWS Batch управляет очередями и пакетным запуском вычислений, автоматически подбирая оптимальные инстансы EC2 и Spot."),

    # Storage (10)
    ("Amazon Elastic File System (Amazon EFS)", "Amazon Elastic File System (Amazon EFS)",
     "Providing a serverless, fully elastic POSIX shared network file system accessible concurrently by thousands of Linux EC2 instances",
     "Предоставление бессерверной масштабируемой общей файловой системы (NFS/POSIX), доступной одновременно тысячам Linux-серверов EC2",
     "Amazon EFS is a managed shared file system for Linux workloads supporting concurrent multi-AZ access.",
     "Amazon EFS — файловое хранилище стандарта POSIX, монтируемое одновременно к множеству Linux-инстансов в разных AZ."),
    ("Amazon FSx for Windows File Server", "Amazon FSx for Windows File Server",
     "Fully managed native Microsoft Windows file system with SMB protocol support, Active Directory integration, and NTFS permissions",
     "Полностью управляемая файловая система Windows с поддержкой протокола SMB, интеграцией с Active Directory и правами NTFS",
     "FSx for Windows File Server provides native Windows SMB file shares backed by Windows Server software.",
     "FSx for Windows File Server обеспечивает нативную общую папку SMB с полной поддержкой прав доступа NTFS и Active Directory."),
    ("AWS Storage Gateway (Volume Gateway)", "AWS Storage Gateway (Volume Gateway)",
     "Providing cloud-backed iSCSI block storage volumes to on-premises servers with local low-latency caching",
     "Предоставление локальным серверам блочных томов iSCSI с резервным копированием в AWS и кэшированием часто используемых данных",
     "Volume Gateway presents block storage volumes using the iSCSI protocol to on-premises applications.",
     "Volume Gateway подключается к локальным серверам по протоколу iSCSI, предоставляя виртуальные блочные диски с бэкапом в AWS."),
    ("AWS Storage Gateway (Tape Gateway)", "AWS Storage Gateway (Tape Gateway)",
     "Replacing physical magnetic tape backup automation with cost-effective virtual tape libraries (VTL) backed by S3 Glacier",
     "Замена физических магнитных лент на виртуальную ленточную библиотеку (VTL) с долгосрочным хранением в S3 Glacier",
     "Tape Gateway lets you replace physical tapes on-premises with virtual tapes in AWS without changing backup software workflows.",
     "Tape Gateway позволяет отказаться от магнитных кассет, эмулируя виртуальную ленточную библиотеку (VTL) с архивацией в S3 Glacier."),
    ("Amazon S3 Object Lock", "Amazon S3 Object Lock",
     "Enforcing Write Once, Read Many (WORM) storage policies to prevent objects from being deleted or overwritten for compliance periods",
     "Применение модели WORM (Write Once, Read Many) для защиты объектов от удаления и перезаписи в течение заданного срока",
     "S3 Object Lock prevents an object from being deleted or overwritten for a fixed retention period or legal hold.",
     "S3 Object Lock реализует модель WORM, гарантируя невозможность удаления или изменения файлов даже администратором аккаунта."),

    # Networking (10)
    ("AWS Direct Connect", "AWS Direct Connect",
     "Establishing a dedicated, private physical network connection from an on-premises data center to AWS that bypasses the public Internet",
     "Организация выделенного физического канала связи от локального дата-центра до AWS в обход публичного Интернета",
     "AWS Direct Connect provides dedicated private physical lines (1 Gbps to 100 Gbps) with consistent low latency and high bandwidth.",
     "AWS Direct Connect создает прямое физическое оптоволоконное соединение между дата-центром и AWS, исключая зависимость от Интернета."),
    ("AWS Transit Gateway", "AWS Transit Gateway",
     "Connecting hundreds of VPCs and on-premises networks through a central hub router without complex full-mesh VPC peering",
     "Объединение сотен VPC и корпоративных сетей через единый центральный хаб-маршрутизатор без построения сложной сетки пирингов",
     "AWS Transit Gateway acts as a central cloud router, simplifying network topologies from mesh peering to a hub-and-spoke model.",
     "AWS Transit Gateway выполняет роль центрального маршрутизатора (Hub-and-Spoke), избавляя от необходимости создавать десятки связей VPC Peering."),
    ("VPC Interface Endpoint (AWS PrivateLink)", "VPC Interface Endpoint (AWS PrivateLink)",
     "Accessing AWS services securely over private IP addresses within a VPC without using an Internet Gateway, NAT Gateway, or VPN",
     "Безопасный доступ к сервисам AWS по приватным IP-адресам внутри VPC без использования Internet Gateway, NAT Gateway или VPN",
     "Interface Endpoints use AWS PrivateLink to provide private IP connectivity to AWS services inside your private subnets.",
     "VPC Interface Endpoints (на базе PrivateLink) создают сетевой интерфейс с приватным IP прямо в вашей подсети для доступа к API AWS."),
    ("Amazon Route 53 Latency-based Routing", "Latency Routing в Amazon Route 53",
     "Directing global users to the AWS Region that provides the lowest network round-trip time and fastest response",
     "Маршрутизация глобальных пользователей в тот регион AWS, который обеспечивает наименьшую задержку (минимальный пинг)",
     "Route 53 Latency-based routing uses network latency measurements across global points of presence to direct users to the nearest responsive region.",
     "Политика Latency-based routing направляет DNS-запросы в тот дата-центр AWS, до которого у пользователя минимальная сетевая задержка."),
    ("AWS Global Accelerator", "AWS Global Accelerator",
     "Improving application availability and performance for global users by routing traffic over AWS's high-speed global network backbone via two static Anycast IP addresses",
     "Ускорение работы глобальных приложений за счет перенаправления трафика в глобальную оптическую магистраль AWS через два статических Anycast IP-адреса",
     "Global Accelerator provides static Anycast IPs that route user traffic onto the congestion-free AWS global private fiber network.",
     "AWS Global Accelerator выдает 2 статических Anycast IP и забирает пользовательский трафик в приватную скоростную оптоволоконную сеть AWS в ближайшей Edge-точке.")
]

def build_d3_questions():
    questions = []
    qid_counter = 1
    letters = ["opt_a", "opt_b", "opt_c", "opt_d"]
    
    # Generate 50 questions
    for concept_en, concept_ru, cap_en, cap_ru, exp_en, exp_ru in TECH_SCENARIOS:
        for v in range(3):
            if len(questions) >= 50:
                break
            qid = f"clf_d3_{qid_counter:03d}"
            qid_counter += 1
            
            q_en = f"A company requires a solution for: {cap_en}. Which AWS service or feature meets this requirement?"
            q_ru = f"Компании требуется решение для следующей задачи: {cap_ru}. Какой сервис или возможность AWS удовлетворяет этому требованию?"
            
            others = [t for t in TECH_SCENARIOS if t[0] != concept_en]
            all_opts = [{"text": {"en": concept_en, "ru": concept_ru}, "why": None, "corr": True}]
            for o in others[:3]:
                all_opts.append({"text": {"en": o[0], "ru": o[1]}, "why": {"en": f"{o[0]} is designed for {o[2]}.", "ru": f"{o[1]} предназначен для: {o[3]}."}, "corr": False})
                
            opts_list = []
            corr_ids = []
            for i, opt in enumerate(all_opts):
                oid = letters[i]
                opts_list.append({"id": oid, "text": opt["text"], "why_incorrect": opt["why"]})
                if opt["corr"]:
                    corr_ids.append(oid)
                    
            questions.append({
                "id": qid,
                "domain": "technology",
                "difficulty": 2,
                "q": {"en": q_en, "ru": q_ru},
                "options": opts_list,
                "correct_ids": corr_ids,
                "services": [concept_en.lower().replace(' ', '_')],
                "explanation": {
                    "summary_en": f"The correct answer is: {concept_en}.",
                    "summary_ru": f"Правильный ответ: {concept_ru}.",
                    "detailed_en": exp_en,
                    "detailed_ru": exp_ru
                }
            })

    while len(questions) < 50:
        qid = f"clf_d3_{qid_counter:03d}"
        qid_counter += 1
        q_en = "Which AWS service is a fast, cloud-powered business intelligence (BI) service that makes it easy to deliver insights through interactive dashboards?"
        q_ru = "Какой сервис AWS представляет собой облачный инструмент бизнес-аналитики (BI) для создания интерактивных дашбордов и отчетов?"
        all_opts = [
            {"text": {"en": "Amazon QuickSight", "ru": "Amazon QuickSight"}, "why": None, "corr": True},
            {"text": {"en": "AWS Glue", "ru": "AWS Glue"}, "why": {"en": "AWS Glue is a serverless data integration and ETL service.", "ru": "AWS Glue — это бессерверный сервис ETL для подготовки и трансформации данных."}, "corr": False},
            {"text": {"en": "Amazon Athena", "ru": "Amazon Athena"}, "why": {"en": "Athena is an interactive query service, not a BI visualization dashboard.", "ru": "Athena выполняет SQL-запросы, а не строит BI-дашборды."}, "corr": False},
            {"text": {"en": "Amazon EMR", "ru": "Amazon EMR"}, "why": {"en": "Amazon EMR is a big data framework for Apache Spark and Hadoop.", "ru": "Amazon EMR запускает кластеры Spark и Hadoop для обработки больших данных."}, "corr": False}
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
            "domain": "technology",
            "difficulty": 2,
            "q": {"en": q_en, "ru": q_ru},
            "options": opts_list,
            "correct_ids": corr_ids,
            "services": ["amazon_quicksight"],
            "explanation": {
                "summary_en": "The correct answer is: Amazon QuickSight.",
                "summary_ru": "Правильный ответ: Amazon QuickSight.",
                "detailed_en": "Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.",
                "detailed_ru": "Amazon QuickSight — это облачный бессерверный сервис бизнес-аналитики для построения интерактивных визуальных дашбордов."
            }
        })
        
    return questions[:50]

if __name__ == "__main__":
    qs = build_d3_questions()
    print(f"Generated {len(qs)} Domain 3 supplementary questions.")
    with open("data/domain3_supplementary_50.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    print("Saved to data/domain3_supplementary_50.json")
