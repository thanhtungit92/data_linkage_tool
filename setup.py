from setuptools import setup

setup(name='data_linkage_tool',
      version='0.6',
      description='Do python project',
      url='https://github.com/thanhtungit92/data_linkage_tool.git',
      author='Tung PT',
      author_email='thanhtungit92@gmail.com',
      license='MIT',
      packages=['data_linkage_tool'],
      install_requires=[
            'pandas',
            'logging',
            'flake8',
      ],
      zip_safe=False
      )

