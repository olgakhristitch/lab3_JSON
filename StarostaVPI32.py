import json

data= {
"Surname": "Khristich",
"Name": "Olga",
"Patronymic" : "Sergeevna",
    "MyAddress": {
    "Street": "Prigorodnii per., h. 21",
     "City": "Rostov-on-Don",
    "PostalCode": 344068
 },
    "PhoneNumbers": [
        "8-928-185-98-50",
        "(863)2-74-57-81"
    ],

"Student": "DSTU",
"Facultet": "Pricladnaya informatica",
"Kurs": "3",
"Group": "VPI32",
"Title": "Starosta",

"Page Vk.com": "http://vk.com/id84736718"

}
with open('StarostaVPI32.json', 'w') as outfile:
    json.dump(data, outfile)