import json


def alertCheck(j):
    input = json.loads(j)
    alert_message = ""
    if(input["bloodPressure"] < input["pressureRange"]["lower"]):
        alert_message += "BloodPressure is Too low, "
    elif(input["bloodPressure"] > input["pressureRange"]["upper"]):
        alert_message = "BloodPressure is Too high, "
    if(input["pulse"] < input["pulseRange"]["lower"]):
        alert_message += "Pulse is Too low, "
    elif(input["pulse"] > input["pulseRange"]["upper"]):
        alert_message += "Pulse is Too high, "
    if(input["bloodOx"] < input["oxRange"]["lower"]):
        alert_message += "BloodOx is Too low, "
    elif(input["bloodOx"] > input["oxRange"]["upper"]):
        alert_message += "BloodOx is Too high, "
    else:
        alert_message += "Every Index is Normal! "
    ui_dict = {
        "patientId": input["patientId"],
        "alert_message": alert_message,
        "bloodPressure": input["bloodPressure"],
        "pulse": input["pulse"],
        "bloodOx": input["bloodOx"]
    }
    ui_json = json.dumps(ui_dict)
    return ui_json


def main():
    j = {"patientId": 71, "pulse": 85, "pulseRange": {"lower": 66, "upper": 99}, "bloodPressure": 61,
         "pressureRange": {"lower": 63, "upper": 94}, "bloodOx": 85, "oxRange": {"lower": 67, "upper": 100}}
    input = json.dumps(j)
    ui = alertCheck(input)
    print(ui)


if __name__ == "__main__":
    main()
