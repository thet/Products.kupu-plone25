from setuptools import setup, find_packages
import os

version = '1.4.17-plone25'

setup(name='Products.kupu',
      version=version,
      description="",
      long_description=open(os.path.join("Products", "kupu", "doc", "README.txt")).read() + "\n" +
                       open(os.path.join("Products", "kupu", "doc", "CHANGES.txt")).read().decode('latin1').encode('ascii','replace'),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        ],
      keywords='',
      author='Kupu Team',
      author_email='kupu-dev@codespeak.net',
      license='Kupu License',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
