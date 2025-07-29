import os

# Banner
os.system("clear")
print("""
\033[91m╔══════════════════════════════════════════════╗
║     \033[92mHTML Deface Generator by butzXploit (V2)\033[91m    ║
╚══════════════════════════════════════════════╝
""")

# Input
judul = input("\033[93m[+] Judul Deface: \033[0m")
pesan = input("\033[93m[+] Pesan Utama: \033[0m")
logo_url = input("\033[93m[+] URL Logo Gambar: \033[0m")
musik_url = input("\033[93m[+] URL Musik Latar (MP3): \033[0m")
bg_url = input("\033[93m[+] URL Background (gambar/video/gif): \033[0m")
nama_file = input("\033[93m[+] Nama File Output (contoh: defaced.html): \033[0m")

# Cek jenis background
is_video = any(ext in bg_url.lower() for ext in ['.mp4', 'youtube.com', 'youtu.be'])

# HTML Generator
if is_video:
    bg_html = f"""
  <video autoplay muted loop id="bgvid" style="position:fixed;right:0;bottom:0;min-width:100%;min-height:100%;z-index:-1;">
    <source src="{bg_url}" type="video/mp4">
  </video>
    """
else:
    bg_html = f"""
  <style>
    body {{
      background: url('{bg_url}') no-repeat center center fixed;
      background-size: cover;
    }}
  </style>
    """

# Gabungkan semua
html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{judul}</title>
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
  <style>
    body {{
      margin: 0;
      padding: 0;
      color: #00ff00;
      font-family: 'Share Tech Mono', monospace;
      text-align: center;
    }}
    h1 {{
      font-size: 3em;
      margin-top: 80px;
      text-shadow: 0 0 10px red;
    }}
    p {{
      font-size: 1.4em;
      margin: 20px;
      text-shadow: 0 0 5px lime;
    }}
    img {{
      margin-top: 30px;
      width: 280px;
      border-radius: 20px;
      box-shadow: 0 0 25px red;
    }}
    .footer {{
      margin-top: 50px;
      font-size: 0.9em;
      color: #aaa;
    }}
  </style>
  {bg_html}
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
