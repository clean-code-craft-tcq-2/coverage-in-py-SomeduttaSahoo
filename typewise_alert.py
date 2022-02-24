
breach_values = {1:'NORMAL',2:'TOO_HIGH',3:'TOO_LOW'}

cooling_types = {'PASSIVE_COOLING':{'lower_limit':0,'upper_limit':35},
'HI_ACTIVE_COOLING':{'lower_limit':0,'upper_limit':45},
'MED_ACTIVE_COOLING':{'lower_limit':0,'upper_limit':40}}

email_messages = {
  "TOO_LOW":{
    "recipient":"a.b@c.com",
    "alert_message":"Hi, the temperature is too low"
  },
  "TOO_HIGH":{
    "recipient":"a.b@c.com",
    "alert_message":"Hi, the temperature is too high"
  }
}

def send_to_controller(breachType):
  header = 0xfeed
  controller_content = '{header}, {breach}'.format(header = header,breach=breachType)
  print(controller_content)
  return controller_content


def send_to_email(breachType):
  email_content = "To: "+email_messages[breachType]['recipient']+"\n"+email_messages[breachType]['alert_message']
  print (email_content)
  return email_content

alert_types = {'CONTROLLER':send_to_controller,'EMAIL':send_to_email}

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return breach_values[3]
  if value > upperLimit:
    return breach_values[2]
  return breach_values[1]


def classify_temperature_breach(coolingType, temperatureInC):
  return infer_breach(temperatureInC, cooling_types[coolingType]['lower_limit'], cooling_types[coolingType]['upper_limit'])


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  if is_valid_input(alertTarget,batteryChar) is False:
    return "INVALID_INPUT"
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if breachType is not breach_values[1]:
    return alert_types[alertTarget](breachType)
  else:
    return breachType

def is_available_in_keys(param,param_belongs_to):
  if param in param_belongs_to.keys():
    return True
  return False

def is_valid_input(alertTarget,batteryChar):
  param_check_list=[is_available_in_keys(alertTarget,alert_types),
                    is_available_in_keys(batteryChar['coolingType'],cooling_types)]
  if False in param_check_list:
    return False
  return True
