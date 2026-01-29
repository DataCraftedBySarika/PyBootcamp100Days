## 🔐 Caesar Cipher – Day 8 (Python)

# **Project Description**

This project is a Caesar Cipher encryption and decryption program written in Python.
It allows users to:
- Encrypt (encode) a message 
- Decrypt (decode) a message 
- Restart the program multiple times 
- Safely handle symbols, numbers, and spaces 
- Only alphabet characters are shifted. 
- All other characters (@, numbers, symbols, spaces) remain unchanged.

# **🛠 Features**
- Encode and decode messages 
- Handles large shift values using modulo 
- Preserves symbols, numbers, and spaces 
- Input validation for user-friendly experience 
- Restart option without restarting the program manually

Clean and readable logic

## ** 📂 Project Structure **
1. main.py        # Main Caesar Cipher program
2. art.py         # Contains ASCII logo
3. README.md      # Project documentation


## **How It Works**

- Each letter is shifted forward or backward based on the shift value 
- The alphabet wraps around using modulo (%)
- Non-alphabet characters are left unchanged 
- Decode reverses the shift automatically

## **Input Handling**

- Invalid encode/decode inputs are rejected 
- Shift value must be numeric 
- Large shift values (e.g. 52, 100) are normalized 
- Symbols like @, #, ! are preserved

## 🧠 **Concepts Learned (Day 8)**

1. Functions 
2. While loops 
3. Input validation 
4. Modulo operator 
5. String manipulation 
6. Conditional logic

