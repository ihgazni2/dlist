from setuptools import setup, find_packages
setup(
      name="dlist",
      version = "0.4",
      description="A list of dict , each dict has only one key.",
      author="dapeli",
      url="https://github.com/ihgazni2/dlist",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/dlist",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['dlist'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist

