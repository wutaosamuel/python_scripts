import sys
import argparse

from selenium import webdriver

class Buy:
  
  def __init__(self, 
                url=None, 
                username=None, 
                password=None):
    self.HomePage = "https://www.louisvuitton.cn/zhs-cn/homepage"
    self.url = url
    self.username = username
    self.password = password
    self.browser = webdriver.Chrome()
  
  def __call__(self, 
                url=None,
                username=None, 
                password=None):
    self.url = url
    self.username = username
    self.password = password
  
  def exec_main(self, argv):
    self.exec_opt(argv)
    self.Login()
    self.AddCart()

  def exec_opt(self, argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-U", "--url", type=str, help="product url")
    parser.add_argument("-u", "--username", type=str, help="username")
    parser.add_argument("-p", "--password", type=str, help="password")

    args = parser.parse_args(argv)
    print(args.url)
    print(args.username)
    print(args.password)

    if args.url == None or args.username == None or args.password == None:
      parser.print_help()
      print("product url, username and password is required")
      parser.exit(0)

    self.__call__(args.url, args.username, args.password)

  def Login(self):
    self.browser.get(self.HomePage)
    u = self.browser.find_element_by_id("loginmylv-bubbleloginFormmylv-bubble")
    p = self.browser.find_element_by_id("passwordloginFormmylv-bubble")
    b = self.browser.find_element_by_id("fakemylv-bubbleSignIn")
    u.send_keys(self.username)
    p.send_keys(self.password)
    b.click()

  def AddCart(self, url=None):
    if url == None:
      print("please enter url")
      sys.exit(1)
    p_page = self.browser.get(url)
    product = p_page.find_element_by_id("addToCartSubmit")
    product.click()

if __name__ == "__main__":
  buy = Buy()
  buy.exec_main(sys.argv[1:])