import allure
from allure import step
from selene import browser, by, be


@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("Recently created issue is shown on the page")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'AngPawl')
def test_github_issue_name():
    with step("Open github main page"):
        browser.open('')

    # WHEN
    with step("Insert 'eroshenkoam/allure-example' to the searchbar"):
        browser.element('.search-input').click()
        browser.element('.QueryBuilder-Input').type(
            'eroshenkoam/allure-example'
        ).press_enter()

    with step("Find 'eroshenkoam/allure-example' among search results and open it"):
        browser.element('[data-testid=results-list]').element(
            by.link_text('eroshenkoam/allure-example')
        ).click()

    with step("Open tab Issues"):
        browser.element('#issues-tab').click()

    # THEN
    with step("Issue 'issue_to_test_allure_report' is shown on the page"):
        browser.element(by.text('issue_to_test_allure_report')).should(be.visible)
