import os

# 🔥 FIX STREAMLIT CRASH
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"
os.environ["STREAMLIT_WATCHER_IGNORE"] = "true"

# phần còn lại của app...
