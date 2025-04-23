from flask import Flask
import os                                   # ← add

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '𝐇𝐞𝐥𝐥𝐨 𝐟𝐫𝐨𝐦 𝐀𝐉 𝐓𝐄𝐂𝐇 𝐖𝐎𝐑𝐋𝐃'

if __name__ == "__main__":
    # Render sets PORT in the container’s env. Default to 5000 for local dev.
    port = int(os.getenv("PORT", 5000))     # ← add
    app.run(host="0.0.0.0", port=port)      # ← modified
