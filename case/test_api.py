# encoding: utf-8
import allure
import pytest
import requests
import sys
sys.path.append("..")
from utils.read_excel import *

test_data = get_xls()

@allure.feature('postman接口测试')
@allure.story('postman-api测试')
@pytest.mark.parametrize('timestamp,target,expected',test_data)
def test_timestamp(timestamp,target,expected,env_config):
    """
    用例描述：测试不同的timestamp和target
    """
    #从yml配置文件获取url
    url = env_config['host']['url']
    payload = {'timestamp':timestamp,'target':target}
    r = requests.get(url,params=payload)
    print(r.url)
    result = r.json()
    assert str(result['before'])==expected
