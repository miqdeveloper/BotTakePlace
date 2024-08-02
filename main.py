import asyncio
import pyppeteer
import json
import time
import os

global path_user
global f_link

  # Gle88
  # Benja88
  # Senha: leleu10a

  # leandro_1171@hotmail.com
  # Leleu10@

  # 739fb6774973746771da4e9cf35dcff5
  
  # https://www.fieltorcedor.com.br/jogos/corinthians-x-sao-paulo-br24/setor/sul/
  # https://www.fieltorcedor.com.br/jogos/corinthians-x-cuiaba-br24/setor/leste-inferior-central/modo-de-compra/

name = "Benja88"
passwd  = "leleu10a"

#Mude o link_ para reservar o lugar 
link_ = "/sul"

#Mude o local da pasta - o local onde a sessao do chrome sera aberta e mantida
path_user = r"C:\Users\Miqueias\AppData\Local\Google\Chrome\User Data\Profile 1"

f_link = None

url_base = "https://www.fieltorcedor.com.br/"

# Mude o link do jogo para rodar o bot copie o link ate /categoria/  Ex: "https://www.fieltorcedor.com.br/jogos/corinthians-x-juventude-br24/categoria/"
url_ = "https://www.fieltorcedor.com.br/jogos/corinthians-x-juventude-br24/categoria/"

os.system("taskkill /f /im chrome.exe /T")


def ler_primeira_linha(nome_arquivo):
  with open(nome_arquivo, 'r') as arquivo:
      fin = arquivo.readline()
      # fin = json.loads(primeira_linha)
      return fin
    
def gravar_em_arquivo(arg1, nome_arquivo='cookies.txt'):
      with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(str(arg1))

def achar_caminho_chrome():
  
  
  
      discos = ['C:', 'D:', 'E:', 'F:', 'G:']
      caminhos_possiveis = [
          '\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
          '\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
      ]

      for disco in discos:
          for caminho in caminhos_possiveis:
              caminho_completo = os.path.join(disco, caminho)
              if os.path.exists(caminho_completo) and os.path.isfile(caminho_completo):
                  return caminho_completo

      return None

c = [{'name': '_ga_W3SFVJMNDD', 'value': 'GS1.1.1717682884.1.1.1717682894.0.0.0', 'domain': '.fieltorcedor.com.br', 'path': '/', 'expires': 1752242894.982901, 'size': 51, 'httpOnly': False, 'secure': False, 'session': False, 'priority': 'Medium', 'sameParty': False, 'sourceScheme': 'Secure', 'sourcePort': 443}, {'name': '_ga', 'value': 'GA1.1.487169462.1717682884', 'domain': '.fieltorcedor.com.br', 'path': '/', 'expires': 1752242884.20839, 'size': 29, 'httpOnly': False, 'secure': False, 'session': False, 'priority': 'Medium', 'sameParty': False, 'sourceScheme': 'Secure', 'sourcePort': 443}, {'name': 'corinthians-csrf', 'value': 'GbuX1FcD0D3Kz2naQICYpI5fL58fheGr', 'domain': 'www.fieltorcedor.com.br', 'path': '/', 'expires': 1749132494.816368, 'size': 48, 'httpOnly': True, 'secure': False, 'session': False, 'sameSite': 'Lax', 'priority': 'Medium', 'sameParty': False, 'sourceScheme': 'Secure', 'sourcePort': 443}]
# print(type(c))
# cookie_f = ler_primeira_linha("cookies.txt")
# print(json.loads(cookie_f))

def ler_arquivo_txt(nome_arquivo):
  
  f_link = None
  try:
      with open(nome_arquivo, 'r') as arquivo:
          linhas = arquivo.readlines()
          lista_linhas = [linha.strip().split(',') for linha in linhas]
          # print(lista_linhas)
          for line in lista_linhas:
            if "<a xlink:href=" and link_ in  str(line[0]):
              f_link = url_base+(line[0].replace("<a xlink:href=", "").replace("""">""", "").replace(""" " """, "" ).replace(""""/""", ""))
              
          return f_link
  except FileNotFoundError:
      print(f"Arquivo '{nome_arquivo}' não encontrado.")
      return None
    
async def main():
  while True:
    try:

      global f_link
      global url_page
      # global browser
      
      url_page = None

      caminho_absoluto = os.path.abspath("2SOLVER")
      
      caminho_chrome = achar_caminho_chrome()

      browser = await pyppeteer.launch(headless=False, args=['--no-sandbox', 
                                                            '--disable-setuid-sandbox',
                                                            f"--user-data-dir={path_user}", 
                                                              f'--disable-extensions-except={caminho_absoluto}', 
                                                              f'--load-extension={caminho_absoluto}',
                                                            
                                                            ],                                     
                                                              executablePath=rf"{caminho_chrome}")

      page = await browser.newPage()
      # await page.setCookie(*c)

      # await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
      PageHtml = await page.goto(f'{url_}')
      
      print("PAGE STATUS: ", PageHtml.status)
      pg_url = str(PageHtml.url)
      
      # while PageHtml.status != 200:
      #   PageHtml = await page.goto(f'{url_}')
      #   await page.waitFor(3000)
      # print(str(PageHtml.request.url))
      
      if "auth" in pg_url:

        # await browser.close()
        # os.system("taskkill /f /im chrome.exe /T")
        # time.sleep(3)       

        # browser = await pyppeteer.launch(headless=False, args=['--no-sandbox', 
        #                                             '--disable-setuid-sandbox',
        #                                             f"--user-data-dir={path_user}", 
        #                                               f'--disable-extensions-except={caminho_absoluto}', 
        #                                               f'--load-extension={caminho_absoluto}',
                                                    
        #                                             ],                                     
        #                                               executablePath=rf"{caminho_chrome}")

        while "auth" in pg_url:
          
          PageHtml =  await page.goto(f'{url_}')
          await page.waitFor(1000)
          
          await page.type("#id_username", name)
          await page.type("#id_password", passwd)
          
          url_page =  str(PageHtml.url)
          print("Acessando URL:", url_page)
          
        
          print("Nao logado...")      
          await page.waitFor(28000)      
          btn = await page.xpath('//*[@id="main"]/div/div/div/div/form/button')
          
          if btn:
            # print(btn[0:])
            await btn[0].click()

          PageHtml = await page.goto(url_)
          pg_url = str(PageHtml.url)
          
          # await browser.close()
          # os.system("taskkill /f /im chrome.exe /T")

          # browser = await pyppeteer.launch(headless=True, args=['--no-sandbox', 
          #                                           '--disable-setuid-sandbox',
          #                                           f"--user-data-dir={path_user}", 
          #                                             f'--disable-extensions-except={caminho_absoluto}', 
          #                                             f'--load-extension={caminho_absoluto}',
                                                    
          #                                           ],                                     
          #                                             executablePath=rf"{caminho_chrome}")
          
          continue

          #   url_page = str(PageHtml.request.url)
          #   coockies_sid = await page.cookies()
          #   pass

            # gravar_em_arquivo(coockies_sid)        
          # continue
            # coockies_s = [ [val['name'], val['value']] for val in coockies_sid]
                  
            # cSid = coockies_s[1][1] 
            # csrf = coockies_s[2][1]
            
            # await page.waitFor(15000)

      print("Logado...")
      
      print("Apartir desse ponto o site vai ficar atualizando sozinho..."+'\n')
      await page.goto(f'{url_}')
      
      # while str(PageHtml.url) == url_:
      #   print(" Ok")
      # await page.goto(f'{url_t}')

      await page.waitForXPath("//p[@class='btn btn-link']")
      
      elem_= await page.xpath("//p[@class='btn btn-link']")
      await elem_[0].click()
      await page.waitFor(1000)

      # await page.evaluate("allow pasting", force_expr=True)
      current_url = await page.evaluate('window.location.href', force_expr=True)
      set_c = str(current_url)
      # print(set_c)
      # await page.waitFor(200000)
      # await browser.close()
        
        # setores_ = await page.goto(set_c)
      setor_select = None
      while not setor_select:
        print("Procurando cadeiras...")
        await page.goto(set_c)

        await page.waitFor(1000)
        
        html = await page.content()

        try:
          with open("log.txt", 'w') as file:
              file.writelines(html)
              file.close()
        except Exception as err:
          # print("erro ao grava")
          pass
        
        setor_select = ler_arquivo_txt("log.txt")
        print("setor", setor_select)

        if setor_select:

            await page.goto(setor_select)
            await page.waitForXPath("//button[contains(@class,'btn btn-primary')]")
            # print(x_)
            elm_ = await page.xpath("//button[contains(@class,'btn btn-primary')]")
            # await elem_[0].click()
            await elm_[0].click()
            await page.waitFor(3000)

            await page.waitForXPath("//div[@class='form-check']")
            # elm_b = await page.xpath("//h4[text()='LUCCA APARÍCIO']")
            await page.evaluate("""
                            function marcarCheckBoxesDisponiveis() {
                                const checkboxes = document.querySelectorAll('input[type="checkbox"]:not(:checked)');
                              
                                for (const checkbox of checkboxes) {
                                  checkbox.checked = true;
                                }
                            };marcarCheckBoxesDisponiveis();document.getElementById("submit_fieltorcedor_booking_by_dependente_form").disabled = false;
""", force_expr=True)
            # await page.waitFor(9999999)
            # await browser.close()
            # await elm_b[0].click()
            await page.waitFor(2000)
            elm_c = await page.xpath("//button[contains(@class,'btn btn-primary')]")
            await elm_c[0].click()

            await page.waitFor(200)
            await browser.close()
            os.system("taskkill /f /im chrome.exe /T")
            break
      # exit()

    except Exception as err:
      await browser.close()
      os.system("taskkill /f /im chrome.exe /T")
      print(err)
      
    
    
    except KeyboardInterrupt:
      os.system("taskkill /f /im chrome.exe /T")
      await browser.close()
      exit(0)
      break

    continue



  # print(ler_arquivo_txt("log.txt"))

asyncio.run(main())