#!/bin/bash
cd "/Users/lucasamarale/Documents/Claude/Projects/Desafio - Estágio Nola"
echo "🍽️  Iniciando Nola Bot..."
python3 proxy.py &
python3 -m http.server 8080 &
sleep 2
open -a "Google Chrome" "http://localhost:8080/nola_chatbot_frontend.html"
wait
