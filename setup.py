from setuptools import find_packages, setup

  
  
# specify requirements of your package here
REQUIREMENTS = ['numpy', 'pandas', 'seaborn', 'scipy', 'tqdm', 'pyarrow', 'scikit-learn', 'matplotlib', 'fastparquet']
  

  
# calling the setup function 
setup(name='fenggi',
      version='0.0.1',
      description='feature engineering',
      url='https://github.com/crunchdao/feature-engineering',
      author='Utkarsh - Matteo',
      author_email='utkarshp1161@gmail.com',
      license='MIT',
      #package_dir={"": "src"},
      packages=find_packages(include=["fenggi", "fenggi.*"]),
      install_requires=REQUIREMENTS,
      )