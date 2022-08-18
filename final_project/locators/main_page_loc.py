from selenium.webdriver.common.by import By


class MainPageLoc:

    main_page_url_loc = 'http://localhost/litecart/en/'

    change_button_loc = (By.XPATH, '//a[@class="fancybox-region"]')

    rs_currency_field_loc = (By.XPATH, '//select[@name="currency_code"]')
    rs_currency_eur_loc = (By.CSS_SELECTOR, '[value="EUR"]')
    rs_country_field_loc = (By.XPATH, '//select[@name="country_code"]')
    rs_country_zimbabwe_loc = (By.CSS_SELECTOR, '[value="ZW"]')
    rs_save_button_loc = (By.XPATH, '//button[@value="Save"]')

    current_currency_loc = (By.XPATH, '//div[@class="currency"]//span')
    current_country_loc = (By.XPATH, '//div[@class="country"]')

    email_address_field_loc = (By.XPATH, '//input[@name="email"]')
    password_field_loc = (By.XPATH, '//input[@name="password"]')
    remember_me_checkbox_loc = (By.XPATH, '//input[@name="remember_me"]')
    login_button_loc = (By. XPATH, '//button[@name="login"]')
    customer_logged_in_loc = (By.XPATH, '//div[@class="notice success"]')

    blue_duck_loc = (By.XPATH, '//img[@alt="Blue Duck"]')
    green_duck_loc = (By.XPATH, '//img[@alt="Green Duck"]')
    purple_duck_loc = (By.XPATH, '//img[@alt="Purple Duck"]')

    cart_loc = (By.XPATH, '//div[@id="cart"]//child::a[3]')
    quantity_of_goods_at_cart_loc = (By.XPATH, '//div[@id="cart"]//span[@class="quantity"]')

    edit_account_link_loc = (By.XPATH, '//a[@href="http://localhost/litecart/en/edit_account"]')




