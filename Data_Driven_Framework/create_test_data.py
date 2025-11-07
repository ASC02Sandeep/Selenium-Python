import openpyxl
import csv
import xml.etree.ElementTree as ET
import os


def create_excel_data():
    """Create Excel test data for name field"""
    os.makedirs("test_data", exist_ok=True)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "NameTests"

    # Headers
    sheet['A1'] = 'TestCaseID'
    sheet['B1'] = 'Name'
    sheet['C1'] = 'ExpectedResult'

    # Test data
    test_data = [
        ('TC001', 'John Doe', 'Valid'),
        ('TC002', '', 'Invalid'),
        ('TC003', 'Jane Smith', 'Valid'),
        ('TC004', 'Test123', 'Invalid')
    ]

    for i, data in enumerate(test_data, start=2):
        sheet[f'A{i}'] = data[0]
        sheet[f'B{i}'] = data[1]
        sheet[f'C{i}'] = data[2]

    workbook.save('test_data/excel_data.xlsx')
    print("Excel test data created: test_data/excel_data.xlsx")


def create_csv_data():
    """Create CSV test data for email field"""
    with open('test_data/csv_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Headers
        writer.writerow(['TestCaseID', 'Email', 'ExpectedResult'])

        # Test data
        test_data = [
            ('TC001', 'test@example.com', 'Valid'),
            ('TC002', 'invalid-email', 'Invalid'),
            ('TC003', 'user@domain.com', 'Valid'),
            ('TC004', '', 'Invalid')
        ]

        writer.writerows(test_data)

    print("CSV test data created: test_data/csv_data.csv")


def create_xml_data():
    """Create XML test data for phone field"""
    root = ET.Element("TestData")

    phone_section = ET.SubElement(root, "PhoneTests")

    test_cases = [
        {'id': 'TC001', 'phone': '1234567890', 'expected': 'Valid'},
        {'id': 'TC002', 'phone': '123', 'expected': 'Invalid'},
        {'id': 'TC003', 'phone': '9876543210', 'expected': 'Valid'},
        {'id': 'TC004', 'phone': 'abc', 'expected': 'Invalid'}
    ]

    for tc in test_cases:
        test_case = ET.SubElement(phone_section, "TestCase")
        test_case.set("testCaseID", tc['id'])

        phone = ET.SubElement(test_case, "Phone")
        phone.text = tc['phone']

        expected = ET.SubElement(test_case, "ExpectedResult")
        expected.text = tc['expected']

    tree = ET.ElementTree(root)
    with open('test_data/xml_data.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8')

    print("XML test data created: test_data/xml_data.xml")


if __name__ == "__main__":
    create_excel_data()
    create_csv_data()
    create_xml_data()
    print("\nAll test data files created successfully!")