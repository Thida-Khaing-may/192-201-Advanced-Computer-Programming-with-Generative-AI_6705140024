# Assignment 03 — CHANGES

**Name:** __Thida Khaing__  **Student ID:** __6705140024__

This file explains what I changed during the refactoring and why I made these changes. I also recorded how I used AI and how I verified my final code.

---

## 1. What I changed

| #  | Code smell in the original                                                           | What I changed it to                                                                                                                                       | OOP concept applied        | How I verified behaviour was unchanged                        |
| -- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------- |
| 1  | Products were stored as tuples such as `("Laptop", 1200.0, "electronics")`.          | Created a `Product` class with `name`, `price`, and `category` attributes.                                                                                 | Classes / Encapsulation    | Ran `python Assignment_03.py` → PASS                          |
| 2  | Order items were stored as tuples containing a product index and quantity.           | Created an `OrderItem` class that contains a `Product` object and a `quantity`.                                                                            | Composition                | Ran the self-test → PASS                                      |
| 3  | Customer tiers used repeated `if/elif` statements for discount calculation.          | Created `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` classes. Each subclass has its own `discount_rate()` method.                  | Inheritance / Polymorphism | Ran the self-test → PASS                                      |
| 4  | Customer tiers also used repeated `if/elif` statements for points calculation.       | Added `points_multiplier()` to the customer classes so each tier provides its own multiplier.                                                              | Inheritance / Polymorphism | Ran the self-test → PASS                                      |
| 5  | The `calc()` function calculated the order and printed the receipt at the same time. | Moved calculations into separate `Order` methods: `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. The `receipt()` method handles printing. | Separation of concerns     | Compared the refactored output with the legacy output → PASS  |
| 6  | The original code contained magic numbers such as `0.07`, `0.03`, `10`, and `100`.   | Replaced them with named constants such as `STANDARD_TAX_RATE`, `BULK_DISCOUNT_RATE`, `POINTS_DIVISOR`, and `DISCOUNT_THRESHOLD`.                          | Clean Code                 | Ran the self-test → PASS                                      |
| 7  | Product tax was calculated using `if cat == "food"` inside the main calculation.     | Added a `tax_rate()` method to `Product` so the product provides its own tax rate.                                                                         | Encapsulation              | Checked the tax rules and ran the self-test → PASS            |
| 8  | `OrderItem` did not validate quantity before using it.                               | Added constructor validation so quantity must be at least `1`.                                                                                             | Encapsulation / Validation | Checked the constructor and ran the self-test → PASS          |
| 9  | The original calculation function used `global TAXRATE`.                             | Removed the global dependency from the refactored code and used named constants instead.                                                                   | Clean Code                 | Ran `python Assignment_03.py` → PASS                          |
| 10 | Orders were represented by nested tuples containing customer and item information.   | Created an `Order` class containing a customer and a list of `OrderItem` objects.                                                                          | Composition                | Checked the object relationships and ran the self-test → PASS |

---

## 2. Short reflection

The change that improved the code the most was replacing the repeated tier `if/elif` statements with customer subclasses. It makes the discount and points rules easier to understand because each customer type has its own behaviour. Separating the calculations from receipt printing also made the `Order` class easier to read and understand. I had to be careful not to change the original discount, tax, points, rounding, or receipt format because the assignment requires exactly the same behaviour. After completing the refactoring, I ran the provided self-test and confirmed that the output matched the original output.

---

## 3. Prompt log (Level 2)

I used AI to help me understand and improve specific parts of the refactoring. I wrote and edited the final code myself and checked the changes using the provided self-test.

| # | My prompt to the AI                                                                     | What it suggested (summary)                                                                                                           | Accept / reject / edited | How I checked it                                                                                |
| - | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------- |
| 1 | "How can I replace the `if tier == ...` discount and points logic with polymorphism?"   | Suggested a `Customer` base class with `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses.                           | Edited                   | Read and understood each method, then ran the self-test → PASS.                                 |
| 2 | "How should I separate the calculation methods from the receipt printing?"              | Suggested putting `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` in `Order`, with `receipt()` responsible for output. | Edited                   | Checked that calculation methods return values and do not print, then ran the self-test → PASS. |
| 3 | "Should I use named constants for the tax, discount, bulk quantity, and points values?" | Suggested replacing magic numbers with named constants such as `STANDARD_TAX_RATE`, `BULK_DISCOUNT_RATE`, and `POINTS_DIVISOR`.       | Accepted / edited names  | Checked that the values were the same as the legacy rules and ran the self-test → PASS.         |
| 4 | "How should I validate quantity in the constructor?"                                    | Suggested checking `quantity < 1` and raising `ValueError`.                                                                           | Accepted                 | Read the validation and confirmed the existing order quantities are valid.                      |
| 5 | "Why does my refactored output need to match the original exactly?"                     | Explained that refactoring should change the structure of the code but not its observable behaviour or output.                        | Accepted                 | Used the provided `GOLDEN_OUTPUT` self-test to compare both outputs.                            |

---

## Ownership statement

By submitting, I confirm that I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.

---

## 4. Before-submit checklist

* [x] `python Assignment_03.py` prints **PASS**.
* [x] No tuples / parallel lists left — products, orders, and items are objects.
* [x] No `if tier == ...` chains — tiers are a class family.
* [x] Calculation methods return values and do not print; printing is separate.
* [x] Constructors validate state; no leftover `global`; magic numbers are named.
* [x] The change table and reflection above are filled in.
* [x] The prompt log is complete and the ownership statement is signed.
