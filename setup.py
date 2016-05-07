import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()


setup(name='websauna.notebook',
      version='0.0',
      description='notebook',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web websauna pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='websauna.notebook',
      install_requires=['websauna'],
      extras_require={
        # Dependencies for running test suite
        'test': ['websauna[test]'],

        # Dependencies to make releases
        'dev': ['websauna[dev]'],
      },

      # Define where this application starts as referred by WSGI web servers
      entry_points="""\
      [paste.app_factory]
      main = websauna.notebook:main
      """,
      )
