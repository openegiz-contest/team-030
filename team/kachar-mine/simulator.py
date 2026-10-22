# Kachar Mine Digital Twin
# Алғашқы симуляциялық модель

TRUCK_COUNT = 4
TRUCK_CAPACITY = 90       # тонна
TRIP_TIME = 20            # минут
WORK_HOURS = 1

trips_per_truck = (WORK_HOURS * 60) / TRIP_TIME

total_ore = TRUCK_COUNT * TRUCK_CAPACITY * trips_per_truck

print("Kachar Mine Digital Twin")
print("-----------------------")
print("Самосвал саны:", TRUCK_COUNT)
print("Бір самосвалдың сыйымдылығы:", TRUCK_CAPACITY, "тонна")
print("Бір рейстің ұзақтығы:", TRIP_TIME, "минут")
print("Бір сағаттағы тасымал:", total_ore, "тонна")

# Экскаваторлар
EXCAVATOR_COUNT = 2
EXCAVATOR_CAPACITY = 400

excavator_output = EXCAVATOR_COUNT * EXCAVATOR_CAPACITY
actual_output = min(total_ore, excavator_output)

print("-----------------------")
print("Экскаватор саны:", EXCAVATOR_COUNT)
print("Экскаваторлардың өнімділігі:", excavator_output, "тонна/сағат")
print("Жүйенің есептік өнімділігі:", actual_output, "тонна/сағат")

# What-if: тағы бір экскаватор қосу
NEW_EXCAVATOR_COUNT = 3

new_excavator_output = NEW_EXCAVATOR_COUNT * EXCAVATOR_CAPACITY
new_output = min(total_ore, new_excavator_output)

increase = new_output - actual_output
increase_percent = increase / actual_output * 100

print("-----------------------")
print("WHAT-IF: 3 экскаватор")
print("Бастапқы өнімділік:", actual_output, "т/сағ")
print("Жаңа өнімділік:", new_output, "т/сағ")
print("Өнімділік өсімі:", increase, "т/сағ")
print("Өсім пайызы:", round(increase_percent, 1), "%")
