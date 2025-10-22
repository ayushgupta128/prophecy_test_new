from setuptools import setup, find_packages
setup(
    name = 'p3_import',
    version = '1.0',
    packages = find_packages(include = ('p3_import*', )) + ['prophecy_config_instances.p3_import'],
    package_dir = {'prophecy_config_instances.p3_import' : 'configs/resources/p3_import'},
    package_data = {'prophecy_config_instances.p3_import' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.4'],
    entry_points = {
'console_scripts' : [
'main = p3_import.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
