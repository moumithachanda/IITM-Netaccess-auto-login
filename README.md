# NetAccess Auto-Login Script

## 🚀 Overview
This script automates the login process for **NetAccess IIT Madras**, selecting the **1-day** access option and authorizing it automatically.

## 📋 Features
- Logs into **NetAccess** using credentials from a `.env` file.
- Selects the **1-day** option instead of the default 1-hour.
- Clicks **Authorize** to grant access.
- Uses Selenium for automation.
- You can see how it is selecting the options step by step.

---

## 🔧 Installation & Setup
### 1️⃣ Install Python 3 (if not installed)
- **macOS** (via Homebrew):
  ```bash
  brew install python3
  ```
- **Windows**: Download and install Python from [python.org](https://www.python.org/).

### 2️⃣ Set Up a Virtual Environment (Recommended)
To avoid conflicts with other Python packages, use a virtual environment:
```bash
python -m venv netaccess_env
source netaccess_env/bin/activate  # macOS/Linux
netaccess_env\Scripts\activate  # Windows
```

After using you can use ```bash
deactivate
```
to deactivate the virtual environment

### 3️⃣ Install Required Dependencies
Run the following command inside the virtual environment:
```bash
pip install selenium python-dotenv
```

### 4️⃣ Install ChromeDriver
- **macOS** (via Homebrew):
  ```bash
  brew install chromedriver
  ```
- **Windows**: Download from [ChromeDriver](https://sites.google.com/chromium.org/driver/) and add it to PATH.

### 5️⃣ Create a `.env` File
1. In the same directory as the script, create a file named `.env`.
2. Add your NetAccess credentials (without quotes):
   ```
   NETACCESS_USERNAME=your_username
   NETACCESS_PASSWORD=your_password
   ```
3. Save the file.

---

## ▶️ Running the Script
Once everything is set up, activate the virtual environment (if not already activated) and run the script:
```bash
python netaccess_script.py
```

✅ The script will automatically:
- Login to NetAccess
- Select the **1-day** option
- Click **Authorize**

---

## 🛠 Troubleshooting
- **Error: Username or Password not found in `.env` file**
  - Ensure you created the `.env` file and added credentials correctly.
- **ChromeDriver not found**
  - Ensure `chromedriver` is installed and accessible in your system PATH.
- **Selenium module not found**
  - Run `pip install selenium` again inside the virtual environment.

---

## 📌 Notes
- Keep your `.env` file private to protect your credentials.
- Works best with **Google Chrome**.
- The script requires an active internet connection.
- Always activate the virtual environment before running the script.

---

## 📜 License
This script is free to use and modify for educational purposes.

---

🚀 **Enjoy hassle-free NetAccess login!**