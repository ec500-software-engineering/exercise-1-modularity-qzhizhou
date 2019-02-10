from output import output
from alert import alert_system
import json
from input import input
from database import storage


def main():
    '''
    input data
    '''
    input_sensor_json = input.readSensorData()
    input_patient_json = input.getPatientInfo()
    input_data = json.loads(input_sensor_json)

    '''
    store in db
    '''
    storage.insert(input_patient_json, input_sensor_json)

    '''
    analysis
    '''
    alert_json = alert_system.alertCheck(input_sensor_json)

    '''
    output to UI
    '''
    patient1 = output.patient()
    patient1.recieveFromAlert(alert_json)

    print("raw input: ", input_data)
    print("final output: " + patient1.send_alert_to_UI())
    print('\n')

    '''search a person with PatientID 1234: '''
    print('patient info: ', storage.searchPerson("1234"))
    '''update this table to set pulse = 100: '''
    storage.update("1234", '17:05:20pm-01/02/2019', 'bloodOx', '90')


if __name__ == "__main__":
    main()
