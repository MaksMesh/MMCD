from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='mmcd',
  version='0.1.0',
  author='MaksMesh',
  author_email='maksmesh2010@gmail.com',
  description='To early.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/MaksMesh/MMCD',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Windows'
  ],
  keywords='ram_overload cmd_spam close_explorer bad_sound create_file BSOD shutdown UnknownModeError DelayedStart SecretStart ',
  project_urls={},
  python_requires='>=3.6'
)