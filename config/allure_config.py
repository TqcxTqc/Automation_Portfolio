from configparser import ConfigParser


def add_allure_env(browser):
    config = ConfigParser()
    config['Environment'] = {
        "Browser": browser.browser.browser_type.name,
        "Browser.Version": browser.browser.version,
    }

    with open("./reports/allure-results/environment.properties", "w") as configFile:
        config.write(configFile)
