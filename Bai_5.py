print("====================================================")
print("     KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI")
print("====================================================\n")

while True:
    print("[Nhập thông tin nhân viên]")
    
    employee_id = input("1. Enter Employee ID: ")
    while employee_id == "":
        print("[!] LỖI: Mã nhân viên không được để trống!")
        employee_id = input("1. Enter Employee ID: ")

    employee_name = input("2. Enter Full Name: ")
    while employee_name == "":
        print("[!] LỖI: Họ tên không được để trống!")
        employee_name = input("2. Enter Full Name: ")

    current_salary = float(input("3. Enter current Salary in VND (Number > 0): "))
    while current_salary <= 0:
        print("[!] LỖI: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
        current_salary = float(input("3. Enter current Salary in VND (Number > 0): "))
        
    performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))
    while performance_score < 1.0 or performance_score > 5.0:
        print("[!] LỖI: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
        performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))

    experience_years = int(input("5. Enter Year of Experience (Integer >= 0): "))
    while experience_years < 0:
        print("[!] LỖI: Kinh nghiệm không được là số âm!")
        experience_years = int(input("5. Enter Year of Experience (Integer >= 0): "))

    print("E-PROFILE CẬP NHẬT")
    print(f"- ID: {employee_id}")
    print(f"- Name: {employee_name}")
    print(f"- Salary: {current_salary} VND")
    print(f"- KPI Score: {performance_score} / 5.0")
    print(f"- Experience: {experience_years} years")

    print("IT SYSTEM LOG")
    print(f"employee_id      | {type(employee_id)}")
    print(f"employee_name    | {type(employee_name)}")
    print(f"current_salary   | {type(current_salary)}")
    print(f"performance_score| {type(performance_score)}")
    print(f"experience_years | {type(experience_years)}")

    choice = input("Do you want to enter another employee? (y/n): ").lower()
    if choice != 'y':
        print("\nĐang tắt Kiosk... Tạm biệt!")
        break