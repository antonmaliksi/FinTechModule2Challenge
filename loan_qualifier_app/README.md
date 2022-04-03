# Loan Qualifier Application

We are proud to introduce you to the new Loan Qualifier Application brought to you by Anton Maliksi. In this new version, we have significantly updated the CLI to allow seemless and efficient user-friendly input. From saving a list of their qualifying loans to instnatly updating the organic .csv file, our work continues to blaze a path towards easier manueverability for users with the informational assistance that means the most.

---

## Technologies

In our forward efforts towards efficiency, we have incorporated languages such as Python with libraries including Fire and Questionary to allow lightning-quick data maniuplation across many widely-used platforms and operating systems. Our versioning has made it possible to complete the framework of such integral modularity and functions like saving the user's qualifying loans.

---
---

## Installation Guide

In our ready-to-use application, we have included the following instruction guide:

### Let's begin

1. Open `app.py`, and add `questionary` to the imports list at the top of the file.

2. Instead of coding the file path, Questionary is used to input the location through the CLI. The following steps were taken to make this change:

    * The file path for the `daily_rate_sheet.csv`file was removed from the `load_bank_data()` function call.

    * Inside the `load_bank-data()` function, a Questionary prompt was replaced with the following Questionary prompt: 
        `questionary.text("Enter a file path to a rate-sheet (.csv):").ask()`

        The new function appears as follows:

        ```python
        def load_bank_data():
            csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
            csvpath = Path(csvpath)
            if not csvpath.exists():
                sys.exit(f"Oops! Can't find this path: {csvpath}")
            return load_csv(csvpath)
        ```

3. Open the CLI and run the Loan Qualifier App with the following code:

    ```shell
    python app.py --credit_score=750 --debt=5000 --income=20000
    ```

4. When prompted for the CSV file path, enter `./data/daily_rate_sheet.csv`.

Now we can dynamically set the location of the `daily_rates_sheet.csv` file!

### Retriever the user's loan information

Create a new function called `get_applicant_info()` with the following steps:

1. In `app.py`, in the `run()` function, remove the parameters for `credit_score`, `debt`, and `income`.

2. Remove all of the defined values for `credit_score`, `debt`, `income`,`loan_amount`, and `home_value`, and set all equal to a new function named `get_applicant_info()`.

    ```python
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()
    ```

This function will prompt the user through the CLI for the User's information, then return it so that you can set the values for `credit_score`, `debt`, `income`,`loan_amount`, and `home_value`.

### Retrieve the pertinent loan information

Write a function called `get_applicant_info()` by doing the following:

1. Above the `find_qualifying_loans()` function, define the new `get_applicant_info()` function.

2. Inside `get_applicant_info()`, set the `credit_score` variable using the Questionary `text()` syntax. Repeat this step for the `debt`, `income`, `loan_amount`, and `home_value` variables. Your code should look as follows:

      ```python
      credit_score = questionary.text("What's your credit score?").ask()
      ```

3. Let's change the User's input into the correct data type! Convert the credit score to `integer` and the rest of the values to `float`.

    Below the Questionary variables, convert the variables from strings to numeric values. Use the following syntax as a guide (the remaining variables will be floats):

    ```python
    credit_score = int(credit_score)
    debt = float(debt)
    ```

4. Inside the `get_applicant_info()` function, write the statement that will return all of the variables.

### Run the code

We're all set! All you need to do now is to run your code.

---
---

## Documentation

The following screenshots observe the changes made to the existing code:

### Software Requirements

![Alt text](https://github.com/antonmaliksi/FinTechModule2Challenge/blob/main/loan_qualifier_app/README/fileio.PNG)

### Systems Design

![Alt text](https://github.com/antonmaliksi/FinTechModule2Challenge/blob/main/loan_qualifier_app/README/import_fileio.PNG)

### Usability

![Alt text](https://github.com/antonmaliksi/FinTechModule2Challenge/blob/main/loan_qualifier_app/README/updated_CLI.PNG)

---

## Contributors

We'd like to thank Anton Maliksi for his instrumental impact in the completion of this application. You can contact him via [LinkedIn](https://www.linkedin.com/in/anton-maliksi-074136186/) or through email at antonmaliksi@gmail.com.

---

## License

No licenses were used for this application.