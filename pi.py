import requests
i = 0
while True:
    data = {"city":"3184",
        "country":"2",
        "day":"12",
        "email":"programm" + str(i) + "@gmail.com",
        "lastname":"Одминка",
        "mounth":"05",
        "name":"Тупой",
        "sex":"1",
        "year":"1997"
    }
    r = requests.post("https://ukropen.net/?go=register", data = data);
    #print(r.text)
    if(r.text.split("|")[0].encode() == b'\xef\xbb\xbfemail_verify'):
        print("Emails: " + str(i))
        i += 1
    else:
        print("Error")
