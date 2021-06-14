import unittest
import HtmlTestRunner
import logging

from reqres.apis import Apis

class TestStringMethods(unittest.TestCase):

    ENDPOINT = "https://rest.iad-03.braze.com"
    APIKEY = "********************************"
    EMAIL = "vashhs@gsy.gh"
    EMAIL_STATUS = "subscribed"
    event = "Bhsj"
    length = 100
    unit = "hour"
    ID = "Dafay"

    @classmethod
    def setUpClass(cls):
        print('test started')

    def test_get(self):
        getApi = Apis()
        resp = getApi.getUnsub(self.ENDPOINT, self.APIKEY, self.EMAIL)
        print('response :: '+str(resp))

    def test_post(self):
        postApi = Apis()
        resp = postApi.postEmailStatus(
            self.ENDPOINT, self.APIKEY, self.EMAIL, self.EMAIL_STATUS) 
        print('response :: '+str(resp))    
        if resp['message'] == 'success':
            print('pass')
        else:
            print('fail')

    def test_get1(self):
        getApi = Apis()
        resp = getApi.cusEveLis(self.ENDPOINT, self.APIKEY)
        print('response :: '+str(resp))
    
    def test_get2(self):
        getApi = Apis()
        resp = getApi.cusEveAnal(self.ENDPOINT, self.APIKEY, self.event, self.length, self.unit)
        print('response :: '+str(resp))
        logging.info(self.APIKEY)
        if resp['message'] == 'success':
            print('pass')
        else:
            print('fail')

    def test_post1(self):
        postApi = Apis()
        resp = postApi.userpro(self.ENDPOINT,self.APIKEY,self.ID)
        print(resp)

    @classmethod
    def tearDownClass(cls):
        print('test ended')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='output'))
