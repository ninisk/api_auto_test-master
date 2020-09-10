# encoding: utf-8
import pytest
import allure
import yaml
import os

@pytest.fixture(scope="session",autouse=True)
def env_config():
    """
    读取yml配置文件
    """
    # project_name = 'api_auto_test'
    # rootPath = os.path.abspath(os.path.join(os.getcwd(), ".."))
    # config_path = os.path.abspath(rootPath +'\\' + 'config\\env_config.yml') # 获取tran.csv文件的路径
    # print(config_path)
    config_path = r'C:\Users\56462\Desktop\api_auto_test-master\config\env_config.yml'

    with open(config_path,'r',encoding='utf-8') as f:
        env_config = yaml.load(f.read()) #读取配置文件
        # print(env_config)
    return env_config

def get_root_path():
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 获取myProject，也就是项目的根路径
    # print(rootPath)
    rootPath = r'C:\Users\56462\Desktop\api_auto_test-master'
    return rootPath

