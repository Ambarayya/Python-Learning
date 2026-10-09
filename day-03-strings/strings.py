# ============================================================
# DAY 3 - PYTHON STRINGS
# ============================================================


# ============================================================
# Problem 1 - Text Normalization
# ============================================================

query = "   How   to   deploy   a Python   model on   CPU?   "

words = query.split()
normalized_query = " ".join(words)

print("Normalized Query:", normalized_query)


# ============================================================
# Problem 2 - Extract Information from a Log
# ============================================================

log = "INFO: User=Ambarayya | Model=Qwen2.5 | Latency=1.82s | Status=SUCCESS"

log_parts = log.split("|")

user = log_parts[0].replace("INFO:", "").strip().split("=")[1]
model = log_parts[1].strip().split("=")[1]
latency = log_parts[2].strip().split("=")[1]
status = log_parts[3].strip().split("=")[1]

print("User:", user)
print("Model:", model)
print("Latency:", latency)
print("Status:", status)


# ============================================================
# Problem 3 - Filename Processing
# ============================================================

filename = "voice_assistant_model_v2.5.onnx"

file_parts = filename.rsplit(".", 1)

print("Filename:", file_parts[0])
print("Extension:", file_parts[1])


# ============================================================
# Problem 4 - Case-Insensitive Keyword Detection
# ============================================================

text = "The vehicle Brake warning light is still ON after restarting the Safari."
keyword = "brake"

keyword_found = keyword.lower() in text.lower()

print("Keyword found:", keyword_found)


# ============================================================
# Problem 5 - String Immutability
# ============================================================

text = "python"

text = text.upper()

print("Uppercase Text:", text)


# ============================================================
# Problem 6 - Clean User Input
# ============================================================

name = "   Ambarayya Math   "

clean_name = name.strip()

print("Clean Name:", clean_name)


# ============================================================
# Problem 7 - Count a Character
# ============================================================

text = "banana"

count = text.count("a")

print(f"'a' appears {count} times")


# ============================================================
# Problem 8 - Check File Extension
# ============================================================

filename = "voice_assistant_model.pt"

is_onnx = filename.lower().endswith(".onnx")

print("ONNX model:", is_onnx)


# ============================================================
# Problem 9 - Extract Username from Email
# ============================================================

email = "amarayya.math@sandlogic.com"

email_parts = email.split("@")
username = email_parts[0]

print("Username:", username)


# ============================================================
# Problem 10 - Normalize a User Query
# ============================================================

query = "  HOW TO RUN PYTHON ON RASPBERRY PI  "

normalized_query = query.strip().lower().capitalize()

print("Normalized Query:", normalized_query)


# ============================================================
# Problem 11 - Normalize a Log Message
# ============================================================

log = "   ERROR:   MODEL   LOADING   FAILED   "

log_parts = log.strip().split()

normalized_log = log_parts[0] + " " + " ".join(log_parts[1:]).lower()

print("Normalized Log:", normalized_log)


# ============================================================
# Problem 12 - Extract and Normalize an API Status
# ============================================================

response = "  STATUS = SUCCESS   "

response_parts = response.strip().lower().split("=")

status = response_parts[1].strip()

print("Status:", status)


# ============================================================
# Problem 13 - Model Filename Processing
# ============================================================

filename = "  QWEN2.5-Instruct.ONNX  "

clean_filename = filename.strip().lower()
file_parts = clean_filename.rsplit(".", 1)

model_name = file_parts[0]
extension = file_parts[1]
is_onnx = clean_filename.endswith(".onnx")

print("Model name:", model_name)
print("Extension:", extension)
print("ONNX model:", is_onnx)