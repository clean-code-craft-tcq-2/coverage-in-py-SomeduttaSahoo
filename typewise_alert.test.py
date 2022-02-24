import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  
  def test_infers_breach_as_high_limits(self):
    self.assertTrue(typewise_alert.infer_breach(110,50, 100)=='TOO_HIGH')
  
  def test_infers_breach_as_normal_limits(self):
    self.assertTrue(typewise_alert.infer_breach(75,50, 100)=='NORMAL')

  def test_classify_temperature_breach_PASSIVE_COOLING_NORMAL(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',30)=='NORMAL')
  
  def test_classify_temperature_breach_PASSIVE_COOLING_HIGH(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',40)=='TOO_HIGH')
  
  def test_classify_temperature_breach_PASSIVE_COOLING_LOW(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',-40)=='TOO_LOW')
  
  def test_send_to_email_High(self):
    self.assertTrue(typewise_alert.send_to_email('TOO_HIGH')=='To: a.b@c.com\nHi, the temperature is too high')
  
  def test_send_to_email_Low(self):
    self.assertTrue(typewise_alert.send_to_email('TOO_LOW') == 'To: a.b@c.com\nHi, the temperature is too low')
  
  def test_send_to_controller_High(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH')==f'{0xfeed}, TOO_HIGH')

  def test_send_to_controller_Low(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_LOW')==f'{0xfeed}, TOO_LOW')
  
  def test_check_and_alert_normal(self):
    self.assertTrue(typewise_alert.check_and_alert('CONTROLLER',{'coolingType':'PASSIVE_COOLING'},30)=="NORMAL")
  
  def test_check_and_alert_low(self):
    self.assertTrue(typewise_alert.check_and_alert('CONTROLLER',{'coolingType':'PASSIVE_COOLING'},-40)==f'{0xfeed}, TOO_LOW')
  
  def test_is_valid_input_true(self):
    self.assertTrue(typewise_alert.is_valid_input('EMAIL',{'coolingType':'PASSIVE_COOLING'})==True)
  
  def test_is_valid_input_false(self):
    self.assertTrue(typewise_alert.is_valid_input('EMAIL',{'coolingType':'PASSIVE_COOLING_1'})==False)
  
  def test_check_and_alert_invalid_input(self):
    self.assertTrue(typewise_alert.check_and_alert('CONTROLLER',{'coolingType':'PASSIVE_COOLING_1'},-40)=='INVALID_INPUT')

  def test_is_available_in_keys_true(self):
    self.assertTrue(typewise_alert.is_available_in_keys('EMAIL',typewise_alert.alert_types)==True)
  
  def test_is_available_in_keys_false(self):
    self.assertTrue(typewise_alert.is_available_in_keys('PASSIVE_COOLING_1',typewise_alert.cooling_types)==False)

if __name__ == '__main__':
  unittest.main()
