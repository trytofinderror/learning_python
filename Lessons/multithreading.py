import time
import threading


def sleep_time(delay: int, text: str) -> None:
    print("Выводим текст:", text, "\n")
    time.sleep(delay)
    print("Выводим текст повторно:", text, "\n")


start_time = time.time()

t_list = []

for i in range(5):
    name = "sleep_time" + str(i)
    print("Был запущен поток", name, "\n")
    td = threading.Thread(target=sleep_time, name=name, args=(10, name))
    td.start()
    t_list.append(td)

# Если сначала запустить необходимое количество потоков, а позже вызвать для всех метод join,
# то код выполнится параллельно, но основной поток продолжит выполнение после окончания выполнения
# кода дополнительных потоков

for t in t_list:
    t.join()

end_time = time.time()

print("Время обработки:", end_time - start_time, "\n")
