# Assignment 03 — CHANGES

**Name:** __Thida Khaing__  **Student ID:** __6705140024__

This file explains the changes I made when refactoring the messy store system. I kept the original business rules and checked the output using the self-test.

---

## 1 · What I changed

| # | Code smell in the original                                                       | What I changed it to                                                                                                                                                                                           | OOP concept applied               | How I verified behaviour was unchanged                                                                  |
| - | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 1 | Product data was stored as tuples such as `("Laptop", 1200.0, "electronics")`.   | Created a `Product` class with `name`, `price`, and `categories` attributes.                                                                                                                                   | Classes / Encapsulation           | Ran `python Assignment_03.py` → PASS.                                                                   |
| 2 | Order items were stored as tuples containing a product index and quantity.       | Created an `OrderItem` class that has a `Product` and a `quantity`.                                                                                                                                            | Composition                       | Checked the `OrderItem` objects and ran the self-test → PASS.                                           |
| 3 | Customer tier rules used repeated `if/elif` statements for discounts and points. | Created `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses, with each class providing its own discount and points behaviour.                                                      | Inheritance / Polymorphism        | Compared the discount and points rules with the legacy code and ran the self-test → PASS.               |
| 4 | `calc()` calculated values and printed the receipt in the same function.         | Created separate calculation methods: `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. `receipt()` handles the receipt output.                                                                  | Separation of calculation and I/O | Checked that the calculation methods return values and do not print. Ran the self-test → PASS.          |
| 5 | The original code used magic numbers and had a `global TAXRATE`.                 | Created named constants such as `TAX_RATE`, `FOOD_TAX`, `DISCOUNT_THRESHOLD`, `BULK_QTY_THRESHOLD`, `BULK_DISCOUNT_RATE`, and `POINTS_DIVISOR`. The refactored calculation code does not use `global TAXRATE`. | Clean Code / Constants            | Compared the constant values with the original business rules and ran `python Assignment_03.py` → PASS. |

---

## 2 · Short reflection

The change that improved the code the most for me was replacing the repeated customer tier calculations with subclasses. Each customer type now has its own discount and points behaviour, so the `Order` class does not need to check which tier it is using. I also learned that refactoring means keeping the original behaviour, so I had to be careful not to change the discount, tax, points, or receipt output. The receipt formatting was especially important because changing a line break, space, or number format could make the self-test fail. I ran the self-test after my changes and confirmed that it printed `PASS`.

---

## 3 · Prompt log (Level 2 — required)

I used AI mainly to understand the existing code, clarify OOP concepts, discuss refactoring choices, and debug small problems. I wrote and edited the final implementation myself and checked the changes against the original behaviour using the self-test.

| # | My prompt to the AI                                                                                                 | What it suggested / explained                                                                                                                                              | Accept / reject / edited | How I checked it                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| 1 | **"Why does the original code use it[0] & it[1] for the order items?"**                                       | Explained that each order item in the legacy code is a tuple where `it[0]` is the product index and `it[1]` is the quantity.                                               | Accepted                 | I checked the original `ORDERS` data and confirmed what each tuple value represented.                                   |
| 2 | **"Why does the self-test use `io.StringIO()` and `redirect_stdout(buf)`?"**                                        | Explained that `StringIO()` stores text in memory and `redirect_stdout()` captures printed output so the self-test can compare it with the legacy output.                  | Accepted                 | I read the `capture()` and `_check()` functions and confirmed how the output comparison works.                          |
| 3 | **"Do I need `isinstance` checks for `int` and `float` in the `OrderItem` constructor?"**                           | Explained the possible use of type validation and discussed whether it was necessary for the assignment.                                                                   | Rejected / simplified    | I kept the constructor validation focused on the required quantity rule, `quantity >= 1`, and ran the self-test → PASS. |
| 4 | **"I don't want to use repetitive append in `receipt()`?"**                                                         | Suggested using `"\n".join()` to combine the item strings before building the receipt.                                                                                     | Accepted                 | I checked the generated receipt against the legacy output and ran the self-test → PASS.                                 |
| 5 | **"points_multiplier can I use another variable, status or something instead of using tier or points_multiplier?"** | Explained that method and attribute names can be changed when they are not required by the assignment, as long as the meaning and references remain correct.               | Accepted and edited      | I used `status` and `points_rate`, checked all references, and ran the self-test.                                       |
| 6 | **"Why am I getting NameError in make_customer?"**                                                              | Helped identify that the name used in `make_customer()` did not match the defined name because of a spelling mistake.                                                      | Accepted and fixed       | I corrected the spelling and ran `python Assignment_03.py` → PASS.                                                      |
| 7 | **"can I change the if/elif for silver, gold and platinum to polymorphism how?"**                                   | Explained how a base `Customer` class and subclasses such as `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` can provide different discount and points behaviour. | Accepted and edited      | I compared each subclass rule with the original tier rules and ran the self-test → PASS.                                |
| 8 | **"Can my calculation methods return the values & keep original values in receipt?"**                               | Explained that calculation methods can return numbers while `receipt()` uses those returned values to produce the original receipt output.                                 | Accepted                 | I checked that the calculation methods do not contain `print()` and ran the self-test → PASS.                           |

### Ownership statement

By submitting, I confirm that I understand and can explain the code I submitted, and that this prompt log reflects my actual AI use for this assignment.

---

## 4 · Before-you-submit checklist

* [x] `python Assignment_03.py` prints **PASS**.
* [x] No tuples / parallel lists are used for the refactored domain model — products, orders, and items are represented by objects.
* [x] No tier `if/elif` chains are used for discount and points calculations — customer tiers are handled using a class family.
* [x] Calculation methods **return** values and do not `print`; receipt output is handled separately.
* [x] Constructors validate object state; no `global TAXRATE` is used by the refactored calculations; magic numbers are named.
* [x] The change table and reflection are filled in.
* [x] The prompt log records the AI prompts that helped with this assignment.
* [x] The ownership statement is included.
      
