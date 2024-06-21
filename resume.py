# Input section
Person_name = input('What is your name: ')
Person_email = input('Enter your Email address: ')
Person_phone = input('Enter your mobile number: ')  # Keep phone number as string
person_summary = input('Why are you an expert at this job? Explain in two or three sentences: ')
n = int(input('Enter number of skills you know: '))
skills = []
for i in range(1, n + 1):
    skills.append(input(f'Enter your Skill number {i}: '))
    
experience = []
has_experience = input('Do you have any previous work experience? (Y/N): ').lower()
if has_experience == 'y':
    n1 = int(input('Enter the number of jobs you have done previously: '))
    for i in range(1, n1 + 1):
        experience.append(input(f'Enter job {i} details: '))
else:
    has_internship = input('You are a fresher. Have you done any internship? (Y/N): ').lower()
    if has_internship == 'y':
        n2 = int(input('How many internships have you done so far? '))
        for i in range(1, n2 + 1):
            experience.append(input(f'Enter details about internship {i}: '))

# Output section
print('-------------------------------RESUME------------------------------------')
print(f'NAME: {Person_name}')
print(f'EMAIL: {Person_email}')
print(f'PHONE NO: {Person_phone}')
print('SUMMARY:')
print(person_summary)
print('SKILLS:')
for skill in skills:
    print(f'* {skill}')
if experience:
    print('EXPERIENCE:')
    for exp in experience:
        print(f'- {exp}')
