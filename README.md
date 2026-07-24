# 🔐 Simple Vault

A simple and secure password manager built with Python.

## 📌 Features

- 🔑 Master password protection
- 🔒 Password encryption using Fernet (Cryptography)
- ➕ Add new passwords
- 📋 List saved accounts
- 🔍 Retrieve passwords
- 🗑️ Delete saved passwords
- 🎲 Generate strong random passwords
- 💾 Data stored securely in `vault.json`

## 🛠️ Technologies Used

- Python 3
- Cryptography (Fernet)
- JSON
- Scrypt Key Derivation Function

## 📂 Project Structure

```
simple_vault/
│── main.py
│── vault.py
│── vault.json
│── requirements.txt
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/KULLANICI_ADIN/simple-vault.git
```

Go to the project directory:

```bash
cd simple-vault
```

Install the required package:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## 📖 Usage

When the application starts, you will see the following menu:

```
1) Add
2) List
3) Get
4) Delete
5) Generate password
6) Exit
```

## 🔒 Security

Passwords are encrypted using the **Fernet** encryption algorithm from the Cryptography library.

The encryption key is derived from the user's master password using the **Scrypt** key derivation function.

## 👩‍💻 Author

Developed by **Gamze Gürel**
