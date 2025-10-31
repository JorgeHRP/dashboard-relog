from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Dados do dashboard
dados = {
    "metricas_gerais": {
        "total_entregadores": 474,
        "media_msg_hora": 316.5,
        "media_msg_minuto": 8.2,
        "pico_max_msg": {"valor": 35, "horario": "19:29"},
        "pico_min_msg": {"valor": 1, "horario": "00:19"},
        "pico_max_chats": {"valor": 17, "horario": "09:57"},
        "pico_min_chats": {"valor": 1, "horario": "00:01"}
    },
    
    "mensagens_mais_comuns": [
        {"mensagem": "boa tarde", "quantidade": 274},
        {"mensagem": "<sem texto>", "quantidade": 160},
        {"mensagem": "boa noite", "quantidade": 135},
        {"mensagem": "sim", "quantidade": 130},
        {"mensagem": "?", "quantidade": 122},
        {"mensagem": "ok", "quantidade": 111},
        {"mensagem": "bom dia", "quantidade": 107},
        {"mensagem": "oi", "quantidade": 94},
        {"mensagem": "ola", "quantidade": 73},
        {"mensagem": "oii", "quantidade": 63}
    ],
    
    "palavras_frequentes": [
        {"palavra": "boa", "frequencia": 855},
        {"palavra": "vaga", "frequencia": 719},
        {"palavra": "não", "frequencia": 707},
        {"palavra": "que", "frequencia": 629},
        {"palavra": "tarde", "frequencia": 589},
        {"palavra": "para", "frequencia": 547},
        {"palavra": "pra", "frequencia": 378},
        {"palavra": "com", "frequencia": 361},
        {"palavra": "tem", "frequencia": 360},
        {"palavra": "noite", "frequencia": 357}
    ],
    
    "temas_principais": [
        {"palavra_chave": "vaga / vagas", "tema": "Pedidos e confirmações de vaga de entrega"},
        {"palavra_chave": "app", "tema": "Problemas ou dúvidas com o aplicativo"},
        {"palavra_chave": "caso", "tema": "Situações operacionais específicas"},
        {"palavra_chave": "pode", "tema": "Solicitações ou pedidos de ajuda"},
        {"palavra_chave": "turno", "tema": "Dúvidas sobre turnos de trabalho e disponibilidade"},
        {"palavra_chave": "seu / como", "tema": "Pedidos de orientação ou esclarecimento de processo"}
    ],
    
    "mensagens_por_hora": [
        {"hora": "00h", "quantidade": 173},
        {"hora": "01h", "quantidade": 4},
        {"hora": "02h", "quantidade": 1},
        {"hora": "03h", "quantidade": 5},
        {"hora": "05h", "quantidade": 1},
        {"hora": "06h", "quantidade": 17},
        {"hora": "07h", "quantidade": 28},
        {"hora": "08h", "quantidade": 64},
        {"hora": "09h", "quantidade": 209},
        {"hora": "10h", "quantidade": 474},
        {"hora": "11h", "quantidade": 359},
        {"hora": "12h", "quantidade": 514},
        {"hora": "13h", "quantidade": 525},
        {"hora": "14h", "quantidade": 628},
        {"hora": "15h", "quantidade": 575},
        {"hora": "16h", "quantidade": 645},
        {"hora": "17h", "quantidade": 673},
        {"hora": "18h", "quantidade": 786},
        {"hora": "19h", "quantidade": 458},
        {"hora": "20h", "quantidade": 354},
        {"hora": "21h", "quantidade": 360},
        {"hora": "22h", "quantidade": 310},
        {"hora": "23h", "quantidade": 116}
    ],
    
    "insights": [
        {
            "tipo": "critico",
            "titulo": "Pico de Atendimento às 18h",
            "descricao": "786 mensagens no horário de maior demanda. Recomenda-se aumentar a equipe de suporte neste período.",
            "icone": "⚠️"
        },
        {
            "tipo": "info",
            "titulo": "Mensagens Automatizáveis",
            "descricao": "42% das mensagens são saudações ou confirmações simples (ok, sim, boa tarde). Potencial para chatbot.",
            "icone": "🤖"
        },
        {
            "tipo": "sucesso",
            "titulo": "Temas Bem Definidos",
            "descricao": "As principais dúvidas concentram-se em: vagas (719 menções), app (problemas técnicos) e turnos.",
            "icone": "✅"
        },
        {
            "tipo": "alerta",
            "titulo": "Madrugada Ativa",
            "descricao": "173 mensagens entre 00h-01h. Avaliar necessidade de suporte 24h ou respostas automáticas.",
            "icone": "🌙"
        }
    ],
    
    "sugestoes": [
        {
            "prioridade": "alta",
            "acao": "Implementar FAQ automatizado sobre vagas",
            "impacto": "Redução estimada de 30-40% no volume de atendimentos manuais",
            "prazo": "Curto prazo (1-2 semanas)"
        },
        {
            "prioridade": "alta",
            "acao": "Criar respostas automáticas para problemas comuns do app",
            "impacto": "Resolução mais rápida de problemas técnicos recorrentes",
            "prazo": "Curto prazo (1-2 semanas)"
        },
        {
            "prioridade": "media",
            "acao": "Escalar equipe de suporte das 16h às 19h",
            "impacto": "Redução do tempo médio de resposta no horário de pico",
            "prazo": "Médio prazo (1 mês)"
        },
        {
            "prioridade": "media",
            "acao": "Dashboard de disponibilidade de vagas em tempo real",
            "impacto": "Redução de perguntas repetitivas sobre vagas disponíveis",
            "prazo": "Médio prazo (1-2 meses)"
        },
        {
            "prioridade": "baixa",
            "acao": "Sistema de notificação push para informações importantes",
            "impacto": "Comunicação proativa reduz dúvidas reativas",
            "prazo": "Longo prazo (3 meses)"
        }
    ]
}

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/dados')
def get_dados():
    return jsonify(dados)

@app.route('/api/metricas')
def get_metricas():
    return jsonify(dados['metricas_gerais'])

@app.route('/api/mensagens-hora')
def get_mensagens_hora():
    return jsonify(dados['mensagens_por_hora'])

@app.route('/api/insights')
def get_insights():
    return jsonify(dados['insights'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)