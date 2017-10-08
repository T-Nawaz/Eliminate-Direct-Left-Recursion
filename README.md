# Eliminate Direct Left Recursion
## Introduction
In Context Free Grammar(CFG) we face 2 types of Left Recuursion:
1. Direct Left Recursion
2. Indirect Left Recursion

Here I've tackled the direct left recursion problem. 
Direct left recursion occurs when the definition can be satisfied with only one substitution. It requires a rule of the form
**A -> Aα** where α is a sequence of nonterminals and terminals.

For example, the rule: **Expression -> Expression + Term** is directly left-recursive.

## Eliminating the direct left recursion
The general algorithm to remove direct left recursion is as follows. For a left-recursive nonterminal **A**, discard any rules of the form **A -> A** and consider those that remain:

**A -> Aα₁ | ... | Aαₙ | 	β₁ | ... | βₘ**

where:

- each **α** is a nonempty sequence of nonterminals and terminals, and
- each **β** is a sequence of nonterminals and terminals that does not start with **A**.

Replace these with two sets of productions, one set for **A**:

**A -> β₁A' | ... | βₘA'**

and another set for the fresh nonterminal **A'** (often called the "tail" or the "rest"):

**A' -> α₁A' | ... | α₁A' | ε**

Repeat this process until no direct left recursion remains.

As an example, consider the rule set

**Expression -> Expression + Expression | Integer | String**

This could be rewritten to avoid left recursion as

**Expression -> Integer Expression' | String Expression'**

**Expression -> Expression Expression' | ε**

** **

[Left Recursion WikiPedia Page](https://en.wikipedia.org/wiki/Left_recursion).
