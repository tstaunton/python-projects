def new_employee(name, role, *qualifications):
    """Summarize the role and qualifications of a new employee."""
    print(f"\n{name} is joining as a {role}, with the following qualifications: ")
    for qualification in qualifications:
        print(f" - {qualification}")