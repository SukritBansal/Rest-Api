# Rest API for data and images
### Requirements
<li>Python
<li>Django
<li>DjangoRestFramework
<li>Pillow

### Overview
<li>GET and POST operations for API
<li>Image is compressed using Pillow module by overriding the save function and compressing the image if it exceeds the given size

### Test Cases
<li>POST Testing
<li>GET Testing
<li>Image size Testing

### How to run the API
Run this commannd in your cmd
<pre>
python manage.py runserver
</pre>
Navigate to 
<pre>
http://localhost:8000/fish/
</pre>



