from setuptools import setup, find_packages
setup(
    name = 'p2_import',
    version = '1.0',
    packages = find_packages(include = ('p2_import*', )) + ['prophecy_config_instances.p2_import'],
    package_dir = {'prophecy_config_instances.p2_import' : 'configs/resources/p2_import'},
    package_data = {'prophecy_config_instances.p2_import' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.4'],
    entry_points = {
'console_scripts' : [
'main = p2_import.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
