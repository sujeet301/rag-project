"""
Starter knowledge base.

Replace or extend these examples with your own documents.
Each record represents one chunk. The `source` and optional `page`
fields are metadata displayed as citations.
"""

documents = [
    {
        "id": "hr-001",
        "text": "Employees receive 20 days of paid leave per year.",
        "source": "hr_policy.txt",
        "page": 1,
    },
    {
        "id": "hr-002",
        "text": "Employees must request planned leave at least 3 days before the leave date.",
        "source": "hr_policy.txt",
        "page": 2,
    },
    {
        "id": "hr-003",
        "text": "Emergency leave can be requested immediately. The employee should inform their manager as soon as practical.",
        "source": "leave_policy.txt",
        "page": 1,
    },
    {
        "id": "benefits-001",
        "text": "Full-time employees receive health insurance according to the company benefits policy.",
        "source": "benefits_policy.txt",
        "page": 1,
    },
    {
        "id": "remote-001",
        "text": "Employees working remotely must follow the company's remote work policy and attend scheduled team meetings.",
        "source": "remote_work_policy.txt",
        "page": 1,
    },
    
    # Attendance Policy
    {
        "id": "attendance-001",
        "text": "Employees must work 8 hours per day, excluding lunch breaks.",
        "source": "attendance_policy.txt",
        "page": 1,
    },
    {
        "id": "attendance-002",
        "text": "Employees must inform their manager if they expect to arrive late to work.",
        "source": "attendance_policy.txt",
        "page": 1,
    },
    {
        "id": "attendance-003",
        "text": "Employees must record their attendance using the company's approved attendance system.",
        "source": "attendance_policy.txt",
        "page": 2,
    },

    # Work From Home Policy
    {
        "id": "remote-002",
        "text": "Employees may work from home up to 2 days per week with manager approval.",
        "source": "remote_work_policy.txt",
        "page": 2,
    },
    {
        "id": "remote-003",
        "text": "Employees working from home must remain reachable during their scheduled working hours.",
        "source": "remote_work_policy.txt",
        "page": 2,
    },

    # Leave Policy
    {
        "id": "leave-001",
        "text": "Unused paid leave may be carried forward up to a maximum of 5 days into the next calendar year.",
        "source": "leave_policy.txt",
        "page": 2,
    },
    {
        "id": "leave-002",
        "text": "Employees must obtain manager approval before taking planned leave.",
        "source": "leave_policy.txt",
        "page": 2,
    },
    {
        "id": "leave-003",
        "text": "Employees who are sick and unable to work must notify their manager as soon as possible.",
        "source": "leave_policy.txt",
        "page": 3,
    },

    # Salary and Payroll Policy
    {
        "id": "payroll-001",
        "text": "Employee salaries are paid on the last working day of each month.",
        "source": "payroll_policy.txt",
        "page": 1,
    },
    {
        "id": "payroll-002",
        "text": "Employees must report salary discrepancies to the HR or payroll department.",
        "source": "payroll_policy.txt",
        "page": 1,
    },
    {
        "id": "payroll-003",
        "text": "Salary information is confidential and should only be shared with authorized individuals.",
        "source": "payroll_policy.txt",
        "page": 2,
    },

    # Office Conduct Policy
    {
        "id": "conduct-001",
        "text": "Employees must treat colleagues, customers, and visitors with respect and professionalism.",
        "source": "code_of_conduct.txt",
        "page": 1,
    },
    {
        "id": "conduct-002",
        "text": "Harassment, bullying, discrimination, and retaliation are prohibited in the workplace.",
        "source": "code_of_conduct.txt",
        "page": 2,
    },
    {
        "id": "conduct-003",
        "text": "Employees should report workplace misconduct to HR or an authorized reporting contact.",
        "source": "code_of_conduct.txt",
        "page": 2,
    },

    # IT and Security Policy
    {
        "id": "security-001",
        "text": "Employees must use strong passwords and must not share their passwords with colleagues.",
        "source": "it_security_policy.txt",
        "page": 1,
    },
    {
        "id": "security-002",
        "text": "Employees must enable multi-factor authentication on company accounts wherever required.",
        "source": "it_security_policy.txt",
        "page": 1,
    },
    {
        "id": "security-003",
        "text": "Employees must report suspected phishing emails or security incidents to the IT department immediately.",
        "source": "it_security_policy.txt",
        "page": 2,
    },
    {
        "id": "security-004",
        "text": "Employees must not upload confidential company data to unapproved external services.",
        "source": "it_security_policy.txt",
        "page": 2,
    },

    # Expense Reimbursement Policy
    {
        "id": "expense-001",
        "text": "Employees may request reimbursement for approved business expenses by submitting an expense report with receipts.",
        "source": "expense_policy.txt",
        "page": 1,
    },
    {
        "id": "expense-002",
        "text": "Expense reports must be submitted within 30 days of the expense date.",
        "source": "expense_policy.txt",
        "page": 1,
    },
    {
        "id": "expense-003",
        "text": "Expenses require approval from the employee's manager before reimbursement.",
        "source": "expense_policy.txt",
        "page": 2,
    },

    # Onboarding Policy
    {
        "id": "onboarding-001",
        "text": "New employees must complete the company's onboarding process during their first week.",
        "source": "onboarding_policy.txt",
        "page": 1,
    },
    {
        "id": "onboarding-002",
        "text": "New employees must complete required security and workplace safety training.",
        "source": "onboarding_policy.txt",
        "page": 1,
    },

    # Resignation Policy
    {
        "id": "resignation-001",
        "text": "Employees are expected to provide 30 days of notice when resigning, subject to their employment agreement.",
        "source": "resignation_policy.txt",
        "page": 1,
    },
    {
        "id": "resignation-002",
        "text": "Departing employees must return company equipment and complete the required exit process.",
        "source": "resignation_policy.txt",
        "page": 2,
    },

    # Performance Review Policy
    {
        "id": "performance-001",
        "text": "Employee performance reviews are conducted twice per year.",
        "source": "performance_policy.txt",
        "page": 1,
    },
    {
        "id": "performance-002",
        "text": "Performance reviews consider work quality, achievement of goals, collaboration, and professional development.",
        "source": "performance_policy.txt",
        "page": 1,
    },
]
