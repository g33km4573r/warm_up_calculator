import pytest


HOME_URL = "https://radiant-stream-4011.herokuapp.com/"

@pytest.mark.webtest
def  test_warm_up_calculator(browser):

    browser.visit(HOME_URL)
    title = browser.find_by_tag("title").first
    assert title.html == "Warm Up Calculator"

    # submit data 
    browser.fill_form({
        "plates": "55,45,44,35,33,25,22,10,5,2.5", 
        "goal": "225"
    })
    browser.find_by_name("submit").first.click()
    assert browser.find_by_id("bar")

    # inspect warm up set
    assert browser.find_by_id("list-group")


