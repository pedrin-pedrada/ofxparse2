# ofxparse2 (fork of ofxparse)

`ofxparse2` is a parser for Open Financial Exchange (`.ofx`) format files, originally based on the excellent [`ofxparse`](https://github.com/jseutter/ofxparse) by Jonathan Seutter.

OFX files are available from almost any online banking website and are commonly used for downloading bank or investment statements. This fork includes enhancements focused on **better compatibility with Brazilian banks**, **automatic encoding detection**, and **improved robustness** for real-world OFX variations.

---

## 🚀 Fork and Enhancements

This repository is a fork of the original [`ofxparse`](https://github.com/jseutter/ofxparse) project.

Bug fixes, improvements, and compatibility updates were made by **Pedro Schneider** ([@pedrin-pedrada](https://github.com/pedrin-pedrada)).

### ✅ What's improved?

- Encoding detection using [`chardet`](https://pypi.org/project/chardet/) to handle files like:

  ```xml
  <?xml version="1.0" encoding="utf-8" ?>

- Handles malformed or partially invalid headers from certain Brazilian banks.

- Better support for common OFX/QFX variations found in South America.

📦 Fork available at: https://github.com/pedrin-pedrada/ofxparse2

---

## 📦 How to Install

You can install `ofxparse2` directly from GitHub using `pip`:

```bash
pip install ofxparse2
```

To add it to a `requirements.txt`:

```
git+https://github.com/pedrin-pedrada/ofxparse2.git
```

---

## 🧪 How to Use

Here’s a simple example of how to parse an `.ofx` file:

```python
from ofxparse import OfxParser
import codecs

with codecs.open("example.ofx", "r", encoding="utf-8") as file:
    ofx = OfxParser.parse(file)

# Access account information
account = ofx.account
print("Account ID:", account.account_id)
print("Bank ID:", account.routing_number)
print("Branch ID:", account.branch_id)

# Access statement and transactions
statement = account.statement
print("Start Date:", statement.start_date)
print("End Date:", statement.end_date)
print("Balance:", statement.balance)

for transaction in statement.transactions:
    print(f"{transaction.date} - {transaction.amount} - {transaction.payee}")
```

---

## 🛠 Development

### Prerequisites

```bash
# Ubuntu
sudo apt-get install python-beautifulsoup python-nose python-coverage-test-runner

# Python 3
pip install BeautifulSoup4 six lxml nose coverage

# Python 2 (legacy)
pip install BeautifulSoup six nose coverage
```

### Running Tests

```bash
nosetests
# or
python -m unittest tests.test_parse
```

### Coverage Report

```bash
coverage run -m unittest tests.test_parse
coverage report
coverage html
firefox htmlcov/index.html
```

---

## 📂 Help Wanted

If you have `.ofx` or `.qfx` files that don't work properly, feel free to contribute!
Please anonymize sensitive information and submit files or issues via GitHub.

---

## 🌐 Original Homepage

- Homepage: https://sites.google.com/site/ofxparse
- Source: https://github.com/jseutter/ofxparse

---

## 📄 License

`ofxparse2` is released under the MIT license. See the [LICENSE](LICENSE) file for full terms.

> The core idea: if you're allowed to use Python for your project, you're also allowed to use this library.

