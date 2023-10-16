from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# Read test cases from "testCase.inp"
with open("testCase.inp", "r") as f:
    test_cases = [line.strip().split() for line in f]
print(test_cases)
# Read expected outputs from "testCase.outp"
with open("testCase.outp", "r") as f:
    expected_outputs = [line.strip() for line in f]
print(expected_outputs)
# Set up Selenium WebDriver
options = Options()
options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge Dev/Application/msedge.exe"
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get('https://quangtrinh1312.github.io/addition-calculate/')

# Iterate through test cases
for i, test_case in enumerate(test_cases):
    a, b = test_case
    driver.find_element(By.ID, 'a').clear()
    driver.find_element(By.ID, 'b').clear()
    driver.find_element(By.ID, 'a').send_keys(a)
    driver.find_element(By.ID, 'b').send_keys(b)
    driver.find_element(By.ID, 'btn').click()

    result_element = driver.find_element(By.ID, 'result')
    result = result_element.text.replace("Result: ", "")

    # Compare the result with the expected output
    if result == expected_outputs[i]:
        print(f"Test Case {i+1}: Pass")
    else:
        print(f"Test Case {i+1}: Fail")

# Close the web browser
driver.quit()
