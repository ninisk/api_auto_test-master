import pytest
import allure

if __name__ == '__main__':
    xml_report_path = 'C:/Users/56462/Desktop/api_auto_test-master/reports/xml/'
    pytest.main(['-s', '-q','--alluredir', xml_report_path])
    # pytest.main()