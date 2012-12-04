from setuptools import setup

setup(
    name='django-fresh',
    version='1.0.3',
    license='Simplified BSD',

    install_requires = [
        'Django',
        'watchdog',
        'beautifulsoup4',
    ],

    description='Auto-refresh your browser when files in your project change.',
    long_description=open('README.md').read(),

    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',

    url='http://github.com/overshard/django-fresh',
    download_url='http://github.com/overshard/django-fresh/downloads',

    include_package_data=True,

    packages=['fresh'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
