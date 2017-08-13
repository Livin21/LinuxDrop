from distutils.core import setup

setup(
    name='LinuxDrop',
    version='0.6',
    packages=['sender', 'receiver', ],
    py_modules=['lidrop'],
    install_requires=[
        'netifaces',
        'flask',
        'Click',
        'urllib2',
    ],
    entry_points='''
        [console_scripts]
        lidrop=lidrop:run
    ''',
    url='https://github.com/Livin21/LinuxDrop',
    license='MIT',
    author='livin',
    author_email='livinmathew99@gmail.com',
    description='Airdrop alternative for Linux <3'
)
