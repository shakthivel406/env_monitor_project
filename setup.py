from setuptools import setup

package_name = 'env_monitor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    description='Indoor environment monitoring using ROS2',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'monitor = env_monitor_pkg.monitor:main',
            'patrol = env_monitor_pkg.patrol:main',
            'zone_visualizer = env_monitor_pkg.zone_visualizer:main',
        ],
    },
)
