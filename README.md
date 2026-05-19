# 🔐 PassMan - Modern Terminal Password Manager

PassMan is a professional, secure, and user-friendly terminal-based password manager built with Python. It provides a sleek, modern CLI interface to manage your digital credentials with ease, ensuring your data is protected using standard encryption and hashing techniques.

![Banner](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Interface](https://img.shields.io/badge/UI-Rich--CLI-cyan?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-SHA256--XOR-green?style=for-the-badge)

## ✨ Key Features

- **🛡️ Master Password Protection**: Secured with SHA-256 hashing to ensure only you can access your vault.
- **📟 Modern CLI Interface**: Built using the `Rich` library for a beautiful, colorful, and interactive terminal experience.
- **📥 Secure Storage**: Passwords are encrypted before being saved to a local JSON file.
- **🎲 Password Generator**: Create strong, random passwords with a built-in strength indicator (0-100%).
- **🔍 Quick Search**: Find your credentials instantly by website name or username.
- **📋 Clipboard Integration**: Copy passwords directly to your clipboard for quick use.
- **📊 Detailed Statistics**: Monitor your vault usage and unique website entries.

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language.
- **Rich**: For advanced terminal formatting, tables, and panels.
- **Pyperclip**: For cross-platform clipboard support.
- **Hashlib**: For secure master password hashing.
- **JSON**: For lightweight local data storage.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/passman.git
   cd passman
   ```

2. **Install the package**:
   Install the package in editable mode (which automatically installs required dependencies):
   ```bash
   pip install -e .
   ```

### Running the Application

Once installed, you can launch PassMan from any directory using the CLI command:

```bash
passman
```

Or run the module directly using Python:
```bash
python -m passman.main
```

> **Note**: On your first run, you will be prompted to create a **Master Password**. Choose a strong one, as it will be the only way to decrypt your stored passwords!

## 📖 Usage Guide

- **Menu Navigation**: Use number keys (0-6) to navigate through the interactive menu.
- **Adding Passwords**: You can manually type a password or use the auto-generator.
- **Viewing Details**: Select a number from the list to view full details, including the decrypted password.
- **Searching**: Use keywords to filter through large lists of credentials.

## 🔒 Security Architecture

PassMan prioritizes your privacy by keeping everything local:

1. **Master Password**: Never stored in plain text. Only the SHA-256 hash is saved.
2. **Data Encryption**: Stored passwords undergo XOR encryption combined with Base64 encoding.
3. **Local Storage**: Your data stays on your machine in `passwords.json`. No cloud syncing, no data leaving your device.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

_Built with ❤️ for a more secure digital life._
