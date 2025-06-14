import telebot
from telebot import types

# دانانی تۆکنی بۆتەکەت
TOKEN = '8075316703:AAH2znlpO1juiLMuPe8-jP0KAR4PqjKimdE'
bot = telebot.TeleBot(TOKEN)

# فانکشنی بەخێرهاتن
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # دروستکردنی کلیلەتەری گۆڕاو
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # دروستکردنی دووگمەکان
    btn1 = types.KeyboardButton('وانەی سەرەتایی')
    btn2 = types.KeyboardButton('پرسیارێک بکە')
    btn3 = types.KeyboardButton('کۆدێک تاقیبکەرەوە')
    btn4 = types.KeyboardButton('پێشبڕکێی کۆد')
    
    markup.add(btn1, btn2, btn3, btn4)
    
    # ناردنی نامەی بەخێرهاتن
    welcome_text = """
بەخێربێیت بۆ بۆتی فێرکاری پایتۆن! 👋

من یارمەتیت دەدەم لە فێربوونی زمانی پایتۆن بە زمانی کوردی. دەتوانیت پرسیار بکەیت، کۆد بنووسیت یان وانە بخوێنیتەوە.

هەڵبژاردەکان:
- وانەی سەرەتایی
- پرسیارێک بکە
- کۆدێک تاقیبکەرەوە
- پێشبڕکێی کۆد

نووسە /help بۆ بینینی هەموو فرمانەکان
    """
    bot.reply_to(message, welcome_text, reply_markup=markup)

# فانکشنی یارمەتی
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
فرمانە بەردەستەکان:
/start - دەستپێکردن
/help - یارمەتی
/lesson - وانەکان
/quiz - تاقیکردنەوە
/project - پڕۆژە

دەتوانیت پرسیارەکەت ڕاستەوخۆ بنووسیت یان لە دووگمەکان هەڵبژێریت.
    """
    bot.reply_to(message, help_text)

# فانکشنی وەڵامدانەوەی پرسیارەکان
@bot.message_handler(func=lambda message: True)
def answer_question(message):
    user_message = message.text.lower()
    
    if user_message == 'وانەی سەرەتایی':
        # وانەی سەرەتایی
        lesson_text = """
**وانەی سەرەتایی: فانکشن لە پایتۆن**

فانکشن لە پایتۆن بەم شێوەیە دروست دەکرێت:

```python
def ناوی_فانکشن(پارامیتەر١, پارامیتەر٢):
    # کۆدی فانکشن
    ئەنجام = پارامیتەر١ + پارامیتەر٢
    return ئەنجام
    
# بانگکردنی فانکشن
نەتيجة = ناوی_فانکشن(5, 3)
print(نەتيجة)  # دەرئەنجام: 8