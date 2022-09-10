import pandas as pd
from urllib.error import HTTPError, URLError


class TablesScraper:
    def __init__(self) -> None:
        self._results = []

    #helpers
    def _extract_tables(self, src:str, only_visible:bool) -> None:
        """
        scrape all tables and save in self._results

        Params:
            - src: a string can be a URL or a soutce code
            - only_visible: True to scrape only displayed tables, False to scrape hidden tables as well.

        """
        try:
            self._results =  pd.read_html(src, displayed_only=only_visible)
        except ValueError:
            self._results =  []


    def _get_source_code(self, url:str, driver_path:str, show_browser:bool) -> tuple[bool, str]:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.common.exceptions import TimeoutException, InvalidArgumentException

        #setup options
        options = Options()
        #show/hide the browser
        options.headless = not show_browser
        #change the default user-agent
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
        #hide Chrome console output
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #block images
        prefs = {"profile.default_content_setting_values":{
            "images": 2
        }}
        options.experimental_options["prefs"] = prefs

        #setup the driver
        driver = webdriver.Chrome(driver_path, options=options)
        #get the URL
        try:
            driver.get(url)
        except TimeoutException:
            return (False, "Time Out!")
        except InvalidArgumentException:
            return (False, "Invalid URL")

        #close the driver and return the source code
        source_code = driver.page_source
        driver.quit()
        return (True, source_code)



    #main
    def scrape_tables(self, url:str, only_visisble:bool=True, JsMode:bool=False, driver_path:str=None, show_browser:bool=False) -> 'int|str':
        if JsMode:
            if driver_path is None:
                raise ValueError("Browser Driver Path is Not Given!")
            #get source code
            out = self._get_source_code(url, driver_path, show_browser)
            if not out[0]:
                #return the error msg
                return out[1]

            url = out[1]
        
        try:
            self._extract_tables(url, only_visisble)
            return len(self._results)
        except HTTPError as e:
            err = e.getcode()
            if err > 500:
                return f"Server Error: {err}"
            if err > 400:
                return f"Client Error: {err}"
            if err > 300:
                return f"Redirection: {err}"
            if err > 200:
                return f"No HTTP Error: {err}"
            if err > 100:
                return f"No HTTP Error: {err}"
        except URLError:
            return "Invalid URL!"
    