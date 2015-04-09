import pytest


HOME_URL = "https://radiant-stream-4011.herokuapp.com/"

@pytest.mark.webtest
def  test_warm_up_calculator(browser):

    browser.visit(HOME_URL)
    title = browser.find_by_tag("title").first
    assert title.html == "Warm Up Calculator"

    # submit data 
    browser.fill_form({"plates": "20x5", "goal": "100"})
    browser.find_by_name("submit").first.click()

    # view results
    # second_goal = browser.find_by_id("warm-up-goal-2").first()
    # assert second_goal.html == "40"

    # second_warm_up_set = browser.find_by_id("warm-up-set-2").first()
    # assert second_warm_up_set.html == "20, 20"
