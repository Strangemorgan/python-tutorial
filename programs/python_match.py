http_status = 200

if http_status == 200 or http_status == 201:
    print("success")
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('server Error')
else:
    print('Unknown')
    
http_status = 501

match http_status:
    case 200 | 201:
        print('success')
    case 400:
        print('Bad request')
    case 404:
        print('Not Found')
    case 500 | 501:
        print('Server Error')
    case _:
        print("Unknown")