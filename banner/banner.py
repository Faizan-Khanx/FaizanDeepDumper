
class Banner(object):
    def LoadDarkdumpBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''
   .____     .    _  _______      .    __    _                  _______   ___     ___   .    
 /        /|    | '      /     /|    |\   |                  '   /    .'   `. .'   `. /    
 |__.    /  \   |    .--'     /  \   | \  |       .---'          |    |     | |     | |    
 |      /---'\  |   /        /---'\  |  \ |                      |    |     | |     | |    
 /    ,'      \ / ,'______/,'      \ |   \|                      /     `.__.'  `.__.' /---/

 Use This Tool For Educational Purpose Only. 
        Developed By: Faizan Khan
        https://github.com/Faizan-Khanx  
        https://t.me/EthicalFaizan
        https://t.me/SedxJerryHack
    
              '''

            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)