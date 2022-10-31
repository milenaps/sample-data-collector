poetry build
poetry run python3.8 -m pip install . -r requirements.txt -t package_tmp
cd package_tmp
rm -rf pets-ddl-scripts-loader/__pycache__
find . -name "*.pyc" -delete
zip -r ../pets-ddl-scripts-loader .
cd ..
rm -rf package_tmp