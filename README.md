# FacebookPokesBot
 A Python Bot for poking friends on Facebook
# Installation and configuration
1. Download and install latest Google Chrome or Chromium Browser
2. Run installed browser, configure it, login to Facebook Account and then exit browser (Don't log out of Facebook!)
3. Download and install latest chromedriver executable for your system
4. Install selenium package using pip installer
5. Configure bot by editing FacebookPokesBot.ini file:
    * DRIVER_PATH - path to your chromedriver executable
    * PROFILE_PATH - path to chrome userdata directory
    * TIMEOUT - how often the program should scan the website for pokes (seconds)
    * FACEBOOK_POKE_BUTTON_TEXT - a text displayed on poke button on your facebook for example "Poke back" or "Odpowiedz na zaczepkę"
6. Run a bot using terminal window
7. Enjoy
# Important notes
* Bot reloads the page every 3 minutes
* FOR LINUX USERS: This bot cannot be run using SSH
