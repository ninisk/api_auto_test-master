# encoding: utf-8
import os

# project_name="api_auto_test-master"
def get_root_path():
    '''
    获取根路径
    :param project_name: 项目名
    :return:
    '''
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = curPath[:curPath.find(project_name+"\\") + len(project_name+"\\")]  # 获取myProject，也就是项目的根路径
    # rootPath = os.path.abspath(os.path.join(os.getcwd(), ".."))

    rootPath = r'C:\Users\56462\Desktop\api_auto_test-master'

    # file_path = os.path.abspath(rootPath+'\\' + 'testdata\\testdata.xlsx')
    file_path = r'C:\Users\56462\Desktop\api_auto_test-master\testdata\testdata.xlsx'
    # print("rootPath= %s",rootPath)
    # print("curPath= %s", curPath)
    # print("file_path= %s", file_path)
    return rootPath
#
# if __name__ == '__main__':
    # print(get_root_path())