Pythonfrom flask import Flask, request, redirect, url_for, render_template_string
import sqlite3
from datetime import datetime, date

app = Flask(__name__)

DB_PATH = 'signos.db'

# ===================== BANCO DE DADOS =====================
def criar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_inicio TEXT NOT NULL,
            data_fim TEXT NOT NULL,
            elemento TEXT NOT NULL,
            planeta TEXT NOT NULL,
            descricao TEXT NOT NULL,
            caracteristicas TEXT NOT NULL,
            pontos_fortes TEXT NOT NULL,
            pontos_fracos TEXT NOT NULL
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM signos")
    if cursor.fetchone()[0] == 0:
        signos = [
            ('Áries', '21/03', '19/04', 'Fogo', 'Marte',
             'Áries é o primeiro signo do zodíaco, conhecido por sua energia e coragem.',
             'Corajoso, líder, aventureiro, independente e dinâmico.',
             'Iniciativa, entusiasmo, honestidade e capacidade de liderança.',
             'Impulsividade e impaciência.'),

            ('Touro', '20/04', '20/05', 'Terra', 'Vênus',
             'Touro valoriza estabilidade, conforto e lealdade.',
             'Paciente, determinado, leal, prático e apreciador do conforto.',
             'Persistência, confiabilidade e bom gosto.',
             'Teimosia e resistência a mudanças.'),

            ('Gêmeos', '21/05', '20/06', 'Ar', 'Mercúrio',
             'Gêmeos é o signo da comunicação e da curiosidade.',
             'Comunicativo, curioso, versátil, inteligente e sociável.',
             'Adaptabilidade, criatividade e capacidade de aprender rápido.',
             'Inconstância e superficialidade ocasional.'),

            ('Câncer', '21/06', '22/07', 'Água', 'Lua',
             'Câncer é sensível, protetor e ligado às emoções e à família.',
             'Emotivo, intuitivo, cuidadoso, leal e imaginativo.',
             'Empatia, proteção e memória emocional.',
             'Sensibilidade excessiva e mudanças de humor.'),

            ('Leão', '23/07', '22/08', 'Fogo', 'Sol',
             'Leão brilha com confiança, generosidade e criatividade.',
             'Confiante, generoso, criativo, carismático e líder natural.',
             'Coragem, otimismo e capacidade de inspirar os outros.',
             'Orgulho e necessidade de atenção.'),

            ('Virgem', '23/08', '22/09', 'Terra', 'Mercúrio',
             'Virgem é prático, detalhista e busca a perfeição.',
             'Organizado, analítico, prestativo, inteligente e perfeccionista.',
             'Atenção aos detalhes, praticidade e dedicação.',
             'Crítica excessiva e preocupação demais.'),

            ('Libra', '23/09', '22/10', 'Ar', 'Vênus',
             'Libra busca harmonia, justiça e beleza nas relações.',
             'Diplomático, justo, sociável, elegante e equilibrado.',
             'Capacidade de ver os dois lados e criar harmonia.',
             'Indecisão e dependência da aprovação dos outros.'),

            ('Escorpião', '23/10', '21/11', 'Água', 'Plutão',
             'Escorpião é intenso, misterioso e profundamente leal.',
             'Intenso, apaixonado, determinado, misterioso e leal.',
             'Força de vontade, intuição e capacidade de transformação.',
             'Ciúmes e tendência a guardar ressentimentos.'),

            ('Sagitário', '22/11', '21/12', 'Fogo', 'Júpiter',
             'Sagitário é aventureiro, otimista e amante da liberdade.',
             'Aventureiro, otimista, honesto, filosófico e independente.',
             'Entusiasmo, senso de humor e espírito livre.',
             'Impaciência e falta de tato às vezes.'),

            ('Capricórnio', '22/12', '19/01', 'Terra', 'Saturno',
             'Capricórnio é ambicioso, responsável e disciplinado.',
             'Ambicioso, responsável, disciplinado, prático e persistente.',
             'Determinação, organização e senso de responsabilidade.',
             'Rigidez e tendência ao pessimismo.'),

            ('Aquário', '20/01', '18/02', 'Ar', 'Urano',
             'Aquário é criativo, independente e visionário.',
             'Criativo, independente, humanitário, inteligente e original.',
             'Inovação, amizade verdadeira e visão de futuro.',
             'Distância emocional e rebeldia.'),

            ('Peixes', '19/02', '20/03', 'Água', 'Netuno',
             'Peixes é sonhador, empático e artístico.',
             'Sonhador, empático, criativo, gentil e intuitivo.',
             'Compaixão, imaginação e sensibilidade artística.',
             'Tendência a fugir da realidade e indecisão.')
        ]

        cursor.executemany('''
            INSERT INTO signos (nome, data_inicio, data_fim, elemento, planeta, descricao, caracteristicas, pontos_fortes, pontos_fracos)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', signos)
        print("Banco de dados criado e populado com sucesso!")

    conn.commit()
    conn.close()


def determinar_signo(mes, dia):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return 'Áries'
    if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return 'Touro'
    if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return 'Gêmeos'
    if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return 'Câncer'
    if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return 'Leão'
    if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return 'Virgem'
    if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return 'Libra'
    if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return 'Escorpião'
    if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return 'Sagitário'
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return 'Capricórnio'
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return 'Aquário'
    if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return 'Peixes'
    return None


def buscar_signo(nome):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signos WHERE nome = ?", (nome,))
    signo = cursor.fetchone()
    conn.close()
    return signo


# Cria o banco ao iniciar
criar_banco()

# ===================== TEMPLATES HTML =====================
HTML_INDEX = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Descubra seu Signo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .card {
            border: none;
            border-radius: 15px;
            overflow: hidden;
        }
        .btn-primary {
            background: linear-gradient(45deg, #667eea, #764ba2);
            border: none;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow-lg">
                    <div class="card-header text-center bg-primary text-white">
                        <h1 class="h3 mb-0">✨ Descubra seu Signo Zodiacal</h1>
                    </div>
                    <div class="card-body">
                        <p class="text-center text-muted">Insira sua data de nascimento para descobrir seu signo.</p>
                        
                        <form action="/resultado" method="POST">
                            <div class="mb-3">
                                <label for="data_nascimento" class="form-label">Data de Nascimento</label>
                                <input type="date" class="form-control" id="data_nascimento" name="data_nascimento" required max="{{ hoje }}">
                            </div>
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg">Descobrir meu Signo</button>
                            </div>
                        </form>
                    </div>
                    <div class="card-footer text-center text-muted">
                        <small>Python + Flask + SQLite</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

HTML_RESULTADO = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seu Signo{% if signo %} - {{ signo['nome'] }}{% endif %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .card { border: none; border-radius: 15px; overflow: hidden; }
        .text-primary { color: #5a67d8 !important; }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                {% if erro %}
                    <div class="alert alert-danger">
                        {{ erro }}
                        <div class="mt-3">
                            <a href="/" class="btn btn-secondary">Voltar</a>
                        </div>
                    </div>
                {% else %}
                    <div class="card shadow-lg">
                        <div class="card-header text-center bg-success text-white">
                            <h1 class="display-5 mb-0">🌟 {{ signo['nome'] }}</h1>
                            <p class="mb-0">{{ signo['data_inicio'] }} a {{ signo['data_fim'] }}</p>
                        </div>
                        <div class="card-body">
                            <div class="row mb-4">
                                <div class="col-md-6">
                                    <h5 class="text-primary">Elemento</h5>
                                    <p class="lead">{{ signo['elemento'] }}</p>
                                </div>
                                <div class="col-md-6">
                                    <h5 class="text-primary">Planeta Regente</h5>
                                    <p class="lead">{{ signo['planeta'] }}</p>
                                </div>
                            </div>

                            <h5 class="text-primary">Descrição</h5>
                            <p>{{ signo['descricao'] }}</p>

                            <h5 class="text-primary mt-4">Principais Características</h5>
                            <p>{{ signo['caracteristicas'] }}</p>

                            <div class="row mt-4">
                                <div class="col-md-6">
                                    <div class="card border-success">
                                        <div class="card-header bg-success text-white">Pontos Fortes</div>
                                        <div class="card-body">
                                            <p class="mb-0">{{ signo['pontos_fortes'] }}</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="card border-warning">
                                        <div class="card-header bg-warning">Pontos a Melhorar</div>
                                        <div class="card-body">
                                            <p class="mb-0">{{ signo['pontos_fracos'] }}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="text-center mt-4">
                                <p class="text-muted">Nascido(a) em {{ data_formatada }}</p>
                                <a href="/" class="btn btn-primary btn-lg">Consultar outra data</a>
                            </div>
                        </div>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</body>
</html>
'''

# ===================== ROTAS =====================
@app.route('/')
def index():
    hoje = date.today().isoformat()
    return render_template_string(HTML_INDEX, hoje=hoje)


@app.route('/resultado', methods=['POST'])
def resultado():
    data_nascimento = request.form.get('data_nascimento')

    if not data_nascimento:
        return redirect(url_for('index'))

    try:
        data = datetime.strptime(data_nascimento, '%Y-%m-%d')
        mes = data.month
        dia = data.day
        data_formatada = data.strftime('%d/%m/%Y')
    except ValueError:
        return redirect(url_for('index'))

    nome_signo = determinar_signo(mes, dia)

    if not nome_signo:
        return render_template_string(HTML_RESULTADO, erro="Não foi possível determinar o signo.")

    signo = buscar_signo(nome_signo)

    if not signo:
        return render_template_string(HTML_RESULTADO, erro="Signo não encontrado no banco de dados.")

    return render_template_string(HTML_RESULTADO, signo=signo, data_formatada=data_formatada)


if __name__ == '__main__':
    print("Servidor iniciado em http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)