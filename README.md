### Locator strategy
```
1. login_button = (By.XPATH, "//*[contains(@resource-id,'tv_forgot_password')]/following-sibling::*[position()=1]")
2. login_button = (By.XPATH, "//*[contains(@resource-id,'tv_forgot_password')]/preceding-sibling::*[last()]")
3. login_button = (By.XPATH, "//*[contains(@resource-id,'tv_forgot_password')]/child::*[position()=1]")
4. login_button = (By.XPATH, "//*[contains(@resource-id,'tv_forgot_password')]/parent::*[position()=1]")
5. login_button = (By.XPATH, "//*[starts-with(@resource-id,'tv_')]")
6. login_button = (By.XPATH, "//*[text() = 'Log in')]")
7. login_button = (By.ID, "login_buttonet.Button")
8. error_message = "//*[@name = '{error}']"
```

### Configure ANDROID_HOME and JAVA_HOME
```
1. Windows -> System variable
   1.1 ANDROID_HOME -> C:\Users\YaroslavPetryk\AppData\Local\Android\Sdk
   1.2 JAVA_HOME -> C:\ProgramFiles/Java/jdk-18.0.1.1
2. Windows -> Environment variable
   2.1 Allure -> C:\ProgramFiles/Allure/bin
   2.2 Python -> C:\Users\YaroslavPetryk\AppData\Local\Programs\Python\Python310
   2.3 Python -> C:\Users\YaroslavPetryk\AppData\Local\Programs\Python\Python310\Scripts
3. Mac OS
   3.1 Command + Shift + .
   3.3 .zshrc ->  export ANDROID_HOME=/Users/yaroslav.petryk/Library/Android/sdk
                  export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-19.jdk/Contents/Home
                  export PATH=$ANDROID_HOME/platform-tools:$PATH
                  export PATH=$ANDROID_HOME/tools:$PATH
                  export PATH=$ANDROID_HOME/tools/bin:$PATH
                  export PATH=$ANDROID_HOME/emulator:$PATH
```

### Mac Os -> Create Appium Xcode project
```
1. https://www.youtube.com/watch?v=4E_Dcu6Ifc0
2. /Applications/Appium Server GUI.app/Contents/Resources/app/node_modules/appium/node_modules/appium-webdriveragent
3. XCode project -> WebDriverAgentLib and WebDriverAgentRunner-> Bundle Identifier: facebook -> yourAppleId

```

### Web Driver initialization
```
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def web_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/')
 ```

### Run all tests
```
pytest
```

### Run tests matching given mark expression

```
pytest -m smoke
```


### Run tests by keyword expression
```
pytest -k <KeywordExpression>
```


### Run an Allure report generation
1. Download and extract Allure into the Program Files (https://github.com/allure-framework/allure2/releases/)
2. Add Path in the system variables to the allure bin folder:
   1. Path (C:\Program Files\allure\bin)


```
pytest --alluredir=allure-results
allure serve tests/allure-results
```

