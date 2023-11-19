from setuptools import setup, find_packages


setup(name='ray_projects',
      version='0.1',
      description='Library containing results of my ray experiments.',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      url="https://github.com/pypa/sampleproject",
          author="Example Author",
    author_email="author@example.com",
     )
