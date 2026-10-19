# itcs386-tdd
TDD lab for ITCS386

# Reflection - ITCS386 TDD Lab

## 1. How many tests did you write in Part A, and how many lines of production code? What is the
ratio?

I wrote 9 tests in test_kitchen.py and kitchen.py has about 41 lines. So the ratio is around 1 test for every 4-5 lines of code.

## 2. When was your bar red for the longest time, and what made it last so long?

Step A6, I changed Quantity to need a unit in A5, but forgot to update my old tests, So they still used Quantity(200) with no unit. So I got TypeError "missing 1 required positional argument: 'unit'" After I changed them to use grams(200) it was green again.


## 3. Find one place where you used Fake It, one where you triangulated, and one where you used
Obvious Implementation. Looking back, was each choice right?

- Fake It: in A1 I made times() just set amount to 600. It showed the test file and the module were connected and working. I also faked plus() to return grams(500) in A6.
- Triangulate: in A2 I added the "times 2 = 400" test, so 600 could not pass anymore and I write amount * multiplier.
- Obvious Implementation: __repr__ and Sum.times() ,worked first try

## 4. Which items are still on your test list? Which would you implement next, and which should you
delete because they were speculation?

Only the __hash__ note is left, I think I should delete it because nothing in the recipe app needs a set of quantities yet. Next I will add a test for what happens when there is no rate, for example reducing ounces to grams without add_rate.

## 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?

Probably not. On paper, a reduce method on a single Quantity does not look necessary. It was added because Converter.reduce needed to call reduce() on both Quantity and Sum in the same way. A paper design would more likely use type checks inside Converter, which is harder to extend.

## 6. Tests after code vs tests first

In Part 0, the code already existed, so the tests were used to check behavior and find bugs. In the shipping exercise, 4 tests failed but there were only 3 bugs, because the 5.2 kg and 6.5 kg cases both exposed the same int() truncation bug.

In Part A, the tests decided the design. test_multiplication_returns_a_new_quantity made Quantity a value object. test_equality led to __eq__. test_simple_addition led to the Sum class, and test_mixed_addition led to passing the converter into reduce. None of these were planned at the start.