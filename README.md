# Book Library API

A simple RESTful API for managing books and categories. Users can register, log in, and perform CRUD operations on books and categories. Each book can be assigned to a category.

---

## Features

- User registration and login (authentication required for most actions)
- CRUD operations for books and categories
- Assign books to categories

---

## Setup Instructions

1. **Clone the repository.**
2. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```
3. **Activate the virtual environment:**
   ```bash
   source myenv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

---

## Authentication

> **Note:** You must register and log in. Only authenticated users can perform most actions.

---

## API Endpoints

### Categories

- **List categories:**  
  `GET /api/create_category/`
- **Create category:**  
  `POST /api/create_category/`
- **Update category:**  
  `PUT /api/update/<id>/category/`
- **Delete category:**  
  `DELETE /api/delete/<id>/category/`

### Books

- **List books:**  
  `GET /api/create_book/`
- **Create book:**  
  `POST /api/create_book/`
- **Update book:**  
  `PUT /api/update/<id>/book/`
- **Delete book:**  
  `DELETE /api/delete/<id>/book/`

---

## Usage Notes

- Use [Postman](https://www.postman.com/) or a similar tool to test endpoints.
- When creating a book, the `posted_by` field is set automatically to the authenticated user.

### Example: Creating a Book in Postman

![How to create a book with Postman](./assets/how_to_post_book.png)

### Example: Updating a Book in Postman

![How to update a book with Postman](./assets/update_book.png)

---

**Open source project for learning purposes.**