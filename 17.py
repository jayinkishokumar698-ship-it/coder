medical_care = input("Do you have medical cause? (y/n): ")

if medical_care.lower() == 'y':
    print("You are allowed to attend the exam.")

attendance = int(input("Enter your attendance percentage: "))

if medical_care.lower() == 'n':
    if attendance >= 75:
        print("You are allowed to attend the exam.")
    else:
        print("You are not allowed to attend the exam.")
