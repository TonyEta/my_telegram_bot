# 🐾 My Telegram AI Bot

Вітаємо у світі інтелектуальних чатів та інтерактивних розваг!  
Цей бот – ваш персональний помічник у Telegram, який вміє спілкуватися, давати рекомендації та навіть допомагати з резюме.  
Все це реалізовано завдяки потужності OpenAI GPT та зручній системі режимів.

---

## 🌟 Основні функції

Бот має 5 основних режимів, доступних через інтерактивне меню:

### 🎯 Доступні режими
- **🎲 `/random`** – Випадковий факт  
- **💬 `/talk`** – Діалог з відомими особистостями  
- **🤖 `/gpt`** – Запитати ChatGPT  
- **🎬 `/leisure`** – Рекомендації книг, фільмів, пісень  
- **📄 `/hr_help`** – Допомога з оформленням резюме  

💡 Завжди можна повернутися в головне меню через `/start`.

---

## 🛠 Встановлення та налаштування

### 1️⃣ Клонування репозиторію
```bash
git clone https://github.com/TonyEta/my_telegram_bot.git
cd your-repo

2️⃣ Створення віртуального середовища

# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Встановлення залежностей

pip install -r requirements.txt

4️⃣ Налаштування змінних середовища

Створіть файл .env у корені проекту:

env
BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here

📁 Структура проекту

my_telegram_bot/
├── buttons/                 # Інлайн-клавіатури для режимів
│   ├── gpt_buttons.py
│   ├── help_buttons.py
│   ├── hr_buttons.py
│   ├── leisure_buttons.py
│   ├── random_buttons.py
│   ├── start_buttons.py
│   └── talk_buttons.py
├── chat_gpt/
│   └── gpt_client.py        # Клієнт для роботи з OpenAI API
├── content/
│   ├── pictures/            # Зображення для ботів
│   └── prompts/             # GPT промпти
├── handlers/                # Обробники повідомлень
│   ├── dialog_handlers.py
│   ├── hr_handlers.py
│   ├── leisure_handlers.py
│   ├── main_handlers.py
│   ├── start_help_handlers.py
│   └── state_handlers.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run.py                   # Головний файл запуску

🚀 Запуск бота
python run.py


💡 Як користуватися

Знайдіть бота в Telegram та натисніть /start.

Оберіть потрібний режим з головного меню.

Використовуйте кнопки для навігації.

Для виходу з режиму або повернення в головне меню натисніть /start.

🎨 Особливості реалізації

Клавіатури
Бот використовує інлайн-клавіатури для зручної навігації:

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_random = InlineKeyboardButton(text="🎲 /random - випадковий факт", callback_data="random")
button_talk = InlineKeyboardButton(text="💬 /talk - діалог з відомою особистістю", callback_data="talk")
button_gpt = InlineKeyboardButton(text="🤖 /gpt - запитати ChatGPT", callback_data="gpt")
button_leisure = InlineKeyboardButton(text="🎬 /leisure - рекомендації", callback_data='leisure')
button_hr_help = InlineKeyboardButton(text="📄 /hr_help - допомога з резюме", callback_data="HR_help")

main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_random],
        [button_talk],
        [button_gpt],
        [button_leisure],
        [button_hr_help]
    ]
)

Стани (FSM)
Для складних сценаріїв (наприклад, створення резюме) використовується Finite State Machine:

from aiogram.fsm.state import StatesGroup, State

class ResumeStates(StatesGroup):
    name = State()
    age = State()
    contacts = State()
    education = State()
    skills = State()
    languages = State()
    motivation = State()
    
Кожен режим має власний обробник:
@router.callback_query(F.data == "random")
async def cmd_random(callback: CallbackQuery):
    photo = FSInputFile("content/pictures/random-picture.jpg")
    fact = await ask_gpt(prompt)
    await callback.message.answer_photo(photo=photo)
    await callback.message.answer(text=fact, reply_markup=random_keyboard)
    
🔧 Технології:
Aiogram 3.x – сучасна бібліотека для Telegram Bot API

OpenAI API – інтеграція з GPT моделями

Python-dotenv – управління конфігурацією

Async/await – асинхронне програмування

FSM (Finite State Machine) – управління станами бота



⚠️ Примітка: Для роботи бота необхідно отримати API ключі від OpenAI та створити бота через @BotFather у Telegram.