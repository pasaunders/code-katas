"""Setup file for code kata assignment."""

from setuptools import setup


setup(
    name="code_katas",
    description="A project to automate drafting thankyou letters.",
    version=0.1,
    author="Patrick",
    author_email="patrick.a.n.saunders@gmail.com",
    license="MIT",
    py_modules=[''],
    package_dir={'': 'src'},
    install_requires=['faker'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        # 'console scripts': [
        #     "file_name = file_name:main"
        # ]
    }
)
