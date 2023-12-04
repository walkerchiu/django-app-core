from setuptools import find_packages, setup

setup(
    name="django-app-core",
    version="1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "Django>=4.2",
        "django-cors-headers>=4.1.0",
        "django-filter>=23.2",
        "django-graphql-jwt>=0.3.4",
        "django-ipware>=5.0.0",
        "django-recaptcha>=3.0.0",
        "django-safedelete>=1.3.2",
        "django-tenants>=3.5.0",
        "graphene-django>=3.1.2",
    ],
    author="Walker Chiu",
    author_email="chenjen.chiou@gmail.com",
    description="",
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
