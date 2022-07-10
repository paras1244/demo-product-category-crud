# demo-product-category-crud
Simple REST API to impliment the catagory model

Implimenting the self foreign key that will solve the problem to add catagory.







hello All
My name is paras,


# steps to follow
open terminal


# create Virtual environment:
python3 -m venv venv

# activate venv
source venv/bin/activate


# clone the project
git clone https://github.com/paras1244/demo-product-category-crud.git 

cd demo-product-category-crud

# installing dependeicies
pip install -r requirements.txt

# run the project
python3 manage.py runserver


# hit admin to check the database
http://127.0.0.1:8000/admin

superuser => admin / admin / admin@gmail.com

# hit api endpoint to access Product
http://127.0.0.1:8000/product/product/

# hit api endpoint to access and Category
http://127.0.0.1:8000/category/category/
