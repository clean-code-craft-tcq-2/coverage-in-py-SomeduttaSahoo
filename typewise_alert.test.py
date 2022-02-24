import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_low_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_infers_breach_as_per_high_limits(self):
        self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == 'TOO_HIGH')
    def test_infers_breach_as_per_normal_limits(self):
        self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')
        
    def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.coolingtype_range('PASSIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 35})
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.coolingtype_range('HI_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 45})
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.coolingtype_range('MED_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 40})
    def test_classify_temperature_breachs_for_OUT_OF_LIMITS(self):
        self.assertTrue(typewise_alert.coolingtype_range('OUT_OF_LIMITS') == {"lowerLimit" : 'Not in limits', "upperLimit" : 'Not in limits'})
        
    def test_classify_temperature_breach_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -50)=='TOO_LOW') 
    def test_classify_temperature_breach_for_NORMAL(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 36)=='NORMAL')  
    def test_classify_temperature_breach_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 47)=='TOO_HIGH') 
        
    def test_send_to_controller_too_high_breachType(self):
        self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH') == f'{0xfeed}, TOO_HIGH')
    def test_send_to_controller_too_low_breachType(self):
        self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == f'{0xfeed}, TOO_LOW')

    def test_check_and_alert_send_to_controller_PASSIVE_COOLING_TOO_LOW(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER','PASSIVE_COOLING',-5) == f'{0xfeed}, TOO_LOW')
    def test_check_and_alert_send_to_controller_PASSIVE_COOLING_TOO_HIGH(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER','PASSIVE_COOLING', 100)==f'{0xfeed}, TOO_HIGH')
    def test_check_and_alert_send_to_controller_PASSIVE_COOLING_NORMAL(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER','PASSIVE_COOLING', 16)==f'{0xfeed}, NORMAL')
    def test_check_and_alert_send_to_controller_HI_ACTIVE_COOLING_TOO_LOW(self):    
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING',-18)==f'{0xfeed}, TOO_LOW')
    def test_check_and_alert_send_to_controller_HI_ACTIVE_COOLING_TOO_HIGH(self): 
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', 260)==f'{0xfeed}, TOO_HIGH')
    def test_check_and_alert_send_to_controller_HI_ACTIVE_COOLING_NORMAL(self):     
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', 40)==f'{0xfeed}, NORMAL')
    def test_check_and_alert_send_to_controller_MED_ACTIVE_COOLING_TOO_LOW(self):    
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'MED_ACTIVE_COOLING', -28)==f'{0xfeed}, TOO_LOW')
    def test_check_and_alert_Send_to_controller_MED_ACTIVE_COOLING_TOO_HIGH(self):       
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'MED_ACTIVE_COOLING', 136)==f'{0xfeed}, TOO_HIGH')
    def test_check_and_alert_send_to_controller_MED_ACTIVE_COOLING_NORMAL(self):       
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'MED_ACTIVE_COOLING',30)==f'{0xfeed}, NORMAL')     
    def test_check_and_alert_send_to_controller_MED_ACTIVE_COOLING_NORMAL(self):       
        self.assertFalse(typewise_alert.check_and_alert('IMPROPER', 'MED_ACTIVE_COOLING',30)==f'{0xfeed}, NOT_APPLICABLE')
        
    def test_send_to_email_TOO_LOW(self):
         self.assertTrue(typewise_alert.send_to_email('TOO_LOW') ==f'To: a.b@c.com, Hi, the temperature is too low')
    def test_send_to_email_TOO_HIGH(self):
        self.assertTrue(typewise_alert.send_to_email('TOO_HIGH') ==f'To: a.b@c.com, Hi, the temperature is too high')  

        
    def test_check_and_alert_send_to_email_PASSIVE_COOLING_TOO_LOW(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING',-5) == f'To: a.b@c.com, Hi, the temperature is too low')
    def test_check_and_alert_send_to_email_PASSIVE_COOLING_TOO_HIGH(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING', 100)==f'To: a.b@c.com, Hi, the temperature is too high')
    def test_check_and_alert_send_to_email_HI_ACTIVE_COOLING_TOO_LOW(self):    
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING',-18)==f'To: a.b@c.com, Hi, the temperature is too low')
    def test_check_and_alert_send_to_email_HI_ACTIVE_COOLING_TOO_HIGH(self): 
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', 260)==f'To: a.b@c.com, Hi, the temperature is too high')
    def test_check_and_alert_send_to_email_MED_ACTIVE_COOLING_TOO_LOW(self):    
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', -28)==f'To: a.b@c.com, Hi, the temperature is too low')
    def test_check_and_alert_send_to_email_MED_ACTIVE_COOLING_TOO_HIGH(self):       
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 136)==f'To: a.b@c.com, Hi, the temperature is too high')   
    def test_check_and_alert_send_to_email_MED_ACTIVE_COOLING_NORMAL(self):       
        self.assertFalse(typewise_alert.check_and_alert('IMPROPER', 'MED_ACTIVE_COOLING',30)==f'To: a.b@c.com, NOT_APPLICABLE')
        
        
if __name__ == '__main__':
  unittest.main()
