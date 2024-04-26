# Remove old distribution files
rm -rf build dist *.egg-info

# Build the package
python setup.py sdist bdist_wheel

# Check contents of the wheel file
unzip -l dist/*.whl
