from input import generateInput
from alert import alert
from output import output
import time
import threading
import json
import queue
import random

input_queue = queue.Queue()
output_queue = queue.Queue()
patient_obj = output.patient()


def process_input():
    while True:
        print('generating\n')
        input_json = generateInput.generate()
        input_queue.put(input_json)
        _time = random.random()
        time.sleep(_time)


def worker_analysis():
    while True:
        print('processing\n')
        input_json = input_queue.get()
        if input_json is None:
            break
        analyse(input_json)
        input_queue.task_done()
        time.sleep(1)


def analyse(input_json):
    ui_json = alert.alertCheck(input_json)
    print(ui_json)
    print('\n')
    output_queue.put(ui_json)


def worker_output():
    while True:
        print('outputing\n')
        ui_json = output_queue.get()
        if ui_json is None:
            break
        sned_to_ui(ui_json)
        output_queue.task_done()
        time.sleep(1)


def sned_to_ui(ui_json):
    patient_obj.recieveFromAlert(ui_json)


def main():
    input_thread = threading.Thread(target=process_input)
    woker_thread = threading.Thread(target=worker_analysis)
    output_thread = threading.Thread(target=worker_output)
    input_thread.start()
    woker_thread.start()
    output_thread.start()
    print("started")
    input_thread.join()
    woker_thread.join()
    output_thread.join()
    print("ended")


if __name__ == "__main__":
    main()
