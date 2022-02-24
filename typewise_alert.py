def infer_breach(value, lowerLimit, upperLimit):
    if value < lowerLimit:
        return 'TOO_LOW'
    if value > upperLimit:
        return 'TOO_HIGH'
    return 'NORMAL'


def coolingtype_range(coolingType):
  coolingType_dict={'PASSIVE_COOLING':{"lowerLimit":0,"upperLimit":35},'HI_ACTIVE_COOLING':{"lowerLimit":0,"upperLimit":45},'MED_ACTIVE_COOLING':{"lowerLimit":0,"upperLimit":40}}					   
  if coolingType in coolingType_dict.keys():
    return(coolingType_dict[coolingType]) 
  else:
    default={"lowerLimit":'Not in limits',"upperLimit":'Not in limits'}
    return(default) 


def classify_temperature_breach(coolingType, temperatureInC):
  cooling_limits  = coolingtype_range(coolingType)
  breach = infer_breach(temperatureInC, cooling_limits["lowerLimit"], cooling_limits["upperLimit"])	
  if 'Not in limits' in cooling_limits.values():
    return 'WARNING'
  else:
    return breach


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar, temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    command = send_to_controller(breachType)
    return command
  elif alertTarget == 'TO_EMAIL':
    command = send_to_email(breachType)
    return command
  else:  
    return "NOT_APPLICABLE"

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return(f'{header}, {breachType}')
  

def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}, Hi, the temperature is too low')
    return(f'To: {recepient}, Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}, Hi, the temperature is too high')
    return(f'To: {recepient}, Hi, the temperature is too high')
  else:
        return(f'To: {recepient}, NOT_APPLICABLE')
