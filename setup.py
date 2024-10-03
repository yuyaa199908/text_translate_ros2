from setuptools import find_packages, setup

package_name = 'text_translate_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aichi2204',
    maintainer_email='yuyaa199908@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'jp2en_publisher = '+ package_name + '.jp2en_publisher:main',
            'en2jp_subscriber = '+ package_name + '.en2jp_subscriber:main',
        ],
    },
)
