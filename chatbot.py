import re
from nltk.chat.util import Chat, reflections


# ---------------------------
# TEXT CLEANING
# ---------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


# ---------------------------
# FAQ RULES (60+ coverage)
# ---------------------------
pairs = [

# ========== GREETING ==========
[r".*(hi|hello|hey|good morning|good evening).*",
 ["Hello! Welcome to SBI Bank Support. How can I help you today?"]],

# ========== ACCOUNT ==========
[r".*(open|create|new).*(account).*",
 ["You can open an SBI Savings Account online at onlinesbi.com or visit your nearest SBI branch."]],

[r".*(document|kyc|proof|required|requirement).*",
 ["Documents required: Aadhaar, PAN, Photo, and Address Proof for KYC."]],

[r".*(minimum|min).*(balance).*",
 ["Minimum balance: ₹3000 (Urban), ₹2000 (Semi-urban), ₹1000 (Rural)."]],

[r".*(account).*(type|types).*",
 ["SBI provides Savings, Current, Salary, Joint, FD, and RD accounts."]],

[r".*(close|delete).*(account).*",
 ["Visit your branch with ID proof and submit account closure form."]],

[r".*(statement|passbook).*",
 ["You can download statements via Net Banking or update passbook at branch."]],

[r".*(update|change).*(mobile|phone).*",
 ["Update mobile number through ATM, branch, or Net Banking profile section."]],


# ========== BALANCE ==========
[r".*(check|know|see|view).*(balance).*",
 ["Check balance using YONO app, ATM, or missed call 9223766666."]],

[r".*(mini).*(statement).*",
 ["Get mini statement by missed call 9223866666."]],


# ========== CARD ==========
[r".*(block|lost|stolen).*(card|atm|debit).*",
 ["Immediately block card using YONO or call 1800-11-2211."]],

[r".*(apply|new).*(debit).*(card).*",
 ["Apply for a new debit card through YONO or branch."]],

[r".*(credit).*(card).*apply.*",
 ["Apply for SBI Credit Card at sbicard.com."]],

[r".*(pin).*(generate|change|reset).*",
 ["Generate or change ATM PIN at ATM or through YONO app."]],

[r".*(withdrawal).*(limit).*",
 ["Daily ATM withdrawal limit depends on card type (₹20k–₹40k approx)."]],


# ========== NET BANKING ==========
[r".*(net|internet).*(banking).*(register|activate).*",
 ["Register for Net Banking at onlinesbi.com using ATM card details."]],

[r".*(forgot|reset).*(password).*",
 ["Reset password using 'Forgot Password' option with OTP verification."]],

[r".*(unlock).*(account).*",
 ["Reset password or contact customer care to unlock account."]],

[r".*(upi).*(activate|register|setup).*",
 ["Activate UPI via YONO SBI app or BHIM app."]],

[r".*(transfer|send).*(money|fund).*",
 ["Transfer funds using NEFT, RTGS, IMPS via Net Banking or YONO app."]],

[r".*(beneficiary|payee).*(add).*",
 ["Add beneficiary in Net Banking → Manage Beneficiary section."]],


# ========== LOANS ==========
[r".*(gold|jewel).*(loan).*",
 ["SBI Gold Loan offers quick loan against gold ornaments with low interest. Visit branch for processing."]],

[r".*(home|house).*(loan).*",
 ["SBI Home Loans start around 8.5% interest with flexible EMI."]],

[r".*(personal).*(loan).*",
 ["Personal loans available with quick approval and minimal documentation."]],

[r".*(education|student).*(loan).*",
 ["Education loans available for studies in India and abroad."]],

[r".*(car|vehicle|auto).*(loan).*",
 ["SBI Vehicle loans available with affordable EMI options."]],

[r".*(loan).*(interest|rate).*",
 ["Interest depends on loan type. Home ~8.5%, Personal ~10.5%, Gold ~9% approx."]],

[r".*(emi).*(calculator).*",
 ["Use EMI calculator available on SBI official website."]],


# ========== CHEQUE / SERVICES ==========
[r".*(cheque).*(book).*",
 ["Request cheque book via YONO or Net Banking."]],

[r".*(stop).*(cheque).*",
 ["Stop cheque payment using Net Banking or branch."]],

[r".*(ifsc).*",
 ["Find IFSC code on passbook or SBI website branch locator."]],


# ========== SUPPORT ==========
[r".*(branch).*(timing|hours).*",
 ["Branch timing: 10 AM – 4 PM (Mon–Fri, except holidays)."]],

[r".*(customer|care|helpline|support).*(number|contact).*",
 ["Call SBI Customer Care: 1800-11-2211 (toll free)."]],

[r".*(complaint|problem|issue).*",
 ["Register complaint via SBI website or customer care."]],


# ========== EXIT ==========
[r".*(thank|thanks).*",
 ["You're welcome! Happy to help 😊"]],

[r".*(bye|exit|quit).*",
 ["Thank you for contacting SBI Bank. Have a nice day!"]],


# ========== DEFAULT ==========
[r"(.*)", ["Sorry, I didn't understand. Please ask banking related questions."]]
]


chatbot = Chat(pairs, reflections)


def get_bot_response(text):
    text = clean_text(text)
    return chatbot.respond(text)
chat_active = True   # add at top (global)

