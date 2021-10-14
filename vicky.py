import json

a = open ('data.json')
data = json.load(a)

print ('''  selamat datang
vicky aditiya permadi
1. melatih bot
2. berbicara dengan bot
''')

while True:
    input_awal = input ("masukan kode: ")
    if input_awal == "1":
        while True:
            x = input("User\t: ")
            if x  == "keluar":
                break
            else:
                y = input("bot\t: ")
                data[x] = y
                b = open('data.json', "w")
                json.dump(data,b)
                b.close()
    elif input_awal == "2":
        while True:
            x = input ("User\t:" )
            if x == 'keluar':
                break
            if x in data:
                print(f'Bot\t: {data[x]}')                
            else:
                print("bot\t: itu kata yang baru")

    else:
            pass
