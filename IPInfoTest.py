import requests
import json
import random

class IPInfoTest:
    
   def test_response(self):
      response = requests.get("https://ipinfo.io/")
      assert response.status_code == 200, "Expected status code is 200. Received: " + response.status_code
      print ("Test response OK")

   def test_positive_known_ip(self):
      ip = "161.185.160.93"
      response = requests.get("https://ipinfo.io/" + ip)

      dict = {}

      try:
         dict = json.loads(response.text)
      except ValueError:
         print("Error to load response")
         return

      assert dict["ip"] == ip, "Wrong IP received. Expected: " + ip + " Received:" + dict["ip"]
      assert dict["city"] == "New York City", "Wrong city received. Expected: New York City. Received:" + dict["city"]
      assert dict["region"] == "New York", "Wrong region received. Expected: New York. Received:" + dict["region"]
      assert dict["country"] == "US", "Wrong country received. Expected: US. Received:" + dict["country"]
      assert dict["org"] == "AS22252 The City of New York", "Wrong org received. Expected: AS22252 The City of New York. Received:" + dict["org"]
      assert dict["postal"] == "10004", "Wrong postal received. Expected: 10004. Received:" + dict["postal"]
      assert dict["timezone"] == "America/New_York", "Wrong timezone received. Expected: America/New_York. Received:" + dict["timezone"]

      print("Test positive known IP OK")

   def test_negative_ip_large_value(self):
      
      address = "https://ipinfo.io/"
      correct_ip = "161.185.160.93"
      
      #1 illegal section
      for i in range(4):
        
        ip = self.generateRandomIllegalIP(correct_ip, [i])
        
        jResponse = requests.get(address + ip)
        dict = json.loads(jResponse.text)
        
        assert jResponse.status_code == 404, "IP: " + ip + " Should fail with error 404, wrong IP. Received: " + str(jResponse.status_code) 
          
      #2 illegal sections
      for i in range(4):
       for j in range(i, 4):
          if i != j:
            ip = self.generateRandomIllegalIP(correct_ip, [i, j])
            jResponse = requests.get(address + ip)
            assert jResponse.status_code == 404, "IP: " + ip + " Should fail with error 404, wrong IP. Received: " + str(jResponse.status_code) 
    
      #3 illegal sections
      indexes = [0, 1, 2, 3]
      for i in range(4):
        indexes.remove(i)
        ip = self.generateRandomIllegalIP(correct_ip, indexes)
        jResponse = requests.get(address + ip)
        assert jResponse.status_code == 404, "IP: " + ip + " Should fail with error 404, wrong IP. Received: " + str(jResponse.status_code)
        indexes = [0, 1, 2, 3]

      #4 illegal sections
      ip = self.generateRandomIllegalIP(correct_ip, [0, 1, 2, 3])
      jResponse = requests.get(address + ip)
      assert jResponse.status_code == 404, "IP: " + ip + " Should fail with error 404, wrong IP. Received: " + str(jResponse.status_code)

      print("Negative test large numbers OK")

   def generateRandomIllegalIP(self, ip, illegalIndexes):

      newIP = ""
      subIP = ip.split(".")
     
      for i in range(len(illegalIndexes)):
         subIP[illegalIndexes[i]] = str(random.randint(256, 10000))

      #build ip from the list
      newIP = '.'.join(subIP)
      return newIP
   
test = IPInfoTest()

test.test_response()
test.test_positive_known_ip()
test.test_negative_ip_large_value()




    


