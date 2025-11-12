# ❌ Example of a possibly biased scoring system

def job_score(applicant):
    """
    applicant: dictionary containing applicant details
    Example:
    {"name": "Akshaya", "gender": "Female", "experience": 5, "education_score": 8, "skills_score": 7}
    """

    score = 0
    # Gender bias risk: unfair preference
    if applicant["gender"] == "Male":
        score += 5  # ❌ Bias — gives extra points to males

    # Legitimate scoring criteria
    score += applicant["experience"] * 2
    score += applicant["education_score"]
    score += applicant["skills_score"]

    return f"{applicant['name']} scored {score} points"

# Example applicants
applicants = [
    {"name": "Shiva", "gender": "Male", "experience": 5, "education_score": 8, "skills_score": 7},
    {"name": "nikitha", "gender": "Female", "experience": 5, "education_score": 8, "skills_score": 7}
]

for a in applicants:
    print(job_score(a))
