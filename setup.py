from setuptools import setup, find_packages

setup(name='pycdk',
      version='0.0.2',
      description='A Python wrapper for the CDK',
      license='AGPLv3',
      author='Ji Hongchao, Xie Yuguang',
      author_email='ji.hongchao@foxmail.com, george@xiegeo.com',
      url='https://github.com/xiegeo/pycdk',
	  include_package_data = True,
      packages=find_packages()
     )