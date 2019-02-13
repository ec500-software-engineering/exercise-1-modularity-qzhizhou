import random
import json
import time


def generate():
    pulse = random.randint(60, 100)
    pulseRangeLower = random.randint(60, 70)
    pulseRangeUpper = random.randint(90, 100)

    bloodPressure = random.randint(60, 100)
    pressureRangeLower = random.randint(60, 70)
    pressureRangeUpper = random.randint(90, 100)

    bloodOx = random.randint(60, 100)
    oxRangeLower = random.randint(60, 70)
    oxRangeUpper = random.randint(90, 100)

    patientId = random.randint(0, 1000)

    data = {
        'patientId': patientId,
        'pulse': pulse,
        'pulseRange': {'lower': pulseRangeLower, 'upper': pulseRangeUpper},
        'bloodPressure': bloodPressure,
        'pressureRange': {'lower': pressureRangeLower, 'upper': pressureRangeUpper},
        'bloodOx': bloodOx,
        'oxRange': {'lower': oxRangeLower, 'upper': oxRangeUpper}
    }

    input_json = json.dumps(data)
    return input_json


def main():
    while(True):
        _time = random.random() * 10
        input = generate()
        print(input)
        time.sleep(_time)


if __name__ == "__main__":
    main()
