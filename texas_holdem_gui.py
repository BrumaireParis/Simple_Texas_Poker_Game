import itertools
import json
import locale
import random
import tkinter as tk
from dataclasses import dataclass, field
from pathlib import Path
from tkinter import messagebox
from typing import List


SUITS = ["S", "H", "D", "C"]
SUIT_SYMBOLS = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}
RANKS = list(range(2, 15))
RANK_LABELS = {
    14: "A",
    13: "K",
    12: "Q",
    11: "J",
    10: "10",
    9: "9",
    8: "8",
    7: "7",
    6: "6",
    5: "5",
    4: "4",
    3: "3",
    2: "2",
}
ROOMS = {
    "beginner": {"small_blind": 10, "big_blind": 20, "buy_in": 1000},
    "normal": {"small_blind": 25, "big_blind": 50, "buy_in": 2000},
    "high": {"small_blind": 100, "big_blind": 200, "buy_in": 6000},
}
DIFFICULTIES = ["easy", "medium", "hard"]
RESOLUTIONS = [
    "1280x720",
    "1366x768",
    "1440x900",
    "1600x900",
    "1680x1050",
    "1920x1080",
    "1920x1200",
    "2560x1440",
    "2560x1600",
    "3440x1440",
    "3840x2160",
]
UI_SCALES = {
    "80%": 0.8,
    "90%": 0.9,
    "100%": 1.0,
    "110%": 1.1,
    "125%": 1.25,
    "150%": 1.5,
}
LEADERBOARD_FILE = Path("leaderboard.json")
VIRTUAL_LEADERBOARD_BLUEPRINT = [
    ("high", 12400, 9, 18),
    ("normal", 4250, 7, 16),
    ("beginner", 1860, 6, 15),
    ("high", 9300, 5, 12),
    ("normal", 3480, 6, 14),
    ("beginner", 1510, 4, 11),
]
LANGUAGES = {
    "zh": "中文",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "pt": "Português",
    "ja": "日本語",
    "ko": "한국어",
}
AI_NAMES = {
    "zh": ["陈晨", "林浩", "周宁", "王磊", "赵雨", "许安", "顾然", "沈澄", "刘洋", "唐悦", "韩枫", "苏宁"],
    "en": ["Alex", "Blake", "Casey", "Drew", "Elliot", "Finley", "Harper", "Jordan", "Morgan", "Quinn", "Riley", "Taylor"],
    "de": ["Lukas", "Felix", "Jonas", "Leon", "Hanna", "Mia", "Emma", "Anna", "Noah", "Paul", "Lea", "Max"],
    "fr": ["Lucas", "Hugo", "Louis", "Jules", "Emma", "Chloé", "Léa", "Manon", "Noah", "Camille", "Inès", "Nathan"],
    "es": ["Mateo", "Lucas", "Sofía", "Valeria", "Martín", "Lucía", "Daniel", "Emma", "Leo", "Paula", "Hugo", "Alba"],
    "pt": ["João", "Miguel", "Pedro", "Lucas", "Maria", "Ana", "Sofia", "Laura", "Gabriel", "Luísa", "Rafael", "Beatriz"],
    "ja": ["陽翔", "蓮", "樹", "湊", "葵", "結菜", "陽菜", "凛", "悠真", "美咲", "大和", "心春"],
    "ko": ["민준", "서준", "도윤", "예준", "서연", "지우", "하윤", "서아", "지호", "유준", "수아", "하린"],
}
BUSINESS_LEADERBOARD_NAMES = {
    "zh": ["埃隆·马斯克", "沃伦·巴菲特", "比尔·盖茨", "杰夫·贝索斯", "马云", "贝尔纳·阿尔诺"],
    "en": ["Elon Musk", "Warren Buffett", "Bill Gates", "Jeff Bezos", "Jack Ma", "Bernard Arnault"],
    "de": ["Elon Musk", "Warren Buffett", "Bill Gates", "Jeff Bezos", "Jack Ma", "Bernard Arnault"],
    "fr": ["Elon Musk", "Warren Buffett", "Bill Gates", "Jeff Bezos", "Jack Ma", "Bernard Arnault"],
    "es": ["Elon Musk", "Warren Buffett", "Bill Gates", "Jeff Bezos", "Jack Ma", "Bernard Arnault"],
    "pt": ["Elon Musk", "Warren Buffett", "Bill Gates", "Jeff Bezos", "Jack Ma", "Bernard Arnault"],
    "ja": ["イーロン・マスク", "ウォーレン・バフェット", "ビル・ゲイツ", "ジェフ・ベゾス", "ジャック・マー", "ベルナール・アルノー"],
    "ko": ["일론 머스크", "워런 버핏", "빌 게이츠", "제프 베이조스", "마윈", "베르나르 아르노"],
}
AVATAR_COLORS = [
    "#2563eb",
    "#7c3aed",
    "#db2777",
    "#ea580c",
    "#16a34a",
    "#0891b2",
    "#4f46e5",
    "#be123c",
]
PLAYER_SECONDS = 30
BUBBLE_SHADES = ["#fff7ed", "#ffedd5", "#fed7aa", "#fdba74", "#fb923c"]


TRANSLATIONS = {
    "zh": {
        "app_title": "德州扑克",
        "new_game": "新游戏",
        "leaderboard": "排行榜",
        "settings": "设置",
        "exit_game": "退出游戏",
        "back": "返回",
        "start": "开始",
        "apply": "应用",
        "language": "语言",
        "resolution": "分辨率",
        "ui_scale": "UI 缩放",
        "fullscreen": "全屏",
        "ai_count": "AI 数量",
        "ai_difficulty": "AI 难度",
        "room": "分房",
        "room_beginner": "新手房",
        "room_normal": "普通房",
        "room_high": "高倍房",
        "difficulty_easy": "初级",
        "difficulty_medium": "中级",
        "difficulty_hard": "高级",
        "ai_suffix": "AI",
        "player": "玩家",
        "main_menu": "主菜单",
        "action_log": "行动记录",
        "check_call": "跟注/看牌",
        "raise": "加注",
        "fold": "弃牌",
        "next_hand": "下一手",
        "check": "看牌",
        "call": "跟注",
        "all_in": "全下",
        "thinking": "思考",
        "thinking_log": "{name} 正在思考...",
        "room_info": "最多 6 人同桌（玩家 + 1 到 5 名 AI）。新手房 盲注 10/20，普通房 25/50，高倍房 100/200。每局会自动轮转庄位、小盲和大盲。",
        "no_records": "暂无真实记录。当前显示虚拟挑战榜，完成一局游戏后会替换为你的成绩。",
        "leaderboard_row": "{rank}. {name}  净收益: {profit}  资金: {chips}  胜局: {wins}/{hands}  胜率: {win_rate}  房间: {room}",
        "confirm_menu_title": "返回主菜单",
        "confirm_menu_text": "当前游戏会保存记录并返回主菜单，确定吗？",
        "game_over": "游戏结束",
        "broke": "你的资金已经输完，游戏结束。",
        "final_winner": "所有 AI 都已离桌，你成为最终赢家。",
        "new_hand": "新一手开始，庄家是 {dealer}。",
        "post_blind": "{name} 支付{blind} {amount}。",
        "small_blind": "小盲",
        "big_blind": "大盲",
        "flop": "翻牌圈。",
        "turn": "转牌圈。",
        "river": "河牌圈。",
        "action_fold": "{name} 弃牌。",
        "action_check": "{name} 看牌。",
        "action_call": "{name} 跟注 {amount}。",
        "action_raise": "{name} 加注到 {amount}。",
        "action_all_in_call": "{name} 全下跟注 {amount}。",
        "timeout_check": "玩家超时，自动看牌。",
        "timeout_fold": "玩家超时，自动弃牌。",
        "wins_pot": "{name} 赢得底池 {amount}。",
        "showdown": "摊牌：{names} 最好牌型 {hand}。分池结算：{awards}。",
        "left_table": "{name} 资金耗尽，离开牌桌。",
        "table_info": "{room}  盲注 {small}/{big}    底池 {pot}    当前下注 {bet}",
        "timer": "玩家倒计时: {seconds}",
        "pot": "底池",
        "current_bet": "当前下注",
        "chips": "资金",
        "round_bet": "本轮",
        "dealer": "庄",
        "hand_8": "同花顺",
        "hand_7": "四条",
        "hand_6": "葫芦",
        "hand_5": "同花",
        "hand_4": "顺子",
        "hand_3": "三条",
        "hand_2": "两对",
        "hand_1": "一对",
        "hand_0": "高牌",
        "raise_range": "最小 {min}  ·  最大 {max}",
    },
    "en": {
        "app_title": "Texas Hold'em",
        "new_game": "New Game",
        "leaderboard": "Leaderboard",
        "settings": "Settings",
        "exit_game": "Exit Game",
        "back": "Back",
        "start": "Start",
        "apply": "Apply",
        "language": "Language",
        "resolution": "Resolution",
        "ui_scale": "UI Scale",
        "fullscreen": "Fullscreen",
        "ai_count": "AI Count",
        "ai_difficulty": "AI Difficulty",
        "room": "Room",
        "room_beginner": "Beginner Room",
        "room_normal": "Standard Room",
        "room_high": "High Stakes",
        "difficulty_easy": "Easy",
        "difficulty_medium": "Medium",
        "difficulty_hard": "Hard",
        "ai_suffix": "AI",
        "player": "Player",
        "main_menu": "Main Menu",
        "action_log": "Action Log",
        "check_call": "Call / Check",
        "raise": "Raise",
        "fold": "Fold",
        "next_hand": "Next Hand",
        "check": "Check",
        "call": "Call",
        "all_in": "All-in",
        "thinking": "Thinking",
        "thinking_log": "{name} is thinking...",
        "room_info": "Up to 6 players at one table. Beginner blinds 10/20, Standard 25/50, High Stakes 100/200. Dealer, small blind, and big blind rotate each hand.",
        "no_records": "No real records yet. A virtual challenge board is shown until you finish a game.",
        "leaderboard_row": "{rank}. {name}  Profit: {profit}  Chips: {chips}  Wins: {wins}/{hands}  Win Rate: {win_rate}  Room: {room}",
        "confirm_menu_title": "Return to Menu",
        "confirm_menu_text": "The current game will be saved before returning to the main menu. Continue?",
        "game_over": "Game Over",
        "broke": "You are out of chips. Game over.",
        "final_winner": "All AI players have left the table. You are the final winner.",
        "new_hand": "New hand started. Dealer: {dealer}.",
        "post_blind": "{name} posts {blind} {amount}.",
        "small_blind": "small blind",
        "big_blind": "big blind",
        "flop": "Flop.",
        "turn": "Turn.",
        "river": "River.",
        "action_fold": "{name} folds.",
        "action_check": "{name} checks.",
        "action_call": "{name} calls {amount}.",
        "action_raise": "{name} raises to {amount}.",
        "action_all_in_call": "{name} is all-in calling {amount}.",
        "timeout_check": "Player timed out and checks.",
        "timeout_fold": "Player timed out and folds.",
        "wins_pot": "{name} wins the pot {amount}.",
        "showdown": "Showdown: {names} best hand {hand}. Side pots: {awards}.",
        "left_table": "{name} is out of chips and leaves the table.",
        "table_info": "{room}  Blinds {small}/{big}    Pot {pot}    Current Bet {bet}",
        "timer": "Player Timer: {seconds}",
        "pot": "Pot",
        "current_bet": "Current Bet",
        "chips": "Chips",
        "round_bet": "This Round",
        "dealer": "D",
        "hand_8": "Straight Flush",
        "hand_7": "Four of a Kind",
        "hand_6": "Full House",
        "hand_5": "Flush",
        "hand_4": "Straight",
        "hand_3": "Three of a Kind",
        "hand_2": "Two Pair",
        "hand_1": "One Pair",
        "hand_0": "High Card",
        "raise_range": "Min {min}  ·  Max {max}",
    },
}


def add_language(lang, overrides):
    data = TRANSLATIONS["en"].copy()
    data.update(overrides)
    TRANSLATIONS[lang] = data


add_language("de", {
    "app_title": "Texas Hold'em",
    "new_game": "Neues Spiel", "leaderboard": "Bestenliste", "settings": "Einstellungen", "exit_game": "Spiel beenden",
    "back": "Zurück", "start": "Start", "apply": "Anwenden", "language": "Sprache", "resolution": "Auflösung",
    "ui_scale": "UI-Skalierung", "fullscreen": "Vollbild", "ai_count": "KI-Anzahl", "ai_difficulty": "KI-Schwierigkeit",
    "room": "Raum", "room_beginner": "Anfängerraum", "room_normal": "Standardraum", "room_high": "High-Stakes-Raum",
    "difficulty_easy": "Einfach", "difficulty_medium": "Mittel", "difficulty_hard": "Schwer", "ai_suffix": "KI",
    "player": "Spieler", "main_menu": "Hauptmenü", "action_log": "Aktionsprotokoll", "check_call": "Mitgehen / Checken",
    "raise": "Erhöhen", "fold": "Passen", "next_hand": "Nächste Hand", "check": "Checken", "call": "Mitgehen",
    "all_in": "All-in", "thinking": "Denkt nach", "thinking_log": "{name} denkt nach...",
    "small_blind": "Small Blind", "big_blind": "Big Blind", "flop": "Flop.", "turn": "Turn.", "river": "River.",
    "room_info": "Bis zu 6 Spieler an einem Tisch. Anfänger-Blinds 10/20, Standard 25/50, High Stakes 100/200. Dealer, Small Blind und Big Blind rotieren jede Hand.",
    "no_records": "Noch keine echten Einträge. Bis zum ersten abgeschlossenen Spiel wird eine virtuelle Bestenliste angezeigt.",
    "leaderboard_row": "{rank}. {name}  Gewinn: {profit}  Chips: {chips}  Siege: {wins}/{hands}  Quote: {win_rate}  Raum: {room}",
    "confirm_menu_title": "Zurück zum Menü", "confirm_menu_text": "Das aktuelle Spiel wird gespeichert. Zum Hauptmenü zurückkehren?",
    "game_over": "Spiel vorbei", "broke": "Du hast keine Chips mehr. Spiel vorbei.",
    "final_winner": "Alle KI-Spieler haben den Tisch verlassen. Du bist der endgültige Gewinner.",
    "new_hand": "Neue Hand gestartet. Dealer: {dealer}.", "post_blind": "{name} zahlt {blind} {amount}.",
    "action_fold": "{name} passt.", "action_check": "{name} checkt.", "action_call": "{name} geht {amount} mit.",
    "action_raise": "{name} erhöht auf {amount}.", "timeout_check": "Spieler ist abgelaufen und checkt.",
    "action_all_in_call": "{name} ist all-in und geht {amount} mit.",
    "timeout_fold": "Spieler ist abgelaufen und passt.", "wins_pot": "{name} gewinnt den Pot {amount}.",
    "showdown": "Showdown: {names} beste Hand {hand}. Side Pots: {awards}.", "left_table": "{name} hat keine Chips mehr und verlässt den Tisch.",
    "table_info": "{room}  Blinds {small}/{big}    Pot {pot}    Aktueller Einsatz {bet}", "timer": "Spieler-Timer: {seconds}",
    "pot": "Pot", "current_bet": "Aktueller Einsatz",
    "chips": "Chips", "round_bet": "Diese Runde", "hand_8": "Straight Flush", "hand_7": "Vierling",
    "hand_6": "Full House", "hand_5": "Flush", "hand_4": "Straight", "hand_3": "Drilling",
    "hand_2": "Zwei Paare", "hand_1": "Ein Paar", "hand_0": "High Card",
})

add_language("fr", {
    "new_game": "Nouvelle partie", "leaderboard": "Classement", "settings": "Paramètres", "exit_game": "Quitter",
    "back": "Retour", "start": "Démarrer", "apply": "Appliquer", "language": "Langue", "resolution": "Résolution",
    "ui_scale": "Échelle UI", "fullscreen": "Plein écran", "ai_count": "Nombre d'IA", "ai_difficulty": "Difficulté IA",
    "room": "Salon", "room_beginner": "Salon débutant", "room_normal": "Salon standard", "room_high": "Hautes mises",
    "difficulty_easy": "Facile", "difficulty_medium": "Moyen", "difficulty_hard": "Difficile", "ai_suffix": "IA",
    "player": "Joueur", "main_menu": "Menu principal", "action_log": "Journal des actions", "check_call": "Suivre / Parole",
    "raise": "Relancer", "fold": "Se coucher", "next_hand": "Main suivante", "check": "Parole", "call": "Suivre",
    "all_in": "Tapis", "thinking": "Réfléchit", "thinking_log": "{name} réfléchit...",
    "small_blind": "petite blind", "big_blind": "grosse blind", "flop": "Flop.", "turn": "Tournant.", "river": "Rivière.",
    "room_info": "Jusqu'à 6 joueurs à la table. Blinds débutant 10/20, standard 25/50, hautes mises 100/200. Le bouton, la petite blind et la grosse blind tournent à chaque main.",
    "no_records": "Aucun vrai record pour le moment. Un classement virtuel s'affiche jusqu'à la fin d'une partie.",
    "leaderboard_row": "{rank}. {name}  Gain: {profit}  Jetons: {chips}  Victoires: {wins}/{hands}  Taux: {win_rate}  Salon: {room}",
    "confirm_menu_title": "Retour au menu", "confirm_menu_text": "La partie actuelle sera sauvegardée avant le retour au menu. Continuer ?",
    "game_over": "Partie terminée", "broke": "Vous n'avez plus de jetons. Partie terminée.",
    "final_winner": "Tous les joueurs IA ont quitté la table. Vous êtes le vainqueur final.",
    "new_hand": "Nouvelle main. Bouton: {dealer}.", "post_blind": "{name} pose {blind} {amount}.",
    "action_fold": "{name} se couche.", "action_check": "{name} fait parole.", "action_call": "{name} suit {amount}.",
    "action_raise": "{name} relance à {amount}.", "action_all_in_call": "{name} est à tapis et suit {amount}.",
    "timeout_check": "Le joueur a dépassé le temps et fait parole.", "timeout_fold": "Le joueur a dépassé le temps et se couche.",
    "wins_pot": "{name} remporte le pot {amount}.", "showdown": "Abattage : {names} meilleure main {hand}. Pots annexes : {awards}.",
    "left_table": "{name} n'a plus de jetons et quitte la table.", "table_info": "{room}  Blinds {small}/{big}    Pot {pot}    Mise actuelle {bet}",
    "timer": "Temps joueur : {seconds}", "pot": "Pot", "current_bet": "Mise actuelle",
    "chips": "Jetons", "round_bet": "Ce tour", "hand_8": "Quinte flush", "hand_7": "Carré",
    "hand_6": "Full", "hand_5": "Couleur", "hand_4": "Suite", "hand_3": "Brelan",
    "hand_2": "Deux paires", "hand_1": "Paire", "hand_0": "Carte haute",
})

add_language("es", {
    "new_game": "Nueva partida", "leaderboard": "Clasificación", "settings": "Ajustes", "exit_game": "Salir",
    "back": "Volver", "start": "Empezar", "apply": "Aplicar", "language": "Idioma", "resolution": "Resolución",
    "ui_scale": "Escala UI", "fullscreen": "Pantalla completa", "ai_count": "Cantidad de IA", "ai_difficulty": "Dificultad IA",
    "room": "Sala", "room_beginner": "Sala principiante", "room_normal": "Sala estándar", "room_high": "Altas apuestas",
    "difficulty_easy": "Fácil", "difficulty_medium": "Medio", "difficulty_hard": "Difícil", "ai_suffix": "IA",
    "player": "Jugador", "main_menu": "Menú principal", "action_log": "Registro", "check_call": "Igualar / Pasar",
    "raise": "Subir", "fold": "Retirarse", "next_hand": "Siguiente mano", "check": "Pasar", "call": "Igualar",
    "all_in": "All-in", "thinking": "Pensando", "thinking_log": "{name} está pensando...",
    "small_blind": "ciega pequeña", "big_blind": "ciega grande", "flop": "Flop.", "turn": "Turn.", "river": "River.",
    "room_info": "Hasta 6 jugadores por mesa. Ciegas principiante 10/20, estándar 25/50, altas apuestas 100/200. Botón, ciega pequeña y ciega grande rotan cada mano.",
    "no_records": "Aún no hay registros reales. Se muestra una clasificación virtual hasta que termines una partida.",
    "leaderboard_row": "{rank}. {name}  Beneficio: {profit}  Fichas: {chips}  Victorias: {wins}/{hands}  Tasa: {win_rate}  Sala: {room}",
    "confirm_menu_title": "Volver al menú", "confirm_menu_text": "La partida actual se guardará antes de volver al menú. ¿Continuar?",
    "game_over": "Fin de la partida", "broke": "Te has quedado sin fichas. Fin de la partida.",
    "final_winner": "Todos los jugadores de IA han dejado la mesa. Eres el ganador final.",
    "new_hand": "Nueva mano. Botón: {dealer}.", "post_blind": "{name} pone {blind} {amount}.",
    "action_fold": "{name} se retira.", "action_check": "{name} pasa.", "action_call": "{name} iguala {amount}.",
    "action_raise": "{name} sube a {amount}.", "action_all_in_call": "{name} va all-in e iguala {amount}.",
    "timeout_check": "El jugador agotó el tiempo y pasa.", "timeout_fold": "El jugador agotó el tiempo y se retira.",
    "wins_pot": "{name} gana el bote {amount}.", "showdown": "Showdown: {names} mejor mano {hand}. Botes secundarios: {awards}.",
    "left_table": "{name} se queda sin fichas y deja la mesa.", "table_info": "{room}  Ciegas {small}/{big}    Bote {pot}    Apuesta actual {bet}",
    "timer": "Temporizador: {seconds}", "pot": "Bote", "current_bet": "Apuesta actual",
    "chips": "Fichas", "round_bet": "Esta ronda", "hand_8": "Escalera de color", "hand_7": "Póker",
    "hand_6": "Full house", "hand_5": "Color", "hand_4": "Escalera", "hand_3": "Trío",
    "hand_2": "Doble pareja", "hand_1": "Pareja", "hand_0": "Carta alta",
    "raise_range": "Mín {min}  ·  Máx {max}",
})

add_language("pt", {
    "new_game": "Novo jogo", "leaderboard": "Classificação", "settings": "Configurações", "exit_game": "Sair",
    "back": "Voltar", "start": "Iniciar", "apply": "Aplicar", "language": "Idioma", "resolution": "Resolução",
    "ui_scale": "Escala da UI", "fullscreen": "Tela cheia", "ai_count": "Número de IA", "ai_difficulty": "Dificuldade da IA",
    "room": "Sala", "room_beginner": "Sala iniciante", "room_normal": "Sala padrão", "room_high": "Altas apostas",
    "difficulty_easy": "Fácil", "difficulty_medium": "Médio", "difficulty_hard": "Difícil", "ai_suffix": "IA",
    "player": "Jogador", "main_menu": "Menu principal", "action_log": "Registro de ações", "check_call": "Pagar / Mesa",
    "raise": "Aumentar", "fold": "Desistir", "next_hand": "Próxima mão", "check": "Mesa", "call": "Pagar",
    "all_in": "All-in", "thinking": "Pensando", "thinking_log": "{name} está pensando...",
    "small_blind": "small blind", "big_blind": "big blind", "flop": "Flop.", "turn": "Turn.", "river": "River.",
    "room_info": "Até 6 jogadores por mesa. Blinds iniciante 10/20, padrão 25/50, altas apostas 100/200. Dealer, small blind e big blind giram a cada mão.",
    "no_records": "Ainda não há registros reais. Uma classificação virtual aparece até você terminar uma partida.",
    "leaderboard_row": "{rank}. {name}  Lucro: {profit}  Fichas: {chips}  Vitórias: {wins}/{hands}  Taxa: {win_rate}  Sala: {room}",
    "confirm_menu_title": "Voltar ao menu", "confirm_menu_text": "O jogo atual será salvo antes de voltar ao menu. Continuar?",
    "game_over": "Fim de jogo", "broke": "Você ficou sem fichas. Fim de jogo.",
    "final_winner": "Todos os jogadores de IA saíram da mesa. Você é o vencedor final.",
    "new_hand": "Nova mão iniciada. Dealer: {dealer}.", "post_blind": "{name} coloca {blind} {amount}.",
    "action_fold": "{name} desiste.", "action_check": "{name} pede mesa.", "action_call": "{name} paga {amount}.",
    "action_raise": "{name} aumenta para {amount}.", "action_all_in_call": "{name} está all-in pagando {amount}.",
    "timeout_check": "O jogador esgotou o tempo e pede mesa.", "timeout_fold": "O jogador esgotou o tempo e desiste.",
    "wins_pot": "{name} ganha o pote {amount}.", "showdown": "Showdown: {names} melhor mão {hand}. Potes paralelos: {awards}.",
    "left_table": "{name} ficou sem fichas e saiu da mesa.", "table_info": "{room}  Blinds {small}/{big}    Pote {pot}    Aposta atual {bet}",
    "timer": "Tempo do jogador: {seconds}", "pot": "Pote", "current_bet": "Aposta atual",
    "chips": "Fichas", "round_bet": "Nesta rodada", "hand_8": "Straight flush", "hand_7": "Quadra",
    "hand_6": "Full house", "hand_5": "Flush", "hand_4": "Sequência", "hand_3": "Trinca",
    "hand_2": "Dois pares", "hand_1": "Par", "hand_0": "Carta alta",
    "raise_range": "Mín {min}  ·  Máx {max}",
})

add_language("ja", {
    "new_game": "新規ゲーム", "leaderboard": "ランキング", "settings": "設定", "exit_game": "終了",
    "back": "戻る", "start": "開始", "apply": "適用", "language": "言語", "resolution": "解像度",
    "ui_scale": "UI拡大率", "fullscreen": "全画面", "ai_count": "AI人数", "ai_difficulty": "AI難易度",
    "room": "ルーム", "room_beginner": "初心者ルーム", "room_normal": "通常ルーム", "room_high": "ハイレート",
    "difficulty_easy": "初級", "difficulty_medium": "中級", "difficulty_hard": "上級", "ai_suffix": "AI",
    "player": "プレイヤー", "main_menu": "メインメニュー", "action_log": "アクションログ", "check_call": "コール / チェック",
    "raise": "レイズ", "fold": "フォールド", "next_hand": "次のハンド", "check": "チェック", "call": "コール",
    "all_in": "オールイン", "thinking": "思考中", "thinking_log": "{name} が考えています...",
    "small_blind": "スモールブラインド", "big_blind": "ビッグブラインド", "flop": "フロップ。", "turn": "ターン。", "river": "リバー。",
    "room_info": "1テーブル最大6人。初心者はブラインド10/20、通常は25/50、ハイレートは100/200です。ディーラー、スモールブラインド、ビッグブラインドは毎ハンド移動します。",
    "no_records": "実記録はまだありません。ゲーム完了までは仮想チャレンジランキングを表示します。",
    "leaderboard_row": "{rank}. {name}  収支: {profit}  チップ: {chips}  勝利: {wins}/{hands}  勝率: {win_rate}  ルーム: {room}",
    "confirm_menu_title": "メニューへ戻る", "confirm_menu_text": "現在のゲームを保存してメニューに戻ります。続行しますか？",
    "game_over": "ゲーム終了", "broke": "チップがなくなりました。ゲーム終了です。",
    "final_winner": "すべてのAIプレイヤーがテーブルを離れました。あなたが最終勝者です。",
    "new_hand": "新しいハンド開始。ディーラー: {dealer}。", "post_blind": "{name} が {blind} {amount} を支払いました。",
    "action_fold": "{name} がフォールド。", "action_check": "{name} がチェック。", "action_call": "{name} が {amount} をコール。",
    "action_raise": "{name} が {amount} にレイズ。", "action_all_in_call": "{name} がオールインで {amount} をコール。",
    "timeout_check": "時間切れで自動チェック。", "timeout_fold": "時間切れで自動フォールド。",
    "wins_pot": "{name} がポット {amount} を獲得。", "showdown": "ショーダウン：{names} の最良役は {hand}。サイドポット：{awards}。",
    "left_table": "{name} はチップ切れでテーブルを離れました。", "table_info": "{room}  ブラインド {small}/{big}    ポット {pot}    現在のベット {bet}",
    "timer": "プレイヤー残り時間: {seconds}", "pot": "ポット", "current_bet": "現在のベット",
    "chips": "チップ", "round_bet": "このラウンド", "hand_8": "ストレートフラッシュ", "hand_7": "フォーカード",
    "hand_6": "フルハウス", "hand_5": "フラッシュ", "hand_4": "ストレート", "hand_3": "スリーカード",
    "hand_2": "ツーペア", "hand_1": "ワンペア", "hand_0": "ハイカード",
    "raise_range": "最小 {min}  ·  最大 {max}",
})

add_language("ko", {
    "new_game": "새 게임", "leaderboard": "순위표", "settings": "설정", "exit_game": "게임 종료",
    "back": "뒤로", "start": "시작", "apply": "적용", "language": "언어", "resolution": "해상도",
    "ui_scale": "UI 배율", "fullscreen": "전체 화면", "ai_count": "AI 수", "ai_difficulty": "AI 난이도",
    "room": "방", "room_beginner": "초보자 방", "room_normal": "일반 방", "room_high": "하이 스테이크",
    "difficulty_easy": "초급", "difficulty_medium": "중급", "difficulty_hard": "고급", "ai_suffix": "AI",
    "player": "플레이어", "main_menu": "메인 메뉴", "action_log": "행동 기록", "check_call": "콜 / 체크",
    "raise": "레이즈", "fold": "폴드", "next_hand": "다음 핸드", "check": "체크", "call": "콜",
    "all_in": "올인", "thinking": "생각 중", "thinking_log": "{name} 생각 중...",
    "small_blind": "스몰 블라인드", "big_blind": "빅 블라인드", "flop": "플롭.", "turn": "턴.", "river": "리버.",
    "room_info": "한 테이블 최대 6명. 초보자 블라인드 10/20, 일반 25/50, 하이 스테이크 100/200. 딜러, 스몰 블라인드, 빅 블라인드는 매 핸드 이동합니다.",
    "no_records": "아직 실제 기록이 없습니다. 게임을 마칠 때까지 가상 도전 순위가 표시됩니다.",
    "leaderboard_row": "{rank}. {name}  수익: {profit}  칩: {chips}  승리: {wins}/{hands}  승률: {win_rate}  방: {room}",
    "confirm_menu_title": "메뉴로 돌아가기", "confirm_menu_text": "현재 게임을 저장하고 메뉴로 돌아갑니다. 계속할까요?",
    "game_over": "게임 종료", "broke": "칩이 모두 떨어졌습니다. 게임 종료.",
    "final_winner": "모든 AI 플레이어가 테이블을 떠났습니다. 당신이 최종 승자입니다.",
    "new_hand": "새 핸드 시작. 딜러: {dealer}.", "post_blind": "{name} {blind} {amount} 지불.",
    "action_fold": "{name} 폴드.", "action_check": "{name} 체크.", "action_call": "{name} {amount} 콜.",
    "action_raise": "{name} {amount}로 레이즈.", "action_all_in_call": "{name} 올인으로 {amount} 콜.",
    "timeout_check": "시간 초과로 자동 체크.", "timeout_fold": "시간 초과로 자동 폴드.",
    "wins_pot": "{name} 팟 {amount} 획득.", "showdown": "쇼다운: {names} 최고 족보 {hand}. 사이드 팟: {awards}.",
    "left_table": "{name} 칩이 없어 테이블을 떠났습니다.", "table_info": "{room}  블라인드 {small}/{big}    팟 {pot}    현재 베팅 {bet}",
    "timer": "플레이어 타이머: {seconds}", "pot": "팟", "current_bet": "현재 베팅",
    "chips": "칩", "round_bet": "이번 라운드", "hand_8": "스트레이트 플러시", "hand_7": "포카드",
    "hand_6": "풀하우스", "hand_5": "플러시", "hand_4": "스트레이트", "hand_3": "트리플",
    "hand_2": "투페어", "hand_1": "원페어", "hand_0": "하이카드",
    "raise_range": "최소 {min}  ·  최대 {max}",
})


ALL_PLAYER_NAMES = frozenset(t["player"] for t in TRANSLATIONS.values())


def default_language():
    try:
        code = (locale.getlocale()[0] or "en").split("_")[0].lower()
    except Exception:
        code = "en"
    return code if code in LANGUAGES else "en"


def localized_ai_name(name, lang):
    return f"{name} ({TRANSLATIONS[lang]['ai_suffix']})"


def strip_ai_suffix(name):
    if "(" in name:
        return name.split("(", 1)[0].strip()
    return name


@dataclass(frozen=True)
class Card:
    rank: int
    suit: str

    def __str__(self):
        return f"{RANK_LABELS[self.rank]}{SUIT_SYMBOLS[self.suit]}"

    @property
    def is_red(self):
        return self.suit in {"H", "D"}


@dataclass
class Player:
    name: str
    chips: int
    is_human: bool = False
    difficulty: str = "medium"
    avatar_color: str = "#64748b"
    style_name: str = "balanced"
    looseness: float = 0.0
    aggression: float = 1.0
    bluff: float = 0.04
    calling_station: float = 0.0
    all_in_bias: float = 0.02
    cards: List[Card] = field(default_factory=list)
    folded: bool = False
    all_in: bool = False
    has_acted: bool = False
    current_bet: int = 0
    committed: int = 0
    hands_won: int = 0

    @property
    def in_hand(self):
        return not self.folded and (self.chips > 0 or self.committed > 0)

    def reset_for_hand(self):
        self.cards = []
        self.folded = False
        self.all_in = False
        self.has_acted = False
        self.current_bet = 0
        self.committed = 0


def make_deck(excluded=None):
    excluded = set(excluded or [])
    deck = [Card(rank, suit) for suit in SUITS for rank in RANKS if Card(rank, suit) not in excluded]
    random.shuffle(deck)
    return deck


def straight_high(ranks):
    unique = sorted(set(ranks), reverse=True)
    if 14 in unique:
        unique.append(1)
    for index in range(len(unique) - 4):
        run = unique[index : index + 5]
        if run[0] - run[4] == 4:
            return run[0]
    return None


def evaluate_five(cards):
    ranks = sorted((card.rank for card in cards), reverse=True)
    suits = [card.suit for card in cards]
    counts = {rank: ranks.count(rank) for rank in set(ranks)}
    groups = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
    flush = len(set(suits)) == 1
    straight = straight_high(ranks)

    if flush and straight:
        return (8, [straight])
    if groups[0][1] == 4:
        quad = groups[0][0]
        kicker = max(rank for rank in ranks if rank != quad)
        return (7, [quad, kicker])
    if groups[0][1] == 3 and groups[1][1] == 2:
        return (6, [groups[0][0], groups[1][0]])
    if flush:
        return (5, ranks)
    if straight:
        return (4, [straight])
    if groups[0][1] == 3:
        trip = groups[0][0]
        kickers = sorted((rank for rank in ranks if rank != trip), reverse=True)
        return (3, [trip] + kickers)
    if groups[0][1] == 2 and groups[1][1] == 2:
        pairs = sorted([groups[0][0], groups[1][0]], reverse=True)
        kicker = max(rank for rank in ranks if rank not in pairs)
        return (2, pairs + [kicker])
    if groups[0][1] == 2:
        pair = groups[0][0]
        kickers = sorted((rank for rank in ranks if rank != pair), reverse=True)
        return (1, [pair] + kickers)
    return (0, ranks)


def evaluate_best(cards):
    return max(evaluate_five(combo) for combo in itertools.combinations(cards, 5))


def best_five_cards(cards):
    return max(itertools.combinations(cards, 5), key=evaluate_five)


def describe_score(score, lang="zh"):
    category, values = score
    labels = " ".join(RANK_LABELS.get(value, str(value)) for value in values)
    return f"{TRANSLATIONS[lang].get(f'hand_{category}', TRANSLATIONS['en'][f'hand_{category}'])} {labels}".strip()


def preflop_strength(cards):
    a, b = sorted(cards, key=lambda card: card.rank, reverse=True)
    score = (a.rank + b.rank) / 30
    if a.rank == b.rank:
        score += 0.28 + a.rank / 60
    if a.suit == b.suit:
        score += 0.08
    if abs(a.rank - b.rank) <= 2:
        score += 0.06
    if a.rank >= 12:
        score += 0.08
    return min(score, 0.98)


def estimate_win_rate(player, community, opponents, samples):
    known = list(player.cards) + list(community)
    wins = 0
    ties = 0
    needed_board = 5 - len(community)
    opponent_count = max(1, opponents)

    for _ in range(samples):
        deck = make_deck(known)
        board = list(community) + [deck.pop() for _ in range(needed_board)]
        player_score = evaluate_best(player.cards + board)
        best_enemy = None
        tie_count = 0
        for _ in range(opponent_count):
            enemy_cards = [deck.pop(), deck.pop()]
            enemy_score = evaluate_best(enemy_cards + board)
            if best_enemy is None or enemy_score > best_enemy:
                best_enemy = enemy_score
                tie_count = 1
            elif enemy_score == best_enemy:
                tie_count += 1
        if player_score > best_enemy:
            wins += 1
        elif player_score == best_enemy:
            ties += 1 / (tie_count + 1)
    return (wins + ties) / samples


def random_ai_profile():
    # Hidden style knobs keep opponents from feeling like one shared strategy.
    profiles = [
        ("紧凶", -0.08, 1.18, 0.04, -0.04, 0.018),
        ("松凶", 0.08, 1.28, 0.09, 0.02, 0.03),
        ("紧弱", -0.10, 0.78, 0.015, -0.08, 0.008),
        ("松弱", 0.10, 0.82, 0.025, 0.08, 0.012),
        ("均衡", 0.0, 1.0, 0.04, 0.0, 0.015),
        ("跟注型", 0.06, 0.72, 0.015, 0.14, 0.006),
    ]
    style_name, looseness, aggression, bluff, calling_station, all_in_bias = random.choice(profiles)
    return {
        "style_name": style_name,
        "looseness": looseness + random.uniform(-0.025, 0.025),
        "aggression": aggression + random.uniform(-0.08, 0.08),
        "bluff": max(0.0, bluff + random.uniform(-0.012, 0.018)),
        "calling_station": calling_station + random.uniform(-0.025, 0.025),
        "all_in_bias": max(0.002, all_in_bias + random.uniform(-0.004, 0.006)),
    }


class TexasHoldemApp:
    def __init__(self, root):
        self.root = root
        self.lang = default_language()
        self.root.title(TRANSLATIONS[self.lang]["app_title"])
        self.root.configure(bg="#123c2c")

        self.resolution = tk.StringVar(value="1366x768")
        self.ui_scale = tk.StringVar(value="100%")
        self.fullscreen = tk.BooleanVar(value=False)
        self.language_label = tk.StringVar(value=LANGUAGES[self.lang])
        self.setup_ai_count = tk.IntVar(value=3)
        self.setup_difficulty = tk.StringVar()
        self.setup_room = tk.StringVar()
        self.sync_localized_options()

        self.players: List[Player] = []
        self.deck: List[Card] = []
        self.community: List[Card] = []
        self.pot = 0
        self.current_bet = 0
        self.min_raise = 0
        self.betting_reopened = True
        self.dealer_index = 0
        self.turn_index = 0
        self.stage = "menu"
        self.hand_running = False
        self.waiting_for_human = False
        self.countdown_seconds = PLAYER_SECONDS
        self.countdown_job = None
        self.ai_action_job = None
        self.bubble_fade_jobs: dict = {}
        self.pending_ai = None
        self.action_log: List[str] = []
        self.action_bubbles = {}
        self.highlight_cards = set()
        self.session_hands = 0
        self._game_room_id = "normal"
        self.leaderboard = self.load_leaderboard()
        self.controls = {}

        self.apply_window_settings()
        self.show_main_menu()

    def clear(self):
        self.cancel_timers()
        for widget in self.root.winfo_children():
            widget.destroy()

    def cancel_timers(self):
        for job in (self.countdown_job, self.ai_action_job, *self.bubble_fade_jobs.values()):
            if job:
                try:
                    self.root.after_cancel(job)
                except tk.TclError:
                    pass
        self.countdown_job = None
        self.ai_action_job = None
        self.bubble_fade_jobs = {}
        self.action_bubbles = {}
        self.pending_ai = None

    def tr(self, key, **kwargs):
        text = TRANSLATIONS.get(self.lang, TRANSLATIONS["en"]).get(key, TRANSLATIONS["en"].get(key, key))
        return text.format(**kwargs) if kwargs else text

    def room_label(self, room_id):
        return self.tr(f"room_{room_id}")

    def difficulty_label(self, difficulty_id):
        return self.tr(f"difficulty_{difficulty_id}")

    def sync_localized_options(self):
        current_room = getattr(self, "selected_room_id", lambda: "normal")()
        current_difficulty = getattr(self, "selected_difficulty_id", lambda: "medium")()
        self.setup_room.set(self.room_label(current_room))
        self.setup_difficulty.set(self.difficulty_label(current_difficulty))
        self.language_label.set(LANGUAGES[self.lang])

    def selected_room_id(self):
        labels = {self.room_label(room_id): room_id for room_id in ROOMS}
        return labels.get(self.setup_room.get(), "normal")

    def selected_difficulty_id(self):
        labels = {self.difficulty_label(difficulty_id): difficulty_id for difficulty_id in DIFFICULTIES}
        return labels.get(self.setup_difficulty.get(), "medium")

    def selected_language_id(self):
        labels = {label: code for code, label in LANGUAGES.items()}
        return labels.get(self.language_label.get(), self.lang)

    def display_record_name(self, name):
        return self.tr("player") if name in ALL_PLAYER_NAMES else name

    def apply_language_choice(self):
        old_room = self.selected_room_id()
        old_difficulty = self.selected_difficulty_id()
        self.lang = self.selected_language_id()
        self.root.title(self.tr("app_title"))
        self.setup_room.set(self.room_label(old_room))
        self.setup_difficulty.set(self.difficulty_label(old_difficulty))

    def apply_window_settings(self):
        self.apply_language_choice()
        self.root.attributes("-fullscreen", self.fullscreen.get())
        if not self.fullscreen.get():
            self.apply_window_geometry()
        try:
            self.root.tk.call("tk", "scaling", UI_SCALES[self.ui_scale.get()])
        except tk.TclError:
            pass
        if self.stage == "game" and hasattr(self, "table_canvas"):
            self.build_game_screen()
            self.refresh(show_all=not self.hand_running)
        elif self.stage == "settings":
            self.show_settings()

    def apply_window_geometry(self):
        width_text, height_text = self.resolution.get().split("x", 1)
        requested_width = int(width_text)
        requested_height = int(height_text)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Tk uses OS logical pixels. On a 4K display with 150% scaling, the
        # usable logical desktop is often around 2560x1440, so cap large
        # presets to keep windowed mode visibly windowed.
        max_width = int(screen_width * 0.92)
        max_height = int(screen_height * 0.88)
        width = min(requested_width, max_width)
        height = min(requested_height, max_height)
        x = max(0, (screen_width - width) // 2)
        y = max(0, (screen_height - height) // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def scale_value(self, value):
        return max(1, int(round(value * UI_SCALES.get(self.ui_scale.get(), 1.0))))

    def font(self, size, bold=False):
        return ("Microsoft YaHei UI", self.scale_value(size), "bold" if bold else "normal")

    def ellipsize(self, text, max_chars):
        return text if len(text) <= max_chars else text[: max(1, max_chars - 1)] + "…"

    def text_units(self, text, minimum=10, maximum=22, padding=2):
        # Tk button/menu widths are character based. CJK glyphs are wider than
        # Latin glyphs visually, so count them a little heavier.
        units = 0
        for char in text:
            units += 1.6 if ord(char) > 127 else 1
        return max(minimum, min(maximum, int(units + padding)))

    def button(self, parent, text, command, width=18):
        return tk.Button(
            parent,
            text=text,
            width=max(width, self.text_units(text, minimum=width, maximum=24)),
            command=command,
            font=self.font(12),
            bg="#f3f4f6",
            fg="#111827",
            activebackground="#d1d5db",
            relief="raised",
            bd=2,
        )

    def label(self, parent, text, size=13, bold=False, fg="#f8fafc", bg="#123c2c"):
        return tk.Label(
            parent,
            text=text,
            font=self.font(size, bold),
            fg=fg,
            bg=bg,
            wraplength=self.scale_value(960),
            justify="left",
        )

    def show_main_menu(self):
        self.stage = "menu"
        self.clear()
        wrapper = tk.Frame(self.root, bg="#123c2c")
        wrapper.pack(fill="both", expand=True)
        center = tk.Frame(wrapper, bg="#123c2c")
        center.place(relx=0.5, rely=0.5, anchor="center")

        self.label(center, self.tr("app_title"), 34, True).pack(pady=(0, 26))
        self.button(center, self.tr("new_game"), self.show_new_game).pack(pady=7)
        self.button(center, self.tr("leaderboard"), self.show_leaderboard).pack(pady=7)
        self.button(center, self.tr("settings"), self.show_settings).pack(pady=7)
        self.button(center, self.tr("exit_game"), self.root.destroy).pack(pady=7)

    def show_new_game(self):
        self.stage = "new_game"
        self.clear()
        panel = tk.Frame(self.root, bg="#123c2c")
        panel.pack(fill="both", expand=True, padx=48, pady=42)
        center = tk.Frame(panel, bg="#123c2c")
        center.place(relx=0.5, rely=0.5, anchor="center")
        self.label(center, self.tr("new_game"), 28, True).pack(pady=(0, 18))

        form = tk.Frame(center, bg="#123c2c")
        form.pack(pady=10)

        self.label(form, self.tr("ai_count"), 13, True).grid(row=0, column=0, sticky="e", pady=10, padx=(0, 20))
        tk.Spinbox(
            form,
            from_=1,
            to=5,
            textvariable=self.setup_ai_count,
            width=8,
            font=self.font(12),
            state="readonly",
        ).grid(row=0, column=1)

        self.label(form, self.tr("ai_difficulty"), 13, True).grid(row=1, column=0, sticky="e", pady=10, padx=(0, 20))
        difficulty_menu = tk.OptionMenu(form, self.setup_difficulty, *(self.difficulty_label(item) for item in DIFFICULTIES))
        difficulty_menu.config(font=self.font(12), width=max(self.text_units(self.difficulty_label(item), 10, 18) for item in DIFFICULTIES))
        difficulty_menu.grid(row=1, column=1)

        self.label(form, self.tr("room"), 13, True).grid(row=2, column=0, sticky="e", pady=10, padx=(0, 20))
        room_menu = tk.OptionMenu(form, self.setup_room, *(self.room_label(item) for item in ROOMS))
        room_menu.config(font=self.font(12), width=max(self.text_units(self.room_label(item), 10, 20) for item in ROOMS))
        room_menu.grid(row=2, column=1)

        info = self.tr("room_info")
        info_label = self.label(center, info, 12, fg="#dbeafe")
        info_label.config(justify="center", wraplength=self.scale_value(620))
        info_label.pack(pady=18)

        controls = tk.Frame(center, bg="#123c2c")
        controls.pack(pady=16)
        self.button(controls, self.tr("start"), self.start_game, 12).pack(side="left", padx=(0, 12))
        self.button(controls, self.tr("back"), self.show_main_menu, 12).pack(side="left")

    def show_settings(self):
        self.stage = "settings"
        self.clear()
        panel = tk.Frame(self.root, bg="#123c2c")
        panel.pack(fill="both", expand=True, padx=48, pady=42)
        center = tk.Frame(panel, bg="#123c2c")
        center.place(relx=0.5, rely=0.5, anchor="center")
        self.label(center, self.tr("settings"), 28, True).pack(pady=(0, 22))

        form = tk.Frame(center, bg="#123c2c")
        form.pack(pady=10)
        self.label(form, self.tr("language"), 13, True).grid(row=0, column=0, sticky="e", pady=12, padx=(0, 22))
        language_menu = tk.OptionMenu(form, self.language_label, *LANGUAGES.values())
        language_menu.config(font=self.font(12), width=max(self.text_units(item, 12, 20) for item in LANGUAGES.values()))
        language_menu.grid(row=0, column=1)

        self.label(form, self.tr("resolution"), 13, True).grid(row=1, column=0, sticky="e", pady=12, padx=(0, 22))
        resolution_menu = tk.OptionMenu(form, self.resolution, *RESOLUTIONS)
        resolution_menu.config(font=self.font(12), width=14)
        resolution_menu.grid(row=1, column=1)

        self.label(form, self.tr("ui_scale"), 13, True).grid(row=2, column=0, sticky="e", pady=12, padx=(0, 22))
        scale_menu = tk.OptionMenu(form, self.ui_scale, *UI_SCALES.keys())
        scale_menu.config(font=self.font(12), width=14)
        scale_menu.grid(row=2, column=1)

        tk.Checkbutton(
            form,
            text=self.tr("fullscreen"),
            variable=self.fullscreen,
            font=self.font(12),
            bg="#123c2c",
            fg="white",
            selectcolor="#123c2c",
            activebackground="#123c2c",
            activeforeground="white",
        ).grid(row=3, column=1, pady=12)

        controls = tk.Frame(center, bg="#123c2c")
        controls.pack(pady=20)
        self.button(controls, self.tr("apply"), self.apply_window_settings, 12).pack(side="left", padx=(0, 12))
        self.button(controls, self.tr("back"), self.show_main_menu, 12).pack(side="left")

    def show_leaderboard(self):
        self.stage = "leaderboard"
        self.clear()
        panel = tk.Frame(self.root, bg="#123c2c")
        panel.pack(fill="both", expand=True, padx=48, pady=42)
        center = tk.Frame(panel, bg="#123c2c")
        center.place(relx=0.5, rely=0.5, anchor="center")
        self.label(center, self.tr("leaderboard"), 28, True).pack(pady=(0, 18))
        source = self.virtual_leaderboard() if self.leaderboard and all(item.get("virtual") for item in self.leaderboard) else self.leaderboard
        entries = sorted(source, key=self.leaderboard_sort_key, reverse=True)[:10]
        if not entries:
            empty_label = self.label(center, self.tr("no_records"), 13)
            empty_label.config(justify="center", wraplength=self.scale_value(620))
            empty_label.pack()
        else:
            if all(item.get("virtual") for item in entries):
                empty_label = self.label(center, self.tr("no_records"), 12, fg="#cbd5e1")
                empty_label.config(justify="center", wraplength=self.scale_value(760))
                empty_label.pack(pady=(0, 12))
            for index, item in enumerate(entries, 1):
                room_id = self.normalize_room_id(item.get("room", "normal"))
                room_name = self.room_label(room_id)
                text = self.tr(
                    "leaderboard_row",
                    rank=index,
                    name=self.display_record_name(item["name"]),
                    profit=self.format_profit(item.get("profit", item["chips"] - ROOMS[room_id]["buy_in"])),
                    chips=self.format_number(item["chips"]),
                    wins=item["wins"],
                    hands=item.get("hands", max(1, item["wins"])),
                    win_rate=self.format_percent(item.get("win_rate", 0)),
                    room=room_name,
                )
                row = self.label(center, text, 14, fg="#e5e7eb")
                row.config(justify="center", wraplength=self.scale_value(760))
                row.pack(pady=5)
        self.button(center, self.tr("back"), self.show_main_menu, 12).pack(pady=24)

    def start_game(self):
        room_id = self.selected_room_id()
        difficulty_id = self.selected_difficulty_id()
        room = ROOMS[room_id]
        # Lock the room for this run; menu labels can be relocalized later.
        self._game_room_id = room_id
        ai_count = max(1, min(5, int(self.setup_ai_count.get())))
        names = random.sample(AI_NAMES.get(self.lang, AI_NAMES["en"]), ai_count)
        colors = random.sample(AVATAR_COLORS, ai_count + 1)
        self.players = [Player(self.tr("player"), room["buy_in"], is_human=True, avatar_color=colors[0])]
        self.session_hands = 0
        for index, name in enumerate(names):
            profile = random_ai_profile()
            self.players.append(
                Player(
                    localized_ai_name(name, self.lang),
                    room["buy_in"],
                    difficulty=difficulty_id,
                    avatar_color=colors[index + 1],
                    **profile,
                )
            )
        self.dealer_index = 0
        self.action_log = []
        self.action_bubbles = {}
        self.highlight_cards = set()
        self.build_game_screen()
        self.start_hand()

    def build_game_screen(self):
        self.stage = "game"
        self.clear()
        self.root.configure(bg="#0b1f1a")
        top = tk.Frame(self.root, bg="#0b1f1a")
        top.pack(fill="x", padx=18, pady=(12, 6))
        self.info_label = self.label(top, "", 12, True, bg="#0b1f1a")
        self.info_label.config(wraplength=self.scale_value(780))
        self.info_label.pack(side="left", fill="x", expand=True)
        self.button(top, self.tr("main_menu"), self.confirm_menu, 10).pack(side="right", padx=(10, 0))

        main = tk.Frame(self.root, bg="#0b1f1a")
        main.pack(fill="both", expand=True, padx=18, pady=(0, 16))

        self.table_canvas = tk.Canvas(main, bg="#0b1f1a", highlightthickness=0)
        self.table_canvas.pack(side="left", fill="both", expand=True)
        self.table_canvas.bind("<Configure>", lambda _event: self.render_table())

        side = tk.Frame(
            main,
            bg="#102820",
            width=self.scale_value(290 if self.lang in {"de", "fr", "es", "pt"} else 260),
            padx=self.scale_value(12),
            pady=self.scale_value(12),
        )
        side.pack(side="right", fill="y", padx=(14, 0))
        side.pack_propagate(False)

        self.sidebar_stats = tk.Frame(side, bg="#102820")
        self.sidebar_stats.pack(fill="x", pady=(0, 12))
        self.room_stat = self.label(self.sidebar_stats, "", 11, True, bg="#102820", fg="#fef3c7")
        self.pot_stat = self.label(self.sidebar_stats, "", 13, True, bg="#102820", fg="#fde68a")
        self.bet_stat = self.label(self.sidebar_stats, "", 11, True, bg="#102820", fg="#e0f2fe")
        self.timer_stat = self.label(self.sidebar_stats, "", 13, True, bg="#102820", fg="#fca5a5")
        for label in (self.room_stat, self.pot_stat, self.bet_stat, self.timer_stat):
            label.config(wraplength=self.scale_value(250 if self.lang in {"de", "fr", "es", "pt"} else 230))
            label.pack(anchor="w", pady=2)

        self.label(side, self.tr("action_log"), 13, True, bg="#102820").pack(anchor="w")
        log_frame = tk.Frame(side, bg="#102820")
        log_frame.pack(fill="both", expand=True, pady=(8, 12))
        self.log_text = tk.Text(
            log_frame,
            height=12,
            wrap="word",
            font=self.font(10),
            bg="#0b1f1a",
            fg="#e5e7eb",
            insertbackground="#e5e7eb",
            relief="flat",
            padx=8,
            pady=8,
            state="disabled",
        )
        self.log_scrollbar = tk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=self.log_scrollbar.set)
        self.log_text.pack(side="left", fill="both", expand=True)
        self.log_scrollbar.pack(side="right", fill="y")
        self.log_text.bind("<MouseWheel>", self.on_log_mousewheel)
        self.log_text.bind("<Button-4>", self.on_log_mousewheel)
        self.log_text.bind("<Button-5>", self.on_log_mousewheel)

        actions = tk.Frame(side, bg="#102820")
        actions.pack(fill="x")
        self.controls["check_call"] = self.button(actions, self.tr("check_call"), self.human_check_call, 12)
        self.controls["raise"] = self.button(actions, self.tr("raise"), self.human_raise, 12)
        self.controls["fold"] = self.button(actions, self.tr("fold"), self.human_fold, 12)
        self.controls["next"] = self.button(actions, self.tr("next_hand"), self.start_hand, 12)
        for button in self.controls.values():
            button.config(wraplength=self.scale_value(210), justify="center")
            button.pack(fill="x", pady=5)

    def confirm_menu(self):
        if messagebox.askyesno(self.tr("confirm_menu_title"), self.tr("confirm_menu_text")):
            self.save_current_record()
            self.show_main_menu()

    def start_hand(self):
        self.cancel_timers()
        human = self.human_player()
        if human.chips <= 0:
            self.end_game(self.tr("broke"))
            return

        self.players = [player for player in self.players if player.is_human or player.chips > 0]
        if len(self.players) < 2:
            self.end_game(self.tr("final_winner"))
            return

        for player in self.players:
            player.reset_for_hand()
        self.highlight_cards = set()
        self.community = []
        self.deck = make_deck()
        self.pot = 0
        self.current_bet = 0
        self.min_raise = self.big_blind()
        self.betting_reopened = True
        self.hand_running = True
        self.waiting_for_human = False
        self.session_hands += 1

        self.dealer_index %= len(self.players)
        if len(self.players) == 2:
            sb_index = self.dealer_index
            bb_index = self.next_seat(self.dealer_index)
        else:
            sb_index = self.next_seat(self.dealer_index)
            bb_index = self.next_seat(sb_index)
        self.post_blind(self.players[sb_index], self.small_blind(), self.tr("small_blind"))
        self.post_blind(self.players[bb_index], self.big_blind(), self.tr("big_blind"))
        self.current_bet = max(player.current_bet for player in self.players)

        for _ in range(2):
            for player in self.players:
                player.cards.append(self.deck.pop())
        for player in self.players:
            player.has_acted = False

        self.turn_index = self.next_seat(bb_index)
        self.log(self.tr("new_hand", dealer=self.players[self.dealer_index].name))
        self.refresh()
        self.advance_actions()

    def small_blind(self):
        return ROOMS[self.selected_room_id()]["small_blind"]

    def big_blind(self):
        return ROOMS[self.selected_room_id()]["big_blind"]

    def post_blind(self, player, amount, name):
        paid = min(amount, player.chips)
        player.chips -= paid
        player.current_bet += paid
        player.committed += paid
        player.all_in = player.chips == 0
        self.pot += paid
        self.log(self.tr("post_blind", name=player.name, blind=name, amount=paid))

    def next_seat(self, index):
        return (index + 1) % len(self.players)

    def active_players(self):
        return [player for player in self.players if player.in_hand]

    def betting_players(self):
        return [player for player in self.players if player.in_hand and not player.all_in]

    def human_player(self):
        return next(player for player in self.players if player.is_human)

    def log(self, text):
        self.action_log.append(text)
        self.action_log = self.action_log[-80:]
        self.update_log_widget()

    def update_log_widget(self):
        if not hasattr(self, "log_text"):
            return
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.insert("end", "\n".join(self.action_log))
        self.log_text.configure(state="disabled")
        self.log_text.see("end")

    def on_log_mousewheel(self, event):
        if not hasattr(self, "log_text"):
            return "break"
        if getattr(event, "num", None) == 4:
            delta = -3
        elif getattr(event, "num", None) == 5:
            delta = 3
        else:
            delta = int(-1 * (event.delta / 120))
        self.log_text.yview_scroll(delta, "units")
        return "break"

    def advance_actions(self):
        if not self.hand_running or self.stage != "game":
            return
        if self.only_one_left():
            self.finish_by_folds()
            return
        if self.betting_round_done():
            self.next_stage()
            return

        player = self.players[self.turn_index]
        if not player.in_hand or player.all_in:
            self.turn_index = self.next_seat(self.turn_index)
            self.advance_actions()
            return

        if player.is_human:
            self.waiting_for_human = True
            self.start_countdown()
            self.refresh()
            return

        self.pending_ai = player
        self.log(self.tr("thinking_log", name=player.name))
        self.refresh()
        delay = random.randint(1400, 3600)
        self.ai_action_job = self.root.after(delay, lambda player=player: self.perform_ai_action(player))

    def perform_ai_action(self, player):
        self.ai_action_job = None
        if not self.hand_running or self.waiting_for_human or player is not self.pending_ai:
            return
        self.pending_ai = None
        if player not in self.players or not player.in_hand or player.all_in:
            self.advance_actions()
            return
        action, amount = self.choose_ai_action(player)
        self.apply_action(player, action, amount)
        self.turn_index = self.next_seat(self.turn_index)
        self.refresh()
        self.root.after(random.randint(600, 1100), self.advance_actions)

    def betting_round_done(self):
        contenders = self.betting_players()
        if not contenders:
            return True
        return all(player.has_acted and player.current_bet == self.current_bet for player in contenders)

    def only_one_left(self):
        return len([player for player in self.players if player.in_hand]) == 1

    def next_stage(self):
        for player in self.players:
            player.current_bet = 0
            player.has_acted = False
        self.current_bet = 0
        self.min_raise = self.big_blind()
        self.betting_reopened = True

        if len(self.community) == 0:
            self.deck.pop()
            self.community.extend([self.deck.pop(), self.deck.pop(), self.deck.pop()])
            self.log(self.tr("flop"))
        elif len(self.community) == 3:
            self.deck.pop()
            self.community.append(self.deck.pop())
            self.log(self.tr("turn"))
        elif len(self.community) == 4:
            self.deck.pop()
            self.community.append(self.deck.pop())
            self.log(self.tr("river"))
        else:
            self.showdown()
            return

        self.turn_index = self.next_seat(self.dealer_index)
        self.refresh()
        self.root.after(350, self.advance_actions)

    def choose_ai_action(self, player):
        to_call = self.current_bet - player.current_bet
        opponents = len([p for p in self.players if p.in_hand and p is not player])
        room_big_blind = self.big_blind()

        if len(self.community) == 0:
            strength = preflop_strength(player.cards)
        elif player.difficulty == "easy":
            made = evaluate_best(player.cards + self.community)
            strength = 0.22 + made[0] * 0.09 + random.uniform(-0.08, 0.08)
        else:
            samples = 45 if player.difficulty == "medium" else 120
            strength = estimate_win_rate(player, self.community, opponents, samples)

        if player.difficulty == "easy":
            strength += random.uniform(-0.18, 0.14)
            difficulty_aggression = 0.75
        elif player.difficulty == "medium":
            strength += random.uniform(-0.07, 0.06)
            difficulty_aggression = 1.0
        else:
            difficulty_aggression = 1.12

        style_aggression = max(0.45, player.aggression * difficulty_aggression)
        adjusted_strength = max(0.02, min(0.99, strength + player.looseness))

        pot_odds = to_call / max(self.pot + to_call, 1)
        stack_after_call = player.chips - to_call
        can_raise = stack_after_call > room_big_blind * 2 and (not player.has_acted or self.betting_reopened)
        strong = adjusted_strength > max(0.64, pot_odds + 0.22)
        medium = adjusted_strength > max(0.39, pot_odds - 0.02 - player.calling_station)
        monster = adjusted_strength > 0.88
        bluffing = random.random() < player.bluff and to_call <= max(room_big_blind * 3, self.pot * 0.25)

        if to_call == 0:
            raise_chance = max(0.0, (adjusted_strength - 0.60) * style_aggression)
            if can_raise and (strong or bluffing or random.random() < min(0.34, raise_chance)):
                return "raise", self.sized_raise(player, adjusted_strength, style_aggression, monster)
            return "check", 0

        if not medium and not bluffing and random.random() > 0.06 + max(0, player.calling_station):
            return "fold", 0
        raise_probability = min(0.42, max(0.03, (adjusted_strength - 0.58) * style_aggression))
        if can_raise and (strong or bluffing) and random.random() < raise_probability:
            return "raise", self.sized_raise(player, adjusted_strength, style_aggression, monster)
        return "call", to_call

    def sized_raise(self, player, strength, aggression, monster=False):
        to_call = self.current_bet - player.current_bet
        base = self.big_blind()
        pot_fraction = random.uniform(0.35, 0.70)
        if strength > 0.78:
            pot_fraction = random.uniform(0.60, 0.95)
        target_raise = max(base, int(self.pot * pot_fraction * aggression))
        total = to_call + target_raise
        stack_limit = int(player.chips * (0.22 + min(0.30, strength * 0.22) + max(0, aggression - 1.0) * 0.10))
        stack_limit = max(to_call + base, stack_limit)
        should_all_in = (
            monster
            and player.chips <= max(base * 8, self.pot * 1.25)
            and random.random() < player.all_in_bias
        )
        if should_all_in:
            return player.chips
        if player.chips <= to_call + base:
            return to_call
        capped_total = min(total, stack_limit, player.chips - 1)
        return max(to_call + base, capped_total)

    def apply_action(self, player, action, amount=0):
        to_call = max(0, self.current_bet - player.current_bet)
        if action == "fold":
            player.folded = True
            player.has_acted = True
            self.log(self.tr("action_fold", name=player.name))
            self.show_action_bubble(player, self.tr("fold"))
            return
        if action == "check":
            player.has_acted = True
            self.log(self.tr("action_check", name=player.name))
            self.show_action_bubble(player, self.tr("check"))
            return
        if action == "call":
            paid = min(to_call, player.chips)
            self.take_chips(player, paid)
            player.has_acted = True
            if player.all_in:
                self.log(self.tr("action_all_in_call", name=player.name, amount=paid))
            else:
                self.log(self.tr("action_call", name=player.name, amount=paid))
            bubble = self.tr("all_in") if player.all_in else f"{self.tr('call')} {paid}"
            self.show_action_bubble(player, bubble)
            return
        if action == "raise":
            paid = min(max(amount, to_call), player.chips)
            previous_bet = player.current_bet
            self.take_chips(player, paid)
            if player.current_bet > self.current_bet:
                raise_size = player.current_bet - self.current_bet
                # No-limit rule: only a full raise reopens action for players who already acted.
                is_full_raise = raise_size >= self.min_raise
                self.current_bet = player.current_bet
                if is_full_raise:
                    self.min_raise = max(self.big_blind(), raise_size)
                    self.betting_reopened = True
                    for other in self.players:
                        if other.in_hand and not other.all_in:
                            other.has_acted = False
                else:
                    # Short all-in: does not reopen betting for players who already acted.
                    self.betting_reopened = False
                player.has_acted = True
                if is_full_raise:
                    self.log(self.tr("action_raise", name=player.name, amount=player.current_bet))
                    self.show_action_bubble(player, f"{self.tr('raise')} {player.current_bet}")
                else:
                    self.log(self.tr("action_all_in_call", name=player.name, amount=paid))
                    self.show_action_bubble(player, self.tr("all_in"))
            else:
                player.has_acted = True
                self.log(self.tr("action_all_in_call", name=player.name, amount=player.current_bet - previous_bet))
                self.show_action_bubble(player, self.tr("all_in"))

    def take_chips(self, player, amount):
        paid = min(amount, player.chips)
        player.chips -= paid
        player.current_bet += paid
        player.committed += paid
        player.all_in = player.chips == 0
        self.pot += paid

    def show_action_bubble(self, player, text):
        pid = id(player)
        old_job = self.bubble_fade_jobs.pop(pid, None)
        if old_job:
            try:
                self.root.after_cancel(old_job)
            except tk.TclError:
                pass
        self.action_bubbles[pid] = {"text": text, "life": len(BUBBLE_SHADES) - 1}
        self.render_table()
        self.bubble_fade_jobs[pid] = self.root.after(450, lambda player_id=pid: self.fade_action_bubble(player_id))

    def fade_action_bubble(self, player_id):
        self.bubble_fade_jobs.pop(player_id, None)
        bubble = self.action_bubbles.get(player_id)
        if not bubble:
            return
        bubble["life"] -= 1
        if bubble["life"] < 0:
            self.action_bubbles.pop(player_id, None)
        self.render_table()
        if player_id in self.action_bubbles:
            self.bubble_fade_jobs[player_id] = self.root.after(450, lambda: self.fade_action_bubble(player_id))

    def start_countdown(self):
        self.stop_countdown()
        self.countdown_seconds = PLAYER_SECONDS
        self.tick_countdown()

    def stop_countdown(self):
        if self.countdown_job:
            try:
                self.root.after_cancel(self.countdown_job)
            except tk.TclError:
                pass
        self.countdown_job = None

    def tick_countdown(self):
        if not self.waiting_for_human or not self.hand_running:
            self.stop_countdown()
            return
        self.refresh()
        if self.countdown_seconds <= 0:
            self.countdown_job = None
            self.handle_timeout()
            return
        self.countdown_seconds -= 1
        self.countdown_job = self.root.after(1000, self.tick_countdown)

    def handle_timeout(self):
        if not self.waiting_for_human or not self.hand_running:
            return
        human = self.human_player()
        to_call = self.current_bet - human.current_bet
        if to_call <= 0:
            self.log(self.tr("timeout_check"))
            self.apply_action(human, "check")
        else:
            self.log(self.tr("timeout_fold"))
            self.apply_action(human, "fold")
        self.after_human_action()
        dlg = getattr(self, "_raise_dialog", None)
        if dlg:
            try:
                dlg.destroy()
            except tk.TclError:
                pass
            self._raise_dialog = None

    def human_check_call(self):
        if not self.waiting_for_human:
            return
        self.stop_countdown()
        human = self.human_player()
        to_call = self.current_bet - human.current_bet
        self.apply_action(human, "check" if to_call == 0 else "call", to_call)
        self.after_human_action()

    def human_raise(self):
        if not self.waiting_for_human:
            return
        human = self.human_player()
        if human.has_acted and not self.betting_reopened:
            return
        to_call = self.current_bet - human.current_bet
        min_amount = min(human.chips, to_call + max(self.min_raise, self.big_blind()))
        max_amount = human.chips
        if min_amount >= max_amount:
            self.stop_countdown()
            self.apply_action(human, "raise", max_amount)
            self.after_human_action()
            return
        self._show_raise_dialog(human, to_call, min_amount, max_amount)

    def _show_raise_dialog(self, human, to_call, min_amount, max_amount):
        dialog = tk.Toplevel(self.root)
        dialog.title(self.tr("raise"))
        dialog.configure(bg="#1e293b")
        dialog.resizable(False, False)
        dialog.grab_set()

        dw = self.scale_value(380)
        dh = self.scale_value(296)
        px = self.root.winfo_x() + (self.root.winfo_width() - dw) // 2
        py = self.root.winfo_y() + (self.root.winfo_height() - dh) // 2
        dialog.geometry(f"{dw}x{dh}+{max(0, px)}+{max(0, py)}")

        amount_var = tk.IntVar(value=min_amount)
        confirmed = [False]

        tk.Label(dialog, text=self.tr("raise"), font=self.font(14, True), bg="#1e293b", fg="#f8fafc").pack(pady=(12, 2))
        tk.Label(
            dialog,
            text=self.tr("raise_range", min=min_amount, max=max_amount),
            font=self.font(10),
            bg="#1e293b",
            fg="#94a3b8",
        ).pack()

        def add_shortcut(parent, label, fraction):
            val = max_amount if fraction is None else max(min_amount, min(max_amount, to_call + int(self.pot * fraction)))
            tk.Button(
                parent,
                text=label,
                command=lambda v=val: amount_var.set(v),
                font=self.font(10),
                bg="#1e3a5f",
                fg="#bfdbfe",
                activebackground="#1d4ed8",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                padx=self.scale_value(6),
                pady=self.scale_value(3),
            ).pack(side="left", padx=self.scale_value(4))

        pot_label = self.tr("pot")
        row1 = tk.Frame(dialog, bg="#1e293b")
        row1.pack(pady=(8, 0))
        add_shortcut(row1, f"1/3 {pot_label}", 1 / 3)
        add_shortcut(row1, f"1/2 {pot_label}", 1 / 2)
        add_shortcut(row1, f"2/3 {pot_label}", 2 / 3)

        row2 = tk.Frame(dialog, bg="#1e293b")
        row2.pack(pady=(4, 2))
        add_shortcut(row2, f"1x {pot_label}", 1)
        add_shortcut(row2, self.tr("all_in"), None)

        tk.Scale(
            dialog,
            from_=min_amount,
            to=max_amount,
            orient="horizontal",
            variable=amount_var,
            font=self.font(9),
            bg="#1e293b",
            fg="#f8fafc",
            troughcolor="#334155",
            activebackground="#3b82f6",
            highlightthickness=0,
            length=self.scale_value(300),
        ).pack(padx=self.scale_value(20), pady=(4, 2))

        btn_frame = tk.Frame(dialog, bg="#1e293b")
        btn_frame.pack(pady=8)

        def on_confirm():
            confirmed[0] = True
            dialog.destroy()

        confirm_btn = self.button(btn_frame, "", on_confirm, 14)
        confirm_btn.pack(side="left", padx=6)
        self.button(btn_frame, self.tr("back"), dialog.destroy, 8).pack(side="left", padx=6)

        def update_label(*_):
            val = amount_var.get()
            label = self.tr("all_in") if val == max_amount else f"{self.tr('raise')} {val}"
            confirm_btn.config(text=self.ellipsize(label, 20))

        amount_var.trace_add("write", update_label)
        update_label()

        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)
        self._raise_dialog = dialog
        dialog.wait_window()
        self._raise_dialog = None

        if confirmed[0] and self.waiting_for_human and self.hand_running:
            self.stop_countdown()
            self.apply_action(human, "raise", amount_var.get())
            self.after_human_action()

    def human_fold(self):
        if not self.waiting_for_human:
            return
        self.stop_countdown()
        self.apply_action(self.human_player(), "fold")
        self.after_human_action()

    def after_human_action(self):
        self.waiting_for_human = False
        self.turn_index = self.next_seat(self.turn_index)
        self.refresh()
        self.root.after(250, self.advance_actions)

    def finish_by_folds(self):
        winner = next(player for player in self.players if player.in_hand and not player.folded)
        winner.chips += self.pot
        winner.hands_won += 1
        self.log(self.tr("wins_pot", name=winner.name, amount=self.pot))
        self.pot = 0
        self.end_hand()

    def showdown(self):
        contenders = [player for player in self.players if player.in_hand and not player.folded]
        scores = {id(player): evaluate_best(player.cards + self.community) for player in contenders}
        best_cards = {id(player): set(best_five_cards(player.cards + self.community)) for player in contenders}
        # Each unique committed amount creates one side-pot layer.
        committed_levels = sorted({player.committed for player in self.players if player.committed > 0})
        previous = 0
        awards = {}
        hand_winners: set = set()

        for level in committed_levels:
            pot_size = (level - previous) * len([player for player in self.players if player.committed >= level])
            eligible = [player for player in contenders if player.committed >= level]
            if eligible and pot_size > 0:
                best_score = max(scores[id(player)] for player in eligible)
                winners = [player for player in eligible if scores[id(player)] == best_score]
                share = pot_size // len(winners)
                remainder = pot_size % len(winners)
                for index, winner in enumerate(winners):
                    amount = share + (1 if index < remainder else 0)
                    winner.chips += amount
                    hand_winners.add(id(winner))
                    awards[winner.name] = awards.get(winner.name, 0) + amount
            previous = level

        for player in contenders:
            if id(player) in hand_winners:
                player.hands_won += 1

        best_overall = max(scores.values())
        overall_winners = [player for player in contenders if scores[id(player)] == best_overall]
        self.highlight_cards = set()
        for player in overall_winners:
            self.highlight_cards.update(best_cards[id(player)])
        best_names = ", ".join(player.name for player in overall_winners)
        award_text = "; ".join(f"{name}+{amount}" for name, amount in awards.items())
        self.log(self.tr("showdown", names=best_names, hand=describe_score(best_overall, self.lang), awards=award_text))
        self.pot = 0
        self.end_hand()

    def end_hand(self):
        self.cancel_timers()
        self.hand_running = False
        self.waiting_for_human = False

        # Identify next dealer by object identity BEFORE removing broke players,
        # so index shifts caused by removal don't corrupt dealer_index.
        surviving_ids = {id(p) for p in self.players if p.is_human or p.chips > 0}
        candidate = self.next_seat(self.dealer_index)
        for _ in range(len(self.players)):
            if id(self.players[candidate]) in surviving_ids:
                break
            candidate = self.next_seat(candidate)
        next_dealer = self.players[candidate]

        broke_ai = [player.name for player in self.players if not player.is_human and player.chips <= 0]
        for name in broke_ai:
            self.log(self.tr("left_table", name=name))
        self.players = [player for player in self.players if player.is_human or player.chips > 0]
        self.dealer_index = self.players.index(next_dealer)

        if self.human_player().chips <= 0:
            self.refresh(show_all=True)
            self.root.after(500, lambda: self.end_game(self.tr("broke")))
            return
        self.refresh(show_all=True)

    def end_game(self, reason):
        self.save_current_record()
        messagebox.showinfo(self.tr("game_over"), reason)
        self.show_main_menu()

    def format_number(self, value):
        return f"{int(value):,}"

    def format_profit(self, value):
        value = int(value)
        sign = "+" if value > 0 else ""
        return f"{sign}{self.format_number(value)}"

    def format_percent(self, value):
        return f"{float(value):.0f}%"

    def leaderboard_sort_key(self, item):
        room_id = self.normalize_room_id(item.get("room", "normal"))
        profit = int(item.get("profit", int(item.get("chips", 0)) - ROOMS[room_id]["buy_in"]))
        return (
            profit,
            float(item.get("win_rate", 0)),
            int(item.get("wins", 0)),
            int(item.get("chips", 0)),
        )

    def save_current_record(self):
        if not self.players:
            return
        hands_played = int(getattr(self, "session_hands", 0))
        if hands_played <= 0:
            return
        human = self.human_player()
        room_id = self.normalize_room_id(getattr(self, "_game_room_id", self.selected_room_id()))
        buy_in = ROOMS[room_id]["buy_in"]
        hands = hands_played
        wins = int(human.hands_won)
        self.leaderboard.append(
            {
                "name": self.tr("player"),
                "chips": human.chips,
                "buy_in": buy_in,
                "profit": human.chips - buy_in,
                "wins": wins,
                "hands": hands,
                "win_rate": wins / hands * 100,
                "room": room_id,
                "virtual": False,
            }
        )
        self.leaderboard = [item for item in self.leaderboard if not item.get("virtual")]
        self.leaderboard = sorted(
            self.leaderboard,
            key=self.leaderboard_sort_key,
            reverse=True,
        )[:20]
        try:
            LEADERBOARD_FILE.write_text(json.dumps(self.leaderboard, ensure_ascii=False, indent=2), encoding="utf-8")
        except OSError:
            pass

    def load_leaderboard(self):
        try:
            data = json.loads(LEADERBOARD_FILE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return self.virtual_leaderboard()
        records = self.normalize_leaderboard(data)
        return records or self.virtual_leaderboard()

    def normalize_room_id(self, room):
        if room in ROOMS:
            return room
        legacy = {
            "新手房": "beginner",
            "普通房": "normal",
            "高倍房": "high",
            "Beginner Room": "beginner",
            "Standard Room": "normal",
            "High Stakes": "high",
        }
        return legacy.get(room, "normal")

    def normalize_leaderboard(self, data):
        if not isinstance(data, list):
            return []
        normalized = []
        # Old saves stored localized "Player" labels; normalize them to the current language.
        legacy_player_names = ALL_PLAYER_NAMES
        for item in data:
            if not isinstance(item, dict):
                continue
            try:
                chips = int(item.get("chips", 0))
                wins = int(item.get("wins", 0))
            except (TypeError, ValueError):
                continue
            room_id = self.normalize_room_id(item.get("room", "normal"))
            buy_in = self.safe_int(item.get("buy_in", ROOMS[room_id]["buy_in"]), ROOMS[room_id]["buy_in"])
            profit = self.safe_int(item.get("profit", chips - buy_in), chips - buy_in)
            hands = max(1, self.safe_int(item.get("hands", max(1, wins)), max(1, wins)))
            win_rate = self.safe_float(item.get("win_rate", wins / hands * 100), wins / hands * 100)
            name = str(item.get("name", self.tr("player")))
            if name in legacy_player_names:
                name = self.tr("player")
            normalized.append(
                {
                    "name": name,
                    "chips": chips,
                    "buy_in": buy_in,
                    "profit": profit,
                    "wins": wins,
                    "hands": hands,
                    "win_rate": win_rate,
                    "room": room_id,
                    "virtual": bool(item.get("virtual", False)),
                }
            )
        return sorted(normalized, key=self.leaderboard_sort_key, reverse=True)[:20]

    def safe_int(self, value, fallback):
        try:
            return int(value)
        except (TypeError, ValueError):
            return fallback

    def safe_float(self, value, fallback):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback

    def virtual_leaderboard(self):
        names = BUSINESS_LEADERBOARD_NAMES.get(self.lang, BUSINESS_LEADERBOARD_NAMES["en"])
        records = []
        # Placeholder records make an empty install feel alive, then disappear on first real save.
        for index, (room_id, chips, wins, hands) in enumerate(VIRTUAL_LEADERBOARD_BLUEPRINT):
            buy_in = ROOMS[room_id]["buy_in"]
            records.append(
                {
                    "name": names[index % len(names)],
                    "chips": chips,
                    "buy_in": buy_in,
                    "profit": chips - buy_in,
                    "wins": wins,
                    "hands": hands,
                    "win_rate": wins / hands * 100,
                    "room": room_id,
                    "virtual": True,
                }
            )
        return sorted(records, key=self.leaderboard_sort_key, reverse=True)

    def refresh(self, show_all=False):
        if self.stage == "menu":
            return
        room_id = self.selected_room_id()
        room = ROOMS[room_id]
        self.info_label.config(
            text=self.tr("table_info", room=self.room_label(room_id), small=room["small_blind"], big=room["big_blind"], pot=self.pot, bet=self.current_bet)
        )
        if hasattr(self, "room_stat"):
            timer_text = self.tr("timer", seconds=f"{self.countdown_seconds:02d}s" if self.waiting_for_human else "--")
            self.room_stat.config(text=f"{self.room_label(room_id)}  {room['small_blind']}/{room['big_blind']}")
            self.pot_stat.config(text=f"{self.tr('pot')}: {self.pot}")
            self.bet_stat.config(text=f"{self.tr('current_bet')}: {self.current_bet}")
            self.timer_stat.config(text=timer_text)
        self.render_table(show_all)
        self.update_log_widget()

        human_turn = self.waiting_for_human and self.hand_running
        to_call = self.current_bet - self.human_player().current_bet
        self.controls["check_call"].config(
            state=("normal" if human_turn else "disabled"),
            text=self.ellipsize((self.tr("check") if to_call == 0 else f"{self.tr('call')} {min(to_call, self.human_player().chips)}"), 22),
        )
        human = self.human_player()
        can_raise = human.chips > to_call and (not human.has_acted or self.betting_reopened)
        self.controls["raise"].config(state=("normal" if human_turn and can_raise else "disabled"))
        self.controls["fold"].config(state=("normal" if human_turn else "disabled"))
        self.controls["next"].config(state=("normal" if not self.hand_running else "disabled"))

    def render_table(self, show_all=False):
        if not hasattr(self, "table_canvas"):
            return
        if not self.table_canvas.winfo_exists():
            return
        canvas = self.table_canvas
        canvas.delete("all")
        width = max(canvas.winfo_width(), self.scale_value(720))
        height = max(canvas.winfo_height(), self.scale_value(500))

        canvas.create_rectangle(0, 0, width, height, fill="#0b1f1a", outline="")
        table_box = (width * 0.10, height * 0.12, width * 0.90, height * 0.78)
        canvas.create_oval(*table_box, fill="#073b2a", outline="#6b4f2a", width=self.scale_value(16))
        canvas.create_oval(
            table_box[0] + self.scale_value(22),
            table_box[1] + self.scale_value(22),
            table_box[2] - self.scale_value(22),
            table_box[3] - self.scale_value(22),
            fill="#0f6b45",
            outline="#0a4d34",
            width=self.scale_value(4),
        )

        canvas.create_text(
            width / 2,
            height * 0.33,
            text=self.ellipsize(f"{self.tr('pot')} {self.pot}", 22),
            fill="#fff7d6",
            font=self.font(18, True),
            width=self.scale_value(260),
        )
        self.draw_chip_stack(canvas, width / 2 + self.scale_value(110), height * 0.37, self.pot, scale=0.82)
        self.draw_cards(canvas, self.community, width / 2, height * 0.47, hidden=False, slots=5, scale=1.0, highlight_cards=self.highlight_cards)

        positions = self.seat_positions(len(self.players))
        for index, player in enumerate(self.players):
            x = width * positions[index][0]
            y = height * positions[index][1]
            self.draw_seat(canvas, player, index, x, y, show_all)

    def seat_positions(self, count):
        layouts = {
            2: [(0.50, 0.78), (0.50, 0.16)],
            3: [(0.50, 0.78), (0.18, 0.38), (0.82, 0.38)],
            4: [(0.50, 0.78), (0.16, 0.54), (0.50, 0.16), (0.84, 0.54)],
            5: [(0.50, 0.78), (0.16, 0.60), (0.22, 0.20), (0.78, 0.20), (0.84, 0.60)],
            6: [(0.50, 0.78), (0.16, 0.62), (0.18, 0.24), (0.50, 0.16), (0.82, 0.24), (0.84, 0.62)],
        }
        return layouts.get(count, layouts[6])

    def draw_seat(self, canvas, player, index, x, y, show_all):
        is_turn = self.hand_running and index == self.turn_index and (not self.waiting_for_human or player.is_human)
        fill = "#1f2937" if not is_turn else "#334155"
        outline = "#facc15" if is_turn else "#475569"
        if player.folded:
            fill = "#3f3f46"

        seat_w = self.scale_value(84)
        seat_top = self.scale_value(48)
        seat_bottom = self.scale_value(32)
        canvas.create_rectangle(x - seat_w, y - seat_top, x + seat_w, y + seat_bottom, fill=fill, outline=outline, width=self.scale_value(3))
        canvas.create_oval(x - self.scale_value(76), y - self.scale_value(37), x - self.scale_value(42), y - self.scale_value(3), fill=player.avatar_color, outline="#e5e7eb", width=self.scale_value(2))
        initials = "".join(part[0] for part in strip_ai_suffix(player.name).split()[:2]).upper()[:2]
        canvas.create_text(
            x - self.scale_value(59),
            y - self.scale_value(20),
            text=initials or "?",
            fill="#f8fafc",
            font=self.font(10, True),
        )
        tags = []
        if index == self.dealer_index:
            tags.append(self.tr("dealer"))
        if player.folded:
            tags.append(self.tr("fold"))
        if player.all_in:
            tags.append(self.tr("all_in"))
        if player is self.pending_ai:
            tags.append(self.tr("thinking"))
        tag_text = f"  {' '.join(tags)}" if tags else ""
        canvas.create_text(
            x + self.scale_value(14),
            y - self.scale_value(28),
            text=self.ellipsize(f"{player.name}{tag_text}", 22),
            fill="#f8fafc",
            font=self.font(10, True),
            width=self.scale_value(122),
        )
        canvas.create_text(
            x + self.scale_value(14),
            y - self.scale_value(7),
            text=self.ellipsize(f"{self.tr('chips')} {player.chips}    {self.tr('round_bet')} {player.current_bet}", 24),
            fill="#d1d5db",
            font=self.font(9),
            width=self.scale_value(124),
        )
        self.draw_chip_stack(canvas, x + self.scale_value(62), y + self.scale_value(42), player.chips, scale=0.42)
        reveal = show_all or player.is_human or not self.hand_running
        self.draw_cards(canvas, player.cards, x - self.scale_value(18), y + self.scale_value(76), hidden=not reveal, slots=2, scale=0.58, highlight_cards=self.highlight_cards)
        self.draw_action_bubble(canvas, player, x, y)

    def draw_action_bubble(self, canvas, player, x, y):
        bubble = self.action_bubbles.get(id(player))
        if not bubble:
            return
        life = max(0, min(bubble["life"], len(BUBBLE_SHADES) - 1))
        fill = BUBBLE_SHADES[life]
        text = self.ellipsize(bubble["text"], 18)
        bubble_y = y - self.scale_value(62) - (len(BUBBLE_SHADES) - 1 - life) * self.scale_value(4)
        half_width = max(self.scale_value(42), len(text) * self.scale_value(8))
        canvas.create_rectangle(
            x - half_width,
            bubble_y - self.scale_value(17),
            x + half_width,
            bubble_y + self.scale_value(17),
            fill=fill,
            outline="#7c2d12",
            width=self.scale_value(2),
        )
        canvas.create_text(
            x,
            bubble_y,
            text=text,
            fill="#431407",
            font=self.font(11, True),
        )

    def draw_chip_stack(self, canvas, x, y, amount, scale=1.0):
        if amount <= 0:
            return
        scale *= UI_SCALES.get(self.ui_scale.get(), 1.0)
        chip_w = int(24 * scale)
        chip_h = max(4, int(7 * scale))
        stack_count = min(4, max(1, amount // max(self.big_blind(), 1)))
        colors = ["#ef4444", "#f8fafc", "#2563eb", "#facc15"]
        for stack in range(stack_count):
            chips = min(5, max(1, amount // max(self.big_blind() * (stack + 1), 1)))
            sx = x + (stack - (stack_count - 1) / 2) * chip_w * 0.72
            for level in range(chips):
                cy = y - level * chip_h * 0.72
                color = colors[stack % len(colors)]
                canvas.create_oval(
                    sx - chip_w / 2,
                    cy - chip_h / 2,
                    sx + chip_w / 2,
                    cy + chip_h / 2,
                    fill=color,
                    outline="#111827",
                    width=1,
                )
                canvas.create_oval(
                    sx - chip_w * 0.22,
                    cy - chip_h * 0.22,
                    sx + chip_w * 0.22,
                    cy + chip_h * 0.22,
                    fill="#f8fafc" if color != "#f8fafc" else "#ef4444",
                    outline="",
                )

    def draw_cards(self, canvas, cards, center_x, center_y, hidden=False, slots=0, scale=1.0, highlight_cards=None):
        highlight_cards = highlight_cards or set()
        scale *= UI_SCALES.get(self.ui_scale.get(), 1.0)
        card_w = int(48 * scale)
        card_h = int(68 * scale)
        gap = int(8 * scale)
        total = max(slots, len(cards))
        start_x = center_x - (total * card_w + (total - 1) * gap) / 2
        for index in range(total):
            x1 = start_x + index * (card_w + gap)
            y1 = center_y - card_h / 2
            x2 = x1 + card_w
            y2 = y1 + card_h
            if index < len(cards):
                card = cards[index]
                text = "◆" if hidden else str(card)
                fill = "#1e3a8a" if hidden else "#f8fafc"
                fg = "#dbeafe" if hidden else ("#b91c1c" if card.is_red else "#111827")
            else:
                text = ""
                fill = "#0b5b3b"
                fg = "#0b5b3b"
            highlighted = index < len(cards) and cards[index] in highlight_cards and not hidden
            outline = "#facc15" if highlighted else "#e5e7eb"
            border_width = self.scale_value(4) if highlighted else self.scale_value(2)
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=border_width)
            canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                text=text,
                fill=fg,
                font=("Microsoft YaHei UI", max(8, int(18 * scale)), "bold"),
            )

def main():
    root = tk.Tk()
    TexasHoldemApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
