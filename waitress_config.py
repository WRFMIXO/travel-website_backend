from waitress import serve
from website_backend.wsgi import application

serve(application, host='16.171.142.69', port=8000)