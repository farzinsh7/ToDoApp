# ToDoApp

Welcome to **ToDoApp**! This application helps you manage your tasks efficiently, similar to Trello.

## Features

- ✅ **Task Management**: Create, edit, and delete tasks.
- 🔒 **User Authentication**: Secure login and registration system.
- 📱 **Responsive Design**: Works on desktops, tablets, and smartphones.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default)

## Installation

Follow these steps to set up the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/farzinsh7/ToDoApp.git
cd ToDoApp
```

### 2️⃣ Create and activate a virtual environment

- **On Windows**:

  ```bash
  python -m venv env
  env\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  python -m venv env
  source env/bin/activate
  ```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply database migrations

```bash
python manage.py migrate
```

### 5️⃣ Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Now, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

1. **Register/Login** to your account.
2. **Create tasks** with a title and description.
3. **Edit or delete** tasks as needed.
4. **Manage your account** (update profile, change password, etc.).

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push your branch (`git push origin feature-branch`).
5. Open a **Pull Request** to the `main` branch.

## License

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/farzinsh7/ToDoApp/blob/main/LICENSE) file for details.

## Contact

For any questions, open an issue or contact the maintainer:

📧 Email: [farzinnater@gmail.com](mailto:farzinnater@gmail.com)  
🔗 GitHub: [farzinsh7](https://github.com/farzinsh7)
