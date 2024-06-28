# Django Live Search with HTMX

Htmx is a JavaScript library that allows you to create modern web applications with less JavaScript by using HTML attributes to handle client-server interactions. It simplifies the process of making asynchronous HTTP requests and dynamically updating the web page based on the server's response.

## Input Field

Here is an example of an HTML input field with htmx attributes and a detailed explanation of each attribute:

### HTML Code

```html
<input type="search" 
        name="keyword" placeholder="Search movies..." 
        hx-post="{% url 'list' %}" 
        hx-trigger="load, input changed delay:500ms, keyword" 
        hx-target="#search-results" 
        hx-indicator=".htmx-indicator"
        hx-headers='{"X-CSRFToken":"{{ csrf_token }}"}'
>
```
