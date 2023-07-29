# Xnara_API
Test task for Xnara


1. git clone
2. Create virtual environment by running ``python -m venv env``
3. Activate the virtual environment ``. env/bin/activate``
4. install the requirements - ``pip install -r requirements.txt``
5. run the server - ``python manage.py runserver``
6. in order to fetch the data related with customer_id, call the endpoint ``http://localhost:8000/api`` with json payload ``{customer_id:<customer id you want to fetch>}``
7. To view the swagger documentation, run ``htttp://localhost:8000/swagger`` - Use the Post method to Post the customer id
8. To check for logs - open logs folder and desired log file
