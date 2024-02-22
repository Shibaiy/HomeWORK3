from selene import browser, have, be


def test_1(browser_management):
    browser.element('#firstName').should(be.blank).type('Maxim')
    browser.element('#lastName').should(be.blank).type('Shibaev')
    browser.element('#userEmail').should(be.blank).type('test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.all('select.react-datepicker__month-select>option')[4].click()
    browser.element('select.react-datepicker__year-select>option[value="1991"]').click()
    browser.element('div.react-datepicker__week > div[aria-label="Choose Friday, May 10th, 1991"').click()
    browser.driver.execute_script("window.scrollBy(0,500)")
    browser.element('#subjectsContainer').click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    fileinput = browser.element('#uploadPicture')
    fileinput.send_keys('C:/Users/pc/PycharmProjects/HomeWORK3/img/gomer.png')
    browser.element('#currentAddress').type('3-я Брянская улица, 22, деревня Образцово, Орловский муниципальный округ')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').click()
    f