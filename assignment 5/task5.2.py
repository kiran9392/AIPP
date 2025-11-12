def loan_approval(applicant):
    # Example applicant format: {"name": "Ramesh", "gender": "Male", "income": 50000, "credit_score": 720, "loan_amount": 200000}

    if applicant["income"] >= 30000 and applicant["credit_score"] >= 650:
        return f"Loan approved for {applicant['name']}"
    else:
        return f"Loan denied for {applicant['name']}"

# Test Cases
applicants = [
    {"name": "Shiva", "gender": "Male", "income": 50000, "credit_score": 720, "loan_amount": 200000},
    {"name": "Nikitha", "gender": "Female", "income": 50000, "credit_score": 720, "loan_amount": 200000}
]

for a in applicants:
    print(loan_approval(a))
