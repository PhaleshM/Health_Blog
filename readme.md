# Django Health Blog [Link](https://phalesh2.pythonanywhere.com/)

This is a health blog platform built using Django, a high-level Python web framework. It allows users to read and write health-related articles, comment on posts, and interact with other users.

## Features

- **User Authentication**: Users can sign up, log in, and log out. Authentication is handled using Django's built-in authentication system.

- **CRUD Operations**: Users can create, read, update, and delete blog posts.

- **Category Management**: Posts can be categorized for better organization and navigation.

- **Comments**: Authenticated users can comment on blog posts.

- **Search Functionality**: Users can search for posts by title or content.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PhaleshM/Health_Blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Health_Blog
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Navigate to the working directory:

   ```bash
   cd Assignment
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Browse Latest Posts: Visit the homepage to browse through the latest blog posts.

- Sign Up or Log In: Sign up or log in to create new posts or comment on existing ones.

- Search Posts: Use the search bar to find posts by title or content.

- View Post Details: Click on a post to view its details, including comments.

- User Profile: Users can view their posts and comments in their profile.

- Delete Comments: Only the owner of a comment and the author of the post on which the comment is made can delete the comment.

- Update Post: Users can change the status of their posts from their profile and then navigate to the detail view to update them.
