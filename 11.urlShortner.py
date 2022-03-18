import bitly_api
 
API_USER = "jackychan123456"
API_KEY = "Thisispokhpass"
bitly = bitly_api.Connection(API_USER, API_KEY)
 
userUrl=input("Insert the URL you want to shorten: ")
response = bitly.shorten(userUrl)
 
# Now let us print the Bitly URL
print(response)