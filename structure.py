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
adres = ''
partners = ''
project = ''
date = 0
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
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_surname_step)
            return
        
        if not is_valid_text(message.text):
            msg = bot.send_message(message.chat.id, "Фамилия должна состоять только из букв")
            bot.register_next_step_handler(msg, process_surname_step)
            return
        
        bot.send_message(message.chat.id, "Введите ваше Имя:")
        bot.register_next_step_handler(message, process_name_step)
    
    def process_name_step(message):
        global name
        name = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_name_step)
            return
        
        if not is_valid_text(message.text):
            msg = bot.send_message(message.chat.id, "Имя должно состоять из букв")
            bot.register_next_step_handler(msg, process_name_step)
            return
        
        bot.send_message(message.chat.id, "Введите ваше Отчество:")
        bot.register_next_step_handler(message, process_otchestvo_step)
        
    def process_otchestvo_step (message):
        global otchestvo
        otchestvo = message.text        
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_otchestvo_step)
            return
        
        if not is_valid_text(message.text):
            msg = bot.send_message(message.chat.id, "Отчество должно состоять из букв")
            bot.register_next_step_handler(msg, process_otchestvo_step)
            return
        
        bot.send_message(message.chat.id, "Введите название Компании:")
        bot.register_next_step_handler(message, process_company_step)
        
    def process_company_step(message):
        global company
        company = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_company_step)
            return
        
        if not is_company_text(message.text):
            msg = bot.send_message(message.chat.id, "Компания должна иметь буквы без спец символов попробуйте снова.")
            bot.register_next_step_handler(msg, process_company_step)
            return
        
        bot.send_message(message.chat.id, "Введите отрасль Компании:")
        bot.register_next_step_handler(message, process_industry_step)
        
    def process_industry_step (message):
        global industry
        industry = message.text        
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_industry_step)
            return
        
        if not is_valid_text(message.text):
            msg = bot.send_message(message.chat.id, "Отрасль должна состоять из букв")
            bot.register_next_step_handler(msg, process_industry_step)
            return
        
        bot.send_message(message.chat.id, "Введите вашу должность в Компании:")
        bot.register_next_step_handler(message, process_post_step)
        
    def process_post_step (message):
        global post
        post = message.text        
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_post_step)
            return
        
        if not is_post_text(message.text):
            msg = bot.send_message(message.chat.id, "Отрасль должна состоять из букв")
            bot.register_next_step_handler(msg, process_post_step)
            return
        
        bot.send_message(message.chat.id, "Введите рабочий e-mail:")
        bot.register_next_step_handler(message, process_work_email_step)
        
    def process_work_email_step (message):
        global wemail
        wemail = message.text        
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_work_email_step)
            return
        
        if not is_valid_wemail(wemail):
            msg = bot.send_message(message.chat.id, "E-mail должен содержать @")
            bot.register_next_step_handler(msg, process_work_email_step)
            return
        
        bot.send_message(message.chat.id, "Введите свой e-mail:")
        bot.register_next_step_handler(message, process_email_step)
        
    def process_email_step (message):
        global email
        email = message.text        
        
        if not handle_all_message(message):
           bot.register_next_step_handler(message, process_email_step)
           return
        
        if not is_valid_email(email):
           msg = bot.send_message(message.chat.id, "E-mail должен содержать @")
           bot.register_next_step_handler(msg, process_email_step)
           return
        
        bot.send_message(message.chat.id, "Введите свой номер телефона:")
        bot.register_next_step_handler(message, process_number_step)
        
    def process_number_step (message):
        global number
        number = message.text        
        
        if not handle_all_message(message):
           bot.register_next_step_handler(message, process_number_step)
           return
        
        if not is_valid_phone_number_format(number):
           msg = bot.send_message(message.chat.id, "Номер телефона должен содержать только цифры. Попробуйте снова:")
           bot.register_next_step_handler(msg, process_number_step)
           return
       
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes_button = types.KeyboardButton('Да')
        no_button = types.KeyboardButton('Нет')
        markup.add(yes_button, no_button)
        bot.send_message(
            message.chat.id,
            f'Вас зовут {surname} {name} {otchestvo}, вы работаете в компании {company}, '
            f'отрасль вашей компании {industry}, вы занимаете должность {post}, '
            f'рабочая почта {wemail}, ваша почта {email}, ваш номер телефона {number}?', reply_markup = markup
            )
        bot.register_next_step_handler(message, confirm_details)
        
    def confirm_details(message):
        if message.text.lower() == 'да':
            for admin_id in ADMIN_USERS:
                markup = types.InlineKeyboardMarkup()
                approve_button = types.InlineKeyboardButton('Подтвердить', callback_data=f'approve_{message.chat.id}')
                reject_button = types.InlineKeyboardButton('Отклонить', callback_data=f'reject_{message.chat.id}')
                markup.add(approve_button, reject_button)
                bot.send_message(
                    admin_id, 
                    f'Новая заявка на проверку:\n'
                    f'Фамилия: {surname}\n'
                    f'Имя: {name}\n'
                    f'Отчество: {otchestvo}\n'
                    f'Компания: {company}\n'
                    f'Отрасль: {industry}\n'
                    f'Должность: {post}\n'
                    f'Рабочий email: {wemail}\n'
                    f'Личный email: {email}\n'
                    f'Номер телефона: {number}',
                    reply_markup=markup
                )
            bot.send_message(message.chat.id, "Ваша заявка отправлена на проверку. Пожалуйста, дождитесь решения администратора.")
        else:
            bot.send_message(message.chat.id, "Регистрация отменена.")
            
            
            
            
            
    @bot.message_handler(func=lambda message: message.text == 'Компания')
    def handele_registration_company(message):
        bot.send_message(message.chat.id, "Начался процесс регистрации компании.")
        bot.send_message(message.chat.id, "Введите название Компании")
        bot.register_next_step_handler(message, process_name_company)
        
    def process_name_company(message):
        global name
        name = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_name_company)
            return
        
        if not is_company_text(message.text):
            msg = bot.send_message(message.chat.id, "Названеие Компании должно состоять из букв без спец символов.")
            bot.register_next_step_handler(msg, process_name_company)
            return
        
        bot.send_message(message.chat.id, "Введите год основания компании:")
        bot.register_next_step_handler(message, process_date_step)
        
    def process_date_step(message):
        global date
        date = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_date_step)
            return
        
        if not is_valid_date(date):
            msg = bot.send_message(message.chat.id, "Дата основания должна быть такая 01.01.2001")
            bot.register_next_step_handler(msg, process_date_step)
            return
        
        bot.send_message(message.chat.id, "Введите сферу вашей деятельности:")
        bot.register_next_step_handler(message, process_industry_company)
        
    def process_industry_company(message):
        global industry
        industry = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_industry_company)
            return
        
        if not is_valid_industry(industry):
            msg = bot.send_message(message.chat.id, "Сфера деятельности должно состоять из букв.")
            bot.register_next_step_handler(msg, process_industry_company)
            return
        bot.send_message(message.chat.id, "Адрес вашего офиса:")
        bot.register_next_step_handler(message, process_adres_step)
        
    def process_adres_step(message):
        global adres
        adres = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_adres_step)
            return
        
        if not is_valid_adres_format(adres):
            msg = bot.send_message(message.chat.id, "Адрес должен содержать буквы, цифры и допустимые спецсимволы (/ , .). Попробуйте снова:")
            bot.register_next_step_handler(msg, process_adres_step)
            return
        
        bot.send_message(message.chat.id, "Введите количество сотрудников в вашей компании:")
        bot.register_next_step_handler(message, process_number_company)
        
    def process_number_company (message):
        global number
        number = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_number_company)
            return
        
        if not is_valid_number(number):
            msg = bot.send_message(message.chat.id, "Количество сотрудников должен буть указан в числовом ввиде.")
            bot.register_next_step_handler(msg, process_number_company)
            return
        
        bot.send_message(message.chat.id, "Введите через запятую своих партнеров:")
        bot.register_next_step_handler(message, process_partners_step)
        
    def process_partners_step(message):
        global partners
        partners = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_partners_step)
            return
        
        if not is_valid_partners (partners):
            msg = bot.send_message(message.chat.id, "Паринеры должны введены буквами.")
            bot.register_next_step_handler(msg, process_partners_step)
            return
        
        bot.send_message(message.chat.id, "Опишите в крации проекты вашей компании.")
        bot.register_next_step_handler(message, process_project_step)
        
    def process_project_step(message):
        global project
        project = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_project_step)
            return
        
        if not is_valid_project(project):
            msg = bot.send_message(message.chat.id, "Описание проекта не должно состоять из одного слова.")
            bot.register_next_step_handler(msg, process_project_step)
            return
        
        bot.send_message(message.chat.id, "Отправьте сайт вашей компании.")
        bot.register_next_step_handler(message, process_web_step)
        
    def process_web_step(message):
        global web
        web = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_web_step)
            return
        
        if not is_valid_web (web):
            msg = bot.send_message(message.chat.id, "Сайт вашей компании должен иметь https://...com")
            bot.register_next_step_handler(msg, process_web_step)
            return
        
        bot.send_message(message.chat.id, "Введите рабочий e-mail:")
        bot.register_next_step_handler(message, process_email)
        
    def process_email(message):
        global wemail
        wemail = message.text
        
        if not handle_all_message(message):
            bot.register_next_step_handler(message, process_email)
            return
        
        if not is_valid_wemail(wemail):
            msg = bot.send_message(message.chat.id, "Электронная почта должна иметь @.")
            bot.register_next_step_handler(msg, process_email)
            return
        
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes_button = types.KeyboardButton('Да')
        no_button = types.KeyboardButton('Нет')
        markup.add(yes_button, no_button)
        bot.send_message(
            message.chat.id,
            f'Название вашей компании: {name} \n'
            f'Год основания вашей компании: {date} \n'
            f'Сфера деятельности вашей компании: {industry} \n'
            f'Адрес вашего офиса: {adres} \n'
            f'Количество сотрудников в вашей компании: {number} \n'
            f'Ваши партнеры: {partners} \n'
            f'Проекты вашей компании: {project} \n'
            f'Сайт вашкй компании: {web} \n'
            f'Рабочий e-mail: {wemail} \n'
            f'Верно? \n', reply_markup = markup
            )
        bot.register_next_step_handler(message, confirm_company)
        
        
        
    def confirm_company(message):
        if message.text.lower() == 'да':
            for admin_id in ADMIN_USERS:
                markup1 = types.InlineKeyboardMarkup()
                approve_button = types.InlineKeyboardButton('Подтвердить', callback_data=f'approve_{message.chat.id}')
                reject_button = types.InlineKeyboardButton('Отклонить', callback_data=f'reject_{message.chat.id}')
                markup1.add(approve_button, reject_button)
                bot.send_message(
                    admin_id,
                    f'Новая заявка от новой Компании на проверку:\n'
                    f'Название вашей компании: {name} \n'
                    f'Год основания вашей компании: {date} \n'
                    f'Сфера деятельности вашей компании: {industry} \n'
                    f'Адрес вашего офиса: {adres} \n'
                    f'Количество сотрудников в вашей компании: {number} \n'
                    f'Ваши партнеры: {partners} \n'
                    f'Проекты вашей компании: {project} \n'
                    f'Сайт вашкй компании: {web} \n'
                    f'Рабочий e-mail: {wemail} \n',
                    reply_markup=markup1
                )
            bot.send_message(message.chat.id, "Ваша заявка отправлена на проверку. Пожалуйста, дождитесь решения администратора.")
        else:
            bot.send_message(message.chat.id, "Регистрация отменена.")
        
        
                    
            
    @bot.callback_query_handler(func=lambda call: call.data.startswith('approve_') or call.data.startswith('reject_'))
    def handle_admin_decision(call):
        action, user_id = call.data.split('_')
        user_id = int(user_id)
        
        if action == 'approve':
            bot.send_message(user_id, "Ваша заявка была одобрена администратором!")
        elif action == 'reject':
            bot.send_message(user_id, "Ваша заявка была отклонена администратором.")
        
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
                
    def handle_all_message(message):
        if message.content_type != 'text':
            send_error_message(message)
            return False
        return True
    
    def is_valid_text(text):
        return bool(re.match("^[A-Za-aA-Яа-яЁё]{2,}$", text))
    
    def is_valid_phone_number_format(number):
        return bool(re.match("^[0-9+]{11,}$", number))
    
    def is_valid_email(email):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
    
    def is_valid_wemail(wemail):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', wemail))
    
    def send_error_message(message):
        bot.send_message(message.chat.id, "Извините, я понимаю только текстовые сообщения")
        
        
    def is_company_text(company):
        return bool(re.match("^[А-ЯA-Za-zа-я ]{2,}$", company))
    
    def is_post_text (post):
        return bool(re.match("^[A-Za-zА-Яа-я ]{2,}$", post))
    
    def is_valid_date(date):
        return bool(re.match("^[0-9 .]$", date))
    
    def is_valid_industry(industry):
        return bool(re.match("^[A-Za-zА-Яа-я ,.]{20,}$", industry))
    
    def is_valid_adres_format(adres):
        return bool(re.match("^[A-Za-z0-9А-Яа-яЁё /,.-]{2,}$", adres))
    
    def is_valid_number (number):
        return bool(re.match("^[0-9]$", number))
    
    def is_valid_partners(partners):
        return bool(re.match("^[A-Za-zА-Яа-я ,]$", partners))
    
    def is_valid_project(project):
        return bool(re.match("^[A-Za-zА-Яа-я0-9 ,.]$", project))
    
    def is_valid_web(web):
        return bool(re.match(r'https://+[A-Za-z]+\.com$' , web))