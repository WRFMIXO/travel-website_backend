from waitress import serve
from website_backend.wsgi import application

serve(application, host='0.0.0.0', port=8000)
