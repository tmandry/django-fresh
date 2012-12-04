from distutils.core import setup


setup(
    name='django-fresh',
    version='1.0.0',
    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',
    packages=['fresh'],
    url='http://github.com/overshard/django-fresh',
    license='Simplified BSD',
    description='Auto-refreshes your browser after updating files in your' + \
                ' project in a development environment.',
    long_description=open('README.md').read(),
    zip_safe=False,
    install_requires=['Django', 'watchdog', 'beautifulsoup4'],
    include_package_data=True
)
