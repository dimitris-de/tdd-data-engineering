# Test-Driven Development (TDD) in Data Engineering with Python

Welcome to this hands-on lab designed to equip data engineers with practical experience in Test-Driven Development (TDD) using Python. This lab covers fundamental and advanced topics, tailored specifically for data engineering.

## Table of Contents

1. [Introduction to TDD and Its Importance in Data Engineering](#1-introduction-to-tdd-and-its-importance-in-data-engineering)
2. [Use Cases Specific to Data Engineering](#2-use-cases-specific-to-data-engineering)
   - [Data Ingestion Pipelines](#data-ingestion-pipelines)
   - [Data Transformation and Cleaning](#data-transformation-and-cleaning)
   - [ETL Processes](#etl-processes)
3. [Edge Cases Handling](#3-edge-cases-handling)
   - [Corrupt or Malformed Data](#corrupt-or-malformed-data)
   - [Missing or Null Values](#missing-or-null-values)
   - [Schema Changes](#schema-changes)
   - [Unexpected Data Formats](#unexpected-data-formats)
4. [Popular TDD Frameworks in Python](#4-popular-tdd-frameworks-in-python)
   - [unittest](#unittest)
   - [pytest](#pytest)
   - [nose2](#nose2)
5. [Advanced TDD Topics](#5-advanced-tdd-topics)
   - [Mocking and Patching](#mocking-and-patching)
   - [Dependency Injection](#dependency-injection)
   - [Testing Asynchronous Code](#testing-asynchronous-code)
   - [Property-Based Testing with Hypothesis](#property-based-testing-with-hypothesis)
6. [Complementary Libraries and Tools](#6-complementary-libraries-and-tools)
   - [coverage.py](#coveragepy)
   - [tox](#tox)
   - [Continuous Integration Tools](#continuous-integration-tools)
   - [Docker for Testing Environments](#docker-for-testing-environments)
7. [Practical Exercises and Projects](#7-practical-exercises-and-projects)
   - [Building a Data Pipeline with TDD](#building-a-data-pipeline-with-tdd)
   - [Testing Data Validation Logic](#testing-data-validation-logic)
   - [Refactoring Legacy Code with TDD](#refactoring-legacy-code-with-tdd)
8. [Integration with Big Data Frameworks](#8-integration-with-big-data-frameworks)
   - [Testing with Apache Spark](#testing-with-apache-spark)
   - [Testing Stream Processing with Kafka](#testing-stream-processing-with-kafka)
9. [Best Practices and Advanced Techniques](#9-best-practices-and-advanced-techniques)
   - [Test Organization](#test-organization)
   - [Performance Testing](#performance-testing)
   - [Security Testing](#security-testing)
10. [Final Project and Assessment](#10-final-project-and-assessment)
    - [Capstone Project](#capstone-project)
    - [Code Review and Feedback](#code-review-and-feedback)
11. [Resources and Documentation](#11-resources-and-documentation)
12. [Additional Considerations](#12-additional-considerations)
    - [Environment Setup](#environment-setup)
    - [Facilitator Notes](#facilitator-notes)
    - [Feedback Mechanisms](#feedback-mechanisms)
13. [Outcome and Evaluation](#13-outcome-and-evaluation)
14. [License](#14-license)

---

## 1. Introduction to TDD and Its Importance in Data Engineering

### Overview

Test-Driven Development (TDD) is a software development practice where tests are written before the actual code. This approach ensures that code is thoroughly tested and meets specified requirements from the onset.

### Objectives of the Lab

- Understand the principles of TDD.
- Learn how TDD improves code quality, reliability, and maintainability.
- Explore how TDD integrates into the Agile development process.
- Discuss challenges in data engineering that TDD can address.

### Content

#### What is TDD?

- **Red-Green-Refactor Cycle**:
  - **Red**: Write a failing test that defines a desired function or improvement.
  - **Green**: Write the minimal code necessary to pass the test.
  - **Refactor**: Clean up the code, ensuring it adheres to standards and is maintainable.

#### Benefits of TDD

- **Improved Code Quality**: Encourages consideration of edge cases and error handling.
- **Documentation**: Tests serve as live documentation for code behavior.
- **Confidence in Refactoring**: A robust test suite allows safe code modifications.

#### TDD in Agile Development

- **Continuous Feedback**: Aligns with Agile's iterative approach.
- **Customer Collaboration**: Tests can be derived from user stories and acceptance criteria.

#### TDD for Data Engineering Challenges

- **Data Integrity**: Ensures data remains accurate through processing.
- **Schema Evolution**: Manages changes in data structures over time.
- **Pipeline Robustness**: Builds resilient data pipelines that handle failures gracefully.

---

## 2. Use Cases Specific to Data Engineering

### Data Ingestion Pipelines

#### Scenario

You need to build a data ingestion pipeline that reads from various data sources in different formats.

#### Exercises

1. **Reading CSV Files**

   - **Test**: Write a test to check if the function correctly reads a CSV file.
   - **Code**: Implement the function to pass the test.

   **Files Involved**:

   - Source code: `src/Ex_1_data_ingestion.py`
   - Test code: `tests/test_Ex_1_data_ingestion.py`
   - Sample data: `data/sample.csv`

   ```python
   # tests/test_Ex_1_data_ingestion.py
   import unittest
   from src.Ex_1_data_ingestion import read_csv_file

   class TestDataIngestion(unittest.TestCase):
       def test_read_csv_file(self):
           data = read_csv_file('data/sample.csv')
           self.assertEqual(len(data), 100)  # Assuming sample.csv has 100 records

   if __name__ == '__main__':
       unittest.main()
   ```

   **Implementation**:

   ```python
   # src/Ex_1_data_ingestion.py
   import csv

   def read_csv_file(file_path):
       """
       Reads a CSV file and returns a list of dictionaries.

       Args:
           file_path (str): Path to the CSV file.

       Returns:
           list: List of dictionaries representing the CSV rows.
       """
       with open(file_path, mode='r', encoding='utf-8') as csvfile:
           reader = csv.DictReader(csvfile)
           data = [row for row in reader]
       return data
   ```

2. **Handling Missing or Additional Fields**

   - **Test**: Write tests for data with missing or additional fields.
   - **Code**: Update the function to handle these scenarios.

   **Files Involved**:

   - Test data: `data/sample_missing_fields.csv`, `data/sample_additional_fields.csv`

   **Test Example**:

   ```python
   # tests/test_Ex_1_data_ingestion.py (additional tests)

   def test_read_csv_file_missing_fields(self):
       data = read_csv_file('data/sample_missing_fields.csv')
       # Implement assertions based on expected behavior

   def test_read_csv_file_additional_fields(self):
       data = read_csv_file('data/sample_additional_fields.csv')
       # Implement assertions based on expected behavior
   ```

### Data Transformation and Cleaning

#### Scenario

Transform raw data into a clean, analysis-ready format.

#### Exercises

1. **Normalization**

   - **Test**: Test a function that normalizes numerical data.
   - **Code**: Implement normalization using Min-Max scaling.

   **Files Involved**:

   - Source code: `src/Ex_2_data_transformation.py`
   - Test code: `tests/test_Ex_2_data_transformation.py`

   **Test Example**:

   ```python
   # tests/test_Ex_2_data_transformation.py
   import unittest
   from src.Ex_2_data_transformation import normalize_column

   class TestDataTransformation(unittest.TestCase):
       def test_normalize_column(self):
           data = [0, 5, 10]
           normalized_data = normalize_column(data)
           self.assertEqual(normalized_data, [0.0, 0.5, 1.0])

   if __name__ == '__main__':
       unittest.main()
   ```

   **Implementation**:

   ```python
   # src/Ex_2_data_transformation.py

   def normalize_column(data):
       """
       Normalizes a list of numerical values using Min-Max scaling.

       Args:
           data (list): List of numerical values.

       Returns:
           list: Normalized list of values between 0 and 1.
       """
       if not data:
           return []
       min_val = min(data)
       max_val = max(data)
       range_val = max_val - min_val
       if range_val == 0:
           return [0.0 for _ in data]
       normalized_data = [(x - min_val) / range_val for x in data]
       return normalized_data
   ```

2. **Aggregation**

   - **Test**: Test aggregation functions like sum and mean.
   - **Code**: Implement the aggregation logic.

   **Test Example**:

   ```python
   # tests/test_Ex_2_data_transformation.py (additional tests)
   import unittest
   from src.Ex_2_data_transformation import calculate_sum, calculate_mean

   class TestDataTransformation(unittest.TestCase):
       def test_calculate_sum(self):
           data = [1, 2, 3, 4, 5]
           total = calculate_sum(data)
           self.assertEqual(total, 15)

       def test_calculate_mean(self):
           data = [1, 2, 3, 4, 5]
           mean = calculate_mean(data)
           self.assertEqual(mean, 3.0)

   if __name__ == '__main__':
       unittest.main()
   ```

   **Implementation**:

   ```python
   # src/Ex_2_data_transformation.py (additional functions)

   def calculate_sum(data):
       return sum(data)

   def calculate_mean(data):
       if not data:
           return 0.0
       return sum(data) / len(data)
   ```

### ETL Processes

#### Scenario

Build an ETL pipeline that extracts data, transforms it, and loads it into a database.

#### Exercises

1. **End-to-End Testing**

   - **Test**: Simulate the entire ETL process in a test.
   - **Code**: Implement each ETL component to pass the tests.

   **Files Involved**:

   - Source code: `src/Ex_3_etl_process.py`
   - Test code: `tests/test_Ex_3_etl_process.py`

   **Test Example**:

   ```python
   # tests/test_Ex_3_etl_process.py
   import unittest
   from src.Ex_3_etl_process import extract_data, transform_data, load_data

   class TestETLProcess(unittest.TestCase):
       def test_etl_pipeline(self):
           raw_data = extract_data('data/input.csv')
           transformed_data = transform_data(raw_data)
           result = load_data(transformed_data, 'data/output.csv')
           self.assertTrue(result)

   if __name__ == '__main__':
       unittest.main()
   ```

   **Implementation**:

   ```python
   # src/Ex_3_etl_process.py
   import csv

   def extract_data(file_path):
       # Implement data extraction logic
       pass

   def transform_data(data):
       # Implement data transformation logic
       pass

   def load_data(data, output_path):
       # Implement data loading logic
       pass
   ```

---

## 3. Edge Cases Handling

### Corrupt or Malformed Data

#### Scenario

Data arrives with unexpected formats or corrupted entries.

#### Exercises

1. **Data Validation**

   - **Test**: Write tests to check how functions handle corrupted data.
   - **Code**: Implement validation and exception handling.

   **Files Involved**:

   - Source code: `src/Ex_4_data_validation.py`
   - Test code: `tests/test_Ex_4_data_validation.py`

   **Test Example**:

   ```python
   # tests/test_Ex_4_data_validation.py
   import unittest
   from src.Ex_4_data_validation import validate_data

   class TestDataValidation(unittest.TestCase):
       def test_validate_corrupted_data(self):
           corrupted_data = {'name': 'John Doe', 'age': 'twenty'}
           with self.assertRaises(ValueError):
               validate_data(corrupted_data)

   if __name__ == '__main__':
       unittest.main()
   ```

   **Implementation**:

   ```python
   # src/Ex_4_data_validation.py

   def validate_data(record):
       """
       Validates a data record.

       Args:
           record (dict): The data record to validate.

       Raises:
           ValueError: If data is invalid.
       """
       if not isinstance(record.get('age'), int):
           raise ValueError('Age must be an integer')
       # Additional validation logic
   ```

### Missing or Null Values

#### Scenario

Your dataset contains missing or null entries.

#### Exercises

1. **Handling Nulls**

   - **Test**: Ensure functions handle `None` or `NaN` without failing.
   - **Code**: Implement strategies like imputation or default values.

   **Test Example**:

   ```python
   # tests/test_Ex_2_data_transformation.py (additional test)
   import unittest
   from src.Ex_2_data_transformation import normalize_column

   class TestDataTransformation(unittest.TestCase):
       def test_normalize_column_with_nulls(self):
           data = [10, None, 30]
           normalized_data = normalize_column(data)
           # Implement assertions based on expected behavior

   if __name__ == '__main__':
       unittest.main()
   ```

### Schema Changes

#### Scenario

The data schema evolves over time, adding or removing fields.

#### Exercises

1. **Backward Compatibility**

   - **Test**: Ensure code handles both old and new schemas.
   - **Code**: Implement flexible parsing logic.

   **Implementation Hint**:

   - Modify `read_csv_file` in `Ex_1_data_ingestion.py` to handle optional fields.

### Unexpected Data Formats

#### Scenario

Data arrives in formats different from what was expected.

#### Exercises

1. **Robust Parsing**

   - **Test**: Write tests for various date formats or encodings.
   - **Code**: Implement parsing functions that handle these variations.

---

## 4. Popular TDD Frameworks in Python

Certainly! Here is a more detailed Section 4 for your README.md, covering popular TDD frameworks in Python with additional explanations, examples, and guidance on how to use them in your project.

---

# Test-Driven Development (TDD) in Data Engineering with Python

...

## 4. Popular TDD Frameworks in Python

In this section, we'll delve deeper into the popular TDD frameworks available in Python. We'll cover their features, how they compare, and provide examples of how to use them in your data engineering projects.

### Overview

Python offers several testing frameworks that facilitate TDD practices. The most commonly used frameworks are:

- **unittest**: Python's built-in testing framework.
- **pytest**: A powerful and easy-to-use testing framework that extends `unittest`.
- **nose2**: A successor to `nose`, providing a layer on top of `unittest` for easier test writing and discovery.

### Choosing the Right Framework

- **unittest** is great for those who prefer a structured, class-based approach and want to use Python's standard library without additional dependencies.
- **pytest** is suitable for those who prefer simplicity and powerful features like fixtures, parameterization, and plugins.
- **nose2** is ideal for developers looking for a middle ground between `unittest` and `pytest`, with automatic test discovery and plugins.

---

### unittest

`unittest` is Python's built-in testing framework inspired by Java's JUnit. It provides a rich set of tools for constructing and running tests.

#### Features of unittest

- **Class-Based Tests**: Organize tests within classes derived from `unittest.TestCase`.
- **Rich Assertions**: Provides a wide range of assertion methods for checking conditions.
- **Test Discovery**: Automatically discover test modules and functions.
- **Setup and Teardown Methods**: Define code to run before and after each test or test class.

#### Basic Example Using unittest

```python
# tests/test_string_methods.py
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Setup code runs before each test method
        pass

    def tearDown(self):
        # Teardown code runs after each test method
        pass

    def test_upper(self):
        self.assertEqual('data'.upper(), 'DATA')

    def test_isupper(self):
        self.assertTrue('DATA'.isupper())
        self.assertFalse('Data'.isupper())

    def test_split(self):
        s = 'data engineering'
        self.assertEqual(s.split(), ['data', 'engineering'])
        # Check for exception
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

#### Using unittest in Your Project

**Example: Testing Data Ingestion with unittest**

- **Test File**: `tests/test_Ex_1_data_ingestion.py`
- **Source File**: `src/Ex_1_data_ingestion.py`

```python
# tests/test_Ex_1_data_ingestion.py
import unittest
from src.Ex_1_data_ingestion import read_csv_file

class TestDataIngestion(unittest.TestCase):

    def setUp(self):
        # Optional setup before each test method
        self.sample_file = 'data/sample.csv'

    def test_read_csv_file(self):
        data = read_csv_file(self.sample_file)
        self.assertEqual(len(data), 100)  # Assuming sample.csv has 100 records

    def test_read_csv_file_missing_fields(self):
        data = read_csv_file('data/sample_missing_fields.csv')
        # Add assertions based on expected behavior with missing fields

    def test_read_csv_file_additional_fields(self):
        data = read_csv_file('data/sample_additional_fields.csv')
        # Add assertions based on expected behavior with additional fields

if __name__ == '__main__':
    unittest.main()
```

**Running the Tests**

```bash
python -m unittest discover -s tests
```

---

### pytest

`pytest` is a third-party testing framework that simplifies writing tests by allowing you to use plain functions instead of requiring classes. It provides powerful features like fixtures, parameterization, and a rich plugin ecosystem.

#### Features of pytest

- **Simple Syntax**: Write tests as simple functions using `assert` statements.
- **Fixtures**: Reusable test setups using the `@pytest.fixture` decorator.
- **Parameterization**: Run the same test with different inputs using `@pytest.mark.parametrize`.
- **Plugin Support**: Extend functionality with a variety of plugins (e.g., `pytest-cov` for coverage).
- **Detailed Failure Reports**: Provides clear and informative error messages.

#### Basic Example Using pytest

```python
# tests/test_sample.py

def test_upper():
    assert 'data'.upper() == 'DATA'

def test_isupper():
    assert 'DATA'.isupper()
    assert not 'Data'.isupper()

def test_split():
    s = 'data engineering'
    assert s.split() == ['data', 'engineering']
    with pytest.raises(TypeError):
        s.split(2)
```

**Note**: You need to install `pytest` via `pip install pytest`.

#### Using pytest in Your Project

**Example: Testing Data Transformation with pytest**

- **Test File**: `tests/test_Ex_2_data_transformation.py`
- **Source File**: `src/Ex_2_data_transformation.py`

```python
# tests/test_Ex_2_data_transformation.py
import pytest
from src.Ex_2_data_transformation import normalize_column

def test_normalize_column():
    data = [0, 5, 10]
    normalized_data = normalize_column(data)
    assert normalized_data == [0.0, 0.5, 1.0]

@pytest.mark.parametrize("input_data, expected", [
    ([1, 2, 3], [0.0, 0.5, 1.0]),
    ([10, 20, 30], [0.0, 0.5, 1.0]),
    ([], []),
])
def test_normalize_column_parametrized(input_data, expected):
    normalized_data = normalize_column(input_data)
    assert normalized_data == expected
```

**Using Fixtures**

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return [0, 5, 10]
```

```python
# tests/test_Ex_2_data_transformation.py
def test_normalize_column_with_fixture(sample_data):
    normalized_data = normalize_column(sample_data)
    assert normalized_data == [0.0, 0.5, 1.0]
```

**Running the Tests**

```bash
pytest tests/
```

---

### nose2

`nose2` is the successor to `nose` and extends `unittest` to make testing easier. It offers automatic test discovery and a range of plugins.

#### Features of nose2

- **Automatic Test Discovery**: Finds tests without the need for boilerplate code.
- **Support for unittest**: Works with `unittest` test cases and methods.
- **Plugins**: Extend functionality with built-in and custom plugins.
- **Simplified Test Running**: Run tests using the `nose2` command.

#### Basic Example Using nose2

```python
# tests/test_string_methods.py
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('data'.upper(), 'DATA')

    def test_isupper(self):
        self.assertTrue('DATA'.isupper())
        self.assertFalse('Data'.isupper())

# No need for the if __name__ == '__main__' block
```

**Running the Tests**

```bash
nose2
```

#### Using nose2 in Your Project

Since `nose2` is built on top of `unittest`, you can use the same test files as shown in the `unittest` examples.

**Installation**

```bash
pip install nose2
```

**Advantages Over unittest**

- **Simpler Test Execution**: No need to add `unittest.main()` in your test files.
- **Enhanced Test Discovery**: Automatically finds tests without specifying paths.
- **Plugin Support**: Extend capabilities with plugins, such as coverage reports.

---

### Comparison of Frameworks

| Feature                   | unittest          | pytest            | nose2            |
|---------------------------|-------------------|-------------------|------------------|
| **Built-in**              | Yes               | No (3rd-party)    | No (3rd-party)   |
| **Test Discovery**        | Manual or via CLI | Automatic         | Automatic        |
| **Test Syntax**           | Class-based       | Function-based    | Class-based      |
| **Fixtures**              | setUp/tearDown    | Fixtures          | setUp/tearDown   |
| **Parameterization**      | Limited           | Yes               | Via plugins      |
| **Assertions**            | `self.assert*`    | Plain `assert`    | `self.assert*`   |
| **Plugins**               | Limited           | Extensive         | Yes              |
| **Learning Curve**        | Moderate          | Easy              | Moderate         |

### Recommendations

- **For Beginners**: Start with `unittest` to understand the fundamentals of testing in Python.
- **For Simplicity and Power**: Use `pytest` for its simplicity, powerful features, and active community.
- **For unittest Compatibility**: If you prefer `unittest` but want better test discovery and plugins, consider `nose2`.

### Integrating the Frameworks into Your Project

- **Consistent Structure**: Organize your tests in the `tests/` directory, mirroring the structure of your `src/` directory.
- **Naming Conventions**: Use `test_*.py` for test files and `test_*` functions or methods.
- **Virtual Environment**: Install the testing framework in your project's virtual environment to manage dependencies.

---

### Examples in the Context of Your Project

**Using unittest with Your Data Engineering Project**

- **Data Ingestion Tests**: `tests/test_Ex_1_data_ingestion.py`
- **Data Transformation Tests**: `tests/test_Ex_2_data_transformation.py`
- **ETL Process Tests**: `tests/test_Ex_3_etl_process.py`

**Using pytest with Your Data Engineering Project**

If you prefer `pytest`, you can write tests without classes and use simple `assert` statements.

```python
# tests/test_Ex_1_data_ingestion.py
from src.Ex_1_data_ingestion import read_csv_file

def test_read_csv_file():
    data = read_csv_file('data/sample.csv')
    assert len(data) == 100
```

**Running Tests with Coverage**

You can use `pytest` plugins to generate coverage reports.

```bash
pip install pytest pytest-cov
pytest --cov=src tests/
```
---

## 5. Advanced TDD Topics

### Mocking and Patching

#### Concept

Simulate external dependencies to isolate code behavior.

#### Exercises

1. **Mocking Database Connections**

   - **Test**: Use `unittest.mock` to mock a database call.
   - **Code**: Ensure your function works with the mock.

   **Files Involved**:

   - Source code: `src/Ex_6_data_storage.py`
   - Test code: `tests/test_Ex_6_data_storage.py`

   **Implementation**:

   ```python
   # src/Ex_6_data_storage.py

   class DatabaseConnection:
       def __init__(self):
           # Simulate database connection setup
           pass

       def insert(self, data):
           # Simulate data insertion
           return True

   def save_to_db(data):
       db = DatabaseConnection()
       return db.insert(data)
   ```

   **Test Example**:

   ```python
   # tests/test_Ex_6_data_storage.py
   import unittest
   from unittest.mock import patch, MagicMock
   from src.Ex_6_data_storage import save_to_db

   class TestDataStorage(unittest.TestCase):
       @patch('src.Ex_6_data_storage.DatabaseConnection')
       def test_save_to_db(self, mock_db_conn):
           mock_instance = MagicMock()
           mock_instance.insert.return_value = True
           mock_db_conn.return_value = mock_instance

           result = save_to_db({'data': 'test'})
           mock_instance.insert.assert_called_once_with({'data': 'test'})
           self.assertTrue(result)

   if __name__ == '__main__':
       unittest.main()
   ```

### Dependency Injection

[Content remains the same, adjust file names if necessary]

---

## 6. Complementary Libraries and Tools

[Content remains the same]

---

## 7. Practical Exercises and Projects

[Content remains the same, but adjust any references to files as per the project structure]

---

## 8. Integration with Big Data Frameworks

### Testing with Apache Spark

#### Scenario

Write unit tests for Spark jobs.

#### Exercises

1. **Using `pyspark.testing`**

   - **Test**: Use `SparkSession` in local mode.
   - **Code**: Implement Spark transformations.

   **Files Involved**:

   - Source code: `src/Ex_7_spark_jobs.py`
   - Test code: `tests/test_Ex_7_spark_jobs.py`

   **Implementation**:

   ```python
   # src/Ex_7_spark_jobs.py
   from pyspark.sql import DataFrame

   def transform_data(df: DataFrame) -> DataFrame:
       # Implement Spark transformations
       return df
   ```

   **Test Example**:

   ```python
   # tests/test_Ex_7_spark_jobs.py
   import unittest
   from pyspark.sql import SparkSession
   from src.Ex_7_spark_jobs import transform_data

   class TestSparkJobs(unittest.TestCase):
       @classmethod
       def setUpClass(cls):
           cls.spark = SparkSession.builder.master("local[1]").appName("Test").getOrCreate()

       @classmethod
       def tearDownClass(cls):
           cls.spark.stop()

       def test_transform_data(self):
           df = self.spark.createDataFrame([('Alice', 1)], ['name', 'value'])
           result_df = transform_data(df)
           self.assertEqual(result_df.count(), 1)

   if __name__ == '__main__':
       unittest.main()
   ```

---

## 9. Best Practices and Advanced Techniques

[Content remains the same]

---

## 10. Final Project and Assessment

[Content remains the same]

---

## 11. Resources and Documentation

[Content remains the same]

---

## 12. Additional Considerations

### Environment Setup

#### Instructions

1. **Install Python 3.x**

   - Download from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

#### Running Tests

To run all unit tests together, use the following command from the root directory of your project:

```bash
python -m unittest discover -s tests
```

This command will discover and run all tests in the `tests/` directory.

---

## 13. Outcome and Evaluation

[Content remains the same]

---

## 14. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
