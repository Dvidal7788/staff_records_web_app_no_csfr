from setuptools import setup, find_packages

setup(
    name='StaffRecordsWebApp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask-Session==0.4.0',
        'Flask-Mail==0.9.1',
        'Flask-WTF==0.15.1',
        'Werkzeug==2.0.3',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn'
    ],
)
