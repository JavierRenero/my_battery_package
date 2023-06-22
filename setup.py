from setuptools import setup

package_name = 'my_battery_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='triqui',
    maintainer_email='jreneb00@estudiantes.unileon.es',
    description='Topic Battery',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'battery_publisher = my_battery_package.battery_publisher:main',
        'battery_subscriber = my_battery_package.battery_subscriber:main',
        ],
    },
)
