import re
from telebot import types
from config import ADMIN_USERS

surname = ''
name = ''
otchestvo = ''
company = ''
industry = ''
post = ''
wemail = ''
email = ''
number = 0


def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        send_welcome(bot, message)
        
    def send_welcome(bot, message):
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        persson_button = types.KeyboardButton('Персона')
        company_button = types.KeyboardButton('Компания')
        markup.add(persson_button, company_button)
        bot.send_message(message.chat.id, "Добро пожаловать! Пожалуйста, выберите как вы хотите зарегистрироваться как Персона или же как Компания:", reply_markup=markup)
        
    @bot.message_handler(func=lambda message: message.text == 'Персона')
    def handele_registration_persson(message):
        bot.send_message(message.chat.id, "Начался процесс регистрации.")
        bot.send_message(message.chat.id, "Введите вашу Фамилию:")
        bot.register_next_step_handler(message, process_surname_step)
        
    def process_surname_step(message):
        global surname
        surname = message.text
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_surname_step)
        #     return
        
        # if not is_valid_text(message.text):
        #     msg = bot.send_message(message.chat.id, "Фамилия должна состоять только из букв")
        #     bot.register_next_step_handler(msg, process_surname_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите ваше Имя:")
        bot.register_next_step_handler(message, process_name_step)
    
    def process_name_step(message):
        global name
        name = message.text
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_name_step)
        #     return
        
        # if not is_valid_text(message.text):
        #     msg = bot.send_message(message.chat.id, "Имя должно состоять из букв")
        #     bot.register_next_step_handler(msg, process_name_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите ваше Отчество:")
        bot.register_next_step_handler(message, process_otchestvo_step)
        
    def process_otchestvo_step (message):
        global otchestvo
        otchestvo = message.text        
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_otchestvo_step)
        #     return
        
        # if not is_valid_text(message.text):
        #     msg = bot.send_message(message.chat.id, "Отчество должно состоять из букв")
        #     bot.register_next_step_handler(msg, process_otchestvo_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите название Компании:")
        bot.register_next_step_handler(message, process_company_step)
        
    def process_company_step(message):
        global company
        company = message.text
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_company_step)
        #     return
        
        # if not is_valid_text(message.text):
        #     msg = bot.send_message(message.chat.id, "Компания должна состоять из букв")
        #     bot.register_next_step_handler(msg, process_company_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите отрасль Компании:")
        bot.register_next_step_handler(message, process_industry_step)
        
    def process_industry_step (message):
        global industry
        industry = message.text        
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_company_step)
        #     return
        
        # if not is_valid_text(message.text):
        #     msg = bot.send_message(message.chat.id, "Отрасль должна состоять из букв")
        #     bot.register_next_step_handler(msg, process_company_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите вашу должность в Компании:")
        bot.register_next_step_handler(message, process_post_step)
        
    def process_post_step (message):
        global post
        post = message.text        
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_company_step)
        #     return
        
        # if not is_valid_text(message.text):
        #     msg = bot.send_message(message.chat.id, "Отрасль должна состоять из букв")
        #     bot.register_next_step_handler(msg, process_company_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите рабочий e-mail:")
        bot.register_next_step_handler(message, process_work_email_step)
        
    def process_work_email_step (message):
        global wemail
        wemail = message.text        
        
        # if not handele_all_message(message):
        #     bot.register_next_step_handler(message, process_company_step)
        #     return
        
        # if not is_valid_email(message.text):
        #     msg = bot.send_message(message.chat.id, "E-mail должен содержать @")
        #     bot.register_next_step_handler(msg, process_company_step)
        #     return
        
        bot.send_message(message.chat.id, "Введите свой e-mail:")
        bot.register_next_step_handler(message, process_email_step)
        
    def process_email_step (message):
        global email
        email = message.text        
        
#        if not handele_all_message(message):
#            bot.register_next_step_handler(message, process_company_step)
#            return
        
#        if not is_valid_email(message.text):
#            msg = bot.send_message(message.chat.id, "E-mail должен содержать @")
#            bot.register_next_step_handler(msg, process_company_step)
#            return
        
        bot.send_message(message.chat.id, "Введите свой номер телефона:")
        bot.register_next_step_handler(message, process_number_step)
        
    def process_number_step (message):
        global number
        number = message.text        
        
#        if not handele_all_message(message):
#            bot.register_next_step_handler(message, process_company_step)
#            return
        
#        if not is_valid_phone_number_format(phone_number):
#            msg = bot.send_message(message.chat.id, "Номер телефона должен содержать только цифры. Попробуйте снова:")
#            bot.register_next_step_handler(msg, process_phone_number_step)
#            return
        
        bot.send_message(
            message.chat.id,
            f'Вас зовут {surname} {name} {otchestvo}, вы работаете в компании {company}, '
            f'отрасль вашей компании {industry}, вы занимаете должность {post}, '
            f'рабочая почта {wemail}, ваша почта {email}, ваш номер телефона {number}?'
        )
        
        
    
        