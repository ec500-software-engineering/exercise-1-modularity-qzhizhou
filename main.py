import json
from input import input
from alert import alert_system
from output import output


def main():
    input_json = input.readSensorData()
    input_data = json.loads(input_json)
    alert_json = alert_system.alertCheck(input_json)
    alert_data = json.loads(alert_json)
    patient1 = output.patient()
    patient1.recieveFromAlert(alert_data)

    print("raw input: ", input_data)
    print("final output: " + patient1.send_alert_to_UI())


if __name__ == "__main__":
    main()
