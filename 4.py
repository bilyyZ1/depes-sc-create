import os
import time

# Banner
os.system("clear")
print("""
\033[91m╔══════════════════════════════════════╗
║     \033[92mHTML Deface Generator by butzXploit\033[91m    ║
╚══════════════════════════════════════╝
""")

# Input user
judul = input("\033[93m[+] Judul deface: \033[0m")
pesan = input("\033[93m[+] Pesan utama: \033[0m")
logo_url = input("\033[93m[+] URL Logo Gambar: \033[0m")
musik_url = input("\033[93m[+] URL Musik Latar (mp3): \033[0m")
nama_file = input("\033[93m[+] Nama file output (contoh: index.html): \033[0m")

# Template HTML
html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{judul}</title>
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
  <style>
    body {{
      background-color: black;
      color: #00ff00;
      font-family: 'Share Tech Mono', monospace;
      text-align: center;
      padding: 40px;
    }}
    h1 {{
      font-size: 3em;
      margin-top: 50px;
    }}
    p {{
      font-size: 1.4em;
    }}
    img {{
      margin-top: 30px;
      width: 300px;
      border-radius: 20px;
      box-shadow: 0 0 25px red;
    }}
    .footer {{
      margin-top: 60px;
      font-size: 0.9em;
      color: #777;
    }}
  </style>
</head>
<body>
  <h1>{judul}</h1>
  <p>{pesan}</p>
  <img src="{logo_url}" alt="logo">
  <audio autoplay loop hidden>
    <source src="{musik_url}" type="audio/mpeg">
  </audio>
  <div class="footer">© 2025 by butzXploit</div>
</body>
</html>
"""

# Simpan file
try:
    with open(nama_file, "w") as f:
        f.write(html_code)
    print(f"\n\033[92m[✓] HTML deface berhasil disimpan sebagai: {nama_file}\033[0m")
except Exception as e:
    print(f"\033[91m[!] Gagal menyimpan file: {e}\033[0m")
