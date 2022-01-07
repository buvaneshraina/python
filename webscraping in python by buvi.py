# Example :retriving html from internet
# to get the html code for the google.com


import urllib.request

def main():
    webUrl=urllib.request.urlopen("http://www.google.com")
    print("resultcode:"+ str(webUrl.getcode()))
    data=webUrl.read()
    print(data)


if __name__=='__main__':
    main()
# result code will be 200  if it has a website