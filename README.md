<h3>Django Live Search with HTMX</h3>

Htmx is a JavaScript library that allows you to create modern web applications with less JavaScript by using HTML attributes to handle client-server interactions. It simplifies the process of making asynchronous HTTP requests and dynamically updating the web page based on the server's response.
Input Field:
'''html
<input type="search" 
        name="keyword" placeholder="Search movies..." 
        hx-post="{% url 'list' %}" 
        hx-trigger="load, input changed delay:500ms, keyword" 
        hx-target="#search-results" 
        hx-indicator=".htmx-indicator"
        hx-headers='{"X-CSRFToken":"{{ csrf_token }}"}'
>
'''
1.<input type="search">: This is a search input field.
2.Attributes:
    a. name="keyword": The name of the input field, used for form submission.
    b.placeholder="Search movies...": Placeholder text inside the input field.
    c.hx-post="{% url 'list' %}": This is an htmx attribute that makes an HTTP POST request to the URL returned by the Django template tag {% url 'list' %}.
    d.hx-trigger="load, input changed delay:500ms, keyword": This specifies that the request should be triggered when the page loads, when the input changes with a delay of 500 milliseconds, or when the "keyword" event occurs.
    e.hx-target="#search-results": This specifies that the response from the server should be inserted into the element with the ID search-results.
    f.hx-indicator=".htmx-indicator": This specifies that the element with the class htmx-indicator should be shown while the request is in progress.
    g.hx-headers='{"X-CSRFToken":"{{ csrf_token }}"}': This includes a CSRF token in the request headers for security.<br>

Search Indicator and Results Container:
'''html
<span class="htmx-indicator"> 
    Searching...
</span> 
<div id="search-results"></div>
'''
1. <span class="htmx-indicator">Searching...</span>: This span element displays "Searching..." text and is shown when an htmx request is in progress.
2. <div id="search-results"></div>: This div element will contain the search results returned by the server.

Script Inclusion
'''html
<script src="https://unpkg.com/htmx.org@1.9.12"></script>'''
<script>: Includes the htmx library from a CDN. This library enables the use of htmx attributes for making AJAX requests and dynamically updating the page.
