# 🔐 Simple Vault

## 📸 Preview

![Simple Vault Preview] <img width="1152" height="2048" alt="WhatsApp Image 2026-07-24 at 22 21 15" src="https://github.com/user-attachments/assets/d760842a-9416-4a04-bba5-9540fcb41c08" />


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
## 🚀 Installation & Run

### 1. Clone the repository

```bash
git clone https://github.com/KULLANICI_ADIN/simple-vault.git
```

### 2. Go to the project folder

```bash
cd simple-vault
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

If `python` does not work on your system, try:

```bash
py main.py
```


## 📦 Requirements

- Python 3.13 or newer (64-bit recommended)
- cryptography

Install all dependencies with:

```bash
pip install -r requirements.txt
```




Developed by **Gamze Gürel**
