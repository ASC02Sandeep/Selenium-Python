import openpyxl
import os


def create_excel_data():
    # Create test_data directory if it doesn't exist
    os.makedirs("test_data", exist_ok=True)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "LoginTests"

    # Headers
    sheet['A1'] = 'TestCaseID'
    sheet['B1'] = 'Username'
    sheet['C1'] = 'Password'
    sheet['D1'] = 'ExpectedResult'

    # Test data for login - using standard and locked out users
    test_data = [
        ('TC001', 'standard_user', 'secret_sauce', 'Success'),
        ('TC002', 'locked_out_user', 'secret_sauce', 'Error'),
        ('TC003', 'problem_user', 'secret_sauce', 'Success'),
        ('TC004', 'performance_glitch_user', 'secret_sauce', 'Success'),
        ('TC005', 'wrong_user', 'wrong_pass', 'Error'),
        ('TC006', '', 'secret_sauce', 'Error'),
        ('TC007', 'standard_user', '', 'Error')
    ]

    for i, data in enumerate(test_data, start=2):
        sheet[f'A{i}'] = data[0]
        sheet[f'B{i}'] = data[1]
        sheet[f'C{i}'] = data[2]
        sheet[f'D{i}'] = data[3]

    file_path = 'test_data/login_data.xlsx'
    workbook.save(file_path)
    print(f"Login test data created successfully at: {file_path}")


if __name__ == "__main__":
    create_excel_data()