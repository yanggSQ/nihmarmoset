from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Marmoset Project Data Processing',
    author='Shiqi Yang',
    license='MIT',
    install_requires=[
        'h5py',
        'ipykernel',
        'jupyter',
        'matplotlib',
        'numpy',
        'opencv_python',
        'pandas',
        'progressbar2',
        'python-dotenv',
        'scikit_learn',
        'scipy',
        'seaborn',
        'ffmpeg-python'
    ],
)
