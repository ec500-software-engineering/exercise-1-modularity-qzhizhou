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
    input_sendor_data = json.loads(input_sensor_json)
    input_patient_data = json.loads(input_patient_json)
    '''
    store in db
    '''
    storage.insert(input_patient_json, input_sensor_json)

    '''
    analysis
    '''
    alert_json, patient_info = alert_system.alertCheck(
        input_patient_json, input_sensor_json)
    '''
    output to UI
    '''
    patient1 = output.patient()
    patient1.recieveFromAlert(alert_json)
    patient1.send_alert_to_UI(patient_info)

    '''update this table to set pulse = 100: '''
    storage.update("1234", '17:05:20pm-01/02/2019', 'bloodOx', '90')
    '''search a person with PatientID 1234: '''
    patient_info = storage.searchPerson("1234")


if __name__ == "__main__":
    main()
