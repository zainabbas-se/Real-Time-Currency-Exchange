# 🌍 Global Exchange  

A **Streamlit-based real-time currency converter** that uses the [ExchangeRate API](https://api.exchangerate-api.com/v4/latest/PKR) to convert between multiple global currencies instantly.

---

## 🚀 Features
- Real-time exchange rates  
- Simple and clean UI (powered by Streamlit)  
- Supports 10+ major currencies  
- Error handling for API or network issues  

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/global-exchange.git
cd global-exchange
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install streamlit requests
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

---

## 💡 How It Works

User selects:
- From Currency  
- To Currency  
- Amount to Convert  

The app fetches exchange rates using:
```bash
https://api.exchangerate-api.com/v4/latest/{from_currency}
```
Then it calculates and displays the converted amount instantly.

---

## 🧮 Example
```yaml
Input:
  From: PKR
  To: USD
  Amount: 1000

Output:
  1000 PKR = 3.58 USD
```

---

## 📸 Screenshot Example
Replace with your actual app screenshot:  
`/screenshots/app_preview.png`

---

## 👨‍💻 Author
**Zain Abbas**  
💼 Freelance Python & Django Developer  
🔗 [LinkedIn](https://linkedin.com/in/zainabbas-se)

---

## 📜 License
This project is licensed under the **MIT License** – you’re free to use, modify, and distribute it with attribution.
