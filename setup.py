from setuptools import setup

setup(name='giosgappsdk',
      version='0.1',
      description='Unofficial python SDK for GiosgApps',
      url='https://github.com/mentholi/giosgapp-python-sdk',
      author='Arsi Halttunen',
      author_email='arsi.halttunen@gmail.com',
      license='MIT',
      packages=['giosgappsdk'],

      # List run-time dependencies here.  These will be installed by pip when
      # your project is installed. For an analysis of "install_requires" vs pip's
      # requirements files see:
      # https://packaging.python.org/en/latest/requirements.html
      install_requires=[
        'requests==2.8.1',
        'PyJWT==1.3.0',
      ],
      zip_safe=False)