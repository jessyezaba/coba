from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

data = [
    {'user': 'idleworks@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0xaa40e8032cbe85e1c99db9181aabd052f77b22a9'},
    {'user': 'sonja0922@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x85f2d7b9d89d0b2e6b82b405ddd11d54bd4d3445'},
    {'user': 'gaojin9907@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x88736994773c789f590fda28786f708b7009acd5'},
    {'user': 'jpuijenbroek@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0x5fbdf8c7b273dd552f06dd8d5b98a309d8d4fdce'},
    {'user': 'tninusyautab1187j@gasss.net', 'password': '@@Masuk123#oZ', 'wallet': '0xd16eb756966c888c12f9cad63b25803dba95fed9'},


]

for idx, line in enumerate(data, start=1):  # Menambahkan fungsi enumerate untuk melacak nomor akun
    try:
        web = web_driver()
        user = line['user']
        password = line['password']
        wallet_address = line['wallet']

        # LOGIN
        web.get('https://dashboard.alchemy.com/signup?a=arbitrum_faucet&redirectUrl=https%3A%2F%2Fwww.alchemy.com%2Ffaucets%2Farbitrum-sepolia%3FauthRefresh%3DTrue')
        time.sleep(3)

        web.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[2]/form/label[1]/input').send_keys(user)
        time.sleep(2)

        web.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[2]/form/label[2]/input').send_keys(password)
        time.sleep(2)

        web.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[2]/form/button').click()
        time.sleep(7)

       
        # END LOGIN

       

        def claim_arbit_sepolia(web, wallet, max_attempts=4):
            attempt = 0
            
            while attempt < max_attempts:
                try:
                    # ARBIT SEPOLIA
                    web.get('https://www.alchemy.com/faucets/arbitrum-sepolia')
                    time.sleep(2)

                    web.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/span/form/div/div[1]/input').send_keys(wallet)
                    time.sleep(3)

                    web.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/span/form/div/div[2]/button/div/span').click()
                    time.sleep(4)

                    element = WebDriverWait(web, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div[2]'))
                    )
                    print(f"Akun ke-{idx}: BERHASIL CLAIM ARBIT !! .")
                    break  # Keluar dari loop jika klaim berhasil dilakukan

                except:
                    
                    attempt += 1  # Tambah jumlah percobaan

                    if attempt == max_attempts:
                        try:
                            si_eror = web.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[3]/div/span')
                            pesan = si_eror.text
                            print(f"Akun ke-{idx}: GAGAL CLAIM ARBIT  - {pesan} ")
                                
                        except:
                            print(f"Akun ke-{idx}: GAGAL CLAIM ARBIT .")

     

       
        claim_arbit_sepolia(web, wallet_address)
       

        time.sleep(1)
        with open('result.txt', "a") as f:
            f.write(user+'\n')
        time.sleep(1)

        web.close()
        
    except:
        print(f"Akun ke-{idx}: TERJADI ERROR")
        web.close()
