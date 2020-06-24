class RandomFileGenerator: 
    first_name =['Asha',
     'Leonore',
     'Elois',
     'Alexia',
     'Debby',
     'Ofelia',
     'Zoraida',
     'Yuki',
     'Stephanie',
     'Kylee',
     'Dell',
     'Angelita',
     'Marlen',
     'Cammy',
     'Melinda',
     'Brooke',
     'Zana',
     'Adolfo',
     'Mee',
     'Charlyn',
     'Lovella',
     'Keri',
     'Francoise',
     'Salvatore',
     'Lesia',
     'Moriah',
     'Dann',
     'Olympia',
     'Anitra',
     'Vito',
     'Gabriela',
     'Bethel',
     'Cathie',
     'Latarsha',
     'Brian',
     'Clemencia',
     'Hisako',
     'Dovie',
     'Sheena',
     'Becky',
     'Latonya',
     'Janene',
     'Nova',
     'Awilda',
     'Britt',
     'Rena',
     'Detra',
     'Melina',
     'Latrina',
     'Beata']


    last_name = ['Buell',
     'Glen',
     'Pidgeon',
     'Bushong',
     'Cockrell',
     'Hoeppner',
     'Puterbaugh',
     'Raimondi',
     'Fobbs',
     'Hirth',
     'Hicklin',
     'Ritter',
     'Keithley',
     'Woodford',
     'Nagle',
     'Welle',
     'Easler',
     'Rotter',
     'Destefano',
     'Billing',
     'Adcock',
     'Haggard',
     'Seekins',
     'Hadden',
     'Noles',
     'Rockmore',
     'Henegar',
     'Beale',
     'China',
     'Grube',
     'Malchow',
     'Sok',
     'Mciver',
     'Caiazzo',
     'Tores',
     'Talley',
     'Gossage',
     'Whitton',
     'Courtemanche',
     'Dancy',
     'Nevitt',
     'Christon',
     'Gayhart',
     'Mcnamee',
     'Seaman',
     'Berkeley',
     'Luckett',
     'Lucus',
     'Volkman',
     'Volkert']

    address = ["Springfield Road",
    "LIVERPOOL",
    "L3 1MY",
    "Park Road",
    "SWANSEA",
    "SA76 8MY",
    "The Crescent",
    "EAST CENTRAL LONDON",
    "EC90 8TP",
    "New Road",
    "HEMEL HEMPSTEAD",
    "HP14 6ME",
    "Windsor Road",
    "DUNDEE",
    "DD13 5SW",
    "Grove Road",
    "ENFIELD",
    "EN42 1ZL",
    "Church Lane",
    "PORTSMOUTH",
    "PO92 2XY",
    "Alexander Road",
    "CARDIFF",
    "CF64 6VI",
    "Church Road",
    "SOUTHEND-ON-SEA",
    "SS5 3TU",
    "Stanley Road",
    "KILMARNOCK",
    "KA78 5OP",
    "The Green",
    "INVERNESS",
    "IV97 4FQ",
    "Church Street",
    "HALIFAX",
    "HX89 5AR",
    "Kings Road",
    "LINCOLN",
    "LN97 1ZM",
    "Queensway",
    "CAMBRIDGE",
    "CB22 5QM",
    "South Street",
    "EDINBURGH",
    "EH15 7AV",
    "Victoria Street",
    "SALISBURY",
    "SP74 2PI",
    "London Road",
    "BRIGHTON",
    "BN41 3LF",
    "Main Road",
    "BELFAST",
    "BT35 4GK",
    "The Drive",
    "MILTON KEYNES",
    "MK36 5JZ",
    "St. John’s Road",
    "GLASGOW",
    "G29 5MU",
    "Green Lane",
    "PETERBOROUGH",
    "PE9 7AN",
    "North Road",
    "CANTERBURY",
    "CT74 2WZ",
    "North Street",
    "TUNBRIDGE WELLS",
    "TN7 9VI",
    "Victoria Road",
    "DERBY",
    "DE3 5FK",
    "West Street",
    "ROMFORD",
    "RM40 2KO",
    "Manor Road",
    "BATH",
    "BA37 4KD",
    "King Street",
    "HULL",
    "HU81 9KO",
    "High Street",
    "OUTER HEBRIDES",
    "HS75 1OC",
    "Richmond Road",
    "WORCESTER",
    "WR14 0NC",
    "New Street",
    "SOUTHALL",
    "UB82 8GV",
    "Park Lane",
    "ABERDEEN",
    "AB1 7JU",
    "Mill Road",
    "WARRINGTON",
    "WA40 9ZD",
    "Albert Road",
    "BOLTON",
    "BL74 5CH",
    "Queen Street",
    "SUTTON",
    "SM99 6ZS",
    "York Road",
    "WESTERN CENTRAL LONDON",
    "WC27 0ZU",
    "The Grove",
    "BLACKPOOL",
    "FY23 1TH",
    "Station Road",
    "DARLINGTON",
    "DL10 4YZ",
    "George Street",
    "BRADFORD",
    "BD63 9FY",
    "Chester Road",
    "NEWPORT",
    "NP29 7WY",
    "Broadway",
    "BIRMINGHAM",
    "B27 0ZP",
    "Grange Road",
    "HARROW",
    "HA95 5XQ",
    "Kingsway",
    "BROMLEY",
    "BR96 9OR",
    "Manchester Road",
    "DUDLEY",
    "DY12 6GU",
    "School Lane",
    "CHESTER",
    "CH19 4MS",
    "Park Avenue",
    "LEICESTER",
    "LE82 8KU",
    "Queens Road",
    "ST ALBANS",
    "AL61 3WC",
    "Mill Lane",
    "CARLISLE",
    "CA79 9XR",
    "Main Street",
    "PRESTON",
    "PR11 6AW",
    "The Avenue",
    "WIGAN",
    "WN4 5PR",
    "Highfield Road",
    "LUTON",
    "LU97 6TN"]
    domain = ['gmail', 'yahoo', 'outlook', 'icloud' ,'realDomain' , 'duckduckgo', 'ourLife' , 'testEmail']

    supported_format = ['csv' , 'txt' , 'json' , 'pickle']
    def random_generator(size, file_name , export_format ):


        '''LIST FOR CREATING THE DATAFRAME'''
        first_list = []
        last_list = []
        full_name_list = []
        age_list = []
        dmain_list = []
        email_list = []
        street_path_list = []
        addr_list = []
        zipcode_list = []
        phone_list = []

        '''TAKES THE SIZE FOR THE FUNCTION'''
        for i in range(size):

            '''FIRST NAME '''
            first = random.choice(first_name)
            first_list.append(first)

            '''LAST NAME'''
            last = random.choice(last_name)
            last_list.append(last)

            '''FULL NAME'''
            full_name = f'{first} {last}'
            full_name_list.append(full_name)

            '''ADDRESS'''
            addr = random.choice(address)

            '''AGE'''
            age = random.randint(18,90)
            age_list.append(age)

            '''DOMAIN'''
            dmain = random.choice(domain)
            dmain_list.append(dmain)

            '''EMAIL'''
            email = f'{first.lower()}.{last.lower()}{random.randint(0,522)}@{dmain}.com'
            email_list.append(email)

            '''STREET PATH'''
            street_path = random.randint(1,125)
            street_path_list.append(street_path)

            '''ADDRESS'''
            addr = f'#{street_path} {addr}'
            addr_list.append(addr)

            '''ZIPCODE'''
            zipcode = random.randint(300000,700000)
            zipcode_list.append(zipcode)

            '''PHONE'''
            phone = f'{random.randint(7100,9100)}{random.randint(100000 , 999999)}'
            phone_list.append(phone)

        '''COLUMN NAMES AND ITS VALUES'''
        columns = ['first_name', 'last_name', 'full_name', 'age', 'email' , 'address','zipcode', 'phone']
        list_values = [first_list, last_list, full_name_list, age_list,  email_list,  addr_list, zipcode_list, phone_list]


        df = pd.DataFrame(dict(zip(columns, list_values)))
        if export_format in supported_format and isinstance(size,int):
            print("Supported Format Detected!")
            for formatted in supported_format:
                if export_format == formatted:
                    eval("df.to_{0}('{1}.{0}', index = False)".format(export_format, file_name))
                    '''EXPORTING THE FILE LOGIC FOR ALL THE FORMATS'''

                    print(f"Successfully Exported Format : {export_format} File Name : {file_name}")
        else:
             raise Exception(
                 f""" Exception occured while passing the function.You passed "{export_format}""
                 Please check if the format is {supported_format}""")


        
'''
FUNCTION random_generator(number_of_rows : int, Name_of_the_file : str, Format_of_the_file : str)'''

'''
EXAMPLE : random_generator(1000, "test123" , "csv")
'''

RandomFileGenerator.random_generator(1000, "test6" ,"csv")
