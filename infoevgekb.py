# ============================================
#   infoevgekb — сайт-визитка Евгения
#   Деплой на Render
# ============================================

from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# ==== Раздача картинки из корня репозитория ====
@app.route('/avatar.jpg')
def avatar():
    return send_from_directory('.', 'avatar.jpg')

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Евгений — Екатеринбург</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0%25' stop-color='%2358a6ff'/%3E%3Cstop offset='100%25' stop-color='%23bc8cff'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='64' height='64' rx='12' fill='url(%23g)'/%3E%3Ctext x='50%25' y='50%25' font-family='Arial' font-size='36' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='central'%3E%D0%95%3C/text%3E%3C/svg%3E">
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
    background:rgba(22,27,34,.85);
    border:1px solid #30363d;
    border-radius:24px;
    padding:50px 40px;
    max-width:600px;
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
    border:4px solid #58a6ff;
    margin:0 auto 20px;
    box-shadow:0 10px 40px rgba(188,140,255,.4);
    display:block;
    background:linear-gradient(135deg, #58a6ff, #bc8cff);
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

  /* ===== ПРОЕКТЫ ===== */
  .section-title {
    font-size:14px;
    color:#8b949e;
    text-transform:uppercase;
    letter-spacing:2px;
    margin:30px 0 16px;
    text-align:left;
    padding-left:4px;
  }
  .projects {
    display:grid;
    gap:12px;
    margin-bottom:24px;
  }
  .project {
    display:flex;
    align-items:center;
    gap:14px;
    padding:16px 20px;
    background:rgba(13,17,23,.6);
    border:1px solid #30363d;
    border-radius:12px;
    text-align:left;
    transition:.2s;
    text-decoration:none;
    color:#e6edf3;
  }
  .project:hover {
    border-color:#58a6ff;
    transform:translateX(4px);
    box-shadow:0 4px 20px rgba(88,166,255,.15);
  }
  .project-icon {
    font-size:28px;
    width:44px;
    height:44px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg, rgba(88,166,255,.2), rgba(188,140,255,.2));
    border-radius:10px;
    flex-shrink:0;
  }
  .project-info { flex:1; min-width:0; }
  .project-name {
    font-weight:600;
    font-size:15px;
    margin-bottom:2px;
  }
  .project-desc {
    color:#8b949e;
    font-size:12px;
  }
  .project-arrow {
    color:#484f58;
    font-size:18px;
    transition:.2s;
  }
  .project:hover .project-arrow {
    color:#58a6ff;
    transform:translateX(4px);
  }

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
    <img class="avatar" src="/avatar.jpg" alt="Евгений">
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
          <div class="info-value">Делать игры и сайты</div>
        </div>
      </div>
    </div>

    <div class="section-title">🚀 Мои проекты</div>
    <div class="projects">
      <a href="https://anygen.onrender.com" target="_blank" class="project">
        <div class="project-icon">🎲</div>
        <div class="project-info">
          <div class="project-name">AnyGen</div>
          <div class="project-desc">43 генератора в одном месте</div>
        </div>
        <div class="project-arrow">→</div>
      </a>

      <a href="https://qrgenhere.onrender.com" target="_blank" class="project">
        <div class="project-icon">📱</div>
        <div class="project-info">
          <div class="project-name">QR Generator</div>
          <div class="project-desc">Генератор QR-кодов с цветами</div>
        </div>
        <div class="project-arrow">→</div>
      </a>
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
