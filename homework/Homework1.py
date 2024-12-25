from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Константы
AVERAGE_SPEED = 45.12  # Средняя скорость (км/ч)
AVERAGE_TRANSFER_TIME = 1.5  # Время пересадки (мин)
AVERAGE_WAITING_TIME = 1  # Время ожидания (мин)

class Station:
    def __init__(self, number, name, line):
        self.number = number  # Номер станции
        self.name = name  # Название станции
        self.line = line  # Линия метро
        self.nearstation = []  # Соседи: [(номер_соседа, расстояние)]

def create_stations_db(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        parts = next(file).split(';')
        stations = [Station(-1, "Unknown", "Unknown") for _ in range(int(parts[0]))]
        
        for line in file:
            parts = line.split(';')
            #print(parts)
            station_num = int(parts[0])
            stations[station_num].number = int(parts[0])
            stations[station_num].name = parts[1]
            stations[station_num].line = parts[2]
            nearstation_num = int(parts[3])
            distance = float(parts[4])

            stations[station_num].nearstation.append((nearstation_num, distance))
            stations[nearstation_num].nearstation.append((station_num, distance))
        # for i in stations:
        #     print(i.number, i.name, i.line, i.nearstation)
    return stations


def dijkstra_algorithm(stations, start):
    size = len(stations)
    dist = [float('inf')] * size
    dist[start] = 0
    visited = [False] * size
    intermediate_stations = [-1] * size

    for _ in range(size):
        nearest = -1
        for v in range(size):
            if ((not visited[v]) and (nearest == -1 or dist[nearest] > dist[v])): 
                nearest = v 
                # print(nearest)
                #break

        visited[nearest] = True
        for (to, distance) in stations[nearest].nearstation:
            if dist[to] > dist[nearest] + distance:
                dist[to] = dist[nearest] + distance
                intermediate_stations[to] = nearest
    #print(intermediate_stations)
    return dist, intermediate_stations

def print_path(stations, dist, intermediate_stations, start, finish):
    path = []
    i = finish
    while i != -1:
        path.append(i)
        i = intermediate_stations[i]
    path.reverse()

    total_time = (60 * dist[finish] / AVERAGE_SPEED) + AVERAGE_WAITING_TIME
    result = []

    for i in range(1, len(path)):
        if stations[path[i]].line != stations[path[i - 1]].line:
            total_time += AVERAGE_WAITING_TIME + AVERAGE_TRANSFER_TIME

    result.append(f"Общее время пути: {total_time:.0f} мин.")
    result.append(f"Маршрут:")
    result.append(f"{stations[path[0]].name} ({stations[path[0]].line})")

    for i in range(1, len(path)):
        if stations[path[i]].line != stations[path[i - 1]].line:
            result.append("_______________________________________________________________")
            result.append(f" - Пересадка с линии {stations[path[i - 1]].line} на линию {stations[path[i]].line}")
            result.append(f" -> {stations[path[i]].name} ({stations[path[i]].line})")
        else:
            travel_time = 60 * (dist[path[i]] - dist[path[i - 1]]) / AVERAGE_SPEED
            result.append(f" -> {stations[path[i]].name} - {travel_time:.1f} мин.")

    return "\n".join(result)


# for i in STATIONS:
#     print(i.number, i.name, i.line)

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

STATIONS = create_stations_db("text.txt")

LINES = {}
for station in STATIONS:
    if station.line not in LINES:
        LINES[station.line] = []
    LINES[station.line].append(station)

user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_states[update.effective_user.id] = {"start_station": None, "end_station": None, "line": None}
    keyboard = [[InlineKeyboardButton(line, callback_data=f"line_{line}")] for line in LINES.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите линию метро:", reply_markup=reply_markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data
    state = user_states.get(user_id, {"start_station": None, "end_station": None, "line": None})

    if data.startswith("line_"):

        line_name = data.split("_")[1]
        state["line"] = line_name
        user_states[user_id] = state


        keyboard = [
            [InlineKeyboardButton(station.name, callback_data=f"start_{station.number}")]
            for station in LINES[line_name]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Вы выбрали линию: {line_name}\nТеперь выберите начальную станцию:", reply_markup=reply_markup)

    elif data.startswith("start_"):

        station_id = int(data.split("_")[1])
        state["start_station"] = station_id
        user_states[user_id] = state

        keyboard = [[InlineKeyboardButton(line, callback_data=f"end_line_{line}")] for line in LINES.keys()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите линию для конечной станции:", reply_markup=reply_markup)

    elif data.startswith("end_line_"):

        line_name = data.split("_")[2]
        state["line"] = line_name
        user_states[user_id] = state

        keyboard = [
            [InlineKeyboardButton(station.name, callback_data=f"end_{station.number}")]
            for station in LINES[line_name]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Вы выбрали линию: {line_name}\nТеперь выберите конечную станцию:", reply_markup=reply_markup)

    elif data.startswith("end_"):
        station_id = int(data.split("_")[1])
        state["end_station"] = station_id
        user_states[user_id] = state

        start = state["start_station"]
        finish = state["end_station"]

        if start is not None and finish is not None:
            dist, intermediate_stations = dijkstra_algorithm(STATIONS, start)
            result = print_path(STATIONS, dist, intermediate_stations, start, finish)
            await query.edit_message_text(f"Маршрут найден:\n\n{result}")
        else:
            await query.edit_message_text("Ошибка: начальная или конечная станция не выбрана.")

def main():
    TOKEN = "7732659490:AAE5CcPr5rBFeWwVr5i0sgbjs76eb7NEnNw"    

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
