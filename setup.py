from setuptools import setup, find_packages

setup(
    name='input_devices',
    version='0.1.1',
    description='High level API wrapper around inputs library for working with input devices like gamepads, joysticks, etc.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MarikTik/input_devices',
    author='Mark Tikhonov',
    author_email='mtik.philosopher@gmail.com',
    license='MIT',
    package_dir={'': 'src'},  # Set 'src' as the root directory for packages
    packages=['input_devices'],  # Find all packages in 'src'
    install_requires=['inputs'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False
)
