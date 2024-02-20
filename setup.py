from setuptools import setup

setup(
    name='usbscanner',
    version='0.0.1',
    packages=['usbscanlars'],
    install_requires=[
        'package_name @ git+https://github.com/larsje99/usb_scanner_lars'
    ],
    entry_points={
        'console_scripts': [
            'usbscanlars = usbscanlars.usb_analyse:main',
        ],
    },
)

