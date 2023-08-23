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
    open_default_browser_page()

    # WHEN
    search_for_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issues_tab()

    # THEN
    assert_issue_name_is_present('issue_to_test_allure_report')


@step("Open github main page")
def open_default_browser_page():
    browser.open('')


@step("Insert {repo} to the searchbar")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('.QueryBuilder-Input').type(repo).press_enter()


@step("Find {repo} among search results and open it")
def open_repository(repo):
    browser.element('[data-testid=results-list]').element(by.link_text(repo)).click()


@step("Open tab Issues")
def open_issues_tab():
    browser.element('#issues-tab').click()


@step("Issue {issue} is shown on the page")
def assert_issue_name_is_present(issue):
    browser.element(by.text(issue)).should(be.visible)
