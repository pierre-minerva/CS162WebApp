This is a basic Kanban flask project with authentication. I have included two pictures of what it looks like. 
The flask server itself is in the flaskr directory. auth.py contains the views and functions for the authentication end. tasks.py has the kanban functionality.
The html uses jinja to extend a basic navigation bar across all html files from a base base.html.
There are two sqlite database tables. One that contains the user information for authentication purposes. The other is the task table which allows for tasks exclusive to a user. schema.sql contains the table information.
The unittesting tests for 200 response code from the home, login, and register page. 
