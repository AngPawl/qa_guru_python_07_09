import allure
from selene import browser, by, be


@allure.tag('web')
@allure.severity(severity_level='Critical')
@allure.feature("Issues")
@allure.story("Recently created issue is shown on the page")
@allure.link("https://github.com/", name='Testing')
@allure.label('owner', 'AngPawl')
def test_github_issue_name():
    browser.open('')

    # WHEN
    browser.element('.search-input').click()
    browser.element('.QueryBuilder-Input').type(
        'eroshenkoam/allure-example'
    ).press_enter()

    browser.element('[data-testid=results-list]').element(
        by.link_text('eroshenkoam/allure-example')
    ).click()

    browser.element('#issues-tab').click()

    # THEN
    browser.element(by.text('issue_to_test_allure_report')).should(be.visible)
