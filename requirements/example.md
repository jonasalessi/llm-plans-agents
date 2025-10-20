## Initial Description

The loan application feature must allow customers to apply for different types of loans (personal, mortgage, auto) through a detailed digital form. The form must collect financial information, the purpose of the loan, and collateral options, with fields validated according to the bank’s credit policy. The system must integrate a real-time credit analysis engine and provide the user with a preliminary approval response.

## Who requested or is responsible for this idea?

## Detailed description for the team implementing this requirement

```markdown
# Requirement: Loan Applications

The loan application feature will allow customers to apply for different types of loans, including:

- **Personal loan**
- **Mortgage loan**
- **Auto loan**

This application will be submitted via a **detailed digital form** that must include the following required fields, validated according to the bank’s credit policy:

### 1. Customer Personal Information:
   - Full name
   - CPF
   - Date of birth
   - Full address
   - Contact phone
   - Email

### 2. Financial Information:
   - Monthly income (validate whether the value is within acceptable limits for the selected loan type)
   - Relationship with the bank (current customer, new customer, credit history with the institution)
   - Other financial obligations (ongoing debts, other loans)

### 3. Loan Purpose:
   - Field to select the loan purpose, for example: "Home renovation", "Vehicle purchase", "Debt consolidation", etc.
   - Free-text field for an additional description, if needed.

### 4. Collateral Options (applicable only to certain loan types such as mortgage and auto):
   - Type of collateral (property, vehicle, etc.)
   - Estimated collateral value
   - Collateral details (vehicle plate, property registry number, etc.)
   - Associated documentation (document upload required)

### 5. Loan Details:
   - Requested amount (validate whether the amount is eligible for the selected loan type)
   - Number of installments (according to the options allowed by the institution)
   - Applicable interest rate (calculate according to the loan type and customer profile)

### 6. Form Validations:
   - All required fields must be filled in for submission.
   - Specific validation rules for each field according to the internal credit policy, such as:
     - Validate CPF and email formats
     - Validate minimum and maximum income ranges permitted for the loan type
     - Ensure collateral values are within accepted limits
     - Apply institution-specific credit rules, such as debt-to-income limits (example: committed income cannot exceed 30%).

### Integration with Credit Analysis System:

The system must integrate with the **real-time** credit analysis engine, which:
- Queries the customer’s credit history with credit bureaus (for example, Serasa, SPC, etc.).
- Assesses the customer’s credit risk based on financial data and banking history.
- Returns a **preliminary response** to the user regarding approval or rejection of the loan, considering risk criteria (example: level of indebtedness, offered collateral, credit score).

This preliminary response will be displayed on screen at the end of the form submission, indicating:
- **Preliminary approval**: If the customer is eligible for the loan, showing the amount and suggested terms.
- **Preliminary rejection**: If the customer does not meet the initial requirements, with an explanatory message, where possible (for example, "insufficient income" or "collateral below minimum value").

### Technical Requirements:
- The form must be responsive and accessible on both desktop and mobile.
- The integration with the credit analysis engine must ensure a maximum response latency of 5 seconds.
- All data traffic must be protected with **SSL** and comply with data protection regulations (LGPD).
- Form submission attempts must be logged for auditing and tracing.

### Test Scenarios:
- Verify that the form rejects invalid data (incorrect CPF, income outside allowed ranges, insufficient collateral).
- Simulate different responses from the credit analysis engine (approved, rejected, pending).
- Test different combinations of loan types and collateral, validating correct behavior for each scenario.

```
### Has our understanding been validated?

## Sketches that visualize our understanding of what needs to be done

![loan-flow drawio](https://gist.github.com/user-attachments/assets/2ab1fcb8-73c5-47d7-bd8b-6087377f3897)

### Have the sketches been validated?

Yes

## Specifications for the test scenarios

```gherkin
Feature: Loan Applications

  Background:
    Given the user is authenticated in the system
    And is on the loan application page

  Scenario: Submission of a valid personal loan form
    Given the user selects "Personal loan"
    And fills all required fields correctly
      | name         | cpf            | birth_date | address         | phone       | email                 |
      | João Silva   | 123.456.789-09 | 01/01/1980 | Rua A, 123, SP  | 11999999999 | joao.silva@email.com  |
    And selects "Home renovation" as the loan purpose
    And enters an additional description "Full kitchen renovation"
    And submits the form
    Then a credit analysis request is sent to the system
    And a preliminary approval is received with the loan details

  Scenario: Attempt to submit with an invalid CPF
    Given the user selects "Mortgage loan"
    And fills the CPF field with "123.456.789-00"
    And tries to submit the form
    Then an error message "Invalid CPF" is displayed

  Scenario: Submission with monthly income outside the limits for a mortgage loan
    Given the user selects "Mortgage loan"
    And fills the monthly income field with "R$ 2000"
    And tries to submit the form
    Then an error message "Monthly income below the minimum required for a mortgage loan" is displayed

  Scenario: Submission with insufficient collateral
    Given the user selects "Auto loan"
    And fills the collateral value field with "R$ 15000"
    And tries to submit the form
    Then an error message "Collateral value below the minimum required for auto loans" is displayed

  Scenario: Simulation of a pending response from the credit analysis system
    Given the user fills a valid loan form
    When the credit analysis system returns a response of "pending additional documentation"
    Then a message "Pending: send additional documentation" is displayed on screen

  Scenario: Verification of protected data compliance during submission
    Given the user fills a valid loan form
    When they submit the form
    Then data transmission occurs over a secure connection (SSL)

```

### Have these scenarios been validated?

Yes

## Stories/Tasks derived to implement the requirement

## Step-by-step list for implementing each story

