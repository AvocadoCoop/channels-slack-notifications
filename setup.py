from setuptools import setup, find_packages


setup(
    name="channels-slack-notifications",
    version='0.0.1',
    description='Send notification to slack using channels',
    keywords="django, channels, slack",
    author="Avocado Co-op <dev@avocadoproject.ca>",
    author_email="dev@avocadoproject.ca",
    url="https://github.com/AvocadoCoop/channels-slack-notifications",
    license="MIT License",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
