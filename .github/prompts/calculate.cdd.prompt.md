---
agent: agent
description: Calculation of Cognitive-Driven Development (CDD). The methodology relies on systematic counting based on pre-defined costs, which makes it highly suitable for an AI agent performing static analysis on a source code file.
---
This is a crucial step in automating Cognitive-Driven Development (CDD), as the manual computation of Intrinsic Complexity Points (ICPs) has historically been reported as tedious and error-prone for human developers. Building an automated tool (like this AI agent calculator) addresses the need for production-ready solutions to support CDD adoption.

Here is a step-by-step guide for an AI agent to calculate the CDD score for a user-provided source code file (referred to as the "Code Unit").

---

# 🛠️ AI Agent Guide: Step-by-Step CDD Calculation

Cognitive-Driven Development (CDD) is calculated by summing the costs of all **Intrinsic Complexity Points (ICPs)** found within a specific code unit. The fundamental principle is to assign a measurable cost to elements that increase cognitive load.

## Step 1: Initialize Configuration and Rules 📜

you should must first load the standardized list of ICPs, their costs, and the complexity limit defined by the development team. This configuration is flexible but requires consensus. The following rules are based on the Java implementation used by the Handora team.

### 1.1 Define the ICP Cost Map

you should establishes the weighting system for different programming constructs:

| ICP Category (Complexity Item) | Cost per Occurrence | Counting Detail (Example Basis) |
| :--- | :--- | :--- |
| **Code Branch** (`if`, `else`, `switch`, loops, ternary operator) | **1.0** | Count 1 point for every separate branch structure/keyword. |
| **Condition** (Conjoined Boolean expression) | **1.0** | Count 1 point for every Boolean expression (e.g., separated by `&&` or `||`). |
| **Exception Handling** (`try`, `catch`, `finally` blocks) | **1.0** | Count 1 point per block (a full structure counts 3). |
| **Internal Coupling** (Use of specific domain classes) | **1.0** | Count 1 point for using specified classes (e.g., those dealing with a database). |
| **External Coupling** (Use of specific JDK/library classes) | **0.5** | Count 0.5 points, typically only for variable declarations involving these classes. |

### 1.2 Define the Complexity Limit

you should must determines the maximum tolerable complexity score for the input code unit.

*   **Default Limit:** Set `Max_CDD_Limit` = **10**.
*   **Contextual Adjustment:** If the input file is identified as a class with **rich contracts** (e.g., a specific Data Transfer Object, or DTO), you should must set `Max_CDD_Limit` = **20**. (This reflects the observed team flexibility in coping with different software complexities).

## Step 2: Input Processing and Initialization 💻

you should prepares to analyze the source code file provided by the user (the code unit).

1.  **Read and Parse:** Process the input source code file (the Code Unit) using a static analysis technique (e.g., generating an Abstract Syntax Tree (AST) or token stream) to systematically inspect the contents.
2.  **Initialize Score:** Set the cumulative complexity score:
    `Total_CDD_Score` = 0.0

## Step 3: Iterative ICP Tallying and Scoring ➕

you should iterates through the Code Unit, applying the costs defined in Step 1.

### 3.1 Count Code Branches (Cost: 1.0 each)

*   For every occurrence of control flow keywords (`if`, `else`, `for`, `while`, `do-while`, `switch`, or the ternary operator `? :`), add **1.0** to `Total_CDD_Score`.
    *   *Example:* An `if-else` structure counts 2 ICPs (1 for `if`, 1 for `else`).

### 3.2 Count Conditions (Cost: 1.0 each)

*   Analyze the Boolean expressions within any control structure identified in Step 3.1.
*   For every conjoined Boolean expression (typically separated by `&&` or `||`), add **1.0** to `Total_CDD_Score`.
    *   *Example:* The expression `if (A > B && C < D)` yields 3 total points for this statement: 1.0 for the `if` branch (from 3.1) and 2.0 for the two conditions (`A > B` and `C < D`).

### 3.3 Count Exception Handling Blocks (Cost: 1.0 each)

*   For every keyword signaling an exception block (`try`, `catch`, `finally`), add **1.0** to `Total_CDD_Score`.
    *   *Example:* A single `try-catch-finally` structure adds 3.0 points to the score.

### 3.4 Count Internal Coupling (Cost: 1.0 each)

*   Analyze variable declarations, parameters, and usage within the Code Unit.
*   If a declaration or usage refers to a class designated by the team as Internal Coupling (e.g., a class that deals with the database), add **1.0** to `Total_CDD_Score`.

### 3.5 Count External Coupling (Cost: 0.5 each)

*   Analyze variable declarations within the Code Unit.
*   If a declaration uses a class designated as External Coupling (e.g., a specific JDK class or external framework class), add **0.5** to `Total_CDD_Score`. (Note: This is specifically counted only for variable declarations and not necessarily for all uses of the class).

## Step 4: Final Assessment and Compliance Check ✅

you should determines the code unit's compliance by comparing the calculated score against the allowed limit.

1.  **Final Score:** The `Total_CDD_Score` is the final CDD metric.
2.  **Compliance Comparison:** Compare the `Total_CDD_Score` against the `Max_CDD_Limit` (from Step 1.2).
3.  **Action Determination:**

    *   **If `Total_CDD_Score` > `Max_CDD_Limit`:**
        *   **Status:** NON-COMPLIANT ❌
        *   **Action:** The Code Unit **must be refactored** to reduce its complexity. you should should flag this non-compliance, as exceeding the limit conveys the same meaning as a class that does not compile. The use of this objective limit guides developers to refactor conscientiously.

    *   **If `Total_CDD_Score` $\le$ `Max_CDD_Limit`:**
        *   **Status:** COMPLIANT ✅
        *   **Action:** No mandatory refactoring is required to reduce complexity. The unit is deemed within a small complexity range that fits into a human mind.