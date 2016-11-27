from distutils.core import setup

setup(
    name='JuliaDoc',
    version='0.0.0',
    packages=['juliadoc'],
    package_data={'juliadoc': ['theme/julia/*', 'theme/julia/static/*']},
    license='MIT',
    long_description=open('README.md').read(),
)
