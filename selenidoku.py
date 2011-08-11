import sudoku
from selenium import webdriver
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://www.websudoku.com/")
    driver.switch_to_frame(0)
    driver.find_element(By.LINK_TEXT, 'Evil').click()
    driver.switch_to_frame(0)

    while True:
        values = driver.find_elements(By.CSS_SELECTOR, "table.t input")
        grid = ""
        for value in values:
            grid += value.get_attribute('value') or '.'
        solution = sudoku.solve(grid)
        count = 0
        for key in sorted(solution.iterkeys()):
            if not values[count].get_attribute('value'):
                values[count].send_keys(solution[key])
            count += 1
        driver.find_element(By.NAME, "submit").click()
        assert 'Congratulations!' in driver.find_element(By.ID, "message").text
        driver.find_element(By.NAME, "newgame").click()
