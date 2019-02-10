# EC500_Spring19

Input Module
================
**The input module consists of the following functions:**

  * **getPatientInfo**: This function is used for capturing patient related info. The Patient Id is used as the unique identifier. This helps in idenitying data corresponding to each patient.
  
     Output: json

     Output Example:
     ```{"1234": {"gender": "Male", "age": "30", "name": "John"}}```

     where "1234" is the patientId

  * **readSensorData**: Reads sensor data and converts it into json format. Inputs and their corresponding datatype is mentioned in the Fig. inpute_module.png. 
    
     Output: json

     Output Example:
    ``` {"1234": {"pulse": "90", "pulseRange": {"upper": "120", "lower": "50"}, "bloodPressure": "80", "pressureRange": {"upper": "100",           "lower": "30"}, "bloodOx": "83", "oxRange": {"upper": "90", "lower": "60"}, "time": "12-Feb-19" }}```

     where "1234" is the patientId

  * **checkInput**: Checks if the sensor's data are valid. If there are no errors, the data is then stored in the database. 

**Technology:**
Python

