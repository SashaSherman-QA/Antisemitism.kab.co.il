from selenium.webdriver.common.by import By


class HomePage:
    section0_strings_from_text = ['אנטישמיות הסיפור האמיתי!' ,'השינוי מתחיל במודעות']
    section0_text_elements_locators = [
        (By.XPATH, r"//div[contains(@class, 'et_pb_section_0')]//p[contains(text(),section0_strings_from_text[0])]"),
        (By.XPATH, r"//div[contains(@class, 'et_pb_section_0')]//p[contains(text(),section0_strings_from_text[1])]")]

    section0_text_elements_locator = (By.XPATH, r"//div[contains(@class, 'et_pb_section_0')]//p")

    section2_strings_from_text = ['איך ייתכן שבשנת 2023','הפתרון לשנאת ישראל', 'כל מה שרציתם לדעת על אנטישמיות']
    # section2_text_elements_locators = [
    #     (By.XPATH, r"//div[contains(@class, 'et_pb_section_2')]//span[contains(text(),section2_strings_from_text[0])]"),
    #     (By.XPATH, r"//div[contains(@class, 'et_pb_section_2')]//span[contains(text(),section2_strings_from_text[1])]")]

    section2_text_elements_locator = [
        (By.XPATH, r"//div[contains(@class, 'et_pb_section_2')]//span")]

    section8_images_single_locator = (By.XPATH, r"//div[contains(@class, 'et_pb_section_8')]//img")
    section8_texts_locator = [(By.XPATH, r"//div[contains(@class, 'et_pb_promo_description')]//p//span")]

    section10_iframe_video_lama_sonim_locator = (By.CSS_SELECTOR, 'iframe[title*="למה שונאים יהודים"]') # iframe


