import asyncio
import pyppeteer
import json
import time
import os

  # Gle88
  # Senha: leleu10a

  # leandro_1171@hotmail.com
  # Leleu10@

  # 739fb6774973746771da4e9cf35dcff5



url_ = "https://www.fieltorcedor.com.br/jogos/corinthians-x-santos-pf24/categoria/"

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

async def main():
  global url_page
  
  url_page = None
    
  caminho_absoluto = os.path.abspath("2SOLVER")
  
  caminho_chrome = achar_caminho_chrome()

  browser = await pyppeteer.launch(headless=False, args=['--no-sandbox', '--disable-setuid-sandbox', f'--disable-extensions-except={caminho_absoluto}', f'--load-extension={caminho_absoluto}'],  executablePath=rf"{caminho_chrome}")

  page = await browser.newPage()
  # await page.setCookie(*c)
  while True:
    try:
        
      await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
      PageHtml = await page.goto(f'{url_}')
      
      print("PAGE STATUS: ", PageHtml.status)
      
      while PageHtml.status != 200:
        PageHtml = await page.goto(f'{url_}')
        await page.waitFor(5000)
      # print(str(PageHtml.request.url))
      

      while "auth" in str(PageHtml.url):
        
        PageHtml =  await page.goto(f'{url_}')
        await page.waitFor(6000)
        
        await page.type("#id_username", "Gle88")
        await page.type("#id_password", "leleu10a")
        
        url_page =  str(PageHtml.url)
        print("Acessando URL:", url_page)
      
        print("Nao logado...")      
        await page.waitFor(25000)      
        btn = await page.xpath('//*[@id="main"]/div/div/div/div/form/button')
        
        if btn:
          # print(btn[0:])
          await btn[0].click()
          url_page = str(PageHtml.request.url)
          continue
        else:
          url_page = str(PageHtml.request.url)
          coockies_sid = await page.cookies()
          # gravar_em_arquivo(coockies_sid)        
        continue
        # coockies_s = [ [val['name'], val['value']] for val in coockies_sid]
              
        # cSid = coockies_s[1][1] 
        # csrf = coockies_s[2][1]
        
        # await page.waitFor(15000)

      print("Logado...")
      print("Apartir desse ponto o site vai ficar atualizando sozinho..."+'\n')
      
      while str(PageHtml.url) == url_:
            await page.goto(f'{url_}')
            await page.waitFor(10000)
            print("Procurando cadeiras...")
            html = await page.content()
            # print(html)
      else:
        pass
    
    except Exception as err:
      print(err)
     # await browser.close()
      # exit(0)
      pass
    
    except KeyboardInterrupt:
      await browser.close()
      exit(0)
      

    
  


asyncio.run(main())