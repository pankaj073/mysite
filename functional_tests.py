from selenium import webdriver
browser = webdriver.PhantomJS();
browser.get('http://localhost:8000')
assert 'Polls' in browser.title, "Browser title was " + browser.title
browser.quit()