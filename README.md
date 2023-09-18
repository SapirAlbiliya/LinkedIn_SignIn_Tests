
# QA Automation Project: LinkedIn Web Testing

Welcome to the repository for the QA Automation Project, focusing on automated testing for LinkedIn's sign-in functionality.

## Overview

This project is an embodiment of skills and efforts to automate web testing scenarios using Python and Selenium. The primary aim was to validate LinkedIn's sign-in functionality under various scenarios to ensure robustness and reliability.

## Features

- Utilizes **Selenium**, a leading web automation framework.
- Crafted with modular design, integrating helper functions to enhance the DRY principle.
- Robust test scenarios:
  - Successful sign-in with valid credentials.
  - Handling sign-ins with incorrect usernames.
  - Handling sign-ins with incorrect passwords.
- Dynamic logging with timestamps for traceability.
- Comprehensive error handling.
- Screenshot capturing for visual documentation of test outcomes.
- Adherence to the Page Object Model (POM) principle.

## Getting Started

### Prerequisites

- Python 3.x
- Selenium
- WebDriver for Chrome (or your browser of choice)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/SapirAlbiliya/LinkedIn_SignIn_Tests.git
   ```

2. Navigate to the project directory:

   ```bash
   cd <current_path>/LinkedIn_SignIn_Tests
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Update the configurations in `config.py` (if any).

### Running the Tests

To run the tests, simply execute:

```bash
python3 tests.py
```

## Reporting

All test outcomes are logged dynamically, with timestamps for easy traceability. Screenshots are captured to provide a visual documentation of test results.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
