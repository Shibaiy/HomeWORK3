from selene import browser, have, be
import os
import variables
import testdata


def test_1(browser_management):
    browser.element(variables.FirstName).type(testdata.FirstName)

    browser.element(variables.LastName).type(testdata.LastName)

    browser.element(variables.Email).type(testdata.Email)

    browser.element(variables.Gender).click()

    browser.element(variables.Mobile).type(testdata.Mobile)

    browser.element(variables.DateofBirth).click()
    browser.element(variables.Month).click()
    browser.element(variables.Year).click()
    browser.element(variables.Day).click()

    browser.driver.execute_script("window.scrollBy(0,500)")

    browser.element(variables.Subjects).click()
    browser.element('#subjectsInput').type('e')
    browser.element('#react-select-2-option-3').click()
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsInput').type('c')
    browser.element('#react-select-2-option-2').click()

    browser.element(variables.Hobbies1).click()
    browser.element(variables.Hobbies3).click()

    fileinput = browser.element(variables.Picture)
    fileinput.send_keys(os.getcwd() + "\img\gomer.png")

    browser.element(variables.CurrentAddress).type(testdata.Address)

    browser.element(variables.State).click()
    browser.element('#react-select-3-option-1').click()
    browser.element(variables.City).click()
    browser.element('#react-select-4-option-2').click()

    browser.element(variables.Submit).click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element("//td[text()='Student Name']/following-sibling::td").should(
        have.text(testdata.FirstName + ' ' + testdata.LastName))
    browser.element("//td[text()='Student Email']/following-sibling::td").should(have.text(testdata.Email))
    browser.element("//td[text()='Gender']/following-sibling::td").should(have.text('Male'))
    browser.element("//td[text()='Mobile']/following-sibling::td").should(have.text(testdata.Mobile))
    browser.element("//td[text()='Date of Birth']/following-sibling::td").should(have.text('10 May,1991'))
    browser.element("//td[text()='Subjects']/following-sibling::td").should(have.text('Commerce, Computer Science'))
    browser.element("//td[text()='Hobbies']/following-sibling::td").should(have.text('Sports, Music'))
    browser.element("//td[text()='Picture']/following-sibling::td").should(have.text('gomer.png'))
    browser.element("//td[text()='Address']/following-sibling::td").should(have.text(testdata.Address))
    browser.element("//td[text()='State and City']/following-sibling::td").should(have.text('Uttar Pradesh Merrut'))
