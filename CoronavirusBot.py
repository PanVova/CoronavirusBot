from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):

    update.message.reply_text('This bot was created to get the latest information about COVID-19 Infected. Country , Population , Confirmed Cases, Recovered Cases, Death Cases. You just write name of the country on English language')


def help_command(update, context):
    update.message.reply_text('This bot was created to get the latest information about COVID-19 Infected. Country , Population , Confirmed Cases, Recovered Cases, Death Cases. You just write name of the country on English language')

def echo(update, context):
        try:
            f = open('Countries/' + update.message.text + ".txt", "r")
            update.message.reply_text("Country: " + f.readline() + "Population: " + f.readline() + "Confirmed: " + f.readline() + "Recovered: " + f.readline() + "Deaths: " + f.readline())
        except Exception:
            update.message.reply_text("This country does not exists ")

def for_start():
    import COVID19Py

    covid19 = COVID19Py.COVID19(data_source="jhu")
    data = covid19.getAll()
    id = 0
    while id <= 265:

        country_name = data['locations'][id]['country']

        if country_name == "Taiwan*":
            country_name = "Taiwan"

        f = open('Countries/' + country_name + ".txt", "w")

        f.write(data['locations'][id]['country'] + '\n')
        f.write(str(data['locations'][id]['country_population']) + '\n')
        f.write(str(data['locations'][id]['latest']['confirmed']) + '\n')
        f.write(str(data['locations'][id]['latest']['recovered']) + '\n')
        f.write(str(data['locations'][id]['latest']['deaths']))

        f.close()
        id = id + 1

def main():

    for_start() # Сделать этот запуск раз в несколько часов

    updater = Updater("CODE", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()