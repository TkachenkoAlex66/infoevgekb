# ============================================
#   infoevgekb — сайт-визитка Евгения
#   Деплой на Render
# ============================================

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Евгений — Екатеринбург</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0%25' stop-color='%2358a6ff'/%3E%3Cstop offset='100%25' stop-color='%23bc8cff'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='64' height='64' rx='12' fill='url(%23g)'/%3E%3Ctext x='50%25' y='50%25' font-family='Arial,sans-serif' font-size='44' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='central'%3E%D0%95%3C/text%3E%3C/svg%3E">
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    font-family:'Segoe UI',Arial,sans-serif;
    background:linear-gradient(135deg, #0d1117 0%, #161b22 50%, #1a1f2e 100%);
    color:#e6edf3;
    min-height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:20px;
  }
  .card {
    background:rgba(22,27,34,.8);
    border:1px solid #30363d;
    border-radius:24px;
    padding:50px 40px;
    max-width:560px;
    width:100%;
    text-align:center;
    backdrop-filter:blur(20px);
    box-shadow:0 20px 60px rgba(88,166,255,.15);
  }
  .avatar {
    width:140px;
    height:140px;
    border-radius:50%;
    object-fit:cover;
    border:4px solid transparent;
    background:linear-gradient(135deg, #58a6ff, #bc8cff) border-box;
    -webkit-mask:linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite:xor;
    mask-composite:exclude;
    margin:0 auto 20px;
    box-shadow:0 10px 40px rgba(188,140,255,.4);
    display:block;
  }
  h1 {
    font-size:42px;
    letter-spacing:2px;
    background:linear-gradient(90deg, #58a6ff, #bc8cff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:6px;
  }
  .subtitle { color:#8b949e; font-size:15px; margin-bottom:30px; }
  .info {
    display:grid;
    gap:14px;
    margin-bottom:30px;
  }
  .info-item {
    display:flex;
    align-items:center;
    gap:14px;
    padding:14px 20px;
    background:rgba(13,17,23,.6);
    border:1px solid #30363d;
    border-radius:12px;
    text-align:left;
    transition:.2s;
  }
  .info-item:hover {
    border-color:#58a6ff;
    transform:translateX(4px);
  }
  .info-icon { font-size:24px; }
  .info-text { flex:1; }
  .info-label { color:#8b949e; font-size:12px; }
  .info-value { font-weight:600; font-size:15px; }
  .socials {
    display:flex;
    gap:12px;
    justify-content:center;
    flex-wrap:wrap;
    margin-top:20px;
  }
  .social-btn {
    padding:12px 24px;
    background:linear-gradient(135deg, #58a6ff, #bc8cff);
    border:none;
    border-radius:30px;
    color:#fff;
    font-size:14px;
    font-weight:600;
    text-decoration:none;
    cursor:pointer;
    transition:.2s;
    display:inline-block;
  }
  .social-btn:hover {
    transform:translateY(-2px);
    box-shadow:0 8px 20px rgba(88,166,255,.3);
  }
  .social-btn.disabled {
    background:#21262d;
    border:1px solid #30363d;
    cursor:default;
    opacity:.7;
  }
  .social-btn.disabled:hover {
    transform:none;
    box-shadow:none;
  }
  .footer {
    margin-top:30px;
    color:#484f58;
    font-size:12px;
  }
</style>
</head>
<body>
  <div class="card">
    <img class="avatar" src="https://raw.githubusercontent.com/TkachenkoAlex66/infoevgekb/main/avatar.jpg" alt="Евгений">
    <h1>Евгений</h1>
    <div class="subtitle">📍 Екатеринбург</div>

    <div class="info">
      <div class="info-item">
        <div class="info-icon">🎂</div>
        <div class="info-text">
          <div class="info-label">Возраст</div>
          <div class="info-value">9 лет (2017 год)</div>
        </div>
      </div>
      <div class="info-item">
        <div class="info-icon">📚</div>
        <div class="info-text">
          <div class="info-label">Учёба</div>
          <div class="info-value">3 класс</div>
        </div>
      </div>
      <div class="info-item">
        <div class="info-icon">🎮</div>
        <div class="info-text">
          <div class="info-label">Хобби</div>
          <div class="info-value">Делать игры</div>
        </div>
      </div>
      <div class="info-item">
        <div class="info-icon">🚀</div>
        <div class="info-text">
          <div class="info-label">Проект</div>
          <div class="info-value"><a href="https://anygen.onrender.com" target="_blank" style="color:#58a6ff;text-decoration:none;">AnyGen — 43 генератора</a></div>
        </div>
      </div>
    </div>

    <div class="socials">
      <a href="https://max.ru/u/f9LHodD0cOJgAOY6oeMWTGmjPgkUXLRT0rMp5OBuqpSDxmQ-EJW4n5Mp-ZA" target="_blank" class="social-btn">📱 MAX</a>
      <div class="social-btn disabled">💬 WhatsApp</div>
    </div>

    <div class="footer">© 2026 · Евгений</div>
  </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
