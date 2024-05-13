# Django Health Blog

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

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Navigate to the project directory:

   ```bash
   cd Assignment
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Visit the homepage to browse through the latest blog posts.
- Sign up or log in to create new posts or comment on existing ones.
- Use the search bar to find posts by title or content.
- Click on a post to view its details, including comments.
- Users can view their posts and comments in their profile.
- Only the owner of a comment and the author of the post on which the comment is made can delete the comment.
