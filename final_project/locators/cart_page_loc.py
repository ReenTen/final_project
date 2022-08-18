from selenium.webdriver.common.by import By


class CartPageLoc:

    cart_page_url_loc = 'http://localhost/litecart/en/checkout'

    blue_duck_price_loc = (By.XPATH, '//li[@class="item"][1]//form/div[1]/p[2]')
    green_duck_price_loc = (By.XPATH, '//li[@class="item"][2]//form/div[1]/p[2]')
    purple_duck_price_loc = (By.XPATH, '//li[@class="item"][3]//form/div[1]/p[2]')

    amount_field_loc = (By.XPATH, '//input[@name="quantity"]')
    update_button_loc = (By.XPATH, '//button[@value="Update"]')
    remove_button_loc = (By.XPATH, '//button[@name="remove_cart_item"]')

    remove_message_loc = (By.XPATH, '//div[@id="checkout-cart-wrapper"]//child::p[1]//em')

    os_blue_duck_quantity_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[2]/td[1]')
    os_green_duck_quantity_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[3]/td[1]')
    os_purple_duck_quantity_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[4]/td[1]')

    os_blue_duck_unit_cost_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[2]/td[4]')
    os_green_duck_unit_cost_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[3]/td[4]')
    os_purple_duck_unit_cost_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[4]/td[4]')

    os_blue_duck_total_price_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[2]/td[6]')
    os_green_duck_total_price_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[3]/td[6]')
    os_purple_duck_total_price_loc = (By.XPATH, '//*[contains(@class,"dataTable rounded-corners")]//tr[4]/td[6]')

    os_payment_due_loc = (By.XPATH, '//tr[@class="footer"]//child::td[2]//strong')

    confirm_order_button = (By.XPATH, '//button[@name="confirm_order"]')
    order_success_message = (By.XPATH, '//div[@id="box-order-success"]/h1')