from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

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
        for i in stations:
            print(i.number, i.name, i.line, i.nearstation)
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
                break

        visited[nearest] = True
        for (to, distance) in stations[nearest].nearstation:
            if dist[to] > dist[nearest] + distance:
                dist[to] = dist[nearest] + distance
                intermediate_stations[to] = nearest
    print(intermediate_stations)
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

    result.append(f"Общее время пути: {total_time:.2f} мин.")
    result.append(f"Маршрут:")
    result.append(f"{stations[path[0]].name} ({stations[path[0]].line})")

    for i in range(1, len(path)):
        if stations[path[i]].line != stations[path[i - 1]].line:
            result.append("_______________________________________________________________")
            result.append(f" - Пересадка с линии {stations[path[i - 1]].line} на линию {stations[path[i]].line}")
            result.append("-----------------------------------------------------------------------------------------")
            total_time += AVERAGE_WAITING_TIME
            
        travel_time = 60 * (dist[path[i]] - dist[path[i - 1]]) / AVERAGE_SPEED
        result.append(f" -> {stations[path[i]].name} - {travel_time:.2f} мин.")

    return "\n".join(result)

STATIONS = create_stations_db("text.txt")

# for i in STATIONS:
#     print(i.number, i.name, i.line)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Введите начальную и конечную станции метро через запятую. Пример:\nА, Б")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    start_name, finish_name = [s.strip() for s in user_input.split(",")]
    start = finish = -1
    for station in STATIONS:
        if station.name == start_name:
            start = station.number
        if station.name == finish_name:
            finish = station.number
    if start == -1 or finish == -1:
        await update.message.reply_text("Ошибка: одна из станций не найдена. Проверьте названия и попробуйте снова.")
        return

    dist, intermediate_stations = dijkstra_algorithm(STATIONS, start)
    result = print_path(STATIONS, dist, intermediate_stations, start, finish)
    await update.message.reply_text(result)

def main():
    TOKEN = "7732659490:AAE5CcPr5rBFeWwVr5i0sgbjs76eb7NEnNw"

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

