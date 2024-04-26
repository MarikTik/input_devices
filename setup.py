from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

setup(
    name='input_devices',
    version='0.1.0',
    description='high level API wrapper around inputs library for working with input devices like gamepads, joysticks, etc.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MarikTik/input_devices',
    author='Mark Tikhonov',
    author_email='mtik.philosopher@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'inputs'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    package_dir={'': 'src'}
)
