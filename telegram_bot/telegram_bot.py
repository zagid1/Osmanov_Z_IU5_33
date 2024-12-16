import logging
import httpx
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = '****************************************************************'

async def translate_text(text: str, target_lang: str) -> str:
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "auto",
        "tl": target_lang,
        "dt": "t",
        "q": text,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        print(response)
        translated_data = response.json()
        print(translated_data)
        translations = [translation[0] for translation in translated_data[0]]
        return ''.join(translations)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\! Добро пожаловать в Osmanov бот\.'
        '\nЯ могу переводить текст и не только\.\n'
        'Для получения списка команд отправте сообщение /help' 
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'при отправке сообщения боту, он переведет его на английский\n\n'
        'Вот список доступных команд:\n'
        '/start - Начать взаимодействие с ботом\n'
        '/help - Показать это сообщение\n'
        '/transl <текст> - Бот переведет на английский сообщение\n'
        '/reverse <текст> - Бот перевернёт ваше сообщение\n'
        '/upper <текст> - Бот преобразует текст в верхний регистр\n'
        '/lower <текст> - Бот преобразует текст в нижний регистр'
    )

async def transl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    try:
        translated_text = await translate_text(text, 'en')
        await update.message.reply_text(translated_text)
    except httpx.HTTPStatusError as e:
        logger.error(f"Ошибка HTTP при переводе: {e}")
        await update.message.reply_text("Не удалось перевести текст. Попробуйте позже.")

async def reverse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if not args:
        await update.message.reply_text('Предоставьте текст для переворота. Например: /reverse Привет')
        return
    reversed_text = ' '.join(args)[::-1]
    await update.message.reply_text(reversed_text)

async def upper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if not args:
        await update.message.reply_text('Предоставьте текст для преобразования. Например: /upper Привет')
        return
    upper_text = ' '.join(args).upper()
    await update.message.reply_text(upper_text)

async def lower(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if not args:
        await update.message.reply_text('Предоставьте текст для преобразования. Например: /lower Привет')
        return
    lower_text = ' '.join(args).lower()
    await update.message.reply_text(lower_text)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
   
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text('Произошла ошибка. Пожалуйста, попробуйте позже.')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("reverse", reverse))
    application.add_handler(CommandHandler("upper", upper))
    application.add_handler(CommandHandler("lower", lower))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, transl))

    application.add_error_handler(error_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
